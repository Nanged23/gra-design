from src.basic.extensions import db
import datetime
import pytz
from sqlalchemy_serializer import SerializerMixin


class MemEvent(db.Model, SerializerMixin):
    __tablename__ = 'mem_event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 自增主键
    user_id = db.Column(db.Integer, nullable=False)  # 用户Id
    event_name = db.Column(db.String(255), nullable=False)  # 纪念日事件名称
    event_date = db.Column(db.TIMESTAMP, nullable=False)  # 纪念日日期
    description = db.Column(db.Text)  # 事件描述
    cur_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    create_time = db.Column(db.TIMESTAMP, default=cur_time)  # 创建时间，默认为当前时间
    update_time = db.Column(db.TIMESTAMP, default=cur_time, onupdate=cur_time)  # 修改时间，默认为当前时间，并在记录更新时自动更新
    serialize_rules = ('-create_time', '-update_time', '-id', '-user_id')

    def __init__(self, user_id, event_name, event_date, description):
        self.user_id = user_id
        self.event_name = event_name
        self.event_date = event_date
        self.description = description

    def __repr__(self):
        return f"<MemEvent {self.event_name} on {self.event_date}>"
