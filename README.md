# Grepship

A simple messaging app made using next.js and flask.

<img src="grepship.png"/>

click it for demo

---

## Feature

- User can sign up and login in this app and data are stored in mongodb.
- It is build in harvest theme - feels like harvesting wheats and other crops(color combo).
- Build using Tailwind for css, next for frontend and flask for backend.

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

---

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

```
	This project isn't just for a hackclub ysws but for our future teamwork quality and leadership
							-Pramish Bhusal
```

---

## License

MIT all right reserved.

## Use of AI

So, we are currently learning all things we got that we can't use AI above 30% but we tried to use below 5% or less(and it is). Both of us tried to use AI very less but some bugs(very few) we got were so hard(silly) that we had to use AI but as a research tool - logic was pure non AI. 

In summary, we used AI as a research tool only not as a working patner/assistance.

---

Markdown writtern by [Pramish Bhusal](https://github.com/gitbhusalhubpramish) and [Hemanta Kendel](https://github.com/hemanta-kandel) both representing team Penguin
