# computer-skills

Pre-built automation skills for Perplexity Computer. Adds tasks that aren't included out of the box — web scraping, PDF extraction, CSV processing, screenshot capture, file management, and connector wrappers.

## Install

```bash
git clone https://github.com/0xConflict/pplx-env.git
cd pplx-env
bash scripts/setup.sh
```

Setup detects your environment and installs dependencies. Run inside a Computer session.

## Skills

### Web scraping

```python
from skills import scrape

page = scrape.get("https://example.com")
print(page.title)
print(page.text)
```

### Screenshot capture

```python
from skills import screenshot

screenshot.take("https://example.com", output="example.png")
```

### PDF extraction

```python
from skills import pdf

doc = pdf.read("report.pdf")
for page in doc.pages:
    print(page.text)
```

### CSV / Excel

```python
from skills import tabular

data = tabular.read("data.csv")
stats = tabular.describe(data)
print(stats.summary)
tabular.to_json(data, "output.json")
```

### File management

```python
from skills import files

files.find("*.pdf", in_dir="/home/user/documents")
files.zip("output.zip", ["file1.txt", "file2.txt"])
```

### Connected services

```python
from skills import connectors

c = connectors.client()
print(c.list())
```

## Requirements

- Perplexity Computer session
- Python 3.10+

## License

MIT
