from flask import jsonify, request, Blueprint
from src.third_platform.douban.service import douban_service

douban_bp = Blueprint('douban_bp', __name__)


@douban_bp.route('/douban/book/', methods=['GET'])
def get_books_info():
    id = request.args.get('id')
    category = request.args.get('category')
    page = request.args.get('page')
    sort = request.args.get('sort')
    return douban_service.get_books(id, category, page, sort)


@douban_bp.route('/douban/movie/', methods=['GET'])
def get_movie_info():
    id = request.args.get('id')
    category = request.args.get('category')
    page = request.args.get('page')
    sort = request.args.get('sort')
    return douban_service.get_movies(id, category, page, sort)


@douban_bp.route('/douban/user/', methods=['GET'])
def get_user_info():
    id = request.args.get('id')
    return douban_service.get_user(id)
