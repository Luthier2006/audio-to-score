interface Props {
  bpm: number
  keySig: string
}

export default function TempoKeyDisplay({ bpm, keySig }: Props) {
  return (
    <div className="flex gap-4 font-semibold">
      <span>BPM: {bpm}</span>
      <span>Tonalidade: {keySig}</span>
    </div>
  )
}
