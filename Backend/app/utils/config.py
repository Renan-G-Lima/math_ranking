import os

from dotenv import load_dotenv
from flask import Flask

# Carregar variáveis do .env
load_dotenv()

# Cria uma instância do Flask
app = Flask(__name__)

# Define a chave secreta de sessões
SECRET_KEY = os.getenv("SECRET_KEY")

# Parâmetros do login tradicional
EMAIL_PARAM = "email"
PASSWORD_PARAM = "password"
NICK_PARAM = "username"
CURSO_PARAM = "curso"

# Parâmetros do login Oauth
OAUTH_PARAM = ""

# Váriaáveis que identificam o projeto no Google Bloud
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")


# URL para acessar a autenticação do Google
GOOGLE_API_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_API_TOKEN_URL = "https://oauth2.googleapis.com/token"
# URL de Callback após aautenticação
GOOGLE_REDIRECT_URI = "http://localhost:5500/callback/google"

GOOGLE_SCOPE = "openid email"

platform = "Platform/pages/"
site = "Site/"
LOGIN_URL = platform + "login.html"
HOME_URL =platform + "home.html"
INDEX_URL = site + "index.html"
TEAM_URL = site +"team.html"
ABOUT_URL = site + "about.html"
PERFIL_URL = platform + "perfil.html"
LEADERBOARD_URL = platform + "leaderboard.html"
SETTINGS_URL = platform + "settings.html"
CHALLENGES_URL = platform + "challenges.html"
CALCULATOR_URL = platform + "calculator/calculator.html"
SUMM_URL = platform + "prop/summ.html"
