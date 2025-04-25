import requests
import json
from src.cur_platform.moment.entity import Moment
import os
from flask import jsonify, request, after_this_request
from src.basic.extensions import db, executor, redis_client
from dotenv import load_dotenv
from src.user.utils.add_score import add_score
import datetime
import pytz
from sqlalchemy.sql.expression import func

load_dotenv()


def get_mood_classify(text, memo_id):
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token=" + get_access_token()

    payload = json.dumps({
        "text": text
    }, ensure_ascii=False)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
    js = json.loads(response.text)
    ans = js["items"][0]
    confidence = ans["confidence"]
    if confidence > 0.5:
        mood_type = ans["sentiment"]  # 0: 悲观，1: 中性，2: 乐观
        if mood_type != 1:
            Moment.query.filter_by(id=memo_id).update({"mood": mood_type})
            db.session.commit()
    return


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    API_KEY = os.getenv("BAIDU_API_KEY")
    SECRET_KEY = os.getenv("BAIDU_SECRET_KEY")
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def get_moods(user_id, limit_time):
    # 查询数据总条数
    total_count = Moment.query.filter(Moment.user_id == user_id, Moment.create_time >= limit_time).count()

    # 查询 mood 值为 0 的条目数量
    mood_0_count = Moment.query.filter(Moment.user_id == user_id, Moment.create_time >= limit_time,
                                       Moment.mood == '0').count()

    # 查询 mood 值为 2 的条目数量
    mood_2_count = Moment.query.filter(Moment.user_id == user_id, Moment.create_time >= limit_time,
                                       Moment.mood == '2').count()

    time_slots = (
        db.session.query(
            func.hour(Moment.create_time),
            func.count(Moment.id)
        )
        .filter(Moment.user_id == user_id)
        .group_by(func.hour(Moment.create_time))
        .all()
    )

    # 将结果转换为字典，并应用时间区间划分
    result = {}
    for hour, count in time_slots:
        if 0 <= hour <= 5:
            slot = "凌晨"
        elif 6 <= hour <= 11:
            slot = "上午"
        elif 12 <= hour <= 17:
            slot = "下午"
        else:
            slot = "晚上"
        result[slot] = result.get(slot, 0) + count
    # 构建结果字典
    result.update({
        "total_count": total_count,
        "bad_moods_count": mood_0_count,
        "good_moods_count": mood_2_count,
    })
    return result


def get_monthly_moods(user_id):
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))

    # 计算一个月前的日期
    one_month_ago = now - datetime.timedelta(days=30)
    return jsonify({"msg": "success", "data": get_moods(user_id, one_month_ago)}), 200


def get_yearly_moods(user_id):
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    one_year_ago = now - datetime.timedelta(days=365)
    key = f"moment_score:user_{user_id}"
    hash_data = redis_client.hgetall(key)
    # 创建一个空字典来存储转换后的数据
    result_dict = {}

    # 遍历从 Redis 中获取的数据
    for field_bytes, value_bytes in hash_data.items():
        # 解码字节串
        field = field_bytes.decode('utf-8')
        value = value_bytes.decode('utf-8')

        # 尝试将 value 转换为整数，如果转换失败，则保持原样
        try:
            value = int(value)
        except ValueError:
            pass  # 如果 value 不能转换为整数，则保持字符串形式

        # 将 field 和 value 添加到字典中
        result_dict[field] = value

    return jsonify(
        {"msg": "success", "data": {"heatMap": result_dict, "moods_sum": get_moods(user_id, one_year_ago)}}), 200


def write_memo(content, user_id):
    memo = Moment(content, user_id)
    db.session.add(memo)
    db.session.commit()
    memo_id = memo.id
    # 记录到总的活动热力图，也记录到 moment 专门的热力图
    add_score(request.full_path, user_id)
    try:
        key = f"moment_score:user_{user_id}"
        score = 1
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        redis_client.hincrbyfloat(key, date_str, score)
    except Exception as e:
        print(f"在获取说说热力图时，Redis 操作失败：{e}")

    @after_this_request
    def after_request(response):
        executor.submit(get_mood_classify, content, memo_id)
        return response

    return jsonify({'msg': '🎉 留下，新的感受～'}), 200


def delete_memo(moment_id):
    memo = Moment.query.filter_by(id=moment_id).first()
    db.session.delete(memo)
    db.session.commit()
    if memo is None:
        return jsonify({'msg': 'moment 不存在~'}), 400
    return jsonify({'msg': 'moment 删除成功~'}), 200


def get_memo(user_id, page):
    per_page = 15  # 每页显示的 memo 数
    memos = Moment.query.filter_by(user_id=user_id).order_by(Moment.create_time.desc()).paginate(page=int(page),
                                                                                                 per_page=per_page)
    all_memos = [memo.to_dict() for memo in memos.items]
    return jsonify({"msg": "success", "data": {'total_pages': memos.pages, 'total_items': memos.total,
                                               'items': all_memos}}), 200
