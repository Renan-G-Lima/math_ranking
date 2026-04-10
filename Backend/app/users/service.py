from functools import wraps

import requests
from email_validator import EmailNotValidError, validate_email
from flask import jsonify, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash

from ..utils.config import *
from .model import *
from .user_test import validate_user


#def login_user(data):
#    if (
#        (email := data.get("email"))
#        and (password := data.get("password"))
#        and validate_user(email, password)
#    ):
#        return {"status": "success"}
#    return {"status": "error", "message": "Invalid credentials"}


# Função para saber se o usuário já está registrado no banco de dados
def check_user(request_data):
    # Pega o email da requisição
    email = request_data.get("email")

    # Checa se as entradas são válidas
    is_valid = check_input(request_data)

    if type(is_valid) != list:
        return is_valid

    # Checa se o email já está registrado
    if get_db_email(email):
        return jsonify({"status_code": "401"})

    # Se não estiver registrado, dá continuidade
    return jsonify({"status_code": "200"})


# Função pra saber se o usuário está logado
def is_logged_in():
    try:
        # Se estiver logado
        if session["user_id"]:
            return True
    except:
        # Caso contrário
        return False


# Função para trocar um código de autorização por um código de autenticação
def get_access_token(auth_code, method=None):
    if method == "Google":
        # Envia para o authentication server para pegar o acess token
        response = requests.post(
            GOOGLE_API_TOKEN_URL,
            data={
                "code": auth_code,
                "grant_type": "authorization_code",
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "redirect_uri": GOOGLE_REDIRECT_URI,
            },
        )

        # Pega o token de acesso retornado
        access_token = response.json()["access_token"]

        return access_token


# Função para pegar informações do usuário a partir de um código de autenticaçãop
def get_user_info(code, method=None):
    if method == "Google":
        response = requests.post(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers={"authorization": f"Bearer {code}"},
        )
        return response.json()


# Função para conferir se a entrada é válida
def check_input(request, oauth=None):

    # Define inválido por padrão
    login = ["Default", "Valid"]

    # Procura por algum campo email, senha e google_token
    email = request.get(EMAIL_PARAM)
    password = request.get(PASSWORD_PARAM)

    # Checa se a entrada é o email e senha tradicional
    if email and password:
        # Se for um email válido, continua, senão marca inválido
        try:
            validate_email(email)
        except EmailNotValidError:
            return {"status_code": "400"}, 400

        # Se a senha tiver o tamanho certo, continua
        if 6 < len(password) < 12:
            return {"status_code": "400"}, 400

    # Checa se a entrada é oauth do google
    elif oauth == "google":
        login[0] = "Google"
    else:
        return {"status_code": "400"}, 400

    return login


# Função para garantir que páginas acessadas necessitem de login
def login_required(f):
    @wraps(f)
    def need_login(function):
        if not session["user_id"]:
            return redirect("/login")
        return function

    return need_login(f)


# Função para autenticar o usuário
def register_user(request, method):
    # Checa se está no banco de dados
    # Se estiver fala que está inválido
    # Se não estiver, salva no banco de dados
    ...


# Função para autenticar o usuário, fornecendo uma sessão
def authenticate_user(request, method):
    if method[0] == "Default":
        email = request.get(EMAIL_PARAM)
        senha = request.get(PASSWORD_PARAM)

        # Gera o hash e pega a senha no banco de dados
        user_db_hash = get_db_hash(email)

        # Se o hash existir, compara, senão retorna

        if user_db_hash and check_password_hash(user_db_hash, senha):
            session["user_id"] = email
            return {"success": "Usuário autenticado."},200
        else:
            
            return {"error": "Email ou senha inválidos."},400
    elif method == "Google":
        # Checa se o usuário está no banco de dados

        # Se estiver, loga
        # Se não estiver, cria um novo
        ...


# Função para registrar o usuário no banco de dados (Login Tradicional)
def register(request_data, request_method):
    email = request_data.get(EMAIL_PARAM)

    if request_method == "Default":
        # Checa se está no banco de dados
        if get_db_hash(email):
            return "Já está registrado"

        # Se não registra o usuário e a senha no banco de dados
        ...


# Função que orquesta o fluxo de registro
def register_user(request_data):
    # Checa o método que o usuário escolheu
    request_method = check_input(request_data)

    if type(request_method) != list:
        return request_method

    # Checa se conseguiu registrar ou não
    registration_complete = register(request_data, request_method[0])
    if registration_complete != True:
        return registration_complete

    # Se der tudo certo loga o usuário
    resposta = authenticate_user(request_data, request_method[0])

    return jsonify(resposta)


# Função que realiza o login do usuário
def login_user(request_data, oauth=None):

    # Checa se a entrada é válida
    request_method = check_input(request_data, oauth)
  
    if type(request_method) != list:
        return request_method
   
    # Autentica o usuário com o método e os dados de entrada
    resposta = authenticate_user(request_data, request_method)
    # Retorna o resultado
    return jsonify(resposta[0]), resposta[1]
