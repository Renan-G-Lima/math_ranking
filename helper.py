from flask import redirect, session
from werkzeug.security import generate_password_hash
from functools import wraps
from config import EMAIL_PARAM, PASSWORD_PARAM, OAUTH_PARAM


# Função para pegar o Hash no banco de dados
def get_db_hash(email):
    ...

# Função para conferir se a entrada é válida
def check_input(request):
    
    # Define inválido por padrão
    login_method = "Invalid"
    
    email = request.get(EMAIL_PARAM)
    password = request.get(PASSWORD_PARAM)
    google_token = request.get(OAUTH_PARAM)

    # Checa se a entrada é do tipo login tradicional
    if email and password:
        login_method = "Default"
    # Checa se a entrada é oauth do google, se não for, retorna inválido
    elif google_token:
        login_method = "Google"
    else:
        login_method = "Invalid"
    
    return login_method

# Função para garantir que páginas acessadas necessitem de login 
def login_required(f):
    @wraps(f)
    def need_login(function):
        if not session["user_id"]:
            return redirect("/login")
        ...

# Função para autenticar o usuário
def authenticate_user(request, method):
    if method == "Default":
        email = request.get(EMAIL_PARAM)
        senha = request.get(PASSWORD_PARAM)

        # Gera o hash e pega a senha no banco de dados 
        hash = generate_password_hash(senha)
        user_db_hash = get_db_hash(email)

        # Se o hash existir, compara, senão retorna
        if user_db_hash and hash == user_db_hash:
            ...
        else:
            return {"error":"Email ou senha inválidos"}
            
        ...
    elif method == "Google":
        ...
    


    # SOLUCIONAR ENTRADA
    ...