# Project Roadmap: Web App with Background Job Processing

---

## Step 0: Prepare Your Environment
- Install Python, Redis (locally or managed)
- Set up Google Cloud Storage (GCS) bucket & credentials
- Install required libraries: FastAPI, Uvicorn, Celery, Redis client, GCS client, email libs

---

## Step 1: Initialize FastAPI Project
- Create FastAPI app structure (`main.py`, etc.)
- Implement `/upload` endpoint to accept file + email
- Validate upload file types (Excel/CSV)
- Test local upload handling

---

## Step 2: Integrate Google Cloud Storage
- Configure GCS client in FastAPI
- Upload incoming files to GCS in `/upload` handler
- Generate unique GCS paths for each upload
- Verify files upload successfully to GCS

---

## Step 3: Design Database & Job Tracking
- Choose DB (PostgreSQL, SQLite for testing)
- Create `JobStatus` table with:
  - `job_id` (UUID)
  - `email`
  - `gcs_path`
  - `status` (pending, processing, done, failed)
  - `error` (nullable)
  - timestamps
- Write DB functions for job create/update

---

## Step 4: Setup Celery with Redis
- Install and configure Redis locally or cloud
- Setup Celery (`celery_app.py`) with Redis broker/backend
- Define Celery tasks (`process_file`)
- Run Celery worker and test startup
- Call Celery tasks asynchronously from `/upload` handler

---

## Step 5: Implement Celery Worker Logic
- Update DB status to `"processing"` at start
- Download file from GCS
- Run analysis code on file
- Update status to `"done"` or `"failed"` with error
- Send completion or failure email to user

---

## Step 6: Create `/status` Endpoint
- Implement GET `/status?job_id=...`
- Query `JobStatus` for current status and errors
- Return JSON status response
- Frontend: implement polling mechanism with JS

---

## Step 7: Frontend UI
- Design `/upload` page:
  - File input, email input, submit button
  - Display job ID on submit
- Design `/status` page:
  - Input for job ID
  - Button to check status
  - Display status dynamically
- Optionally auto-poll `/status`

---

## Step 8: Testing and Debugging
- Test full upload → processing → email → status flow
- Test error handling scenarios
- Test multiple concurrent jobs and queue behavior
- Test worker restarts and resilience

---

## Step 9: Deployment Preparation
- Containerize app and worker (Docker)
- Deploy FastAPI backend and Celery worker (GCP, AWS, Heroku)
- Use managed Redis service if possible
- Secure environment variables (DB, GCS, email creds)
- Setup process manager or orchestrator to run worker continuously

---

## Step 10: Monitoring and Maintenance
- Add logging for backend and worker
- Monitor queue and worker health
- Set up alerts for failures or backlog
- Plan for scaling workers if needed

---

# Summary Table

| Step | Task                                  | Outcome                     |
|-------|-------------------------------------|-----------------------------|
| 0     | Setup environment                   | Ready dev environment       |
| 1     | FastAPI upload endpoint             | Accept file + email         |
| 2     | Upload file to GCS                  | File stored in cloud        |
| 3     | Database and job tracking           | Job status tracked          |
| 4     | Setup Celery + Redis                | Async queue & worker ready  |
| 5     | Celery task implementation          | File processed async        |
| 6     | `/status` endpoint + polling         | User checks job status      |
| 7     | Frontend UI                        | User interaction            |
| 8     | Testing and debugging               | Stable, reliable system     |
| 9     | Deployment                        | Production-ready            |
| 10    | Monitoring and scaling             | Maintain & improve          |
