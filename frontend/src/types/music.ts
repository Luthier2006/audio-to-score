export interface Stem {
  name: string
  path: string
}

export interface AnalysisResult {
  bpm: number
  key: string
  notes: number[]
}

export interface InstrumentConfig {
  stem: string
  instrument: string
}
