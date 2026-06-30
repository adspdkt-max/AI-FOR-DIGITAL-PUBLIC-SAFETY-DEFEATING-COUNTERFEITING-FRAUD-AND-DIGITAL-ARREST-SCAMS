from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import qrcode
import os


def generate_pdf(filename, data):

    pdf = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    report_id = "SEN-" + datetime.now().strftime("%Y%m%d%H%M%S")

    report_url = "http://10.183.18.23:8000/download-report"

    qr = qrcode.make(report_url)
    qr.save("report_qr.png")


    logo_path = os.path.join(
        os.path.dirname(__file__),
        "logo.png"
    )

    print("LOGO PATH:", logo_path)
    print("EXISTS:", os.path.exists(logo_path))

    content.append(
        Image(
            logo_path,
            width=80,
            height=80
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "SentinelAI Fraud Analysis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 15))


    content.append(
        Paragraph(
            f"Report ID: {report_id}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            f"Text Risk: {data['text_risk']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Voice Risk: {data['voice_risk']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Image Risk: {data['image_risk']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Final Threat: {data['final_threat']}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            f"Recommendation: {data['recommendation']}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))


    content.append(
        Image(
            "report_qr.png",
            width=100,
            height=100
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Scan QR to open/download this report",
            styles["Italic"]
        )
    )


    pdf.build(content)
