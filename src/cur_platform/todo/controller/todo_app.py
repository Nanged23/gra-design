from flask import request, Blueprint
from src.cur_platform.todo.service import todo_service

todo_bp = Blueprint('todo_bp', __name__, url_prefix='/todo')


# TODO todo的 deadline 通知功能

@todo_bp.route('/record_memday', methods=['POST'])
def record_day():
    # TODO 纪念日新增类别便签，以便展示对应背景
    """
    新增纪念日
    """
    params = request.get_json()
    mem_name = params.get('name')
    mem_date = params.get('date')
    user_id = params.get('user_id')
    mem_desc = params.setdefault('description', '')
    return todo_service.record_memday(user_id, mem_name, mem_date, mem_desc)


@todo_bp.route('/get_memday', methods=['GET'])
def get_day():
    """
    获取用户的所有纪念日
    """
    user_id = request.args.get('user_id')
    return todo_service.get_memday(user_id)


@todo_bp.route('/record_todo', methods=['POST'])
def record_todo():
    params = request.get_json()
    user_id = params.get('user_id')
    title = params.get('title')
    tags = params.get('tags')
    set_time = params.get('set_time')
    finish_time = params.get('finish_time')
    return todo_service.record_todo(user_id, title, tags, set_time, finish_time)


@todo_bp.route('/get_todo', methods=['GET'])
def get_todo():
    args = request.args
    user_id = args.get('user_id')
    is_finished = args.get('is_finished')
    tags = args.get('tags')
    page = args.get('page')
    return todo_service.get_todo(user_id, is_finished, tags, page)


@todo_bp.route('/monthly_todos', methods=['GET'])
def get_monthly_todos():
    args = request.args
    user_id = args.get("user_id")
    return todo_service.get_monthly_todos(user_id)


@todo_bp.route('/annually_todos', methods=['GET'])
def get_yearly_todos():
    args = request.args
    user_id = args.get("user_id")
    return todo_service.get_yearly_todos(user_id)
