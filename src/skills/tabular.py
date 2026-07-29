"""CSV / Excel processing skill."""

import csv
import json
import os


def read(path, sheet=None, delimiter=None):
    ext = os.path.splitext(path)[1].lower()
    if ext in (".xlsx", ".xls"):
        return _read_excel(path, sheet)
    if delimiter is None:
        delimiter = "\t" if ext == ".tsv" else ","
    return _read_csv(path, delimiter)


def _read_csv(path, delimiter=","):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)


def _read_excel(path, sheet=None):
    import subprocess
    cmd = ["python3", "-c", f"""
import json
try:
    import openpyxl
    wb = openpyxl.load_workbook('{path}', read_only=True)
    ws = wb['{sheet}'] if '{sheet}' != 'None' else wb.active
    rows = list(ws.iter_rows(values_only=True))
    headers = [str(h) for h in rows[0]]
    data = [dict(zip(headers, [str(v) if v is not None else '' for v in r])) for r in rows[1:]]
    print(json.dumps(data))
except ImportError:
    print('[]')
"""]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout) if result.stdout.strip() else []


def to_json(data, output):
    with open(output, "w") as f:
        json.dump(data, f, indent=2)
    return output


def describe(data):
    if not data:
        return {"rows": 0, "columns": [], "summary": "Empty dataset"}
    columns = list(data[0].keys())
    return {
        "rows": len(data),
        "columns": columns,
        "summary": f"{len(data)} rows, {len(columns)} columns: {', '.join(columns[:5])}{'...' if len(columns) > 5 else ''}"
    }
