from fastapi import APIRouter, UploadFile, File
from agents.speech_agent import extract_audio_features, calculate_risk
import tempfile
import os

router = APIRouter()

@router.post("/analyze-voice")
async def analyze_voice(file: UploadFile = File(...)):

    print("\n========== VOICE FILE RECEIVED ==========")
    print(f"Filename: {file.filename}")
    print("=========================================\n")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

    features = extract_audio_features(temp_path)

    print("Audio Features:")
    print(features)

    risk_level = calculate_risk(features)

    print(f"Voice Risk Level: {risk_level}")

    os.remove(temp_path)

    return {
        "filename": file.filename,
        "risk_level": risk_level,
        "features": features
    }
