"""
创建 redis 数据库链接、声明 MySQL 的 ORM、创建 Executor 队列、创建 SocketIO 实例
"""
from flask_sqlalchemy import SQLAlchemy
import redis
import os
from dotenv import load_dotenv
from flask_executor import Executor
from flask_socketio import SocketIO
socketio = SocketIO()
load_dotenv()
# MySQL 的 ORM
db = SQLAlchemy()
# 创建 Redis 客户端实例
redis_client = redis.from_url(os.getenv("REDIS_LOCAL_URL"))
# 创建后台执行任务者
executor = Executor()
