from flask import Flask, request, render_template, send_file
import pytesseract
from PIL import Image
import pdfplumber
import os
from utils import extract_entities, fill_form

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['document']
    if file.filename == '':
        return "No selected file", 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = ""
    if file.filename.lower().endswith('.pdf'):
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    else:
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img)

    entities = extract_entities(text)

    filled_form_path = fill_form(entities, OUTPUT_FOLDER)

    return send_file(filled_form_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
