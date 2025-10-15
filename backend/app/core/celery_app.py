from celery import Celery
from backend.app.core.config import settings

# Create Celery app instance
celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

# Optional: load task modules from all registered apps
celery_app.autodiscover_tasks(["backend.app.tasks"])

# (Optional) Configure Celery if needed
# celery_app.conf.update(
#     task_track_started=True,
#     result_expires=3600,
# )

if __name__ == "__main__":
    celery_app.start()
