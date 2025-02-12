from flask import jsonify, request, Blueprint
from src.cur_platform.todo.service import todo_service

todo_bp = Blueprint('todo_bp', __name__, url_prefix='/todo')


@todo_bp.route('/record_memday', methods=['POST'])
def record_day():
    """
    新增纪念日
    """
    mem_name = request.get_json().get('name')
    mem_date = request.get_json().get('date')
    user_id = request.get_json().get('user_id')
    mem_desc = request.get_json().setdefault('description', '')
    return todo_service.record_memday(user_id, mem_name, mem_date, mem_desc)


@todo_bp.route('/get_memday', methods=['GET'])
def get_day():
    """
    获取用户的所有纪念日
    """
    user_id = request.args.get('user_id')
    return todo_service.get_memday(user_id)
