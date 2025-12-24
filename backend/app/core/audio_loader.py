# ================================
# backend/app/core/audio_loader.py
# ================================
import librosa


def load_audio(path):
y, sr = librosa.load(path, sr=None)
return y, sr


# ================================
# backend/app/core/stem_separator.py
# ================================
def separate_stems(audio_path):
# Placeholder for Demucs/Spleeter
return {
"vocals": audio_path,
"instrumental": audio_path
}