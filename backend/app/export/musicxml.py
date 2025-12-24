import shutil
import os
from .base import Exporter

EXPORT_DIR = "storage/exports"

class MusicXMLExporter(Exporter):

    def export(self, score_path: str) -> str:
        os.makedirs(EXPORT_DIR, exist_ok=True)

        filename = os.path.basename(score_path)
        target = os.path.join(EXPORT_DIR, filename)

        shutil.copy(score_path, target)
        return target


def export_musicxml(score_path: str) -> str:
    exporter = MusicXMLExporter()
    return exporter.export(score_path)
