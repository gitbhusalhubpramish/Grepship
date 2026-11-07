# Messaging flow.

This is a bit complex part of the app so I have made a docs about this matter and planning about how to do work.

## Frontend

The frontend is writtern by next js env and with two file in it. The `page.js` file is the page file for next js which simpilly wraps the `inbox.js` file inside it and do some server site work like metadata which can't be done in client side (`"use client"`). 

### Interface

The interface is divided into three parts:

- **menu(reciver list):** This is a list of user to show messages notification and quick access for messaging or selecting a user to message. This includes cards of user which has profile pic at left then aside it their's username. It also renders a red button with animation when a user sends a message.

- **Inbox:** This is the main part of the app which only get rendered when a chat is selected. Here we can see chat history and send messages to the chat. Here if the message is sent it render to right else left(same as messenger). It also render profile pic (stored in `menu`) and message(in `inbox`).

- **Chat Option:** This part is the option of user like user details and about bolcking, reporting user or delete the chat. This is hidden by default.

### Flow

The flow looks like this:

- **Fetch history:** First the app fetch chats then fetches it's history if selected. This stores the profile pic and username of every chat also whether the message is read or not. The struct look like this:

```js
menu={
	[
		username: str,
		profilepic: str,
		Isread:bool,
	]
}
inbox = {
	[
		sent:bool,
		time: time,
		Isread: bool,
		message: str,
	]
}
```

- **Messages notification:** Here the app uses websoket api where server can send notification on client site. So, Here messages are rendered without refreshing the app. It fetch data from backend then render `message_body` parts to chat history and keep the chat in first.

- **Send messages:** Here Messages are sent by the user to chat. It includes `reciver`, `message` and `time`.


