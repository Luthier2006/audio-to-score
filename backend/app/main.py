# ================================
# backend/app/main.py
# ================================
from fastapi import FastAPI
from app.api.routes import upload, stems, analysis, score


app = FastAPI(title="Audio to Score API")


app.include_router(upload.router, prefix="/upload")
app.include_router(stems.router, prefix="/stems")
app.include_router(analysis.router, prefix="/analysis")
app.include_router(score.router, prefix="/score")