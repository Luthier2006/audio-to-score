from fastapi import Depends, HTTPException
from backend.app.config import settings
import os

def get_settings():
    return settings


def validate_file_exists(path: str):
    if not os.path.exists(path):
        raise HTTPException(
            status_code=404,
            detail="Arquivo não encontrado"
        )
    return path


def validate_audio_file(path: str):
    validate_file_exists(path)

    if not path.lower().endswith((".wav", ".mp3", ".flac")):
        raise HTTPException(
            status_code=400,
            detail="Formato de áudio não suportado"
        )
    return path


def validate_score_file(path: str):
    validate_file_exists(path)

    if not path.lower().endswith(".musicxml"):
        raise HTTPException(
            status_code=400,
            detail="Arquivo de partitura inválido"
        )
    return path
