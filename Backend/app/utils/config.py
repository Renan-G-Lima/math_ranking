from flask import Flask
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Cria uma instância do Flask
app = Flask(__name__)

# Define a chave secreta de sessões
SECRET_KEY = os.getenv("SECRET_KEY")

# Parâmetros do login tradicional
EMAIL_PARAM = "email"
PASSWORD_PARAM = "password"

#Parâmetros do login Oauth
OAUTH_PARAM = ""

# Váriaáveis que identificam o projeto no Google Bloud
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# URL de Callback após aautenticação
REDIRECT_URI = "http://localhost:5000/callback"

# URL para acessar a autenticação do Google
GOOGLE_API_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_API_TOKEN_URL = "https://oauth2.googleapis.com/token"