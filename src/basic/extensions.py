"""
创建 redis 数据库链接
声明 MySQL 的 ORM
"""
from flask_sqlalchemy import SQLAlchemy
import redis
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from flask_executor import Executor

load_dotenv()
# MySQL 的 ORM
db = SQLAlchemy()
# 创建 Redis 客户端实例
redis_client = redis.from_url(os.getenv("REDIS_LOCAL_URL"))
# 创建后台执行任务者
executor = Executor()
