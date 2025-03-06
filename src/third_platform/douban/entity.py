from src.basic.extensions import db
import datetime
import pytz
from sqlalchemy_serializer import SerializerMixin


class Douban(db.Model, SerializerMixin):
    __tablename__ = 'douban'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 自增主键
    user_id = db.Column(db.Integer, nullable=False)  # 对应的用户 ID
    img = db.Column(db.String(255))
    link = db.Column(db.String(255))
    name = db.Column(db.String(255))
    date = db.Column(db.TIMESTAMP)
    row_type = db.Column(db.String(255))
    content_type = db.Column(db.String(255))
    author = db.Column(db.String(255))
    language = db.Column(db.String(255))
    cur_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    create_time = db.Column(db.TIMESTAMP, default=cur_time)  # 创建时间，默认为当前时间
    serialize_rules = ('-row_type', '-id', '-user_id')

    def __init__(self, user_id, img, link, name, date, row_type, content_type, author, language):
        self.user_id = user_id
        self.img = img
        self.link = link
        self.name = name
        self.date = date
        self.row_type = row_type
        self.content_type = content_type
        self.author = author
        self.language = language

    def __repr__(self):
        return f"<Douban {self.name},{self.link}>"
