from fastapi import APIRouter
from pydantic import BaseModel

from agents.nlp_agent import detect_scam

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/analyze-text")
def analyze_text(request: TextRequest):

    print("\n========== TEXT RECEIVED ==========")
    print(request.text)
    print("===================================\n")

    result = detect_scam(request.text)

    print("NLP Result:", result)

    return result
