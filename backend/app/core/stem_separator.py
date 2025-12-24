import subprocess
import uuid
from pathlib import Path
from backend.app.config import settings




def separate_stems(audio_path: Path) -> Path:
job_id = str(uuid.uuid4())
output_dir = settings.STEMS_PATH / job_id
output_dir.mkdir(parents=True, exist_ok=True)


subprocess.run([
"demucs",
"-n",
"htdemucs",
"-o",
str(output_dir),
str(audio_path)
], check=True)


return output_dir