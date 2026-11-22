from flask_socketio import emit, join_room
from extensions import socketio, mongo
import requests
from flask import Blueprint, request, jsonify
from utils.auth import auth_user_by_session

inb_bp = Blueprint("inbox", __name__, url_prefix="/api/inbox")

@socketio.on("connect")
def handel_connect():
	print("connecting...")
	session= request.cookies.get("session_id")
	print(session)
	user= auth_user_by_session(session)
	if not user:
		return False


@socketio.on("send_message")
def new_msg(data):
	print("hey")
	session = request.cookies.get("session_id")
	print(session)
	response = auth_user_by_session(session)
	print(data)
	
	reciver = data.get("reciver")
	print(reciver)
	message= data.get("message")

	if response is None:
		print("auth", response)
		return {"status":"error", "message": "Unauthorized"}
	
	newmsg = {"message": message, "time": data.get("time"), "sender": response["username"], "Isread": False}

	chat = mongo.db.chats.find_one({"participants": {"$all": [response["username"], reciver]}})
	print(chat)

	if chat:
		mongo.db.chats.update_one({"_id": chat["_id"]}, {"$push": {"message": newmsg}})
	else:
		mongo.db.chats.insert_one({"participants": [response["username"], reciver], "message": [newmsg]})

#	mongo.db.chats.update_one({"participants": {"$all": [response["username"], reciver]}}, {"$push": {"messages": {"message":message, "time":data.get("time"), "sender":response["username"], "Isread": False}}}, upsert=True)

	mongo.db.user.update_one({"username": reciver}, {"$pull": {"friends": {"username": response["username"]}}})
	mongo.db.user.update_one({"username": response["username"]}, {"$pull": {"friends": {"username": reciver}}})

	mongo.db.usrdata.update_one({"username": reciver}, {"$push": {"chats": {"$each":[{"username": response["username"], "Isread":False}], "$position":0}}})
	mongo.db.usrdata.update_one({"username": response["username"]}, {"$push": {"friends": {"$each": [{"username": reciver, "Isread": True}], "$position":0}}})
	emit("new_message", {"username": reciver, "message": message, "time": data.get("time")})

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
	session = request.cookies.get("session_id")
	current_user = auth_user_by_session(session)
	if current_user is None:
		return {"error": "auth error"}, 401
	print(current_user)
	friends = mongo.db.users.find_one({"username": current_user["username"]}, {"friends":1, "_id":0})
	print(friends["friends"])
	friends_data = mongo.db.users.find({"username":{"$in": list(friends["friends"] or [])}}, {"_id":0, "username":1, "profile_pic":1})
	print(friends_data)
	return jsonify(friends_data), 200

@inb_bp.route("/<username>")
def chat(username):
	session = request.cookies.get("session_id")
	current_user = auth_user_by_session(session)
	if current_user is None:
		return {"error": "auth error"}, 401
	cht = mongo.db.chats.find_one({"participants":{"$all": [current_user["username"], username]}})
	print(cht)
	return jsonify(cht or []), 200

