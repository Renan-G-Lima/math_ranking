from .user_test import validate_user

def login_user(data):
    if (
        (email := data.get("email"))
         and (password := data.get("password"))
         and validate_user(email, password)
    ):
        
        return {"status": "success"}
    return {"status": "error", "message": "Invalid credentials"}
