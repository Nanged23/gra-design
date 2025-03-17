from src.basic.extensions import db
import datetime
import pytz
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import event


def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Shanghai'))


class Article(db.Model, SerializerMixin):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 自增主键
    title = db.Column(db.String(255), nullable=False)  # 密码，不允许为空
    slug = db.Column(db.String(255), nullable=False, unique=True)  # 邮箱，不允许为空，并且唯一
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    author_id = db.Column(db.Integer, nullable=False)  # 对应的作者 ID
    tags = db.Column(db.String(255))  # 标签
    cover = db.Column(db.String(255))  # 文章封面
    views_count = db.Column(db.Integer, nullable=False, default=0)
    cur_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    create_time = db.Column(db.TIMESTAMP, default=get_current_time)  # 创建时间，默认为当前时间
    modify_time = db.Column(db.TIMESTAMP, default=get_current_time)  # 修改时间，默认为当前时间，并在记录更新时自动更新
    serialize_rules = ('-create_time', '-author_id')

    def __init__(self, title, slug, content, excerpt, author_id, tags, cover):
        self.title = title
        self.slug = slug
        self.content = content
        self.excerpt = excerpt
        self.author_id = author_id
        self.tags = tags
        self.cover = cover

    def __repr__(self):
        return f"<Article {self.title},{self.content}>"


@event.listens_for(Article, 'before_update')
def update_modify_time(mapper, connection, target):
    # 检查 title, cover, content, tags 是否有变化
    if any([
        db.inspect(target).attrs.title.history.has_changes(),
        db.inspect(target).attrs.cover.history.has_changes(),
        db.inspect(target).attrs.content.history.has_changes(),
        db.inspect(target).attrs.tags.history.has_changes()
    ]):
        target.modify_time = get_current_time()
