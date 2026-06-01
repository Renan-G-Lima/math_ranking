from flask import Blueprint, jsonify, request
from .service import generate_problem

problems_blueprint = Blueprint("problems", __name__)


@problems_blueprint.route("/problems", methods=["GET"])
def get_problems():

    if not (difficulty := request.args.get("difficulty")):
        return jsonify({"error": "Difficulty not provided"})

    if not (problem_type := request.args.get("type")):
        return jsonify({"error": "Problem type not provided"})

    problem = generate_problem(
        problem_type,
        difficulty
    )

    if problem.get("error"):
        return jsonify(problem)

    return jsonify(problem)
