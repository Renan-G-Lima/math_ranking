from flask import request, jsonify

user_badge = [
    {"email": "user", "password": "123"},
    {"email": "user1", "password": "123"},
    {"email": "user2", "password": "123"}
]

def validate_user(email, password):
    return any(
        email == user["email"] and password == user["password"]
        for user in user_badge
    )
