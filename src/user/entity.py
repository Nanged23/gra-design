from src.basic.database import db
from src.basic.marshmallow import ma
import datetime
import pytz


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 自增主键
    email = db.Column(db.String(255), nullable=False, unique=True)  # 邮箱，不允许为空，并且唯一
    password = db.Column(db.String(255), nullable=False)  # 密码，不允许为空
    cur_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    create_time = db.Column(db.TIMESTAMP, default=cur_time)  # 创建时间，默认为当前时间
    modify_time = db.Column(db.TIMESTAMP, default=cur_time, onupdate=cur_time)  # 修改时间，默认为当前时间，并在记录更新时自动更新

    def __init__(self, email, password):
        self.email = email
        self.password = password  # 注意：这里应该存储的是已经哈希过的密码

    def __repr__(self):
        return f"<User {self.email}>"


class UserDetail(db.Model):
    __tablename__ = 'user_detail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    signature = db.Column(db.String(255))
    wechat_id = db.Column(db.String(255))
    wechat_token = db.Column(db.String(255))
    douban_id = db.Column(db.String(255))
    keep_phone = db.Column(db.String(11))
    keep_password = db.Column(db.String(255))
    cur_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    create_time = db.Column(db.TIMESTAMP, default=cur_time)  # 创建时间，默认为当前时间
    modify_time = db.Column(db.TIMESTAMP, default=cur_time, onupdate=cur_time)  # 修改时间，默认为当前时间，并在记录更新时自动更新

    def __repr__(self):
        return f"<UserDetail(id={self.id}, user_id={self.user_id})>"


# 定义 User 的 Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True  # 可选：用于反序列化


# 定义 UserDetail 的 Schema
class DetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserDetail
        sqla_session = db.session
        load_instance = True  # 可选：用于反序列化
