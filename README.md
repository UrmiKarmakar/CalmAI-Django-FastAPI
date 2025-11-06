# 🧘 CalmAI: AI-Powered Meditation App

CalmAI is a modular meditation app that generates emotionally tuned, voice-guided sessions using AI. It combines:

- 🎙️ OpenAI GPT-4o → for generating meditation scripts
- 🗣️ ElevenLabs → for voice synthesis
- 🌿 FFmpeg → for mixing voice with ambient backgrounds
- ⚡ FastAPI → for backend API
- 🌐 Django → for optional frontend/admin interface

## 🔄 Workflow Overview

1. **User sends a POST request** to `/api/generate/` with mood, voice, and background.
2. **FastAPI backend**:
   - Uses OpenAI to generate a meditation script
   - Sends the script to ElevenLabs for voice synthesis
   - Mixes the voice with ambient background using FFmpeg
3. **Output**:
   - `sessionX.mp3`: voice-only
   - `sessionX_final.mp3`: final mixed meditation session

