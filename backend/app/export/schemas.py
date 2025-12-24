from pydantic import BaseModel

class ExportRequest(BaseModel):
    score_path: str
    format: str
