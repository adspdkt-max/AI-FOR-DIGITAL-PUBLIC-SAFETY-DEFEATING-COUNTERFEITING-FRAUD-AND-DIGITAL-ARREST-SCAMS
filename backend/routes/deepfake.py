from fastapi import APIRouter, UploadFile, File
from agents.deepfake_agent import analyze_face
import tempfile
import os

router = APIRouter()

@router.post("/analyze-face")
async def analyze_face_image(file: UploadFile = File(...)):

    print("\n========== FACE IMAGE RECEIVED ==========")
    print(f"Filename: {file.filename}")
    print("=========================================\n")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

    result = analyze_face(temp_path)

    print("Face Analysis Result:")
    print(result)

    os.remove(temp_path)

    return result
