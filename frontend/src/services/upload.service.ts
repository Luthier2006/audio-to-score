import { api } from "./api"

export async function uploadAudio(file: File) {
  const form = new FormData()
  form.append("file", file)

  const res = await api.post("/upload", form)
  return res.data
}
