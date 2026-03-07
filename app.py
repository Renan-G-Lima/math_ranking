from flask import Flask, request, jsonify
from helper import *
app = Flask(__name__)

credenciais_do_usuario = [
    {"email": "user", "password": "123"}
]


# LOGIN DE USUÁRIO
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return "Página de login vem aqui"

    elif request.method == "POST":
        # Receber a requisição do usuário
        request_data = request.json


        # Checar se a requisição é válida e retornar o método de login
        request_method = check_input(request_data)

        if request_method == "Invalid":
            return jsonify({"error": "Dados de entrada inválidos"})
        

        # Autentica o usuário com o método e os dados de entrada
        resposta = authenticate_user(request_data, request_method)

        # Retorna o resultado
        return jsonify(resposta)


app.run(debug=True)