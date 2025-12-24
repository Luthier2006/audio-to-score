from celery import Celery

celery_app = Celery(
    "audio_to_score",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["workers.tasks"]
)

celery_app.conf.update(
    task_track_started=True,
    result_expires=3600
)
