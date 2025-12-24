import music21 as m21


def apply_articulations(part: m21.stream.Part) -> m21.stream.Part:
    """
    Aplica articulações básicas com base no contexto musical.
    """

    notes = list(part.recurse().notes)

    for i, note in enumerate(notes):
        # staccato em notas curtas
        if note.quarterLength <= 0.5:
            note.articulations.append(m21.articulations.Staccato())

        # acento em início de compasso
        measure = note.getContextByClass(m21.stream.Measure)
        if measure and note.offset == 0:
            note.articulations.append(m21.articulations.Accent())

        # tenuto em notas longas
        if note.quarterLength >= 2.0:
            note.articulations.append(m21.articulations.Tenuto())

    return part
