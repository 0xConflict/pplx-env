# computer-skills

Pre-built skills for Perplexity Computer. Adds common automation tasks that aren't included out of the box — web scraping with headless Chrome, PDF extraction, CSV/Excel processing, screenshot capture, and more.

## Install

```bash
git clone https://github.com/0xConflict/pplx-env.git
cd pplx-env
bash scripts/setup.sh
```

Setup auto-detects your Computer sandbox environment and installs dependencies.

## Skills

### Web scraping
```python
from skills import scrape

page = scrape.get("https://example.com")
print(page.title)
print(page.text)
links = page.links()
```

### Screenshot capture
```python
from skills import screenshot

screenshot.take("https://example.com", output="example.png")
screenshot.take_full_page("https://example.com", output="full.png")
```

### PDF extraction
```python
from skills import pdf

doc = pdf.read("report.pdf")
for page in doc.pages:
    print(page.text)

tables = pdf.extract_tables("report.pdf")
```

### CSV / Excel
```python
from skills import tabular

data = tabular.read("data.csv")
data = tabular.read("data.xlsx", sheet="Sheet1")
tabular.to_json(data, "output.json")

# Quick analysis
stats = tabular.describe(data)
print(stats.summary)
```

### File management
```python
from skills import files

files.find("*.pdf", in_dir="/home/user/documents")
files.watch("/tmp/downloads", on_change=lambda f: print(f"New: {f}"))
files.zip("output.zip", ["file1.txt", "file2.txt"])
```

### Connectors
```python
from skills import connectors

# Uses your Computer session's connected services
c = connectors.client()
emails = c.tool("gcal", "search_email", queries=["invoice"])
events = c.tool("gcal", "list_events", days=7)
```

## How it works

Perplexity Computer sessions have a service endpoint at `/tmp/.tools_service_endpoint` with session-scoped credentials for connected services. The connector skill wraps this — everything else uses standard Python libraries.

## Requirements

- Perplexity Computer session (for connector skills)
- Python 3.10+
- No external dependencies beyond what Computer already has installed

## License

MIT
