from src.basic.extensions import db
import datetime
import pytz
from sqlalchemy_serializer import SerializerMixin


class Moment(db.Model, SerializerMixin):
    __tablename__ = 'moment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(1))
    cur_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    create_time = db.Column(db.TIMESTAMP, default=cur_time)
    serialize_rules = ('-id',)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"<Article {self.id}:{self.content}>"
