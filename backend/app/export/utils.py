import os

def validate_score_path(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError("Arquivo de partitura não encontrado")

    if not path.endswith(".musicxml"):
        raise ValueError("Formato de partitura inválido")
