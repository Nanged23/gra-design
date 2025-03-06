from flask import jsonify, request, Blueprint
from src.third_platform.douban.service import douban_service

douban_bp = Blueprint('douban_bp', __name__, url_prefix="/douban")


@douban_bp.route('/data/', methods=['GET'])
def get_info():
    args = request.args
    user_id = args.get('user_id')
    category = args.get('category')
    page = args.get('page')
    return douban_service.get_data(user_id, category, page)


@douban_bp.route('/user/', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id')
    return douban_service.get_user(user_id)


@douban_bp.route('/demo', methods=['GET'])
# 向数据库写入数据用的接口
def geta():
    douban_service.temp()
    return jsonify({"mes": 1}), 200
