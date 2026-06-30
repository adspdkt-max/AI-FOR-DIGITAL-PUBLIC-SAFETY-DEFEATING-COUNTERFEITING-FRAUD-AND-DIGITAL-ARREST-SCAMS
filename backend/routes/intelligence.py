from fastapi import APIRouter
from pydantic import BaseModel

from agents.coordinator_agent import calculate_final_threat

router = APIRouter()

class ThreatRequest(BaseModel):
    speech_risk: str
    nlp_risk: str

@router.post("/analyze-threat")
def analyze_threat(request: ThreatRequest):

    print("\n========== THREAT ANALYSIS ==========")

    print("Speech Risk:", request.speech_risk)
    print("NLP Risk   :", request.nlp_risk)

    final_threat = calculate_final_threat(
        request.speech_risk,
        request.nlp_risk
    )

    print("Final Threat:", final_threat)

    print("====================================\n")

    return {
        "speech_risk": request.speech_risk,
        "nlp_risk": request.nlp_risk,
        "final_threat": final_threat
    }
