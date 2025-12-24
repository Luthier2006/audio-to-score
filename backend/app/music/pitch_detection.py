# ================================
# backend/app/music/pitch_detection.py
# ================================
import librosa


def detect_pitch(path):
y, sr = librosa.load(path)
pitches, mags = librosa.piptrack(y=y, sr=sr)
notes = []
for i in range(pitches.shape[1]):
index = mags[:, i].argmax()
pitch = pitches[index, i]
if pitch > 0:
notes.append(float(pitch))
return notes