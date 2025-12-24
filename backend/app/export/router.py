from fastapi import APIRouter
from .schemas import ExportRequest
from .factory import export_score

router = APIRouter(prefix="/export", tags=["Export"])

@router.post("/")
def export_endpoint(payload: ExportRequest):
    output = export_score(
        payload.score_path,
        payload.format
    )

    return {
        "exported_file": output
    }
