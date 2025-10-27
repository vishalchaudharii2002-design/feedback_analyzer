from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the API routes
from backend.app.api import upload, status, analyze

# Initialize FastAPI app
app = FastAPI(title="File Processor")

# Optional: Add CORS for local frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for the modular routes
app.include_router(upload.router)
app.include_router(status.router, prefix="/status", tags=["status"])
app.include_router(analyze.router, prefix="/analyze", tags=["analyze"])
