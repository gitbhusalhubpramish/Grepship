# Grepship 🚀

An open-source, real-time messaging platform for students and small business - no ads, no restrictions, work in your browser

**official Repository:** [github.com/gitbhushalhubpramish/Grepship](https://github.com/gitbhushalhubpramish/Grepship)

---
## Features

- **Completely open source** 
- **Cross-device** 
- **Fast and reliable**
- **Free for everyone**
- **Build For:** business owners, developers, engineers, students
  
## Tech Stack

**Backend**
- Python 3.12+
- Flask (app factory pattern)
- MongoDB Atlas (pymongo)
- Flask session (cookie-based auth)
- werkzeug.security (scrypt password hashing)

**Frontend**
- Next.js 16 (App router)
- React
- Tailwind CSS
- Custom earth-tone theme

## Project structure

\`\`\`
Grepship/
|----- grepship/
|       |---- app/                              -> next.js pages
|       |---- components/               -> React components
|       |---- public/                           -> static assets
|       |----  backend/                     -> Flask API
|                   |---- app.py               -> Flask app factory
|                   |---- extensions.py   -> PyMongo instance 
|                   |---- models/             -> MongoDB helpers
|                   |---- routes/               -> API blueprints
|                   |---- utils/                    -> helpers (password hashing)
|                   |---- requirements.txt
|---- README.md
\`\`\`

## Running Locally

### Prerequistites

- **git** - version control
- **Python 3.10+** - for the backend
- **Node.js 20+** and **npm** - for the frontend

### 1. Clone the repository

\`\`\` bash
git clone https://github.com/gitbhusalhubpramish/Grepship.git
cd Grepship
\`\`\`

### 2. Backend setup (Flask)

\`\`\`bash
cd grepship/backend

python3 -m venv venv
source venv/bin/activate              # windows: venv\\scripts\\activate

pip install -r requirements.txt

# Crete .env file with:
# PORT=5000
# SECRET_KEY=<generate a random 64-char hex>
# MONGO_URI=<your MongoDB Atlas connection string>

python app.py
\`\`\`

Backend runs at **http://localhost:5000**

### 3. Frontend setup (Next.js)

\`\`\`bash
cd grepship
npm install
npm run dev
\`\`\`

Frontend runs at **http://localhost:3000**

## API Endpoints

|  Method | Endpoint                    | Description                     |
| -------------|------------------------------|-----------------------------------|
| POST      | '/api/auth/register'   | Create a new account   |
| POST      | '/api/auth/login'        | Login                                |
| POST      | '/api/auth/logout'     | Clear session                   |
| GET        | '/api/auth/me'            | Get current user             |

See [\ 'backend/API.md\'](grepship/backend/API.md) for full details. 

## Contibuting

Grepship is a two-person project built at [Hack Club](https://hackclub.com)

- **[Pramish Bhusal](https://github.com/gitbhusalhubpramish)** — Frontend (Next.js, React, Tailwind)
- **[Hemanta Kandel](https://github.com/hemanta-kandel)** — Backend (Flask, MongoDB, auth)

Pull request welcome, For major changes, open an issue first. 

## License
Completely open source. 