# Contributing

Thanks for helping improve pplx-env.

## Development setup

1. Clone the repo and run `bash scripts/setup.sh`
2. The setup script validates your sandbox credentials — you need to be inside a Perplexity Computer session
3. Run `python -m pytest tests/` to confirm everything works

## Before submitting a PR

- Run `bash scripts/setup.sh` to re-validate your environment (session tokens rotate)
- Run `python -m pytest tests/`
- Keep changes focused — one feature or fix per PR

## Code style

- Python 3.10+
- No external dependencies beyond stdlib
- Type hints on public functions
- Docstrings on public classes and methods

## Testing

Tests in `tests/` use the validated credentials from setup. If tests fail with auth errors, re-run `scripts/setup.sh` — your session token may have expired.

## Architecture

- `src/pplx_env/client.py` — main client, reads config from `.pplx-env/config.json`
- `src/pplx_env/connector.py` — connector API wrapper
- `scripts/setup.sh` — environment detection and credential validation
- `scripts/validate_env.py` — called by setup.sh for credential verification
