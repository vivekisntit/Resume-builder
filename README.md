# Resume Builder (AI-Powered CLI)
An intelligent command-line Resume Builder that generates clean, professional, ATS-friendly resumes and exports them as polished PDF files.

---

## Project Overview

This project combines structured resume input, AI-driven content enhancement, and automated document rendering into a python command-line application.

**The application**:
- Collects resume details interactively
- Enhances experience and project bullet points using AI
- Formats content into a structured document
- Exports the final resume as a professional PDF
- Can be distributed as a standalone Windows executable
---
## Core Features

- Interactive CLI-based resume input
- AI enhancement for:
    - Professional Experience
    - Project descriptions
    - Roles & Responsibilities
- Structured document formatting
- Automatic PDF generation
- Standalone .exe packaging (no Python required)

---

## Tech Stack

- Python
- Google Gemini 2.5 Flash api
- python-
- docx2pdf
- PyInstaller

---

## Project Structure
```bash
src/
|
├── main.py
├── config.py
|
├── cli/
│   └── input_collector.py
│
├── ai/
│   └── enhancer.py 
|
├── builder/
│   ├── head.py
│   ├── education.py
│   ├── experience.py
│   ├── projects.py
│   └── skills.py
|
├── .env
├── requirements.txt
└── README.md
```
---

## Setup Instructions
### Clone the Repository

```bash
git clone https://github.com/vivekisntit/Resume-builder.git
cd Resume-builder
```
### Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Download Executable
- You can download the standalone Windows executable from the Releases section.

- No Python installation required.

- The key is requested at runtime and is not stored.

### Create gemini api
Use this link to get api: https://aistudio.google.com/api-keys

### v1.0.0 – Initial AI-Powered CLI Version
- This is the first release of the Resume Builder.

- This application includes interactive CLI input, OpenAI-based enhancement, DOCX generation, and Windows .exe packaging.

- This is going to be an open-source resume builder for quick professional resume production.

### v1.2.0 – Architectural upgraded Version
- This is the Second release of the Resume Builder.

- Migrated from OpenAI to Google Gemini 2.5 Flash, cleaner project structure (CLI, AI, Builder separation), improved PDF export workflow, and enhanced packaging stability. This release is a more production-ready structure of the project.

- Project remains open-source.

### v2.0.0 - coming soon
- Will migrate from python-docx to lateX... stay tuned

---
## Demo result

![result](C:\Users\demo_image.png)
