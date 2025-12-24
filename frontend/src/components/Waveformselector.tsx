import { useEffect, useRef } from "react"
import WaveSurfer from "wavesurfer.js"

export default function WaveformSelector({ url }: { url: string }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!ref.current) return

    const ws = WaveSurfer.create({
      container: ref.current,
      waveColor: "#999",
      progressColor: "#4f46e5",
      height: 100
    })

    ws.load(url)
    return () => ws.destroy()
  }, [url])

  return <div ref={ref} />
}
