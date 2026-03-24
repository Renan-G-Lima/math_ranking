from flask import Blueprint, request, jsonify
from .service import validate_submission

submissions_blueprint = Blueprint("submissions", __name__)

@submissions_blueprint.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({
            "is_correct": False,
            "correct_answer": None,
            "difficulty": None,
            "error": "No data provided"
        })

    result = validate_submission(data)

    return jsonify(result)