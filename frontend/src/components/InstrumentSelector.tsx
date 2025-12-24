interface Props {
  value: string
  onChange: (v: string) => void
}

export default function InstrumentSelector({ value, onChange }: Props) {
  return (
    <select value={value} onChange={e => onChange(e.target.value)}>
      <option value="piano">Piano</option>
      <option value="vocal">Voz</option>
      <option value="guitar">Guitarra</option>
      <option value="bass">Baixo</option>
      <option value="drums">Bateria</option>
    </select>
  )
}
