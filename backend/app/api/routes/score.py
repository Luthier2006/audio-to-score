# ================================
# backend/app/api/routes/score.py
# ================================
from fastapi import APIRouter
from app.score.xml_builder import build_musicxml


router = APIRouter()


@router.post("/")
def generate_score(notes: list, bpm: float, key: str, instrument: str):
xml = build_musicxml(notes, bpm, key, instrument)
return {"musicxml": xml}