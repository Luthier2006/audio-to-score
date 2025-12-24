// ================================
// frontend/src/pages/UploadPage.tsx
// ================================
import { useNavigate } from 'react-router-dom'


export default function UploadPage() {
const navigate = useNavigate()


function handleUpload() {
navigate('/stems')
}


return (
<div className="p-8">
<h1 className="text-2xl font-bold">Upload de Áudio</h1>
<input type="file" className="mt-4" />
<button onClick={handleUpload} className="mt-4 px-4 py-2 bg-blue-600 text-white">
Enviar
</button>
</div>
)
}