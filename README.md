# Grepship

A simple messaging app for friends and small teams. It works in your browser, no ads, no signup fees.

Repo: https://github.com/gitbhusalhubpramish/Grepship

## What it does

- Sign up with username + password (email is optional)
- Log in, log out
- Session stays until you close the tab
- (coming soon) Send messages, view inbox, chat with people

We built this for Hack Club's ThirdSpace program.

## Stack

Backend:
- Python + Flask
- MongoDB Atlas (PyMongo)
- Flask sessions for login
- werkzeug for password hashing

Frontend:
- Next.js 16
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
