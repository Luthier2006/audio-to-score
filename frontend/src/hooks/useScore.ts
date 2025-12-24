// ================================
// frontend/src/hooks/useScore.ts
// ================================
import { useState } from 'react'


export function useScore() {
const [musicxml, setMusicxml] = useState<string>('')
return { musicxml, setMusicxml }
}