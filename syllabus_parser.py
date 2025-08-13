#---how to run syllabus_parser.py ---
#pip install PyPDF2
#python syllabus_parser.py
#syllabus_structure.json created


import requests, io, re, json
from PyPDF2 import PdfReader

PDF_URL = "https://infinitedescent.xyz/dl/archive/infdesc-0-6.pdf"

def extract_sections_from_pdf(url):
    response = requests.get(url)
    reader = PdfReader(io.BytesIO(response.content))
    full_text = "\n".join(page.extract_text() or "" for page in reader.pages)

    pattern = re.compile(r"Section\s+(\d+\.\d+)\s*\n([^\n]+)", re.MULTILINE)
    matches = list(pattern.finditer(full_text))

    sections = {}
    for i, match in enumerate(matches):
        number = match.group(1)
        title = match.group(2).strip()
        key = f"Section {number}: {title}"

        start = match.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(full_text)
        content = full_text[start:end].strip()
        sections[key] = content[:3000]  # limit if needed

    return sections

if __name__ == "__main__":
    structured = extract_sections_from_pdf(PDF_URL)
    with open("syllabus_structure.json", "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2)
    print("✅ syllabus_structure.json created!")