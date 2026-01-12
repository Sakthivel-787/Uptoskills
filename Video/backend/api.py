# backend/api.py
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.gemini_api import generate_text
from backend.tts import text_to_speech
from backend.wave2lip import generate_video
import os

# --------------------------
# FastAPI App
# --------------------------
app = FastAPI(title="AI Lesson Generator")

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow requests from any origin (can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# Request Model
# --------------------------
class LessonRequest(BaseModel):
    course: str
    topic: str
    celebrity: str

# --------------------------
# Root Route (optional)
# --------------------------
@app.get("/")
def home():
    return {"message": "Welcome to AI Lesson Generator Backend!"}

# --------------------------
# Generate Lesson Endpoint
# --------------------------
@app.post("/generate")
def generate_lesson(data: LessonRequest, background_tasks: BackgroundTasks):
    """
    Starts lesson generation in the background:
    1. Gemini text generation
    2. Text-to-Speech conversion
    3. Lip-sync video generation with Wave2Lip
    """
    background_tasks.add_task(process_lesson, data)
    return {"status": "Processing started"}

# --------------------------
# Background Task
# --------------------------
def process_lesson(data: LessonRequest):
    try:
        # 1️⃣ Generate text from Gemini
        prompt = f"Explain {data.topic} in 50 words."
        script = generate_text(prompt)

        # Save script
        os.makedirs("outputs/audio/", exist_ok=True)
        script_file = f"outputs/audio/script_{data.topic}.txt"
        with open(script_file, "w", encoding="utf-8") as f:
            f.write(script)

        # 2️⃣ Convert text to speech
        audio_file = f"outputs/audio/{data.topic}.wav"
        text_to_speech(script, audio_file)

        # 3️⃣ Generate lip-sync video
        celeb_img = f"assets/celebrities/{data.celebrity.lower()}.jpg"
        os.makedirs("outputs/video/", exist_ok=True)
        video_file = f"outputs/video/{data.topic}.mp4"
        generate_video(celeb_img, audio_file, video_file)

        print(f"✅ Lesson ready: {video_file}")

    except Exception as e:
        print(f"❌ Error generating lesson: {e}")
