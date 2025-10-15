# 📁 Web-Based File Processing App

This project is a complete web application that allows users to:

- Upload CSV or Excel files via a web interface
- Queue file processing as a background job using Celery
- Store files in Google Cloud Storage (GCS)
- Receive job status and results via email
- Track job status through a status page

---

## ⚙️ Tech Stack

### Backend

- **FastAPI** – High-performance API framework
- **Celery** – Asynchronous task queue
- **Redis** – Message broker for Celery
- **SQLite** – Lightweight relational database
- **Pandas / openpyxl** – File parsing and data analysis
- **Google Cloud Storage (GCS)** – File storage
- **aiosmtplib** – Email sending (async)
- **python-dotenv / Pydantic** – Configuration handling

### Frontend

- **HTML + CSS**
- **Vanilla JavaScript**

---

## 📂 Folder Structure

```
my_project/
│
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   ├── models/
│   │   ├── tasks/
│   │   └── utils/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
├── worker/                  # Celery worker setup
│   ├── celery_worker.py
│   ├── Dockerfile
│   └── README.md
│
├── frontend/                # Static web frontend
│   ├── index.html
│   ├── status.html
│   ├── style.css
│   └── script.js
│
├── .env                     # Environment variables
├── docker-compose.yml       # (Optional) for unified Docker setup
└── README.md                # (You're here)
```

---

## 🚀 Running the Project (Locally)

### Prerequisites

- Python 3.10+
- Redis server (for local development)
- Google Cloud credentials set up locally

---

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Add a `.env` file inside `backend/`:
   ```env
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   GCS_BUCKET_NAME=your-gcs-bucket
   EMAIL_SENDER=your@email.com
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Start the Celery worker (in another terminal):
   ```bash
   cd backend
   celery -A app.core.celery_app.celery_app worker --loglevel=info
   ```

### Frontend

Just open `frontend/index.html` and `frontend/status.html` in your browser.

No build step is needed — it's pure HTML, CSS, and JS.

---

## 🐳 Docker Setup (Optional)

Make sure Docker and Docker Compose are installed.

Add a `docker-compose.yml` in the root (if not already):

```yaml
version: '3'

services:
  redis:
    image: redis
    ports:
      - "6379:6379"

  backend:
    build: ./backend
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - redis
    env_file:
      - ./backend/.env

  worker:
    build: ./worker
    volumes:
      - ./backend:/app
    depends_on:
      - redis
    env_file:
      - ./backend/.env
```

Run everything:
```bash
docker-compose up --build
```

---

## 🔧 Features & Flow

1. User uploads a file at `/upload`.
2. Backend uploads the file to GCS and queues a background job in Redis via Celery.
3. The Celery worker downloads the file from GCS, processes it, and stores the result.
4. Once done, the worker sends an email to the user.
5. Meanwhile, users can check status via `/status`.

---

## ✅ TODO / Future Improvements

- Add user login/auth (to associate jobs with users)
- Improve progress feedback on frontend
- Use PostgreSQL for production-grade data
- Dashboard UI for job history and results
- Unit tests for tasks and API routes

---

## 📧 Maintainer

Built with ❤️ by [Mayur Bodhare]  