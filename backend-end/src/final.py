from flask import Flask
from src.third_platform.weread.controller.app import weread_bp
from src.user.controller.user_app import user_bp
from src.third_platform.douban.controller.douban_app import douban_bp
from flask_cors import CORS
from src.basic.database import db
from src.basic.marshmallow import ma

if __name__ == "__main__":
    bps = [weread_bp, user_bp, douban_bp]
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stream'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    for bp in bps:
        app.register_blueprint(bp)
    app.run(port=5000, debug=True, host="0.0.0.0")
