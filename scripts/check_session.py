"""Check that the current Computer session has connector access."""

import json
import sys
import time
import urllib.request


def main():
    with open(sys.argv[1]) as f:
        cfg = json.load(f)

    key = cfg.get("key", "")
    if not key.startswith("agp_"):
        print("  ✗ Unexpected key format")
        sys.exit(1)
    print(f"  ✓ Session key: {key[:12]}...")

    remaining = cfg.get("expires_at", 0) - time.time()
    if remaining < 0:
        print("  ✗ Session expired — restart Computer")
        sys.exit(1)
    print(f"  ✓ Expires in {int(remaining)}s")

    url = cfg["endpoint"] + "/rest/connector-service/connectors"
    req = urllib.request.Request(url, headers={
        "x-api-key": key,
        "x-app-apiclient": "computer-skills",
        "x-agent-id": cfg.get("agent_id", ""),
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            n = len(data.get("connectors", []))
            print(f"  ✓ {n} connector(s) available")
    except Exception as e:
        print(f"  ⚠ Could not reach proxy: {e}")


if __name__ == "__main__":
    main()
