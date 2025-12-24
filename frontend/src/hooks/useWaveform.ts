import { useEffect, useRef } from "react"
import WaveSurfer from "wavesurfer.js"

export function useWaveform(url?: string) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!ref.current || !url) return

    const ws = WaveSurfer.create({ container: ref.current })
    ws.load(url)

    return () => ws.destroy()
  }, [url])

  return ref
}
