from workers.celery_app import celery_app
import shutil
import os

@celery_app.task(bind=True)
def export_score(self, score_path: str, export_format: str = "musicxml"):
    export_dir = "storage/exports"
    os.makedirs(export_dir, exist_ok=True)

    filename = os.path.basename(score_path)
    target = os.path.join(export_dir, filename)

    shutil.copy(score_path, target)

    return target
