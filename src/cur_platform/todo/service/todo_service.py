from flask import jsonify

from src.basic.database import db
from src.cur_platform.todo.entity import MemEvent


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
