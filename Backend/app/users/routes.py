from flask import Blueprint, jsonify, redirect, render_template, request, url_for
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

# @user_blueprint.route("/login", methods=["POST"])
# def login():
#    if (data := request.get_json()):
#        result = login_user(data)
#        return jsonify(result["status"] == "success")
#
#    return jsonify(False)


@user_blueprint.route("/", methods=["GET"])
def homepage():
    if is_logged_in():
        return render_template("Platform/pages/index.html")
    return render_template("Site/index.html")

@user_blueprint.route("/team", methods=["GET"])
def team():
    return render_template("Site/team.html")

@user_blueprint.route("/about", methods=["GET"])
def about():
    return render_template("Site/about.html")

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Checa se o usuário já está logado
        if is_logged_in():
            return redirect("/")

        # Retorno alterado para render_template, a renderização da página não estava sendo exibida
        return render_template("Platform/pages/login.html")

    elif request.method == "POST":

        # Recebe a requisição do usuário
        request_data = request.get_json()

        # Loga o usuário e retorna se deu certo
        return login_user(request_data)


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
    return is_valid_response


# Rota para autorizar o login do oauth Google
@user_blueprint.route("/authorize/google", methods=["POST"])
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
