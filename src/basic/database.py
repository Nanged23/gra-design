"""
创建 redis 数据库链接
声明 MySQL 的 ORM
"""
from flask_sqlalchemy import SQLAlchemy
import redis
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
# MySQL 的 ORM
db = SQLAlchemy()

# Redis 连接
parsed_url = urlparse(os.getenv('REDIS_REMOTE_URL'))

pool = redis.ConnectionPool(
    host=parsed_url.hostname,
    port=parsed_url.port,
    password=parsed_url.password,
    db=0,
    decode_responses=True,
)

# 创建 Redis 客户端实例
redis_client = redis.Redis(connection_pool=pool)
