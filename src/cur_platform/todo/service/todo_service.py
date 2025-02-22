from flask import jsonify
from sqlalchemy import and_
from src.basic.extensions import db
from src.cur_platform.todo.entity import MemEvent, Todo


def record_memday(user_id, mem_name, mem_date, mem_desc):
    """
    新增纪念日
    """
    mem_day = MemEvent(user_id=user_id, event_name=mem_name, event_date=mem_date, description=mem_desc)
    db.session.add(mem_day)
    db.session.commit()
    return jsonify({"msg": "success", "data": "新增纪念日成功"}), 201


def get_memday(user_id):
    """
    获取用户的所有纪念日
    """
    mem_day = MemEvent.query.filter_by(user_id=user_id).all()
    return jsonify({"msg": "success", "data": [_.to_dict() for _ in mem_day]}), 200


def record_todo(user_id, title, tags, set_time, finish_time):
    """
    新增todo
    """
    todo = Todo(user_id=user_id, title=title, tags=tags, set_time=set_time, finish_time=finish_time)
    db.session.add(todo)
    db.session.commit()
    return jsonify({"msg": "success", "data": "新增 todo 成功"}), 201


def get_todo(user_id, is_finished, tags, page, per_page=5):
    """
    获取用户的所有todo
    """
    conditions = [Todo.user_id == user_id]  # 基础条件
    if int(is_finished) == 1:
        conditions.append(Todo.finish_time != None)
    else:
        conditions.append(Todo.finish_time == None)

    if tags:
        conditions.append(Todo.tags == tags)

    paginated_result = Todo.query.filter(and_(*conditions)).paginate(page=int(page),
                                                                     per_page=per_page)  # 使用 and_ 连接所有条件
    todos = paginated_result.items  # 获取当前页的Todo列表
    total_pages = paginated_result.pages  # 获取总页数
    total_items = paginated_result.total  # 获取总条数
    todo_list = [todo.to_dict() for todo in todos]
    return jsonify({"msg": "success", "data": {'total_pages': total_pages, 'total_items': total_items,
                                               'items': todo_list}}), 200
