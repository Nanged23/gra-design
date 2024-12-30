from flask import jsonify, request, Blueprint
from src.user.service import user_service
from src.user.service import code_verify

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user/login', methods=['POST'])
def user_login():
    email = request.get_json().get('email')
    password = request.get_json().get('password')
    return user_service.login(email, password)


@user_bp.route('/user/get_code', methods=['POST'])
def get_code():
    email = request.get_json().get('email')
    return code_verify.send_email(email)


@user_bp.route('/user/register', methods=['POST'])
def user_register():
    email = request.get_json().get('email')
    password = request.get_json().get('password')
    return user_service.register(email, password)


@user_bp.route('/user/detail', methods=['GET'])
def user_detail():
    user_id = request.args.get('id')
    if not user_id:
        return jsonify({'data': '不存在用户 id '}), 400
    data = user_service.get_user_by_id(user_id)
    return data


@user_bp.route('/user/update', methods=['POST'])
def user_update():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({'data': '不存在用户 id 或未有修改内容'}), 400
    return user_service.update_user_by_id(data)
