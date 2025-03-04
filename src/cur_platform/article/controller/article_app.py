from flask import jsonify, request, Blueprint
from src.cur_platform.article.service import article_service

article_bp = Blueprint('article_bp', __name__, url_prefix='/article')


@article_bp.route('/write', methods=['POST'])
def write_article():
    params = request.form.to_dict()  # 用来处理 multipart/form-data 格式
    content = params.get('content')
    title = params.get('title')
    tags = params.get('tags')
    user_id = params.get('user_id')
    word_diff = params.get('word_diff')
    cover = request.files.get('cover')
    return article_service.write_article(title, content, user_id, tags, cover, word_diff)


@article_bp.route('/delete', methods=['GET'])
def delete_article():
    args = request.args
    article_id = args.get('article_id')
    word_diff = args.get('word_diff')
    return article_service.delete_article(article_id, word_diff)


@article_bp.route('/get', methods=['GET'])
def get_article():
    args = request.args
    user_id = args.get('user_id')
    type = args.get('type')  # 0:获取所有文章 1:获取单篇文章
    extra = args.get('extra')
    if extra is None or extra == '':
        if type == 1:
            return jsonify({'msg': '未获取到文章 id !'}), 400
        else:
            return jsonify({'msg': '未获取到当前页码 !'}), 400
    return article_service.get_article(user_id, type, extra)


@article_bp.route('/get_by_tags', methods=['GET'])
def get_by_tags():
    args = request.args
    user_id = args.get('user_id')
    extra = args.get('extra')
    tag = args.get('tag')
    return article_service.get_by_tags(user_id, extra, tag)


@article_bp.route('/update', methods=['POST'])
def update_article():
    params = request.form.to_dict()
    article_id = params.get('article_id')
    word_diff = params.get('word_diff')
    cover_file = request.files.get('cover')
    return article_service.update_article(article_id, params, cover_file, word_diff)


@article_bp.route('/word_cloud', methods=['GET'])
def get_word_cloud():
    user_id = request.args.get('user_id')
    return article_service.get_word_cloud(user_id)


@article_bp.route('/word_count', methods=['GET'])
def get_word_count():
    user_id = request.args.get('user_id')
    return article_service.get_word_count(user_id)


@article_bp.route('/most_viewed', methods=['GET'])
def get_most_viewed():
    user_id = request.args.get('user_id')
    return article_service.get_most_viewed(user_id)


@article_bp.route('/time_preference', methods=['GET'])
def get_time_preference():
    user_id = request.args.get('user_id')
    return article_service.get_time_preference(user_id)
