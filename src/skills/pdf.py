"""PDF extraction skill — read text and tables from PDFs."""

import subprocess
import json


class _Page:
    def __init__(self, number, text):
        self.number = number
        self.text = text


class _Document:
    def __init__(self, pages):
        self.pages = pages
        self.text = "\n\n".join(p.text for p in pages)


def read(path):
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", path, "-"],
            capture_output=True, text=True, timeout=30
        )
        pages_text = result.stdout.split("\f")
        pages = [_Page(i + 1, t.strip()) for i, t in enumerate(pages_text) if t.strip()]
        return _Document(pages)
    except FileNotFoundError:
        try:
            result = subprocess.run(
                ["python3", "-c", f"import fitz; doc=fitz.open('{path}'); [print(p.get_text()) for p in doc]"],
                capture_output=True, text=True, timeout=30
            )
            return _Document([_Page(1, result.stdout)])
        except Exception:
            raise RuntimeError("No PDF reader available (install poppler-utils or pymupdf)")


def extract_tables(path):
    try:
        import csv
        import io
        result = subprocess.run(
            ["pdftotext", "-layout", "-tsv", path, "-"],
            capture_output=True, text=True, timeout=30
        )
        reader = csv.DictReader(io.StringIO(result.stdout), delimiter="\t")
        return list(reader)
    except Exception:
        return []
