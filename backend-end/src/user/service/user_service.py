"""
网站个人信息相关
"""
from flask import jsonify
from src.basic.database import db
import bcrypt
from sqlalchemy.orm import aliased
from src.user.entity import User
from src.user.entity import UserDetail
from src.user.entity import UserSchema
from src.user.entity import DetailSchema


def hash_password(password):
    # 生成盐，并对密码进行哈希
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def login(email, password):
    """
    :param email:邮箱
    :param password:密码
    :return: 登录结果
    """
    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'data': '邮箱或密码错误'}), 401
    return jsonify({'data': '登录成功'}), 200


def register(email, password):
    """
    :param email:邮箱
    :param password:密码
    :return: 注册结果
    """
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'data': '该邮箱已注册'}), 400

    hashed_password = hash_password(password)
    new_user = User(email=email, password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'data': '注册成功！'}), 201
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'data': '数据库发生错误，请稍后再试'}), 500


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

    user_schema = UserSchema()
    detail_schema = DetailSchema()

    # 将结果中的两个对象都序列化
    serialized_result = {
        'user': user_schema.dump(results[0]),
        'detail': detail_schema.dump(results[1]) if results[1] else None
    }
    return jsonify({"data": serialized_result}), 200


def update_user_by_id(data):
    """
    :param data: 前端传递的待修改 json 数据
    :return: 更新用户的个人资料
    """

    # 更新 UserDetail 表中的信息
    user_id = data['id']
    if 'detail' in data:
        detail_data = data['detail']
        user_detail = UserDetail.query.filter_by(user_id=user_id).first()
        if user_detail:
            for key, value in detail_data.items():
                setattr(user_detail, key, value)
            db.session.commit()

    # 更新 User 表中的信息
    if 'user' in data:
        user_data = data['user']
        user = User.query.get(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            db.session.commit()

    return jsonify({'data': "更新成功"}), 200
