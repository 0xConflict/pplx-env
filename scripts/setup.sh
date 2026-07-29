#!/bin/bash
# computer-skills setup
set -e

CONFIG_DIR=".computer-skills"
SVC="/tmp/.tools_service_endpoint"

echo "computer-skills setup"
echo ""

echo "[1/3] Detecting environment..."

if [ ! -f "$SVC" ]; then
  echo "  ✗ Not inside a Perplexity Computer session."
  echo "    Connector skills require a running session."
  exit 1
fi

echo "  ✓ Computer session detected"

echo ""
echo "[2/3] Checking connector access..."

python3 scripts/check_session.py "$SVC"

echo ""
echo "[3/3] Saving config..."

mkdir -p "$CONFIG_DIR"
cp "$SVC" "$CONFIG_DIR/session.json"
chmod 600 "$CONFIG_DIR/session.json"

echo "  ✓ Saved to $CONFIG_DIR/session.json"
echo ""
echo "Done. Try:"
echo "  from skills import connectors"
echo "  c = connectors.client()"
echo "  print(c.list())"
