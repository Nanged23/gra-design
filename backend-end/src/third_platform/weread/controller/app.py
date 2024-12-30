from flask import jsonify, request, Blueprint
from src.third_platform.weread.service.token import get_cookies
from src.third_platform.weread.service.token import init_browser
from src.third_platform.weread.service.token import get_qrcode
from src.third_platform.weread.service.user import get_user_bookshelf
from src.third_platform.weread.service.user import get_user_info

weread_bp = Blueprint('weread', __name__)

browser_instance = None


# index 路由
@weread_bp.route('/weread', methods=['GET'])
def home():
    return "这是有关微信阅读的路由！", 200


@weread_bp.route('/weread/login', methods=['GET'])
async def login():
    """
    经检测，登录所需二维码约 3Kb，并不大，选择直接传输；如后续不满足性能要求，可考虑其他方案
    :return:
    """
    global browser_instance
    browser_instance = await init_browser(browser_instance)
    qr_code_data = await get_qrcode(browser_instance)

    return jsonify({'qrcode': qr_code_data}), 200


@weread_bp.route('/weread/cookies', methods=['POST'])
async def get_cookies():
    """
    :return:传递给前端所需认证信息，之后的请求都携带本凭证
    """
    global browser_instance
    if not browser_instance:
        return jsonify("未获取到浏览器实例，！"), 500
    specific_cookies = await get_cookies(browser_instance)
    # TODO 需要存储在 redis 中
    return jsonify(specific_cookies), 200


@weread_bp.route('/weread/info', methods=['POST'])
def get_bookshelf():
    vid = request.cookies.get('vid')
    skey = request.cookies.get('skey')
    print(vid, skey)
    info1 = get_user_bookshelf(vid, skey)
    info2 = get_user_info(vid, skey)
    print(info1, info2)
    info2.update(info1)
    response = jsonify(info2)
    return response, 200
