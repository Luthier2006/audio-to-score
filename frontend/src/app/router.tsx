import { createBrowserRouter } from "react-router-dom"
import UploadPage from "../pages/UploadPage"
import StemSelectPage from "../pages/StemSelectPage"
import MusicConfigPage from "../pages/MusicConfigPage"
import ScoreViewerPage from "../pages/ScoreViewerPage"

export const router = createBrowserRouter([
  { path: "/", element: <UploadPage /> },
  { path: "/stems", element: <StemSelectPage /> },
  { path: "/config", element: <MusicConfigPage /> },
  { path: "/score", element: <ScoreViewerPage /> }
])
