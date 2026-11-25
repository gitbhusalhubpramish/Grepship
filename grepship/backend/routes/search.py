from flask import Blueprint, jsonify, request
from extensions import mongo

ser_bp = Blueprint("search", __name__, url_prefix="/api/search")

@ser_bp.route("/")
def search():
	query = request.args.get("q", "").strip()
	if not query:
		return jsonify({"error": "empty query"}), 400
	users = mongo.db.users.find({"username": {"$regex": query, "$options": "i"}}, {"_id":0, "username":1}).limit(10)
	return jsonify(users)

@ser_bp.route("/search")
def searchlong():
	query = request.args.get("q", "").strip()
	if not query:
		return jsonify({"error": "empty query"}), 400
	users = mongo.db.users.find({"username": {"$regex": query, "$options": "i"}}, {"_id":0, "username":1, "profile_pic":1})

	return jsonify(users)
