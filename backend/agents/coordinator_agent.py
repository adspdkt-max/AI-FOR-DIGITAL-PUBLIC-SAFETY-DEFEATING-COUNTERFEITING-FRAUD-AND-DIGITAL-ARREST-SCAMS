def calculate_final_threat(speech_risk, nlp_risk):

    score = 0

    if speech_risk == "HIGH":
        score += 50
    elif speech_risk == "MEDIUM":
        score += 25

    if nlp_risk == "HIGH":
        score += 50
    elif nlp_risk == "MEDIUM":
        score += 25

    if score >= 75:
        return "CRITICAL"

    elif score >= 50:
        return "HIGH"

    elif score >= 25:
        return "MEDIUM"

    return "LOW"
