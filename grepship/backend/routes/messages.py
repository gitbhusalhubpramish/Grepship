from flask_socketio import emit, join_room
from extension import socketio, mongo
import requests

@socketio.on("send_message")
def new_msg(data):
	cookies = dict(request.cookies)
	response = requests.get("/api/auth/me", cookies=cookies, timeout=5)
	if response.status_code != 200:
		reutrn False
	mongo.db.chats.update_one({"participants": {"$all": [response.username, data.reciver]}, {"$push": {"messages": {"message":data.message, "time":data.time, "sender":response.username, "Isread": False}}}}, upsert=True)

	
