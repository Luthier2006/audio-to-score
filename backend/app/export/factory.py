from .musicxml import export_musicxml
from .pdf import export_pdf
from .midi import export_midi

def export_score(score_path: str, format: str):
    if format == "musicxml":
        return export_musicxml(score_path)

    if format == "pdf":
        return export_pdf(score_path)

    if format == "midi":
        return export_midi(score_path)

    raise ValueError("Formato de exportação não suportado")
