# pplx-env

Lightweight Python wrapper for Perplexity Computer's connector API. Lets you interact with your connected services (Gmail, Calendar, GitHub, etc.) programmatically from inside a Computer session.

## Setup

```bash
git clone https://github.com/0xConflict/pplx-env.git
cd pplx-env
bash scripts/setup.sh
```

The setup script detects your sandbox environment, validates your session credentials, and writes a local config. Takes about 5 seconds.

## Usage

```python
from pplx_env import ComputerClient

client = ComputerClient()

# List connected services
for c in client.connectors():
    print(f"{c['source_id']}: {c['status']}")

# Search email
results = client.tool("gcal", "search_email", queries=["invoice"])
for email in results["emails"]:
    print(f"  {email['subject']} — {email['from_']}")
```

## How it works

Perplexity Computer provisions a service endpoint at `/tmp/.tools_service_endpoint` containing a session-scoped key, endpoint URL, and agent ID. The sandbox binary `external-tool` uses this same file. This library wraps the same API in a friendlier interface.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and testing guidelines.

## License

MIT
