import music21 as m21


INSTRUMENT_MAP = {
    "Piano": m21.instrument.Piano,
    "Violin": m21.instrument.Violin,
    "Viola": m21.instrument.Viola,
    "Cello": m21.instrument.Violoncello,
    "Guitar": m21.instrument.Guitar,
    "Bass": m21.instrument.Bass,
    "Flute": m21.instrument.Flute,
    "Oboe": m21.instrument.Oboe,
    "Clarinet": m21.instrument.Clarinet,
    "Saxophone": m21.instrument.AltoSaxophone,
    "Trumpet": m21.instrument.Trumpet,
    "Trombone": m21.instrument.Trombone,
    "Voice": m21.instrument.Vocalist
}


def map_instrument(name: str) -> m21.instrument.Instrument:
    """
    Mapeia nome textual para instrumento Music21 real.
    """

    instrument_cls = INSTRUMENT_MAP.get(name, m21.instrument.Piano)
    return instrument_cls()
