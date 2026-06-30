import librosa
import numpy as np

def extract_audio_features(audio_path):

    y, sr = librosa.load(audio_path, sr=None)

    features = {
        "duration": librosa.get_duration(y=y, sr=sr),
        "sample_rate": sr,
        "zero_crossing_rate": float(np.mean(librosa.feature.zero_crossing_rate(y))),
        "spectral_centroid": float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))),
        "rms_energy": float(np.mean(librosa.feature.rms(y=y)))
    }

    return features
def calculate_risk(features):

    score = 0

    if features["rms_energy"] < 0.05:
        score += 30

    if features["spectral_centroid"] > 3000:
        score += 40

    if features["zero_crossing_rate"] > 0.20:
        score += 30

    if score >= 60:
        return "HIGH"

    elif score >= 30:
        return "MEDIUM"

    return "LOW"
