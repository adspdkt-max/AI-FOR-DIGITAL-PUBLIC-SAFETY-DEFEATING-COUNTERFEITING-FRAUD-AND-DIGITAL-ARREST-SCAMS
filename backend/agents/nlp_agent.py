def detect_scam(text):

    text = text.lower()

    digital_arrest_keywords = [
        "cbi",
        "ed",
        "enforcement directorate",
        "customs",
        "cyber crime",
        "crime branch",
        "police department",
        "supreme court",
        "high court",

        "arrest warrant",
        "digital arrest",
        "legal action",
        "criminal case",
        "court order",
        "fir registered",
        "non bailable warrant",
        "investigation ongoing",
        "money laundering",
        "drug trafficking",
        "illegal transaction",
        "tax evasion",

        "immediately",
        "urgent",
        "final warning",
        "last chance",
        "within 30 minutes",
        "account blocked",
        "account suspended",
        "freeze account",
        "bank account frozen",
        "service terminated",

        "aadhaar linked",
        "pan linked",
        "kyc verification",
        "video verification",
        "verification call",
        "identity verification",
        "confirm your identity",

        "do not disconnect",
        "stay on the call",
        "transfer money",
        "safe account",
        "secure account",
        "temporary transfer",
        "verify funds",
        "share otp",
        "provide otp",
        "send otp",
        "bank verification",
        "account verification",

        "atm pin",
        "debit card",
        "credit card",
        "internet banking",
        "net banking",
        "bank credentials",
        "login credentials",
        "bank account number",

        "aadhaar number",
        "pan card",
        "passport number",
        "driving licence",
        "personal details",

        "your account is under investigation",
        "national security issue",
        "confidential investigation",
        "suspicious transaction detected",
        "illegal activity detected",
        "your number will be blocked",
        "your account will be frozen",
        "cooperate with investigation",
        "secret operation",
        "keep this confidential"
    ]

    matches = []

    for keyword in digital_arrest_keywords:
        if keyword in text:
            matches.append(keyword)

    confidence = min(len(matches) * 10, 95)

    if len(matches) >= 5:
        risk = "HIGH"
        scam_type = "Digital Arrest Scam"

    elif len(matches) >= 2:
        risk = "MEDIUM"
        scam_type = "Suspicious Communication"

    else:
        risk = "LOW"
        scam_type = "Normal"

    return {
        "scam_type": scam_type,
        "risk_level": risk,
        "confidence": confidence,
        "matched_keywords": matches
    }
