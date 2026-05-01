from flask import Blueprint, session, jsonify, redirect, render_template, request, url_for
from ..utils.config import *
from .service import (
    check_user,
    get_access_token,
    get_user_info,
    is_logged_in,
    login_user,
    register_user,
)


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["GET"])
def homepage():
    if is_logged_in():
        return render_template(HOME_URL)
    return render_template(INDEX_URL)

# Rota para apresentação do time
@user_blueprint.route("/team", methods=["GET"])
def team():
    return render_template(TEAM_URL)

# Rota para o sobre do projeto
@user_blueprint.route("/about", methods=["GET"])
def about():
    return render_template(ABOUT_URL)

# Rota paa o perfil do usuário
@user_blueprint.route("/perfil", methods=["GET"])
def perfil():
    return render_template(PERFIL_URL)

# Rota para a tabela de classificação
@user_blueprint.route("/leaderboard", methods=["GET"])
def leaderboard():
    return render_template(LEADERBOARD_URL)

# Rota para as configurações
@user_blueprint.route("/settings", methods=["GET"])
def settings():
    return render_template(SETTINGS_URL)

# Rota dos desafios
@user_blueprint.route("/challenges", methods=["GET"])
def challenges():
    return render_template(CHALLENGES_URL)

# Rota da calculadora
@user_blueprint.route("/calculator", methods=["GET"])
def calculator():
    return render_template(CALCULATOR_URL)

# Especificamente dos estudos.
@user_blueprint.route("/summStudy", methods=["GET"])
def summStudy():
    return render_template(SUMM_URL)
    


# Rota para login do usuário
@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Checa se o usuário já está logado
        if is_logged_in():
            return redirect("/")

        # Retorno alterado para render_template, a renderização da página não estava sendo exibida
        return render_template(LOGIN_URL)

    elif request.method == "POST":

        # Recebe a requisição do usuário
        request_data = request.get_json()

        # Loga o usuário e retorna se deu certo
        return login_user(request_data)

# Rota para logout do usuário
@user_blueprint.route("/logout", methods=["GET"])
def logout():
    try:

        if session["user_id"]:
            session.clear()

        return redirect("/team")
    except:
        return redirect("/")

# Rota para registrar um usuário de maneira tradicional
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

    #return is_valid_response

    return register_user(request_data)


# Rota para autorizar o login do oauth Google
@user_blueprint.route("/info/user", methods=["GET"])
def get_user():

    email = session["user_id"]

    info = get_user(email)
    
    return jsonify(info)

# Rota para autorizar o login do oauth Google
@user_blueprint.route("/authorize/google", methods=["GET"])
def login_google_authorize():

    # Prepara a url de autorização
    auth_url = GOOGLE_API_URL + "?"
    auth_url += f"client_id={GOOGLE_CLIENT_ID}"
    auth_url += f"&redirect_uri={GOOGLE_REDIRECT_URI}"
    auth_url += f"&scope={GOOGLE_SCOPE}"
    auth_url += "&response_type=code"

    # Se der tudo certo, envia para a página de autorização
    return redirect(auth_url)


# Receber a resposta da autorização de login do Google
@user_blueprint.route("/callback/google", methods=["GET", "POST"])
def login_google_callback():

    # Recebe o código de autorização
    auth_code = request.args.get("code")

    # Se recebeu esse código
    if auth_code:
        # Envia para o authentication server para pegar o acess token
        access_token = get_access_token(auth_code, "Google")

        # Obtém as informações principais do usuário com o token
        response = get_user_info(access_token, "Google")

        google_id = response["sub"]

        # Se tiver conta loga, se não tiver registra umanova
        login_user(google_id, "google")
        return response

    return "AUTHORIZATION CODE não foi recebido"