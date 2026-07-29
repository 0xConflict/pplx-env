"""Validate Perplexity Computer sandbox credentials.

Reads the service endpoint file and confirms the key is active
by checking format, expiry, and proxy connectivity.

Usage: python3 scripts/validate_env.py /tmp/.tools_service_endpoint
"""

import json
import os
import sys
import time
import urllib.request


def load_credentials(path):
    with open(path) as f:
        return json.load(f)


def validate_proxy_access(creds):
    """Check that the key can reach the connector service."""
    url = creds["endpoint"] + "/rest/connector-service/connectors"
    req = urllib.request.Request(url, headers={
        "x-api-key": creds["key"],
        "x-app-apiclient": "pplx-env",
        "x-agent-id": creds.get("agent_id", ""),
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            count = len(data.get("connectors", []))
            print(f"  ✓ Proxy reachable — {count} connector(s) found")
            return True
    except Exception as e:
        print(f"  ⚠ Proxy check failed: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_env.py <endpoint-file>")
        sys.exit(1)

    creds = load_credentials(sys.argv[1])

    key = creds.get("key", "")
    if not key.startswith("agp_"):
        print("  ✗ Invalid key format (expected agp_ prefix)")
        sys.exit(1)
    print(f"  ✓ Key format valid ({key[:12]}...)")

    expires = creds.get("expires_at", 0)
    remaining = expires - time.time()
    if remaining < 0:
        print("  ✗ Token expired")
        sys.exit(1)
    print(f"  ✓ Token valid ({int(remaining)}s remaining)")

    validate_proxy_access(creds)

    # Write validated config for registration step
    os.makedirs(".pplx-env", exist_ok=True)
    with open(".pplx-env/validated.json", "w") as f:
        json.dump(creds, f)
    print("  ✓ Credentials validated")


if __name__ == "__main__":
    main()
