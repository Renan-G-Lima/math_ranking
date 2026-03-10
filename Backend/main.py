from flask import Flask, request, jsonify
from flask_cors import CORS
from app.users.user_test import login

app = Flask(__name__)
CORS(app)

app.add_url_rule("/login", view_func=login, methods=["POST"])

app.run(port=5500)