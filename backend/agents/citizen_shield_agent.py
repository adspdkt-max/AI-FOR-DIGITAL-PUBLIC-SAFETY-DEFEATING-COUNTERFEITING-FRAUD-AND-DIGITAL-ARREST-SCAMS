from unittest import result


def analyze_citizen_risk(voice_risk, text_risk, image_risk):

    score = 0

    # Voice Risk
    if voice_risk == "HIGH":
        score += 30
    elif voice_risk == "MEDIUM":
        score += 15

    # Text Risk
    if text_risk == "HIGH":
        score += 40
    elif text_risk == "MEDIUM":
        score += 20

    # Image Risk
    if image_risk == "HIGH":
        score += 30
    elif image_risk == "MEDIUM":
        score += 15

    # Final Threat
    if score >= 70:
        final_threat = "CRITICAL"
        recommendation = (
            "Possible Digital Arrest Scam. "
            "Do not transfer money. Report immediately."
        )

    elif score >= 50:
        final_threat = "HIGH"
        recommendation = (
            "Suspicious activity detected. "
            "Verify caller identity before proceeding."
        )

    elif score >= 25:
        final_threat = "MEDIUM"
        recommendation = (
            "Potential risk detected. Proceed cautiously."
        )

    else:
        final_threat = "LOW"
        recommendation = (
            "No significant scam indicators detected."
        )

    result={
        "voice_risk": voice_risk,
        "text_risk": text_risk,
        "image_risk": image_risk,
        "final_threat": final_threat,
        "recommendation": recommendation
    }
    import json

    with open(
    "database/latest_report.json",
    "w"
      ) as f:
     json.dump(result, f, indent=4)
     return result
