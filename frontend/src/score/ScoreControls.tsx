interface Props {
bpm: number
keySignature: string
instrument: string
onChangeInstrument: (i: string) => void
}


export default function ScoreControls({
bpm,
keySignature,
instrument,
onChangeInstrument
}: Props) {
return (
<div className="bg-white p-4 rounded shadow">
<div>BPM: {bpm}</div>
<div>Tom: {keySignature}</div>


<select
value={instrument}
onChange={e => onChangeInstrument(e.target.value)}
className="mt-2"
>
<option>Piano</option>
<option>Violin</option>
<option>Guitar</option>
<option>Flute</option>
<option>Voice</option>
</select>
</div>
)
}
```