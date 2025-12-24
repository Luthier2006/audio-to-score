interface Props {
  label: string
  checked: boolean
  onChange: (v: boolean) => void
}

export default function StemCheckbox({ label, checked, onChange }: Props) {
  return (
    <label className="flex gap-2">
      <input
        type="checkbox"
        checked={checked}
        onChange={e => onChange(e.target.checked)}
      />
      {label}
    </label>
  )
}
