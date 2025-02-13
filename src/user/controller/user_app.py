from flask import jsonify, request, Blueprint
from ..service import user_service
from ..service import code_verify

user_bp = Blueprint('user_bp', __name__, url_prefix="/user")


@user_bp.route('/login', methods=['POST'])
def user_login():
    params = request.get_json()
    email = params.get('email')
    password = params.get('password')
    return user_service.login(email, password)


@user_bp.route('/get_code', methods=['POST'])
def get_code():
    params = request.get_json()
    email = params.get('email')
    return code_verify.send_email(email)


@user_bp.route('/register', methods=['POST'])
def user_register():
    params = request.get_json()
    email = params.get('email')
    password = params.get('password')
    code = params.get('code')
    return user_service.register(email, password, code)


@user_bp.route('/detail', methods=['GET'])
def user_detail():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'msg': '请携带用户 id '}), 400
    data = user_service.get_user_by_id(user_id)
    return data


@user_bp.route('/update', methods=['POST'])
def user_update():
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({'msg': '不存在用户 id 或未有修改内容'}), 400
    return user_service.update_user_by_id(data)


@user_bp.route('/record_score', methods=['GET'])
def add_score():
    args = request.args
    user_id = args.get('user_id')
    score = args.get('score')
    return user_service.record_daily_score(user_id, float(score))


@user_bp.route('/get_score', methods=['GET'])
def get_score():
    user_id = request.args.get('user_id')
    return user_service.get_daily_score(user_id)
