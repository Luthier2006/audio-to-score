# ================================
# backend/app/score/xml_builder.py
# ================================
from music21 import stream, note, metadata, key, tempo


def build_musicxml(notes, bpm, tonalidade, instrument_name):
s = stream.Stream()
s.insert(0, metadata.Metadata())
s.append(tempo.MetronomeMark(number=bpm))
s.append(key.Key(tonalidade))


for p in notes:
n = note.Note()
n.pitch.frequency = p
n.quarterLength = 1
s.append(n)


return s.write('musicxml')