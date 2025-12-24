# ================================
# backend/app/music/tempo.py
# ================================
import librosa


def detect_tempo(path):
y, sr = librosa.load(path)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
return float(tempo)