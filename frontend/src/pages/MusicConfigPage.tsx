// ================================
// frontend/src/pages/MusicConfigPage.tsx
// ================================
import { useNavigate } from 'react-router-dom'


export default function MusicConfigPage() {
const navigate = useNavigate()


return (
<div className="p-8">
<h1 className="text-xl font-bold">Configuração Musical</h1>
<div className="mt-4">
<label>Instrumento:</label>
<select className="ml-2">
<option>Piano</option>
<option>Voz</option>
<option>Guitarra</option>
</select>
</div>
<button onClick={() => navigate('/score')} className="mt-6 px-4 py-2 bg-purple-600 text-white">
Gerar Partitura
</button>
</div>
)
}