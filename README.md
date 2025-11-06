# CalmAI Meditation App
CalmAI is an AI-powered meditation and mindfulness assistant that generates personalized, emotionally resonant guided sessions. It combines GPT-4o for script generation, ElevenLabs for voice synthesis, and ambient background mixing to deliver immersive, calming audio experiences tailored to your mood.

# Features
Personalized meditation scripts using OpenAI GPT-4o
Natural voice synthesis with ElevenLabs (Jess, Adam, etc.)
Ambient background mixing (rain, forest, ocean, stream, wind)
Full transparency: GPT-generated script returned with audio
Multilingual support (Norwegian, Bengali, Hindi, more)
FastAPI backend with modular, production-grade architecture
Test scripts for mood-specific user flows

# Tech Stack
Python 3.11+

FastAPI for backend API

OpenAI GPT-4o for meditation script generation

ElevenLabs TTS API for voice synthesis

FFmpeg for audio mixing

Dotenv for environment management

Run FastAPI Backend
bash
uvicorn backend.main:app --reload

# Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/your-username/CalmAI.git
cd CalmAI/calm_backend
2. Create and Activate Virtual Environment
bash
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # macOS/Linux
3. Install Dependencies
bash
pip install -r ../requirements.txt
4. Add .env File
Create a .env file in calm_backend/:

# Running Django Server
From inside calm_backend/:

bash
python manage.py runserver

Code
Starting development server at http://127.0.0.1:8000/

# Testing the API

Using Postman or curl
URL: http://127.0.0.1:8000/api/generate/

Method: POST

Headers: Content-Type: application/json

Body:

json
{
  "mood": "tired",
  "voice": "female",
  "background": "forest",
  "answers": ""
}
Output Location
After a successful request, check:

Code
calm_backend/backend/output/
You’ll find:

sessionX.mp3 → voice-only

sessionX_final.mp3 → final mixed meditation session
