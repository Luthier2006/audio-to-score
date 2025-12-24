from workers.celery_app import celery_app
import librosa
import music21 as m21

@celery_app.task(bind=True)
def generate_score(self, stem_path: str, bpm: float, key: str, instrument: str):
    y, sr = librosa.load(stem_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    stream = m21.stream.Part()
    stream.insert(0, m21.tempo.MetronomeMark(number=bpm))
    stream.insert(0, m21.key.Key(key))
    stream.insert(0, m21.instrument.fromString(instrument))

    for frame in range(pitches.shape[1]):
        pitch = pitches[:, frame].max()
        if pitch > 0:
            note = m21.note.Note(
                m21.pitch.Pitch(m21.pitch.Pitch().frequencyToMidi(pitch))
            )
            note.quarterLength = 0.25
            stream.append(note)

    output_path = stem_path.replace("stems", "scores") + ".musicxml"
    stream.write("musicxml", output_path)

    return output_path
