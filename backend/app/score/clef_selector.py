import music21 as m21


def select_clef(part: m21.stream.Part) -> m21.clef.Clef:
    """
    Seleciona clave automaticamente com base na tessitura.
    """

    pitches = [n.pitch.midi for n in part.recurse().notes if n.pitch]

    if not pitches:
        return m21.clef.TrebleClef()

    avg_pitch = sum(pitches) / len(pitches)

    if avg_pitch >= 60:
        return m21.clef.TrebleClef()

    if 48 <= avg_pitch < 60:
        return m21.clef.AltoClef()

    return m21.clef.BassClef()


def apply_clef(part: m21.stream.Part) -> m21.stream.Part:
    clef = select_clef(part)
    part.insert(0, clef)
    return part
