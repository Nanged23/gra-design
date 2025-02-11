from flask import Flask, url_for, jsonify
from src.third_platform.weread.controller.weread_app import weread_bp
from src.user.controller.user_app import user_bp
from src.cur_platform.article.controller.article_app import article_bp
from src.cur_platform.todo.controller.todo_app import todo_bp
from src.third_platform.douban.controller.douban_app import douban_bp
from flask_cors import CORS
from src.basic.database import db
import traceback
from dotenv import load_dotenv
from src.basic.database import mysql_address

if __name__ == "__main__":
    load_dotenv()
    bps = [
        weread_bp,
        user_bp,
        douban_bp,
        article_bp,
        todo_bp
    ]
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = mysql_address
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    for bp in bps:
        app.register_blueprint(bp)


    @app.before_request
    def before_first_request():
        with app.app_context():
            # 在应用上下文中获取 api 地址并存储，方便其他蓝图调用
            add_score_url = url_for("user_bp.add_score", _external=True)
            app.config["ADD_SCORE_API"] = add_score_url


    @app.errorhandler(Exception)
    def handle_exception():

        print("======================⚠️：发生错误 ======================")
        tb = traceback.format_exc()  # 获取完整的堆栈跟踪信息
        print(tb)  # 打印到控制台
        print("======================⚠️：发生错误 ======================")

        return jsonify({'msg': '服务器内部错误'}), 500


    app.run(port=5000, debug=True, host="0.0.0.0")
