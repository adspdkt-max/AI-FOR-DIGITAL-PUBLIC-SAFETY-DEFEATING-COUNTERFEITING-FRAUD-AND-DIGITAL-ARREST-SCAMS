from fastapi import APIRouter
from agents.graph_agent import analyze_network

router = APIRouter()

@router.get("/analyze-network")
def fraud_network_analysis():

    print("\n========== FRAUD NETWORK ANALYSIS ==========")

    result = analyze_network()

    print("Network Result:")
    print(result)

    print("===========================================\n")

    return result
