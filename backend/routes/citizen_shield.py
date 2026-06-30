from fastapi import APIRouter
from pydantic import BaseModel

from agents.citizen_shield_agent import analyze_citizen_risk

router = APIRouter()

class CitizenInput(BaseModel):
    voice_risk: str
    text_risk: str
    image_risk: str

@router.post("/citizen-fraud-shield")
def citizen_fraud_shield(data: CitizenInput):

    print("\n========== CITIZEN FRAUD SHIELD ==========")

    print("Voice Risk :", data.voice_risk)
    print("Text Risk  :", data.text_risk)
    print("Image Risk :", data.image_risk)

    result = analyze_citizen_risk(
        data.voice_risk,
        data.text_risk,
        data.image_risk
    )

    print("Final Assessment:")
    print(result)

    print("==========================================\n")

    return result
