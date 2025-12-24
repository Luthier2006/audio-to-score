# <h1 align="center">Audio to Score</h1>

**Audio to Score** is a complete platform for **converting audio into musical scores with a high degree of coherence and realism**, respecting **tempo (BPM), sound, instrumentation, muscles, clefs, and real voices**.

The project was conceived as a **professional pipeline**, combining stem separation, musical analysis, rhythmic quantization, and the generation of editorial scores.

---

## <h1>Main Features</h1>

- Audio upload (WAV, MP3, FLAC)
- Stem separation (vocals, instruments, etc.)
- Audio temporal segmentation
- Real musical analysis:

- Real BPM

- Correct key

- Configurable time signature
- Instrument selection by stem
- Musical notation rules (editorial readability)
- Intelligent rhythmic quantization
- Voice separation (e.g., right/left hand piano)
- Automatic key selection
- Automatic articulations (staccato, tenuto, accent)
- Export to:

- XML ​​Music

- PDF

- MIDI
- Asynchronous processing with Celery + Redis
- Fully dockerized environment

---

## <h1>Architecture</h1>

````
audio-to-score/
├── backend/
│ ├── app/
│ │ ├── api/
│ │ ├── core/
│ │ ├── export/
│ │ ├── models/
│ │ ├── music/
│ │ └── score/
│ └── requirements.txt
│
├── frontend/
│ ├── public/
│ └── src/
│ ├── components/
│ ├── hooks/
│ ├── score/
│ ├── services/
│ └── styles/
│
├── workers/
│ └── tasks/
│
├── storage/
│ ├── uploads/
│ ├── stems/
│ ├── segments/
│ ├── scores/
│ └── exports/
│
├── docker/
│
├── docs/
│
└── docker-compose.yml

````


---

---
## <h1>Technology Stack</h1>

### Backend
- Python 3.10+
- FastAPI
- Music21
- Librosa
- Demucs
- Celery + Redis

### Frontend
- React
- TypeScript
- Vite
- Redux Toolkit
- VexFlow / Verovio
- WaveSurfer.js

### Infrastructure
- Docker
- Docker Compose

---

## <h1>How to Run the Project</h1>

### Prerequisites
- Docker
- Docker Compose

### <h1>Getting Everything Up and Running</h1>
````
docker-compose up --build
````
