import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from backend.script_generator import generate_script
from backend.tts_engine import synthesize_voice
from backend.mixer import mix_background
from backend.mood_questions import get_questions

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Enable CORS for API access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure output folder exists
os.makedirs("backend/output", exist_ok=True)

# Serve audio files from /output
app.mount("/output", StaticFiles(directory="backend/output"), name="output")

# Root endpoint (optional)
@app.get("/")
def root():
    return {"message": "CalmAI backend is running"}

# Request and response models
class GenerateRequest(BaseModel):
    mood: str
    answers: str
    voice: str
    background: str

class GenerateResponse(BaseModel):
    file: str
    script: List[dict]

# Mood-based questions
@app.get("/questions")
def get_mood_questions(mood: str):
    logging.info("Fetching questions for mood: %s", mood)
    questions = get_questions(mood)
    return {"questions": questions}

# Meditation session generator
@app.post("/generate", response_model=GenerateResponse)
async def generate_session(req: GenerateRequest):
    try:
        logging.info("Generating session for mood: %s, voice: %s", req.mood, req.voice)

        # Generate meditation script
        tokens = generate_script(req.mood, req.answers)
        if not tokens or not isinstance(tokens, list):
            raise ValueError("No tokens returned from GPT")

        # Synthesize voice
        voice_path = synthesize_voice(tokens, req.voice)
        if not voice_path:
            raise RuntimeError("Voice synthesis failed")

        # Mix background
        final_path = mix_background(voice_path, req.background)

        return {
            "file": f"/output/{os.path.basename(final_path)}",
            "script": tokens
        }

    except Exception as e:
        logging.error("ERROR in /generate: %s", e)
        return JSONResponse(status_code=500, content={"error": str(e)})

# Download endpoint
@app.get("/download")
def download_file(filename: str):
    file_path = os.path.join("backend", "output", filename)
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename, media_type='audio/mpeg')
    return JSONResponse(status_code=404, content={"error": "File not found"})
