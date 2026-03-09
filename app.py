from flask import Flask, request, jsonify
from helper import *
from config import app


# LOGIN DE USUÁRIO
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return "Página de login vem aqui"

    elif request.method == "POST":
        # Receber a requisição do usuário
        request_data = request.json
        # Se for Registro
        ...
        # Se for Login

        # Checar se a requisição é válida e retornar o método de login
        request_method = check_input(request_data)

        if request_method == "Invalid":
            print("erro")
            return jsonify({"error": "Dados enviados de maneira inconvencional"})


        # Autentica o usuário com o método e os dados de entrada
        resposta = authenticate_user(request_data, request_method)
        print(resposta)
        print(request_method)

        # Retorna o resultado
        return jsonify(resposta)

if __name__ == "__main__":
    app.run(debug=True)