import os

# Base project directory
base_dir = r"."

# Define folders to create
folders = [
    # Backend folders
    "backend/app/api",
    "backend/app/core",
    "backend/app/db",
    "backend/app/tasks",
    "backend/app/utils",

    # Frontend folders
    "frontend/css",
    "frontend/js",

    # Worker folder
    "worker",
]

# Define files to create with their paths relative to base_dir
files = [
    # Backend files
    "backend/app/__init__.py",
    "backend/app/main.py",
    "backend/app/api/__init__.py",
    "backend/app/api/upload.py",
    "backend/app/api/status.py",
    "backend/app/core/__init__.py",
    "backend/app/core/config.py",
    "backend/app/core/celery_app.py",
    "backend/app/db/__init__.py",
    "backend/app/db/models.py",
    "backend/app/db/crud.py",
    "backend/app/db/session.py",
    "backend/app/tasks/__init__.py",
    "backend/app/tasks/process_file.py",
    "backend/app/utils/__init__.py",
    "backend/app/utils/gcs.py",
    "backend/app/utils/email.py",
    "backend/app/utils/analysis.py",
    "backend/app/utils/job_status.py",
    "backend/requirements.txt",
    "backend/Dockerfile",
    "backend/README.md",

    # Frontend files
    "frontend/index.html",
    "frontend/status.html",
    "frontend/css/styles.css",
    "frontend/js/upload.js",
    "frontend/js/status.js",

    # Worker files
    "worker/celery_worker.py",
    "worker/Dockerfile",

    # Root files
    "docker-compose.yml",
    "ROADMAP.md",
    "README.md",
]

def create_folders(base, folder_list):
    for folder in folder_list:
        path = os.path.join(base, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

def create_files(base, file_list):
    for file in file_list:
        path = os.path.join(base, file)
        # Ensure folder exists (redundant if create_folders run first)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Create empty file if it doesn't exist
        if not os.path.exists(path):
            with open(path, 'w') as f:
                pass
            print(f"Created file: {path}")
        else:
            print(f"File already exists: {path}")

if __name__ == "__main__":
    create_folders(base_dir, folders)
    create_files(base_dir, files)
    print("Folder structure setup complete.")
