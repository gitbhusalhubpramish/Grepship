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

## Layout

Grepship/
└── grepship/
├── app/ Next.js pages
├── components/ React components
├── public/ images, static files
└── backend/ Flask API
├── app.py
├── models/
├── routes/
└── utils/

## How to run it

You need Python 3.10+ and Node.js 20+.

**Backend (Flask):**

cd grepship/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

Make a `.env` file in `grepship/backend/` with:

PORT=5000
SECRET_KEY=some random string
MONGO_URI=your MongoDB Atlas connection string

Flask runs on http://localhost:5000.

**Frontend (Next.js):**

cd grepship
npm install
npm run dev


Next.js runs on http://localhost:3000.

The Next.js config has a rewrite that sends `/api/*` calls to Flask, so you can call `/api/auth/login` from the browser without worrying about CORS.

## API

Auth endpoints (all under `/api/auth/`):

- `POST /signup` — create account. Body: `{username, password, email?}`
- `POST /login` — login. Body: `{username, password}`
- `POST /logout` — clears session
- `GET /me` — returns current user or `{user: null}`

More endpoints coming for messages and inbox.

## Contributing

Two of us are building this:

- Pramish — frontend
- Hemanta — backend

PRs welcome.

## License

MIT.
