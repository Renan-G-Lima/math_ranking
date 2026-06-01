"""
Esse arquivo é totalmente teste para validar os calculos via URL
"""

from flask import Blueprint, jsonify, request
from .service import validate_submission

submissions_test_blueprint = Blueprint("submissions_test", __name__)

@submissions_test_blueprint.route("/submit_test", methods=["GET"])
def submit_test():
    data = {
        "x": request.args.get("x"),
        "y": request.args.get("y"),
        "operation": request.args.get("operation"),
        "answer": request.args.get("answer"),
    }
    if not all(data.values()):
        return jsonify({"error": "Missing parameters"}), 400

    result = validate_submission(data)

    if result.get("error"):
        return jsonify(result), 400

    return jsonify(result)