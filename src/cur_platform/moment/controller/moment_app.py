from flask import jsonify, request, Blueprint
from src.cur_platform.moment.service import moment_service

moment_bp = Blueprint('moment_bp', __name__, url_prefix='/moment')


@moment_bp.route('/monthly_moods', methods=['GET'])
def get_monthly_moods():
    args = request.args
    user_id = args.get("user_id")
    return moment_service.get_monthly_moods(user_id)


@moment_bp.route('/annually_moods', methods=['GET'])
def get_yearly_moods():
    args = request.args
    user_id = args.get("user_id")
    return moment_service.get_yearly_moods(user_id)


@moment_bp.route('/write', methods=['POST'])
def write_memo():
    params = request.get_json()
    content = params.get('content')
    user_id = params.get('user_id')
    return moment_service.write_memo(content, user_id)


@moment_bp.route('/delete', methods=['POST'])
def delete_memo():
    params = request.get_json()
    moment_id = params.get('moment_id')
    return moment_service.delete_memo(moment_id)


@moment_bp.route('/get', methods=['GET'])
def get_memo():
    args = request.args
    user_id = args.get('user_id')
    page = args.get('page')
    return moment_service.get_memo(user_id, page)
