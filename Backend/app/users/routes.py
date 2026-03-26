from flask import Blueprint, request, jsonify
from .service import login_user
from ..modules.helper import *

user_blueprint = Blueprint("user", __name__)

#@user_blueprint.route("/login", methods=["POST"])
#def login():
#    if (data := request.get_json()):
#        result = login_user(data)
#        return jsonify(result["status"] == "success")
#
#    return jsonify(False)


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

    # Loga o usuário e retorna se deu certo
    return register_user(request_data)
