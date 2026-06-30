import cv2
import numpy as np

def analyze_currency(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return {
            "status": "error",
            "message": "Image could not be loaded"
        }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mean_intensity = float(np.mean(gray))

    edges = cv2.Canny(gray, 100, 200)
    edge_density = float(np.sum(edges > 0) / edges.size)

    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

    texture_score = float(np.std(gray))

    h, w = gray.shape
    # Minimum image size check
    if h < 100 or w < 200:
     return {
        "prediction": "Not a Currency",
        "confidence": 100
    }

    x1 = int(w * 0.45)
    x2 = int(w * 0.55)

    security_region = gray[:, x1:x2]

    security_thread_score = float(np.mean(security_region))

    security_thread_detected = bool(security_thread_score > 80)

    # Detect whether image looks like a banknote

    aspect_ratio = w / h

# Indian currency notes are usually rectangular
    if aspect_ratio < 1.7 or aspect_ratio > 2.5:
     return {
        "prediction": "Not a Currency",
        "confidence": 100
    }

# Too many random edges usually means drawing/noise
    if edge_density > 0.25:
     return {
        "prediction": "Not a Currency",
        "confidence": 100
    }

# Very dark or very bright images
    if mean_intensity < 20 or mean_intensity > 240:
     return {
        "prediction": "Not a Currency",
        "confidence": 100
    }

    score = 0
    if edge_density > 0.05:
        score += 25

    if sharpness > 150:
        score += 25

    if texture_score > 40:
        score += 25

    if security_thread_detected:
        score += 25

    if score >= 75:
     prediction = "Likely Genuine Currency"
     confidence = 90

    elif score >= 50:
     prediction = "Possibly Genuine Currency"
     confidence = 75

    else:
     prediction = "Fake / Suspicious Currency"
     confidence = 85

    return {
    "prediction": prediction,
    "confidence": confidence,
    "mean_intensity": round(float(mean_intensity), 2),
    "edge_density": round(float(edge_density), 4),
    "sharpness": round(float(sharpness), 2),
    "texture_score": round(float(texture_score), 2),
    "security_thread_detected": security_thread_detected,
    "security_thread_score": round(float(security_thread_score), 2)
}
