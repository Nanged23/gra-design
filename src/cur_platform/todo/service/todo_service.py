from flask import jsonify
from sqlalchemy import and_
from src.basic.extensions import db
from src.cur_platform.todo.entity import MemEvent, Todo
import datetime
import pytz
from sqlalchemy import func, cast, Date, Integer


def record_memday(user_id, mem_name, mem_date, mem_desc,category):
    """
    新增纪念日
    """
    mem_day = MemEvent(user_id=user_id, event_name=mem_name, event_date=mem_date, description=mem_desc,category=category)
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


def get_todo(user_id, is_finished, tags, page, type, per_page=5):
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
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))

    if type is None or type == "":
        conditions.append(Todo.set_time.is_(None))
    else:
        conditions.append(Todo.set_time >= now)
        if type == "recent":
            conditions.append(
                Todo.set_time <= now + datetime.timedelta(days=1))
        elif type == "future":
            conditions.append(
                Todo.set_time > now + datetime.timedelta(days=1))
    paginated_result = Todo.query.filter(and_(*conditions)).order_by(Todo.create_time.desc()).paginate(page=int(page),
                                                                                                       per_page=per_page)  # 使用 and_ 连接所有条件
    todos = paginated_result.items  # 获取当前页的Todo列表
    total_pages = paginated_result.pages  # 获取总页数
    total_items = paginated_result.total  # 获取总条数
    todo_list = [todo.to_dict() for todo in todos]
    return jsonify({"msg": "success", "data": {'total_pages': total_pages, 'total_items': total_items,
                                               'items': todo_list}}), 200


def get_todos(user_id, limit_time):
    # 查询近一个月的数据总行数
    total_count = db.session.query(Todo).filter(Todo.user_id == user_id, Todo.create_time >= limit_time).count()

    # 查询近一个月内 finish_time 字段不为空的行数
    finished_count = db.session.query(Todo).filter(
        Todo.user_id == user_id,
        Todo.create_time >= limit_time,
        Todo.finish_time != None
    ).count()

    # 准时完成的todo 数量
    ontime_finished_count = db.session.query(Todo).filter(
        Todo.user_id == user_id,
        Todo.create_time >= limit_time,
        Todo.finish_time != None,
        Todo.finish_time <= Todo.set_time
    ).count()

    # 最快速完成的todo
    fastest_todo = db.session.query(Todo).filter(
        Todo.user_id == user_id,
        Todo.create_time >= limit_time,
        Todo.finish_time != None
    ).order_by(
        (Todo.finish_time - Todo.create_time)  # 计算完成时间差
    ).first()

    # 最慢速完成的todo
    slowest_todo = db.session.query(Todo).filter(
        Todo.user_id == user_id,
        Todo.create_time >= limit_time,
        Todo.finish_time != None
    ).order_by(
        (Todo.finish_time - Todo.create_time).desc()  # 计算完成时间差
    ).first()

    # 完成todo 最多的一天
    most_productive_day = db.session.query(
        cast(Todo.finish_time, Date),  # 将 finish_time 转换为日期
        func.count()
    ).filter(
        Todo.user_id == user_id,
        Todo.create_time >= limit_time,
        Todo.finish_time != None
    ).group_by(
        cast(Todo.finish_time, Date)  # 按照日期分组
    ).order_by(
        func.count().desc()
    ).first()

    # 最久未完成的todo
    longest_pending_todo = db.session.query(Todo).filter(
        Todo.user_id == user_id,
        Todo.finish_time == None
    ).order_by(
        Todo.create_time
    ).first()

    # 各标签的总数量和完成率
    tag_summary = db.session.query(
        Todo.tags,
        func.count(),
        func.sum(cast(Todo.finish_time != None, Integer))  # 将布尔值转换为整数 (1 或 0)
    ).filter(
        Todo.user_id == user_id,
        Todo.create_time >= limit_time
    ).group_by(
        Todo.tags
    ).all()

    # 构建结果字典
    result = {
        "total_count": total_count,
        "finished_count": finished_count,
        "ontime_finished_count": ontime_finished_count,
        "fastest_todo": {
            "title": fastest_todo.title,
            "completion_time": (
                    fastest_todo.finish_time - fastest_todo.create_time).total_seconds()
        } if fastest_todo else None,
        "slowest_todo": {
            "id": slowest_todo.id,
            "title": slowest_todo.title,
            "completion_time": (
                    slowest_todo.finish_time - slowest_todo.create_time).total_seconds()
        } if slowest_todo else None,
        "most_productive_day": {
            "date": most_productive_day[0].strftime('%Y-%m-%d'),
            "count": most_productive_day[1]
        } if most_productive_day else None,
        "longest_pending_todo": {
            "id": longest_pending_todo.id,
            "title": longest_pending_todo.title,
            "create_time": longest_pending_todo.create_time.strftime(
                '%Y-%m-%d %H:%M:%S')
        } if longest_pending_todo else None,
        "tag_summary": [{
            "tag": tag,
            "total": total,
            "finished": finished,
            "completion_rate": (finished / total) * 100 if total > 0 else 0
        } for tag, total, finished in tag_summary]
    }

    return result


def get_monthly_todos(user_id):
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    one_month_ago = now - datetime.timedelta(days=30)
    return jsonify({"msg": "success", "data": get_todos(user_id, one_month_ago)}), 200


def get_yearly_todos(user_id):
    now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    one_year_ago = now - datetime.timedelta(days=365)
    return jsonify({"msg": "success", "data": get_todos(user_id, one_year_ago)}), 200
