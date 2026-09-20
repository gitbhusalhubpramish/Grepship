# Grepship

A simple messaging app for friends and small teams. It works in your browser, no ads, no signup fees. It was made using next.js, python flask, tailwind by team peanguin - [Pramish Bhusal](https://github.com/gitbhusalhubpramish) and [Hemanta Kendel](https://github.com/hemanta-kandel)

Repo: [Grepship](https://github.com/gitbhusalhubpramish/Grepship)

## Feature and page navigation

- **User auth:** User auth data is handel by mongodb database and backend is writtern by flask - we check user session, and signup/login in this auth session.

- **Interactive UI:** We made a user friendly UI using nextjs, react, and tailwind/postcss. The color combo is managed so that it matches thirdspace week 1 theme - **Harvest**

- **Messaging and Inbox:** While writing this docs it's not done yet but will be done by next week, further week or we may have done some this week too...

---

## Stack

Backend:
- Python + Flask
- MongoDB Atlas (PyMongo)
- Flask sessions for login
- werkzeug for password hashing

Frontend:
- Next.js 16 with react compiler
- Tailwind CSS

---

## Layout

```
Grepship/
	grepship/
		app/
			index.js		#root index file
			page.js			#home page file
			signup/			#signup page folder
				page.js			#main file wraping the page
				signup.js		#main ui file it is seprate cuz node doesnt allow react hooks in server component
			login/
				page.js			#main file wraping the page
				signup.js		#main ui file
			global.css			#css file - just `@import "tailwind"` :P
			favicon.ico			#app icon
		backend/
			app.py			#backend server main file
			extensions.py			
			requirements.txt	#requirements file - what are required to run the app
			models/
				user.py			#some function related to user auth
			routes/
				auth.py			# for `/auth` endpoint
			utils/
				security.py		# some securit file ig
		components/
			navbar.js		#navbar component file
		public/
			default_profile.png	# default profile pic of user when logged in
		... other stuff...
```

**Here:**

- It's almost all in next.js file structre - it was made with it ofc...
- Backend is handel by flask which is in `grepship/backend/` folder where `app.py` is the main file and other app were created to make it easy to optmize
- some most(everywere) used components like navbar was shifted in components folder and included in index.js to keep it pernamently rateer than making some chaos.
- public folder stores public images like default vercel logos and default profile pic for users.
- some config files are there which wasn't used by us much but some amount were used.
- Most of the security are handel in backend - we can't trust the clent site.

## How to run it

You need Python 3.10+ and Node.js 20+.

**Backend (Flask):**

Open terminal and run this command:

```base
cd grepship/backend
python3 -m venv venv		#for linux
source venv/bin/activate	#for linux
pip install -r requirements.txt
python app.py
```

Make a `.env` file in `grepship/backend/` with:

```env
PORT=5000
SECRET_KEY=some random string
MONGO_URI=your MongoDB Atlas connection string
```

Flask runs on http://localhost:5000.

**Frontend (Next.js):**

```base
cd grepship
npm install
npm run dev
```

Next.js runs on `http://localhost:3000`.

The Next.js config has a rewrite that sends `/api/*` calls to Flask, so you can call `/api/auth/login` from the browser without worrying about CORS.

## API

Auth endpoints (all under `/api/auth/`):

- `POST /signup` — create account. Body: `{username, password, email?, conformpass}`
- `POST /login` — login. Body: `{username, password}`
- `POST /logout` — clears session
- `GET /me` — returns current user or `{user: null}`

More endpoints coming for messages and inbox.

## Contributing

Two of us are building this:

- Pramish — Frontend(Nextjs)
- Hemanta — Backend(Flask)

PRs and issues are welcome.

---

## What we learnt form this

- Nextjs
- Flask
- Designing(ui/ux and logo)
- Database
- web security
- Most importently **Team work**

	This project isn't just for a hackclub ysws but for our future teamwork quality and leadership
							-Pramish Bhusal


## License

MIT all right reserved.

## Use of AI

So, we are currently learning all things we got that we can't use AI above 30% but we tried to use below 5% or less(and it is). Both of us tried to use AI very less but some bugs(very few) we got were so hard(silly) that we had to use AI but as a research tool - logic was pure non AI. 

In summary, we used AI as a research tool only not as a working patner/assistance.

---

Markdown writtern by [Pramish Bhusal](https://github.com/gitbhusalhubpramish) and [Hemanta Kendel](https://github.com/hemanta-kandel) both representing team Penguin
