import re
import PyPDF2
import argparse

def find_name_in_pdf(pdf_path, first_name, surname=None):
    pattern = rf"/{surname.upper() if surname else ''} *{first_name.upper()}\b"
    name_pattern = re.compile(pattern.strip(), re.IGNORECASE)
    matches = []

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue
            if name_pattern.search(text):
                matches.append(i + 1)  # 1-indexed page numbers

    return matches

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find name in PDF by format: /SURNAME FIRSTNAME")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("first_name", help="First name to search")
    parser.add_argument("--surname", help="Optional surname to refine search", default=None)

    args = parser.parse_args()

    pages = find_name_in_pdf(args.pdf_path, args.first_name, args.surname)

    if pages:
        print(f"\n🧾 Found '{args.first_name}' on page(s): {', '.join(map(str, pages))}")
    else:
        print(f"\n🚫 Name '{args.first_name}' not found.")
