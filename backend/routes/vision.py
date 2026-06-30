from fastapi import APIRouter, UploadFile, File
from agents.vision_agent import analyze_currency
import tempfile
import os

router = APIRouter()

@router.post("/analyze-currency")
async def analyze_currency_note(file: UploadFile = File(...)):

    print("\n========== CURRENCY IMAGE RECEIVED ==========")
    print(f"Filename: {file.filename}")
    print("=============================================\n")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

    result = analyze_currency(temp_path)

    print("Currency Analysis Result:")
    print(result)

    os.remove(temp_path)

    return result
