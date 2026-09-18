# Grepship 🚀

An open-source, real-time messaging platform for students and small businesses — no ads, no restrictions, works in your browser.

**Official Repository:** [github.com/gitbhusalhubpramish/Grepship](https://github.com/gitbhusalhubpramish/Grepship)

---

## Features

- **Completely open source** — MIT licensed, no restrictions
- **Cross-device** — works in any modern browser
- **Fast and reliable** — real-time messaging
- **Free for everyone** — no ads, no age limit, no paywall
- **Built for:** business owners, developers, engineers, students

## Tech Stack

**Backend**

- Python 3.12+
- Flask (app factory pattern)
- MongoDB Atlas (PyMongo)
- Flask sessions (cookie-based auth)
- `werkzeug.security` (scrypt password hashing)

**Frontend**

- Next.js 16 (App Router)
- React
- Tailwind CSS
- Custom earth-tone theme

## Project Structure

```text
Grepship/
├── grepship/
│   ├── app/              # Next.js pages
│   ├── components/       # React components
│   ├── public/           # static assets
│   └── backend/          # Flask API
│       ├── app.py        # Flask app factory
│       ├── extensions.py # PyMongo instance
│       ├── models/       # MongoDB helpers
│       ├── routes/       # API blueprints
│       ├── utils/        # helpers (password hashing)
│       └── requirements.txt
└── README.md
```

## Running Locally

### Prerequisites

- **git** — version control
- **Python 3.10+** — for the backend
- **Node.js 20+** and **npm** — for the frontend

### 1. Clone the repository

```bash
git clone https://github.com/gitbhusalhubpramish/Grepship.git
cd Grepship
```

### 2. Backend setup (Flask)

```bash
cd grepship/backend

python3 -m venv venv
source venv/bin/activate              # Windows: venv\Scripts\activate

pip install -r requirements.txt

# Create a .env file with:
# PORT=5000
# SECRET_KEY=<generate a random 64-char hex>
# MONGO_URI=<your MongoDB Atlas connection string>

python app.py
```

Backend runs at **http://localhost:5000**

### 3. Frontend setup (Next.js)

```bash
cd grepship
npm install
npm run dev
```

Frontend runs at **http://localhost:3000**

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Create a new account |
| POST | `/api/auth/login` | Login (returns session cookie) |
| POST | `/api/auth/logout` | Clear session |
| GET | `/api/auth/me` | Get current user |

See [`backend/API.md`](grepship/backend/API.md) for full details.

## Contributing

Grepship is a two-person project built at [Hack Club](https://hackclub.com):

- **[Pramish Bhusal](https://github.com/gitbhusalhubpramish)** — Frontend (Next.js, React, Tailwind)
- **[Hemanta Kandel](https://github.com/hemanta-kandel)** — Backend (Flask, MongoDB, auth)

Pull requests welcome. For major changes, open an issue first.

## License

MIT — free to use, modify, and distribute.