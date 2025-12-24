// ================================
// frontend/src/pages/ScoreViewerPage.tsx
// ================================
export default function ScoreViewerPage() {
return (
<div className="p-8">
<h1 className="text-xl font-bold">Partitura Gerada</h1>
<div className="mt-4 border p-4">(Renderização da partitura aqui)</div>
<button className="mt-4 px-4 py-2 bg-gray-800 text-white">Exportar PDF</button>
</div>
)
}