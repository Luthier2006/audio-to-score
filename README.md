# 🎼 Audio to Score

**Audio to Score** é uma plataforma completa para **converter áudio em partitura musical com alto grau de coerência e realismo**, respeitando **andamento (BPM), tonalidade, instrumentação, articulações, claves e vozes reais**.

O projeto foi pensado como um **pipeline profissional**, unindo separação de stems, análise musical, quantização rítmica e geração de partituras editoriais.

---

## ✨ Principais Funcionalidades

- 🎧 Upload de áudio (WAV, MP3, FLAC)
- 🎤 Separação de stems (vocais, instrumentos, etc.)
- ✂️ Segmentação temporal do áudio
- 🎼 Análise musical real:
  - BPM real
  - Tonalidade correta
  - Compasso configurável
- 🎹 Seleção de instrumentos por stem
- 🧠 Regras de notação musical (legibilidade editorial)
- 🎵 Quantização rítmica inteligente
- 🎶 Separação de vozes (ex: piano mão direita / esquerda)
- 🎻 Seleção automática de clave
- 🎚️ Articulações automáticas (staccato, tenuto, acento)
- 📄 Exportação em:
  - MusicXML
  - PDF
  - MIDI
- ⚙️ Processamento assíncrono com Celery + Redis
- 🐳 Ambiente totalmente dockerizado

---

## 🏗️ Arquitetura

