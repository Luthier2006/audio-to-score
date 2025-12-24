from pydantic import BaseModel
from typing import List

class AnalysisResult(BaseModel):
    bpm: float
    key: str
    notes: List[float]

class ScoreRequest(BaseModel):
    notes: List[float]
    bpm: float
    key: str
    instrument: str
