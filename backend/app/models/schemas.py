from pydantic import BaseModel
from typing import List, Optional


class UploadResponse(BaseModel):
    file_id: str
    path: str


class StemResponse(BaseModel):
    stems: List[str]


class AnalysisResult(BaseModel):
    bpm: float
    key: str
    time_signature: Optional[str] = "4/4"


class Segment(BaseModel):
    id: str
    start: float
    end: float
    stem: Optional[str] = None


class ScoreRequest(BaseModel):
    stem_path: str
    instrument: str
    bpm: float
    key: str
    time_signature: str = "4/4"


class ScoreResponse(BaseModel):
    score_path: str


class ExportRequest(BaseModel):
    score_path: str
    format: str


class ExportResponse(BaseModel):
    exported_file: str
