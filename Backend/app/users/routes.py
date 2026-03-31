from flask import Blueprint, request, jsonify, redirect, session, url_for
from .service import login_user, is_logged_in, check_user, register_user, get_oauth_data
from ..utils.config import GOOGLE_API_URL

user_blueprint = Blueprint("user", __name__)

#@user_blueprint.route("/login", methods=["POST"])
#def login():
#    if (data := request.get_json()):
#        result = login_user(data)
#        return jsonify(result["status"] == "success")
#
#    return jsonify(False)

@user_blueprint.route("/", methods=["GET"])
def homepage():
    return "<h1>Linda Página de Login</h1>"

@user_blueprint.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        # Checa se o usuário já está logado
        if is_logged_in():
            return redirect("/")
        
        # Se não envia página de login
        return "Página de login vem aqui"

    elif request.method == "POST":

        # Recebe a requisição do usuário
        request_data = request.get_json()
        
        # Loga o usuário e retorna se deu certo
        return login_user(request_data)
        


@user_blueprint.route("/register", methods=["POST"])
def register():
    # Recebe a requisição do usuário 
    request_data = request.get_json()
    
    # Checa se o usuário fornecido já está no banco de dados
    is_valid_response = check_user(request_data)

    # Se for o segundo botão de registro, cadastra o usuário.
    if request_data.get("btn_action") == "register_user":
        
        # Tenta registrar o usuário e retorna se deu certo
        return register_user(request_data)
    
    # Retorna se a entrada é válida
    return is_valid_response
    

@user_blueprint.route("/callback",methods=["GET","POST"])
def callback():
    # Recebe a requisição
    auth_code = request.args.get("code")
    if auth_code:
        return "Callback recebido"
    
    return "AUTHORIZATION CODE não foi recebido"

# Rota necessária para autorizar o login do oauth
@user_blueprint.route("/authorize", methods=["POST"])
def authorize():
    # Recebe a requisição do usuário 
    request_data = request.form.get("oauth")
    
    # Se o usuário tentar acessar o endpoint de autorizar sem fornecer um método
    if request_data != "google":
        # Redireciona para a página de login
        return redirect("/login")
    # Pega os dados necessários
    data = get_oauth_data(request_data)

    # Pega o client id, reirect_uri e o escopo
    client_id = data["client_id"]
    redirect_uri = data["redirect_uri"]
    scope = data["scope"]

    # Prepara a url de autorização
    auth_url = GOOGLE_API_URL + "?"
    auth_url += f"client_id={client_id}"
    auth_url += f"&redirect_uri={redirect_uri}"
    auth_url += f"&scope={scope}"
    auth_url += "&response_type=code"

    # Se der tudo certo, envia para a página de autorização
    return redirect(auth_url)

