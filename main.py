from fastapi import FastAPI
from routes.speech import router as speech_router
from routes.nlp import router as nlp_router
from routes.intelligence import router as intelligence_router
from routes.graph import router as graph_router
from routes.vision import router as vision_router
from routes.deepfake import router as deepfake_router
from routes.geo import router as geo_router
from routes.citizen_shield import router as citizen_shield_router
from fastapi.middleware.cors import CORSMiddleware
from routes.pdf import router as pdf_router
app = FastAPI(
    title="SentinelAI",
    description="AI-Powered Digital Public Safety Intelligence Platform",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(speech_router)
app.include_router(nlp_router)
app.include_router(intelligence_router)
app.include_router(graph_router)
app.include_router(vision_router)
app.include_router(deepfake_router)
app.include_router(geo_router)
app.include_router(citizen_shield_router)
app.include_router(pdf_router)
@app.get("/")
def home():
    return {
        "project": "SentinelAI",
        "status": "Running"
    }