from flask import Flask
from flask_cors import CORS
from app.users.routes import user_blueprint
from app.problems.routes import problems_blueprint
from app.submissions.routes import submissions_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(problems_blueprint)
    app.register_blueprint(submissions_blueprint)

    return app
