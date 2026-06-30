from fastapi import APIRouter
from agents.geo_agent import analyze_hotspots

router = APIRouter()

@router.get("/crime-hotspots")
def crime_hotspots():

    return analyze_hotspots()
