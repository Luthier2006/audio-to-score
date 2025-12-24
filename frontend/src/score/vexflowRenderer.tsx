import { useEffect, useRef } from "react"
import Vex from "vexflow"

export default function VexflowRenderer({ notes }: { notes: string[] }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!ref.current) return
    ref.current.innerHTML = ""

    const VF = Vex.Flow
    const renderer = new VF.Renderer(ref.current, VF.Renderer.Backends.SVG)
    renderer.resize(500, 200)

    const context = renderer.getContext()
    const stave = new VF.Stave(10, 40, 400)
    stave.addClef("treble").draw(context)

    const vfNotes = notes.map(
      n => new VF.StaveNote({ keys: [n], duration: "q" })
    )

    const voice = new VF.Voice({ num_beats: vfNotes.length, beat_value: 4 })
    voice.addTickables(vfNotes)

    new VF.Formatter().joinVoices([voice]).format([voice], 300)
    voice.draw(context, stave)
  }, [notes])

  return <div ref={ref} />
}
