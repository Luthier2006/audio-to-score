// ================================
// frontend/src/pages/StemSelectPage.tsx
// ================================
import { useNavigate } from 'react-router-dom'


export default function StemSelectPage() {
const navigate = useNavigate()


return (
<div className="p-8">
<h1 className="text-xl font-bold">Selecione as Partes</h1>
<div className="mt-4 space-y-2">
<label><input type="checkbox" /> Vocal</label><br />
<label><input type="checkbox" /> Piano</label><br />
<label><input type="checkbox" /> Guitarra</label><br />
<label><input type="checkbox" /> Baixo</label><br />
</div>
<button onClick={() => navigate('/config')} className="mt-6 px-4 py-2 bg-green-600 text-white">
Continuar
</button>
</div>
)
}