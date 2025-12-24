from workers.celery_app import celery_app
import librosa
import numpy as np

@celery_app.task(bind=True)
def analyze_stem(self, stem_path: str):
    y, sr = librosa.load(stem_path, mono=True)

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    key_index = np.argmax(np.sum(chroma, axis=1))

    keys = [
        "C", "C#", "D", "D#", "E", "F",
        "F#", "G", "G#", "A", "A#", "B"
    ]

    return {
        "bpm": float(round(tempo, 2)),
        "key": keys[key_index],
        "sr": sr
    }
