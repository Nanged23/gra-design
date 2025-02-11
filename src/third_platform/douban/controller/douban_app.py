from flask import jsonify, request, Blueprint
from src.third_platform.douban.service import douban_service

douban_bp = Blueprint('douban_bp', __name__, url_prefix="/douban")


@douban_bp.route('/book/', methods=['GET'])
def get_books_info():
    args = request.args
    user_id = args.get('user_id')
    category = args.get('category')
    page = args.get('page')
    sort = args.get('sort')
    return douban_service.get_books(user_id, category, page, sort)


@douban_bp.route('/movie/', methods=['GET'])
def get_movie_info():
    args = request.args
    user_id = args.get('user_id')
    category = args.get('category')
    page = args.get('page')
    sort = args.get('sort')
    return douban_service.get_movies(user_id, category, page, sort)


@douban_bp.route('/user/', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id')
    return douban_service.get_user(user_id)
