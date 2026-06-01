import os
from app.problems.routes import problems_blueprint
from app.ranking.routes import ranking_blueprint
from app.submissions.routes import submissions_blueprint
from app.users.routes import user_blueprint
from app.utils.config import SECRET_KEY
from flask import Flask
from flask_cors import CORS

# Abaixo registrei uma rota totalmente teste vinda da submissions para teste via GET na URL
from app.submissions.routes_test import submissions_test_blueprint


def create_app():
    app = Flask(__name__)
    
    app.template_folder = "../../Frontend/"
    app.static_folder = "../../Frontend/"
    app.secret_key = SECRET_KEY
    CORS(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(problems_blueprint)
    app.register_blueprint(submissions_blueprint)
    app.register_blueprint(ranking_blueprint)

    # Rota de teste da submissions
    app.register_blueprint(submissions_test_blueprint)

    return app
