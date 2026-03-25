from flask import Blueprint, jsonify
from .service import spitter_of_sums

problems_blueprint = Blueprint("problems", __name__)

@problems_blueprint.route("/problems", methods=["GET"])
def get_problems():
    problem = spitter_of_sums()
    return jsonify(problem)