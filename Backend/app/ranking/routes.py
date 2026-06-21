from flask import Blueprint, jsonify

from .test_service import get_ranking

ranking_blueprint = Blueprint("ranking", __name__)

@ranking_blueprint.route("/ranking", methods=["GET"])
def ranking():
    data = get_ranking()
    return jsonify(data)
