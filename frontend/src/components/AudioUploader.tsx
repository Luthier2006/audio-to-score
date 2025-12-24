import { ChangeEvent } from "react"

interface Props {
  onUpload: (file: File) => void
}

export default function AudioUploader({ onUpload }: Props) {
  function handleChange(e: ChangeEvent<HTMLInputElement>) {
    if (e.target.files?.[0]) {
      onUpload(e.target.files[0])
    }
  }

  return <input type="file" accept="audio/*" onChange={handleChange} />
}
