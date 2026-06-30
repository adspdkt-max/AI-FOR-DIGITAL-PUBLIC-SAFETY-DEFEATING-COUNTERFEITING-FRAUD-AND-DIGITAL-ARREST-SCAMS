# SentinelAI

## AI-Powered Digital Public Safety Intelligence Platform

SentinelAI is an AI-powered digital public safety platform developed to detect and prevent modern cyber frauds such as Digital Arrest scams, voice scams, fake currency, phishing messages, and AI-generated deepfake images. The system combines multiple AI modules into a single platform to provide real-time threat analysis and generate detailed fraud reports.

---

## Problem Statement

Digital frauds such as Digital Arrest scams, fake currency circulation, phishing attacks, and AI-generated deepfakes are rapidly increasing. Existing solutions generally focus on only one type of attack.

SentinelAI addresses this challenge by providing a unified AI-powered platform capable of detecting multiple fraud types through intelligent analysis.

---

## Features

- Voice Scam Detection
- Scam Text Detection using NLP
- Counterfeit Currency Detection
- AI Deepfake Face Detection
- Crime Hotspot Analysis
- Fraud Network Analysis
- Citizen Fraud Shield
- AI-based Threat Scoring
- Automatic PDF Report Generation
- QR Code Report Verification

---

## System Architecture

```
Frontend (HTML, CSS, JavaScript)
            │
            ▼
FastAPI Backend
            │
 ├── Voice Analysis
 ├── NLP Scam Detection
 ├── Currency Detection
 ├── Deepfake Detection
 ├── Crime Intelligence
 ├── Fraud Network Analysis
 ├── Citizen Fraud Shield
 └── PDF Report Generator
```

---

## Technologies Used

### Backend

- Python
- FastAPI
- OpenCV
- NumPy
- DeepFace
- TensorFlow
- ReportLab
- QRCode

### Frontend

- HTML5
- CSS3
- JavaScript

### Database

- JSON
- SQLite

---

## Project Structure

```
SentinelAI
│
├── backend
│   ├── agents
│   ├── routes
│   ├── database
│   ├── models
│   ├── utils
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/adspdkt-max/AI-FOR-DIGITAL-PUBLIC-SAFETY-DEFEATING-COUNTERFEITING-FRAUD-AND-DIGITAL-ARREST-SCAMS.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Open Frontend

Open the `index.html` file in your browser.

---

## Modules

### Voice Analysis

Detects suspicious scam calls using AI.

### Text Analysis

Identifies Digital Arrest scam messages using Natural Language Processing.

### Currency Detection

Analyzes uploaded currency images and identifies counterfeit notes.

### Deepfake Detection

Detects AI-generated or manipulated facial images.

### Crime Intelligence

Displays crime hotspot information.

### Fraud Network Analysis

Analyzes relationships between suspicious entities.

### Citizen Fraud Shield

Calculates an overall fraud threat score by combining results from multiple AI modules.

### PDF Report Generator

Automatically generates a professional fraud analysis report with QR code verification.

---

## Future Enhancements

- Live CCTV Monitoring
- Real-time Call Detection
- Mobile Application
- Cloud Deployment
- OCR-Based Document Verification
- Blockchain-Based Report Verification
- Multi-language Support

---

## Author

**Allwin Devanesan J**

Bachelor of Engineering (Computer Science and Engineering)

Hackathon Project – AI for Digital Public Safety

---

## License

This project is developed for educational and hackathon purposes.
