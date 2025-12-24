import { useEffect, useRef } from "react"
import verovio from "verovio"

export default function VerovioRenderer({ xml }: { xml: string }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!ref.current || !xml) return

    const toolkit = new verovio.toolkit()
    toolkit.loadData(xml)
    ref.current.innerHTML = toolkit.renderToSVG(1)
  }, [xml])

  return <div ref={ref} />
}
