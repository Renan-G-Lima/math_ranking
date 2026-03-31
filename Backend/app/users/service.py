from flask import redirect, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from ..utils.config import *
from email_validator import validate_email, EmailNotValidError

from .user_test import validate_user

db = {
    "email":"opa@gmail.com",
    "hash":"scrypt:32768:8:1$SRbaynN1oyijm4oa$da0f0e766343f1996ff9b2471cde112c93af416bd3ee791dc9b2367b1ab981ce59917f6b779794b6afc99eeb81f0b789e1ccd07dc0e0ef9944283b67abffef66" 
}

def login_user(data):
    if (
        (email := data.get("email"))
         and (password := data.get("password"))
         and validate_user(email, password)
    ):   
        return {"status": "success"}
    return {"status": "error", "message": "Invalid credentials"}




# Função para pegar o Hash de um email no banco de dados
def get_db_hash(email):
    # Enquanto não pega no banco de dados
    if db["email"] == email:
        return db["hash"]
    
# Função para pegar um determinado email no banco de dados
def get_db_email(email):
    if db["email"] == email:
        return True
def get_oauth_data():
    return {"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET,"redirect_uri":REDIRECT_URI,"scope":"openid"}# Função para saber se o usuário já está registrado no banco de dados
def check_user(request_data):
    # Pega o email da requisição
    email = request_data.get("email")

    # Checa se as entradas são válidas
    is_valid = check_input(request_data)

    if type(is_valid) != list:
        return is_valid
    
    # Checa se o email já está registrado
    if get_db_email(email):
        return jsonify({"status_code":"401"})

    # Se não estiver registrado, dá continuidade
    return jsonify({"status_code":"200"})

# Função pra saber se o usuário está logado
def is_logged_in():
    # Se estiver logado
    if session["user_id"]:
        return True
    
    # Caso contrário
    return False


# Função para conferir se a entrada é válida
def check_input(request):
    
    # Define inválido por padrão
    login = ["Default","Valid"]
    
    # Procura por algum campo email, senha e google_token
    email = request.get(EMAIL_PARAM)
    password = request.get(PASSWORD_PARAM)
    google_token = request.get(OAUTH_PARAM)

    # Checa se a entrada é o email e senha tradicional 
    if email and password:
        # Se for um email válido, continua, senão marca inválido
        try:
            validate_email(email)
        except EmailNotValidError:
            return jsonify({"status_code":"400"})
        
        # Se a senha tiver o tamanho certo, continua
        if 6 < len(password) < 12:
            return jsonify({"status_code":"400"})
        
    # Checa se a entrada é oauth do google
    elif google_token:
        login[0] = "Google"
    else:
        return jsonify({"status_code":"400"})
    
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
    if method == "Default":
        email = request.get(EMAIL_PARAM)
        senha = request.get(PASSWORD_PARAM)

        # Gera o hash e pega a senha no banco de dados 
        user_db_hash = get_db_hash(email)
        
        # Se o hash existir, compara, senão retorna

        if user_db_hash and check_password_hash(user_db_hash, senha):
            session["user_id"] = email
            return {"success":"Usuário autenticado."}
        else:
            return {"error":"Email ou senha inválidos."}
    elif method == "Google":
        ...

# Função para registrar o usuário no banco de dados
def register(request_data, request_method):
    email = request_data.get(EMAIL_PARAM)

    if request_method == "google":
         ...
    elif request_method == "Default":
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
    registration_complete = register(request_data,request_method[0])
    if registration_complete != True:
        return registration_complete

    # Se der tudo certo loga o usuário
    resposta = authenticate_user(request_data,request_method[0])

    return jsonify(resposta)

    

# Função que realiza o login do usuário
def login_user(request_data):

    # Checa se a entrada é válida
    request_method = check_input(request_data)

    if type(request_method) != list:
        return request_method

    # Autentica o usuário com o método e os dados de entrada
    resposta = authenticate_user(request_data, request_method)

    # Retorna o resultado
    return jsonify(resposta)