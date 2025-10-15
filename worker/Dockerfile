# worker/Dockerfile

FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy backend app code into container (adjust path if needed)
COPY ../backend /app/backend

# Copy worker code
COPY . /app/worker

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Set environment variables (adjust as needed)
ENV PYTHONPATH=/app/backend

# Default command to run celery worker
CMD ["python", "worker/celery_worker.py"]
