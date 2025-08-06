import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def save_results(results, folder, domain):
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{domain.replace('.', '_')}_{timestamp}.pdf"
    filepath = os.path.join(folder, filename)

    doc = SimpleDocTemplate(filepath, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for section, content in results.items():
        story.append(Paragraph(f"[{section.upper()}]", styles['Heading3']))
        if isinstance(content, dict):
            for k, v in content.items():
                story.append(Paragraph(f"{k}: {v}", styles['BodyText']))
        elif isinstance(content, list):
            for item in content:
                story.append(Paragraph(f"• {item}", styles['BodyText']))
        else:
            story.append(Paragraph(str(content), styles['BodyText']))
        story.append(Spacer(1, 12))

    doc.build(story)
    print(f"[+] PDF report generated: {filepath}")
