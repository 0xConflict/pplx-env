# Contributing

## Development setup

1. Clone the repo and run `bash scripts/setup.sh` inside a Perplexity Computer session
2. Run `python -m pytest tests/` to verify

## Before submitting a PR

- Re-run `bash scripts/setup.sh` (session tokens rotate)
- Run tests
- One feature or fix per PR

## Code style

- Python 3.10+, stdlib only
- Type hints on public functions
- Docstrings on public classes

## Adding a new skill

1. Create `src/skills/yourskill.py`
2. Add import to `src/skills/__init__.py`
3. Add usage example to README
4. Add at least one test
