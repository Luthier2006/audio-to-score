import math
from typing import List
import music21 as m21


def quantize_stream(
    stream: m21.stream.Stream,
    time_signature: str = "4/4",
    min_division: float = 0.25
) -> m21.stream.Stream:
    """
    Quantiza ritmos para valores musicais legíveis
    (semicolcheia como menor divisão padrão).
    """

    ts = m21.meter.TimeSignature(time_signature)
    stream.insert(0, ts)

    for element in stream.recurse().notes:
        ql = element.quarterLength
        quantized = round(ql / min_division) * min_division
        element.quarterLength = max(min_division, quantized)

    stream.makeMeasures(inPlace=True)
    stream.makeTies(inPlace=True)

    return stream
