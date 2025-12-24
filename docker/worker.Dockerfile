FROM python:3.11-slim

WORKDIR /worker
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY workers .
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]
