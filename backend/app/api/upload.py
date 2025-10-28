from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse
import shutil
import os
import uuid

from backend.app.core.config import settings
from backend.app.core.celery_app import celery_app
# from app.models.job import Job, SessionLocal
from backend.app.tasks.process_file import process_file_task
from backend.app.utils.gcs import upload_file_to_gcs

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...), email: str = Form(...)):
    job_id = str(uuid.uuid4())

    # Save file temporarily
    tmp_file_path = f"/tmp/{job_id}_{file.filename}"
    with open(tmp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Upload file to Google Cloud Storage
    gcs_file_url = upload_file_to_gcs(tmp_file_path, job_id, file.filename)

    # Create DB entry for the job
    # db = SessionLocal()
    # job = Job(id=job_id, filename=file.filename, email=email, status="queued", file_url=gcs_file_url)
    # db.add(job)
    # db.commit()
    # db.close()

    # Queue background task
    process_file_task.delay(job_id, gcs_file_url, email)

    # Remove the temporary file
    os.remove(tmp_file_path)

    return {"message": "File uploaded and job queued", "job_id": job_id}

@router.get("/")
async def get_upload_status():
    # return {"message": "Upload route to receive files."}
    return FileResponse('frontend/upload.html')
