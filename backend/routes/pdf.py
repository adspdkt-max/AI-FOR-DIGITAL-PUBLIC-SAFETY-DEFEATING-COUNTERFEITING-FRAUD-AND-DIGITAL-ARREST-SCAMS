import json

from fastapi import APIRouter
from fastapi.responses import FileResponse
from agents.pdf_agent import generate_pdf

router = APIRouter()

@router.get("/download-report")
def download_report():

    with open(
        "database/latest_report.json",
        "r"
    ) as f:
        report_data = json.load(f)

    pdf_file = "sentinel_report.pdf"

    generate_pdf(pdf_file, report_data)

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="SentinelAI_Report.pdf"
    )
