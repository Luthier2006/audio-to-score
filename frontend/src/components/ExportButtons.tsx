// ================================
// frontend/src/components/ExportButtons.tsx
// ================================
export function ExportButtons() {
return (
<div className="flex gap-2">
<button className="px-3 py-2 bg-gray-700 text-white">MusicXML</button>
<button className="px-3 py-2 bg-gray-700 text-white">PDF</button>
<button className="px-3 py-2 bg-gray-700 text-white">MIDI</button>
</div>
)
}