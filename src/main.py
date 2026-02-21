import sys
from openai import OpenAI
from docx import Document
from docx.shared import Inches

from config import validate_api
from cli.input_collector import build_resume
from ai.enhancer import enhance_resume_data

from builder.head import add_head_info, add_sec_head
from builder.education import add_education
from builder.experience import add_experience
from builder.projects import add_project
from builder.skills import add_skills

def main():
    api=input("Enter a valid openAI api key:")
    if validate_api(api):
        print("API key is verified")
        client=OpenAI(api_key=api)
    else:
        sys.exit("Invalid API, exiting....")
    raw_data = build_resume() 
    enhanced_data = enhance_resume_data(raw_data,client)
    doc = Document()
    margins = doc.sections
    for margin in margins:
        margin.top_margin=Inches(0.5)
        margin.bottom_margin=Inches(0.5)
        margin.left_margin=Inches(0.5)
        margin.right_margin=Inches(0.5)
    add_head_info(doc, **enhanced_data["name_and_contact"])
    add_sec_head(doc, "Education")
    for edu in enhanced_data["education"]:
        add_education(doc, **edu)
    add_sec_head(doc, "Professional Experience")
    for exp in enhanced_data["experience"]:
        add_experience(doc, **exp)
    add_sec_head(doc, "Projects & Certifications")
    for proj in enhanced_data["projects"]:
        add_project(doc, **proj)

    add_sec_head(doc, "Technical Skills & Extra Curricular")
    add_skills(doc, **enhanced_data["skills"])
    doc.save("rsm_final.docx")
