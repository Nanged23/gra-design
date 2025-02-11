"""
创建 redis 数据库链接
声明 MySQL 的 ORM
"""
from flask_sqlalchemy import SQLAlchemy
import redis
import os
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
# 创建Redis连接池
pool = redis.ConnectionPool(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0, decode_responses=True)

# 创建Redis客户端实例
redis_client = redis.Redis(connection_pool=pool)

mysql_address = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    os.getenv('MYSQL_USER'),
    os.getenv('MYSQL_PASSWORD'),
    os.getenv('MYSQL_HOST'),
    os.getenv('MYSQL_PORT'),
    os.getenv('MYSQL_DB')
)
