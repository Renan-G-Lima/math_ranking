from flask import redirect, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from .config import EMAIL_PARAM, PASSWORD_PARAM, OAUTH_PARAM
from email_validator import validate_email, EmailNotValidError
db = {
    "email":"opa@gmail.com",
    "hash":"scrypt:32768:8:1$SRbaynN1oyijm4oa$da0f0e766343f1996ff9b2471cde112c93af416bd3ee791dc9b2367b1ab981ce59917f6b779794b6afc99eeb81f0b789e1ccd07dc0e0ef9944283b67abffef66" 
}

# Função para pegar o Hash no banco de dados
def get_db_hash(email):
    # Enquanto não pega no banco de dados
    if db["email"] == email:
        return db["hash"]


def is_logged_in():
    # Se estiver logado
    if session["user_id"]:
        return True
    
    # Caso contrário
    return False
# Função para conferir se a entrada é válida
def check_input(request):
    
    # Define inválido por padrão
    login_method = "Invalid"
    
    email = request.get(EMAIL_PARAM)
    password = request.get(PASSWORD_PARAM)
    google_token = request.get(OAUTH_PARAM)

    # Checa se a entrada é do tipo login tradicional
    if email and password:
        # Se for um email válido, continua, senão marca inválido
        try:
            validate_email(email)
        except EmailNotValidError:
            login_method = "Invalid"
        else:
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
        return function
    
    return need_login(f)

# Função para autenticar o usuário
def register_user(request, method):
    # Checa se está no banco de dados
    # Se estiver fala que está inválido
    # Se não estiver, salva no banco de dados
    ...

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

def register_user(request_data):
    # Checa o método que o usuário escolheu
    request_method = check_input(request_data)

    if request_method == "Invalid":
        return jsonify({"error": "Dados enviados de maneira inconvencional"})
    
    # Checa se conseguiu registrar ou não
    registration_complete = register(request_data,request_method)
    if registration_complete == False:
        return jsonify({"error":"Email ou Senha inválidos"})

    # Se der tudo certo loga o usuário
    resposta = authenticate_user(request_data,request_method)

    return jsonify(resposta)

    


def login_user(request_data):

    # Checa o método que o usuário escolheu
    request_method = check_input(request_data)

    if request_method == "Invalid":
        return jsonify({"error": "Dados enviados de maneira inconvencional"})

    # Autentica o usuário com o método e os dados de entrada
    resposta = authenticate_user(request_data, request_method)

    # Retorna o resultado
    return jsonify(resposta)