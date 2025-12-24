# ================================
# backend/app/music/key_detection.py
# ================================
import librosa
import numpy as np


KEYS = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']


def detect_key(path):
y, sr = librosa.load(path)
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
key_index = np.argmax(chroma.mean(axis=1))
return KEYS[key_index]