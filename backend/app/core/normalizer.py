import librosa
import soundfile as sf
from pathlib import Path
from backend.app.config import settings




def normalize_audio(audio_path: Path) -> Path:
y, sr = librosa.load(audio_path, mono=True)
y = librosa.util.normalize(y)


output_path = settings.UPLOADS_PATH / f"normalized_{audio_path.name}"
sf.write(output_path, y, sr)


return output_path