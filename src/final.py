import os
from flask import Flask, request, jsonify, send_file
from src.basic.extensions import db, executor
from src.user.controller.user_app import user_bp
from src.cur_platform.todo.controller.todo_app import todo_bp
from src.cur_platform.article.controller.article_app import article_bp
from src.cur_platform.moment.controller.moment_app import moment_bp
from src.third_platform.weread.controller.weread_app import weread_bp
from src.third_platform.douban.controller.douban_app import douban_bp
from flask_cors import CORS
import traceback
from dotenv import load_dotenv
from flask_socketio import SocketIO
from pyppeteer import launch
import asyncio
from pyppeteer.errors import PyppeteerError

# 创建 Flask 应用
load_dotenv()
bps = [
    weread_bp,
    user_bp,
    douban_bp,
    article_bp,
    todo_bp,
    moment_bp
]
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = 'mys11ecret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_LOCAL_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

# 初始化扩展
db.init_app(app)
executor.init_app(app)

# 初始化 Flask-SocketIO
socketio = SocketIO(app, async_mode='threading', cors_allowed_origins="*")  # 允许跨域  # 使用 eventlet 作为异步模式

# 注册蓝图
for bp in bps:
    app.register_blueprint(bp)

browser_instances = {}
loop = None


# WebSocket 事件
@socketio.on('connect')
def handle_connect():
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    sid = request.sid
    print(f"客户端已连接: IP={client_ip}, User-Agent={user_agent}, SID={sid}")


@socketio.on('disconnect')
def handle_disconnect():
    print("客户端已断开")


browser_instance = None
loop = None


@socketio.on('message')
def handle_message():
    sid = request.sid

    async def fetch_qrcode():
        try:
            browser_instance = await launch(
                headless=True,
                handleSIGINT=False,
                handleSIGTERM=False,
                handleSIGHUP=False,
                executablePath='/Users/dongliwei/Downloads/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing',
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )
            browser_instances[sid] = browser_instance
            page = await browser_instance.newPage()
            await page.goto('https://r.qq.com#login', {'waitUntil': 'load', 'timeout': 30000})
            await page.waitForSelector('img[src^="data:image/png;base64"]', {'timeout': 10000})
            qrcode_data = await page.evaluate('''() => {
                 const img = document.querySelector('img[src^="data:image/png;base64"]');
                 return img ? img.src : null;
             }''')
            return qrcode_data
        except Exception as e:
            print(f"错误:{e}")
            return None

    try:
        global loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        qrcode_data = loop.run_until_complete(fetch_qrcode())
        if qrcode_data:
            socketio.emit("message", qrcode_data, to=sid)
        else:
            print(f"发送错误信息 (二维码获取失败): SID={sid}")
            socketio.emit("error", "无法获取二维码", to=sid)
    except Exception as e:
        print(f"处理 message 错误: SID={sid}, 错误: {type(e).__name__}: {e}")


@socketio.on("cookie_data")
def get_weread_cookie():
    sid = request.sid
    print(f"收到 cookie_data 请求: SID={sid}")
    browser_instance = browser_instances[sid]

    async def fetch_cookie(browser, max_retries=5):
        specific_cookies = {
            'wr_vid': None,
            'wr_skey': None
        }
        cnt = 0
        try:
            print(f"创建新页面: SID={sid}")
            page = await browser.newPage()
            print(f"加载页面: https://weread.qq.com/, SID={sid}")
            await page.goto('https://weread.qq.com/', {'waitUntil': 'load', 'timeout': 30000})
            while not all(specific_cookies.values()) and cnt < max_retries:
                print(f"获取 cookies: 尝试 {cnt + 1}, SID={sid}")
                all_cookies = await page.cookies()
                for cookie in all_cookies:
                    if cookie.get('name') == 'wr_vid':
                        specific_cookies['wr_vid'] = cookie.get('value')
                    elif cookie.get('name') == 'wr_skey':
                        specific_cookies['wr_skey'] = cookie.get('value')
                if all(specific_cookies.values()):
                    break
                await asyncio.sleep(0.5)  # Short delay before reload
                print(f"重新加载页面以获取 cookies: SID={sid}")
                await page.reload({'waitUntil': 'load', 'timeout': 30000})
                cnt += 1
            print(f"Cookies 获取结果: {specific_cookies}, SID={sid}")
            return specific_cookies
        except Exception as e:
            print(f"获取 cookies 时发生其他错误: SID={sid}, 错误: {type(e).__name__}: {e}")
            return None

    browser_to_close = None
    try:
        global loop
        asyncio.set_event_loop(loop)
        specific_cookies = loop.run_until_complete(fetch_cookie(browser_instance))

        if specific_cookies and all(specific_cookies.values()):
            print(f"发送 cookies 数据: SID={sid}")
            socketio.emit("cookie_data", specific_cookies, to=sid)
        else:
            print(f"发送错误信息 (无法获取 cookies): SID={sid}")
            socketio.emit("error", {"msg": "无法获取 cookies，请稍后重试或重新扫码"}, to=sid)

    except Exception as e:
        # Catch errors during the async execution or handler logic
        print(f"处理 cookie_data 错误: SID={sid}, 错误: {type(e).__name__}: {e}")
        socketio.emit("error", {"msg": f"处理请求时出错: {str(e)}"}, to=sid)

    finally:
        browser_to_close = browser_instances.pop(sid, None)

        if browser_to_close:
            if loop and not loop.is_closed():  # Check if loop is valid
                try:
                    print(f"尝试关闭浏览器实例: SID={sid}")
                    loop.run_until_complete(browser_to_close.close())
                    print(f"浏览器实例已关闭: SID={sid}")
                except RuntimeError as e:
                    # Specifically handle "Event loop is closed" error
                    if "Event loop is closed" in str(e):
                        print(f"关闭浏览器失败: SID={sid}, 错误: 事件循环已关闭")
                        # Attempt cleanup without loop (less ideal, might leak process)
                    else:
                        print(f"关闭浏览器时发生运行时错误: SID={sid}, 错误: {e}")
                except Exception as e:
                    print(f"关闭浏览器失败: SID={sid}, 错误: {e}")
            else:
                print(f"无法使用事件循环关闭浏览器 (循环无效或已关闭): SID={sid}")


# 根路由
@app.route('/', methods=['GET'])
def root():
    return jsonify({'🎉 接口文档': 'https://nanged23.apifox.cn/'}), 200


# 404 错误处理
@app.errorhandler(404)
def not_found(error):
    return send_file('./assert/404.jpeg', mimetype='image/png')


# 全局异常处理
@app.errorhandler(Exception)
def handle_exception(e):
    print("⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ ⚠️：发生错误 ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
    tb = traceback.format_exc()
    print(tb)
    print("⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆ ⚠️：发生错误 ⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆")
    return jsonify({'msg': '服务器内部错误'}), 500


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True, allow_unsafe_werkzeug=True)
    # app.run(host="0.0.0.0", port=5000, debug=True)
