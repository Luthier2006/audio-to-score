# ================================
# backend/app/api/routes/stems.py
# ================================
from fastapi import APIRouter
from app.core.stem_separator import separate_stems


router = APIRouter()


@router.post("/")
def create_stems(audio_path: str):
stems = separate_stems(audio_path)
return {"stems": stems}