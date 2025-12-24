import librosa
from pathlib import Path
from backend.app.config import settings
import uuid




def segment_audio(audio_path: Path, segment_duration: float = 10.0):
y, sr = librosa.load(audio_path, mono=True)
total_duration = librosa.get_duration(y=y, sr=sr)


segments = []
start = 0.0


while start < total_duration:
end = min(start + segment_duration, total_duration)
segments.append({
"id": str(uuid.uuid4()),
"start": start,
"end": end
})
start = end


output = settings.SEGMENTS_PATH / f"{audio_path.stem}_segments.json"
output.parent.mkdir(parents=True, exist_ok=True)


import json
with open(output, "w") as f:
json.dump(segments, f, indent=2)


return output