"""
网站个人信息相关
"""
from flask import jsonify
from src.basic.extensions import db
import bcrypt
from sqlalchemy.orm import aliased
from src.user.entity import User
from src.user.entity import UserDetail
from src.basic.extensions import redis_client
import random
import string
import pytz
from datetime import datetime


def generate_username(length=5):
    # 定义字符集，包括数字、大小写字母
    characters = string.ascii_letters + string.digits
    # 随机选择字符并组合成指定长度的字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def hash_password(password):
    print(password)
    # 生成盐，并对密码进行哈希
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed_password.decode('utf-8'))
    return hashed_password.decode('utf-8')


def login(email, password):
    """
    :param email:邮箱
    :param password:密码
    :return: 登录结果
    """
    user = User.query.filter_by(email=email).first()
    user_id = user.id
    user_name = UserDetail.query.filter_by(user_id=user_id).first().user_name
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'msg': '邮箱或密码错误'}), 401
    # 在增加登录积分之前，查询当天是否已有分数，有则证明已经登录过
    date_str = datetime.now().strftime("%Y%m%d")
    key = f"score:user_{user_id}"
    if (redis_client.hget(key, date_str) or b'0').decode('utf-8') == '0':
        record_daily_score(user_id, 0.5)
    # 更新 lastLoginTime
    user.modify_time = datetime.now(pytz.timezone('Asia/Shanghai'))
    db.session.commit()

    return jsonify({'msg': '登录成功', "data": {"user_id": user_id, "user_name": user_name}}), 200


def register(email, password, code):
    """
    :param email:邮箱
    :param password:密码
    :param code:验证码
    :return: 注册结果
    """
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'msg': '该邮箱已注册'}), 400
    if str(code) != redis_client.get(email).decode('utf-8'):
        return jsonify({'msg': '验证码错误'}), 400
    hashed_password = hash_password(password)
    new_user = User(email=email, password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        user_id = User.query.filter_by(email=email).first().id
        user_name = 'user_' + generate_username()
        new_user_detail = UserDetail(user_id=user_id, user_name=user_name, signature='这个人很懒，什么都没有留下')
        db.session.add(new_user_detail)
        db.session.commit()
        return jsonify({'msg': '注册成功！', 'data': user_name}), 201
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'msg': '数据库发生错误，请稍后再试'}), 500


def get_user_by_id(user_id):
    """
    :param user_id: 用户 id
    :return: 获取用户的个人资料
    """
    user_alias = aliased(User)
    detail_alias = aliased(UserDetail)
    results = db.session.query(user_alias, detail_alias) \
        .outerjoin(detail_alias, user_alias.id == detail_alias.user_id) \
        .filter(user_alias.id == user_id).first()

    return jsonify({"msg": "success", "data": [_.to_dict() for _ in results]}), 200


def update_user_by_id(data):
    """
    :param data: 前端传递的待修改 json 数据
    :return: 更新用户的个人资料
    """

    # 更新 UserDetail 表中的信息
    user_id = data['user_id']
    if 'detail' in data:
        detail_data = data['detail']
        user_detail = UserDetail.query.filter_by(user_id=user_id).first()
        if user_detail:
            for key, value in detail_data.items():
                setattr(user_detail, key, value)
            db.session.commit()

    # 更新 User 表中的信息
    if 'user' in data:
        # 先校验验证码是否正确
        if data['user']['code'] is not None and data['user']['email'] is not None:
            code = str(data['user']['code'])
            email = data['user']['email']
            if code != redis_client.get(email).decode('utf-8'):
                return jsonify({'msg': '验证码错误'}), 400
        user = User.query.get(user_id)
        if 'password' in data['user']:
            user.password = hash_password(data['user']['password'])
        if 'email' in data['user']:
            user.email = data['user']['email']
        db.session.commit()

    return jsonify({"msg": "success", "data": "更新成功"}), 200


def record_daily_score(user_id, score):
    """
    计算热力图数据
    Args:
        user_id (str): 用户 ID.
        score (float):  分数。
    """
    print("dsdsaa111")
    date_str = datetime.now().strftime("%Y%m%d")  # 按照天为粒度计算用户每日活跃度
    key = f"score:user_{user_id}"
    try:
        redis_client.hincrbyfloat(key, date_str, score)
        print("ds11")
        print(f"用户 {user_id} 在 {date_str} 的分数增加 {score} 成功。")
    except Exception as e:
        print(f"Redis 操作失败：{e}")
    return f"用户 {user_id} 的分数已记录，增加了 {score}"


def get_daily_score(user_id):
    """
    获取 score:user_123 hash 的所有 field-value 并返回 JSON 格式数据。
    :param user_id: 用户 id
    :return:
    """
    try:
        last_login_time = User.query.filter_by(id=user_id).first().modify_time
        create_time = User.query.filter_by(id=user_id).first().create_time
        # 获取每日积分
        hash_data = redis_client.hgetall(f'score:user_{user_id}')
        if hash_data:
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
            return jsonify({"msg": "success", "data": {"heatMap": result_dict, "lastLoginTime": last_login_time,
                                                       "createTime": create_time}}), 200
        else:
            return jsonify({"msg": "每日活动情况为空，请检查 user_id "}), 404
    except Exception as e:
        print(e)
        return jsonify({"msg": "服务器[查询每日活动情况]异常，请稍后再试"}), 500
