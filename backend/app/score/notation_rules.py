import music21 as m21


def apply_notation_rules(part: m21.stream.Part) -> m21.stream.Part:
    """
    Aplica regras editoriais básicas de notação:
    - remove durações excessivamente curtas
    - consolida pausas
    - organiza compassos
    """

    cleaned = m21.stream.Part()
    cleaned.insert(0, part.getInstrument())
    cleaned.insert(0, part.getTimeSignatures()[0])
    cleaned.insert(0, part.getKeySignatures()[0])

    for el in part.recurse():
        if isinstance(el, m21.note.Note):
            if el.quarterLength < 0.125:
                el.quarterLength = 0.25
            cleaned.append(el)

        elif isinstance(el, m21.note.Rest):
            if el.quarterLength < 0.25:
                el.quarterLength = 0.25
            cleaned.append(el)

    cleaned.makeMeasures(inPlace=True)
    cleaned.makeBeams(inPlace=True)

    return cleaned
