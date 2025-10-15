# worker/celery_worker.py

from backend.app.core.celery_app import celery_app

if __name__ == "__main__":
    # Start Celery worker with default options
    celery_app.worker_main()
