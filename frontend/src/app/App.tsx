// ================================
// frontend/src/app/App.tsx
// ================================
import { Routes, Route } from 'react-router-dom'
import UploadPage from '../pages/UploadPage'
import StemSelectPage from '../pages/StemSelectPage'
import MusicConfigPage from '../pages/MusicConfigPage'
import ScoreViewerPage from '../pages/ScoreViewerPage'


export default function App() {
return (
<Routes>
<Route path="/" element={<UploadPage />} />
<Route path="/stems" element={<StemSelectPage />} />
<Route path="/config" element={<MusicConfigPage />} />
<Route path="/score" element={<ScoreViewerPage />} />
</Routes>
)
}