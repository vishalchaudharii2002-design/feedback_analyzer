from fastapi import APIRouter
from fastapi.responses import JSONResponse
# from app.models.job import Job, SessionLocal

router = APIRouter()

@router.get("/{job_id}")
def get_status(job_id: str):
    # db = SessionLocal()
    # job = db.query(Job).filter(Job.id == job_id).first()
    # db.close()

    # if not job:
    #     return JSONResponse(status_code=404, content={"error": "Job not found"})

    # return {
    #     "job_id": job.id,
    #     "status": job.status,
    #     "filename": job.filename,
    #     "email": job.email,
    #     "result_url": job.result_url
    # }

    pass