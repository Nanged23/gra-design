import os
from flask import Flask, url_for, jsonify, request, send_file
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
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_LOCAL_URL")
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
#     'connect_args': {'ssl': {'ca': '/etc/secrets/cert.pem'}}
# }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)
executor.init_app(app)
for bp in bps:
    app.register_blueprint(bp)


@app.route('/', methods=['GET'])
def root():
    return jsonify({'🎉 接口文档': 'https://nanged23.apifox.cn/'}), 200


@app.errorhandler(404)
def not_found(error):
    return send_file('./assert/404.jpeg', mimetype='image/png')


@app.before_request
def before_first_request():
    # url = request.url
    # if url.startswith("https://"):  # 说明是从平台内部访问的 Redis，修改为内部访问地址
    #     inner_redis_url = os.getenv("REDIS_INNER_URL")
    #     database.redis_client = database.redis.from_url(inner_redis_url)

    with app.app_context():
        # 将增加积分的逻辑暴露给所有接口
        add_score_url = url_for("user_bp.add_score", _external=True)
        app.config["ADD_SCORE_API"] = add_score_url


@app.errorhandler(Exception)
def handle_exception(e):
    print("⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇ ⚠️：发生错误 ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
    tb = traceback.format_exc()  # 获取完整的堆栈跟踪信息
    print(tb)  # 打印到控制台
    print("⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆ ⚠️：发生错误 ⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆")

    return jsonify({'msg': '服务器内部错误'}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=False, host="0.0.0.0")
