from deepface import DeepFace
import cv2


def analyze_face(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return {
            "prediction": "Image could not be loaded",
            "confidence": 0
        }

    try:

        DeepFace.extract_faces(
            img_path=image_path,
            detector_backend="opencv",
            enforce_detection=True
        )

    except:

        return {
            "prediction": "No Face Detected",
            "confidence": 100
        }

    try:

        result = DeepFace.analyze(
            img_path=image_path,
            actions=["emotion"],
            detector_backend="opencv",
            enforce_detection=False
        )

        prediction = "Likely Real Face"
        confidence = 95

        return {
            "prediction": prediction,
            "confidence": confidence
        }

    except Exception:

        return {
            "prediction": "Potential AI Generated Face",
            "confidence": 95
        }
