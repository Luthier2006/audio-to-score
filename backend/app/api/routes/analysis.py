# ================================
# backend/app/api/routes/analysis.py
# ================================
from fastapi import APIRouter
from app.music.tempo import detect_tempo
from app.music.key_detection import detect_key
from app.music.pitch_detection import detect_pitch


router = APIRouter()


@router.post("/")
def analyze(stem_path: str):
bpm = detect_tempo(stem_path)
key = detect_key(stem_path)
notes = detect_pitch(stem_path)
return {"bpm": bpm, "key": key, "notes": notes}