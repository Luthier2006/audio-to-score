import { useState } from "react"

export function useAudio() {
  const [audioUrl, setAudioUrl] = useState<string | null>(null)

  function load(file: File) {
    setAudioUrl(URL.createObjectURL(file))
  }

  return { audioUrl, load }
}
