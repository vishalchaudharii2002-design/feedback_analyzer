# 🚀 Backend – FastAPI + Celery + Redis + SQLite

This is the backend for a web application that allows users to:
- Upload CSV/Excel files
- Queue file processing jobs in the background
- Track job status
- Receive an email when the job is completed

---

## 📦 Tech Stack

- **FastAPI** – Web framework
- **Celery** – Background job processing
- **Redis** – Message broker and result backend for Celery
- **SQLite** – Lightweight database
- **Google Cloud Storage (GCS)** – File storage
- **Pandas / openpyxl** – File parsing and analysis

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo/backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file**
   
   Add the following to `backend/.env`:
   ```env
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   GCS_BUCKET_NAME=your-gcs-bucket-name
   EMAIL_SENDER=your@email.com
   ```

---

## 🚀 Run the App

### 1. Start FastAPI server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
📎 Visit: http://localhost:8000/docs

### 2. Start the Celery worker
In a new terminal, run:
```bash
celery -A app.core.celery_app.celery_app worker --loglevel=info
```

---

## 🐳 Docker (Optional)

### 1. Build the backend Docker image
```bash
docker build -t my-fastapi-backend .
```

### 2. Use Docker Compose
Use the `docker-compose.yml` file in the project root to run:
- Backend
- Redis
- Worker

---

## 📡 API Endpoints

| Method | Path      | Description              |
|--------|-----------|--------------------------|
| POST   | /upload   | Upload a file for job    |
| GET    | /status   | Check status of a job    |

---

## ✅ To Do

- Add authentication
- Store job logs
- Improve error handling and retries
- Add frontend integration

---

## 📂 Related Folders

- `frontend/` – HTML/CSS/JS client
- `worker/` – Celery worker setup
- `.env` – Environment config

---

## 📧 Maintainer

Built by Mayur Bodhare