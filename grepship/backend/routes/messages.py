from flask_socketio import emit, join_room
from extensions import socketio, mongo
import requests
from flask import Blueprint, request, jsonify
from utils.auth import auth_user_by_session

inb_bp = Blueprint("inbox", __name__, url_prefix="/api/inbox")

@socketio.on("send_message")
def new_msg(data):
	cookies = dict(request.cookies)
	response = requests.get("/api/auth/me", cookies=cookies, timeout=5)
	if response.status_code != 200:
		return jsonify({"error":"unathorized"}), 401
	mongo.db.chats.update_one({"participants": {"$all": [response.username, data.reciver]}}, {"$push": {"messages": {"message":data.message, "time":data.time, "sender":response.username, "Isread": False}}}, upsert=True)

	mongo.db.usrdata.update_one({"username": data.reciver}, {"$pull": {"chats": {"username": response.username}}})
	mongo.db.usrdata.update_one({"username": response.username}, {"$pull": {"chats": {"username": data.reciver}}})

	mongo.db.usrdata.update_one({"username": data.reciver}, {"$push": {"chats": {"$each":[{"username": response.username, "Isread":False}], "$position":0}}})
	mongo.db.usrdata.update_one({"username": response.username}, {"$push": {"chats": {"$each": [{"username": data.reciver, "Isread": True}], "$position":0}}})
	emit("new_message", {"username": response.username, "message": data.message, "time": data.time})

	print("Success")

@inb_bp.route("/search")
def search():
	query = request.args.get("q", "").strip()
	session = request.cookies.get("session_id")
	current_user = auth_user_by_session(session)

	if not query:
		return jsonify({"error": "empty query"}), 400
	chats = mongo.db.chats.find({"$and":[{"participants":current_user}, {"participants":{"$regex": query, "$options": "i"}}]}, {"participants":1, "_id":0})
	usernames = {user for chat in chats for user in chat["participants"]}
	usernames.discard(current_user)
	
	users = mongo.db.users.find({"username":{"$in": list(usernames)}}, {"_id":0, "username":1, "profile_pic":1})

	return jsonify({"users": users, "success":True, "ok":True}), 200

@inb_bp.route("/menu")
def menu():
	pass
