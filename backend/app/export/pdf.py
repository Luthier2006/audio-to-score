import os
import music21 as m21
from .base import Exporter

EXPORT_DIR = "storage/exports"

class PDFExporter(Exporter):

    def export(self, score_path: str) -> str:
        os.makedirs(EXPORT_DIR, exist_ok=True)

        score = m21.converter.parse(score_path)
        output_path = os.path.join(
            EXPORT_DIR,
            os.path.basename(score_path).replace(".musicxml", ".pdf")
        )

        score.write("musicxml.pdf", output_path)
        return output_path


def export_pdf(score_path: str) -> str:
    exporter = PDFExporter()
    return exporter.export(score_path)
