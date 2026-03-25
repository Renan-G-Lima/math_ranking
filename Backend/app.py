from flask import Flask, request
from app.modules.helper import *
from app.modules.config import app



# LOGIN DE USUÁRIO
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        # Checa se o usuário já está logado
        if is_logged_in():
            return redirect("/")
        
        # Se não envia página de login
        return "Página de login vem aqui"

    elif request.method == "POST":

        # Recebe a requisição do usuário
        request_data = request.json
        action = request_data.get("btn_action")

        # Se for Registro
        if action == "register":
            return register_user(request_data)
        # Se for Login
        elif action == "login":
            return login_user(request_data)
        
        # Checar se a requisição é válida e retornar o método de login
        

if __name__ == "__main__":
    app.run(debug=True)