import music21 as m21


def split_voices(stream: m21.stream.Part):
    """
    Separa vozes simultâneas em múltiplas camadas (ex: piano RH/LH).
    """

    voices = stream.voices
    if len(voices) > 1:
        return voices

    voice_high = m21.stream.Voice(id="RH")
    voice_low = m21.stream.Voice(id="LH")

    for note in stream.recurse().notes:
        if note.pitch.midi >= 60:
            voice_high.append(note)
        else:
            voice_low.append(note)

    part = m21.stream.Part()
    part.insert(0, stream.getInstrument())
    part.insert(0, stream.getTimeSignatures()[0])
    part.insert(0, stream.getKeySignatures()[0])

    part.insert(0, voice_high)
    part.insert(0, voice_low)

    return part
