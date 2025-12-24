from workers.celery_app import celery_app
import os
import subprocess
import uuid

@celery_app.task(bind=True)
def separate_stems(self, audio_path: str):
    job_id = str(uuid.uuid4())
    output_dir = f"storage/stems/{job_id}"
    os.makedirs(output_dir, exist_ok=True)

    subprocess.run([
        "demucs",
        "--two-stems=vocals",
        "-o",
        output_dir,
        audio_path
    ], check=True)

    return {
        "job_id": job_id,
        "stems_path": output_dir
    }
