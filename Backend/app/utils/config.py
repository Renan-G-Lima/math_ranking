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