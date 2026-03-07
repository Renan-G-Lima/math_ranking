# Função para checar se a entrada é válida


def check_input(request):
    
    # Define inválido por padrão
    login_method = "Invalid"
    
    # Checa se a entrada é do tipo login tradicional
    try:
        email = request.get("email")
        password = request.get("password")     
        login_method = "Default"
    except:
        pass

    # Checa se a entrada é oauth do google, se não for, retorna inválido
    try:
        google_token = request.get("google_token")
        login_method = "Google"
    except:
        pass
    
    return login_method

    
# Função para autenticar o usuário
def authenticate_user(request, method):

    if method == "Default":
        # Gerar o hash da senha
        # Checar se o hash existe no banco de dados
        # Checar se a senha corresponde ao hash armazenado
        ...
    elif method == "Google":
        ...
    


    # SOLUCIONAR ENTRADA
    ...