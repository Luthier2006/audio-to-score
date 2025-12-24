import { configureStore, createSlice, PayloadAction } from "@reduxjs/toolkit"

interface ProjectState {
  fileId: string | null
  audioUrl: string | null
  stems: string[]
  musicXML: string | null
}

const initialState: ProjectState = {
  fileId: null,
  audioUrl: null,
  stems: [],
  musicXML: null
}

const projectSlice = createSlice({
  name: "project",
  initialState,
  reducers: {
    setFile(state, action: PayloadAction<{ id: string; url: string }>) {
      state.fileId = action.payload.id
      state.audioUrl = action.payload.url
    },
    setStems(state, action: PayloadAction<string[]>) {
      state.stems = action.payload
    },
    setMusicXML(state, action: PayloadAction<string>) {
      state.musicXML = action.payload
    }
  }
})

export const { setFile, setStems, setMusicXML } = projectSlice.actions

export const store = configureStore({
  reducer: {
    project: projectSlice.reducer
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
