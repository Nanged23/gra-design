"""
创建 redis 数据库链接
声明 MySQL 的 ORM
"""
from flask_sqlalchemy import SQLAlchemy
import redis

db = SQLAlchemy()
# 创建Redis连接池
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

# 创建Redis客户端实例
redis_client = redis.Redis(connection_pool=pool)
