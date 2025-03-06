
from src.third_platform.douban.entity import Douban
from lxml import etree
import os
import re
from pypinyin import lazy_pinyin
from src.cur_platform.article.service.ai_service import get_summary
from src.cur_platform.article.entity import Article
from flask import jsonify, request, after_this_request
from src.basic.extensions import db, executor
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
import uuid
from dotenv import load_dotenv
from src.user.utils.add_score import add_score
from src.basic.extensions import redis_client
from collections import defaultdict
from sqlalchemy import and_
from sqlalchemy.sql.expression import func


