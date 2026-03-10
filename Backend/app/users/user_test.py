from flask import request, jsonify

user_badge = [
    {"email": "user", "password": "123"},
    {"email": "user1", "password": "123"},
    {"email": "user2", "password": "123"}
]

def login():
    user_data = request.json or {}

    for user in user_badge:
        if (
            user_data.get("email") == user["email"]
            and user_data.get("password") == user["password"]
        ):
            return jsonify(True)

    return jsonify(False)