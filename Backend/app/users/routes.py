from flask import Blueprint, request, jsonify
from .service import login_user

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/login", methods=["POST"])
def login():
    if (data := request.get_json()):
        result = login_user(data)
        return jsonify(result["status"] == "success")

    return jsonify(False)