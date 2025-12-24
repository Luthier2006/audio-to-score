# ================================
# backend/app/api/routes/upload.py
# ================================
from fastapi import APIRouter, UploadFile
import shutil, uuid, os


router = APIRouter()
UPLOAD_DIR = "storage/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
def upload_audio(file: UploadFile):
file_id = str(uuid.uuid4())
path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
with open(path, "wb") as buffer:
shutil.copyfileobj(file.file, buffer)
return {"file_id": file_id, "path": path}