from functools import wraps

import requests
from email_validator import EmailNotValidError, validate_email
from flask import jsonify, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from ..utils.config import *
from .model import *
from .user_test import validate_user

# Função para saber se o usuário já está registrado no banco de dados
def check_user(request_data):
    # Checa se as entradas são válidas
    request_type, is_valid = check_input(request_data)

    # Pega o email da requisição
    email = request_data.get("email")

    if not is_valid:
        return jsonify("Dados inseridos são incorretos", 400)

    # Checa se o email já está registrado
    if email_registered(email):
        return jsonify({"error": "Dados inseridos são incorretos"}, 401)

    # Se não estiver registrado, dá continuidade
    return jsonify({"status":"Sucesso"},200)


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
    if method == "Default":
        email = request.get(EMAIL_PARAM)
        senha = request.get(PASSWORD_PARAM)

        # Pega o hash no banco de dados
        user_db_hash = get_db_hash(email)

        # Se o hash existir e for igual, autentica, senão retorna
        if user_db_hash and check_password_hash(user_db_hash, senha):
            session["user_id"] = email
            return {"success": "Usuário autenticado."}, 200
        
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
    password = request_data.get(PASSWORD_PARAM)
    
    if request_method == "Default":
        # Checa se está no banco de dados
        if get_db_hash(email):

            return "Já está registrado"

        try:
            hash = generate_password_hash(password)
            date = datetime.now()

            # Adiciona novo usuário na tabela de maneira tradicional
            insert_default_user(email, hash, date)
            
            return True
            
        except:

            return "Ocorreu algum erro ao cadastrar usuário"
        
        

# Função que orquesta o fluxo de registro
def register_user(request_data, oauth=None):
    # Checa o método que o usuário escolheu
    request_method, is_valid = check_input(request_data, oauth)

    if is_valid == False:
        return jsonify("Não foi reconhecido nenhum dos métodos de registro", 400)
 
    # Checa se conseguiu registrar ou não
    registration_complete = register(request_data, request_method)
    if registration_complete != True:
        return jsonify(registration_complete, 400)
    
    
    
    # Se der tudo certo loga o usuário
    resposta = authenticate_user(request_data, request_method)

    return jsonify(resposta), resposta[1]


# Função que realiza o login do usuário
def login_user(request_data, oauth=None):

    # Checa se a entrada é válida
    request_method, is_valid = check_input(request_data, oauth)
  
    if is_valid == False:
        return jsonify("Não foi reconhecido nenhum dos métodos de login", 400)
   
    # Autentica o usuário com o método e os dados de entrada
    resposta = authenticate_user(request_data, request_method)
    
    # Retorna o resultado
    return jsonify(resposta), resposta[1]



# Função para conferir se a entrada é válida
def check_input(request, oauth=None):

    # Define Inválido por padrão
    login_type = "Default"
    is_valid = False

    # Checa se o login é com o google
    if oauth == "google":
        login_type = "Google"
        is_valid = True
    
    else:
    # Se não for, procura por algum campo email, senha e google_token
        try:
            email = request.get(EMAIL_PARAM)
            password = request.get(PASSWORD_PARAM)
        except:
            email = None
            password = None

        # Checa se foi encontrado algum email e senha
        if email and password:

            # Testa se o email é válido
            try:
                validate_email(email)
            # Senão retorna
            except EmailNotValidError:
                return {"status_code": "400"}, 400

            # Checa se a senha tem entre 6 e 12 números
            if 6 < len(password) < 12:
                return {"status_code": "400"}, 400
            
            login_type = "Default"
            is_valid = True

    return login_type, is_valid