import requests
import json
from src.cur_platform.moment.entity import Moment
import os
from flask import jsonify, request, after_this_request
from src.basic.extensions import db, executor
from dotenv import load_dotenv
from src.user.utils.add_score import add_score

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
        mood_type = ans["sentiment"]  # 0: 负向，1: 中性，2: 正向
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


def get_moods(user_id):
    # TODO 分时段获取心情情况：按月 按年 按周
    return None


def write_memo(content, user_id):
    memo = Moment(content, user_id)
    db.session.add(memo)
    db.session.commit()
    memo_id = memo.id
    add_score(request.full_path, user_id)

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
    memos = Moment.query.filter_by(user_id=user_id).paginate(page=int(page), per_page=per_page)
    all_memos = [memo.to_dict() for memo in memos.items]
    return jsonify({"msg": "success", "data": {'total_pages': memos.pages, 'total_items': memos.total,
                                               'items': all_memos}}), 200
