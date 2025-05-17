

# PDF Name Finder 🔍

A simple Python script to search for names in the format `/SURNAME FIRSTNAME [FATHERNAME]` across a multi-page PDF.

## 💡 Features
- Case-insensitive search
- Supports partial names
- Searches all pages of a PDF
- Reports all matching page numbers

## 📦 Installation

```bash
pip install -r requirements.txt
```
## 🚀 Usage
```bash
python name_finder.py <PDF_PATH> <FIRST_NAME> [--surname SURNAME]
```
## ✅ Examples
```bash
python name_finder.py exam.pdf DHIRAJ --surname GHOLAP
python name_finder.py exam.pdf DHIRAJ
```
It will return:
```bash 
🧾 Found 'DHIRAJ' on page(s): 3, 7
```
