from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.users.user_test import login

    #app.add_url_rule("/login", view_func=login, methods=["POST"])
    app.add_url_rule("/login", view_func=login, methods=["GET"])

    return app
