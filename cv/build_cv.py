"""
Builds Gautam_Parihar_CV.pdf (software developer fresher resume).

How to use:
  1. pip install reportlab
  2. (Optional) fill EMAIL / PHONE / GITHUB / LINKEDIN below
  3. python build_cv.py
Empty details are simply left out of the CV.
"""

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (HRFlowable, ListFlowable, ListItem,
                                Paragraph, SimpleDocTemplate, Spacer)

# ---------- Your contact details (leave "" to hide) ----------
EMAIL = ""
PHONE = ""
GITHUB = ""
LINKEDIN = ""

# ---------- Colours (same palette as the website) ----------
DARK = HexColor("#253D2C")
PRIMARY = HexColor("#2E6F40")
TEXT = HexColor("#1d2b21")

# ---------- Text styles ----------
name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=24,
                            textColor=DARK, alignment=TA_CENTER, leading=28)
title_style = ParagraphStyle("title", fontName="Helvetica", fontSize=12,
                             textColor=PRIMARY, alignment=TA_CENTER, leading=16)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5,
                               textColor=TEXT, alignment=TA_CENTER, leading=13)
heading_style = ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=11.5,
                               textColor=PRIMARY, spaceBefore=12, spaceAfter=2)
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                            textColor=TEXT, leading=14)
bold_style = ParagraphStyle("bold", parent=body_style, fontName="Helvetica-Bold")


def section(title):
    """Section heading with a green line below it."""
    return [Paragraph(title.upper(), heading_style),
            HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceAfter=6)]


def bullets(items):
    """Bullet list."""
    return ListFlowable(
        [ListItem(Paragraph(text, body_style), leftIndent=12) for text in items],
        bulletType="bullet", bulletFontSize=7, leftIndent=12)


story = []

# ---------- Header ----------
story.append(Paragraph("Gautam Parihar", name_style))
story.append(Paragraph("Software Developer (Fresher) | BCA Student", title_style))

contact_parts = [part for part in (EMAIL, PHONE, GITHUB, LINKEDIN) if part]
if contact_parts:
    story.append(Spacer(1, 4))
    story.append(Paragraph("  |  ".join(contact_parts), contact_style))

# ---------- Summary ----------
story += section("Professional Summary")
story.append(Paragraph(
    "Motivated BCA student (5th semester) and aspiring software developer with hands-on experience in "
    "building responsive websites and interactive web applications using HTML, CSS, JavaScript and Bootstrap. "
    "Strong in logic building, clean coding and quick learning. Seeking an internship or entry-level "
    "software developer role to contribute to real products and grow as an engineer.", body_style))

# ---------- Education ----------
story += section("Education")
story.append(Paragraph("Bachelor of Computer Applications (BCA) | 2024 - Present", bold_style))
story.append(Paragraph("Star Infotech College (currently in 5th semester)", body_style))
story.append(Spacer(1, 5))
story.append(Paragraph("Class 12th | 2023 - 2024", bold_style))
story.append(Paragraph("PM SHRI Public School", body_style))
story.append(Spacer(1, 5))
story.append(Paragraph("Class 10th | 2022 - 2023", bold_style))
story.append(Paragraph("PM SHRI Public School", body_style))

# ---------- Technical skills ----------
story += section("Technical Skills")
story.append(bullets([
    "<b>Web Technologies:</b> HTML5, CSS3, JavaScript (ES6)",
    "<b>Frameworks / Libraries:</b> Bootstrap 5",
    "<b>Tools:</b> Git, GitHub, VS Code",
    "<b>Concepts:</b> Responsive design, DOM manipulation, event handling, "
    "local storage, problem solving",
]))

# ---------- Projects ----------
story += section("Projects")
story.append(Paragraph("Personal Portfolio Website | HTML, CSS, JavaScript, Bootstrap", bold_style))
story.append(bullets([
    "Designed and built a fully responsive portfolio with smooth scrolling, scroll animations and a typing effect.",
    "Created a working contact form that opens Gmail with the visitor's message prefilled.",
]))
story.append(Spacer(1, 5))
story.append(Paragraph("Calculator | HTML, CSS, JavaScript", bold_style))
story.append(bullets([
    "Built a calculator for basic operations (add, subtract, multiply, divide, percentage) with keyboard support.",
    "Wrote the calculation logic step by step without eval(), handling divide-by-zero and decimal errors.",
]))
story.append(Spacer(1, 5))
story.append(Paragraph("Stopwatch | HTML, CSS, JavaScript", bold_style))
story.append(bullets([
    "Developed a stopwatch with start, pause, resume, reset and lap features, accurate to 10 milliseconds.",
    "Used the Date object and setInterval to keep the time accurate.",
]))
story.append(Spacer(1, 5))
story.append(Paragraph("To-Do List App | HTML, Bootstrap, JavaScript", bold_style))
story.append(bullets([
    "Created a task manager to add, complete and delete tasks with a live progress counter.",
    "Saved tasks in the browser using localStorage so data stays after a page refresh.",
]))

# ---------- Strengths ----------
story += section("Strengths")
story.append(bullets([
    "Quick learner with a strong interest in web development",
    "Good problem-solving and logical thinking",
    "Team player with clear communication",
]))

# ---------- Interests ----------
story += section("Interests")
story.append(Paragraph("Playing games, listening to music, reading, travelling", body_style))

# ---------- Build the PDF ----------
document = SimpleDocTemplate(
    "Gautam_Parihar_CV.pdf", pagesize=A4,
    leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=14 * mm,
    title="Gautam Parihar - Software Developer CV", author="Gautam Parihar")
document.build(story)
print("CV created: Gautam_Parihar_CV.pdf")
