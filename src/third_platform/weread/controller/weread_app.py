from flask import jsonify, request, Blueprint
from src.third_platform.weread.service import authentication, weread_service
import threading

weread_bp = Blueprint('weread', __name__, url_prefix="/weread")

browser_instance = None
browser_lock = threading.Lock()
browser_initialized = False


# 登录整体流程介绍：请求登录->开启无头浏览器->从官网获取登录二维码->(login函数完毕)->扫码认证会在无头浏览器的官网网页中留下 cookie->从浏览器中截获 cookie->完成登录(get_cookies函数)

@weread_bp.route('/login', methods=['GET'])
async def login():
    """
    经检测，登录所需二维码约 3Kb，并不大，选择直接传输；如后续不满足性能要求，可考虑其他方案
    """
    try:
        global browser_instance
        browser_instance = await authentication.init_browser(browser_instance)
        qr_code_data = await authentication.get_qrcode(browser_instance)
        return jsonify({"mes": "success", "data": {"qrcode": qr_code_data}}), 200
    except Exception as e:
        print(e)
        return jsonify({"mes": "获取二维码超时"}), 500


@weread_bp.route('/cookies', methods=['POST'])
async def get_cookies():
    """
    点击页面上的“我已扫码”就调用本函数，尝试获取用户信息
    :return:传递给前端所需认证信息，前端需保存为 cookie 存储，并在之后的请求都携带本凭证
    """
    if not browser_instance:
        return jsonify("未获取到浏览器实例，！"), 500
    specific_cookies = await authentication.get_cookies(browser_instance)
    return jsonify({"mes": "success", "data": {"cookies": specific_cookies}}), 200


@weread_bp.route('/info', methods=['POST'])
def get_info():
    vid = request.cookies.get('vid')
    skey = request.cookies.get('skey')
    bookshelf_info = weread_service.get_user_bookshelf(vid, skey)
    user_info = weread_service.get_user_info(vid, skey)
    return jsonify({"msg": "success", "data": {"user_info": user_info, "bookshelf_info": bookshelf_info}}), 200


@weread_bp.route('/summary', methods=['POST'])
def get_summary():
    vid = request.cookies.get('vid')
    skey = request.cookies.get('skey')
    type = request.get_json().get('type')
    return weread_service.get_summary(vid, skey, type)


@weread_bp.route('/book_detail', methods=['GET'])
def get_book_detail():
    vid = request.cookies.get('vid')
    skey = request.cookies.get('skey')
    book_id = request.get_json().get('book_id')
    return weread_service.get_book_detail(vid, skey, book_id)
