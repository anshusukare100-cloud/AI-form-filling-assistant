# AI-Powered Form Filling Assistant

## Overview
A simple Flask web app that extracts key information (Name, DOB, Address, Aadhaar, PAN) from uploaded scanned documents (PDF/images) and produces a pre-filled Word document.

## Requirements
- Python 3.9+ recommended
- Tesseract OCR installed on the system and accessible in PATH.

## Install Tesseract (important)
- **Ubuntu / Debian**: `sudo apt-get install tesseract-ocr`
- **Windows**: Download installer from https://github.com/tesseract-ocr/tesseract and install. Add tesseract to PATH.

## Setup
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows (PowerShell)
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
```

Open http://127.0.0.1:5000/ in your browser.

## Notes & Next Steps
- This is a prototype: entity extraction uses heuristics and regex. For production, use a trained NER model and more robust OCR (Google Vision, AWS Textract).
- To handle Indian languages, integrate Indic OCR or translation services.
- To support handwritten text, use advanced OCR like Google Vision or fine-tuned models.
