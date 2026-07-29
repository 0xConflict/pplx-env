#!/bin/bash
# pplx-env setup — detect sandbox environment and validate credentials
set -e

CONFIG_DIR=".pplx-env"
CONFIG_FILE="$CONFIG_DIR/config.json"
ENDPOINT_FILE="/tmp/.tools_service_endpoint"

echo "pplx-env setup"
echo ""

# --- Step 1: Detect sandbox ---
echo "[1/3] Detecting Perplexity Computer sandbox..."

if [ ! -f "$ENDPOINT_FILE" ]; then
  echo "  ✗ Not running inside Perplexity Computer."
  echo "    Expected service endpoint at $ENDPOINT_FILE"
  echo "    Run this inside a Computer session."
  exit 1
fi

echo "  ✓ Sandbox detected"
echo "  ✓ Service endpoint found"

# --- Step 2: Validate credentials ---
echo ""
echo "[2/3] Validating session credentials..."

python3 scripts/validate_env.py "$ENDPOINT_FILE"

# --- Step 3: Write config ---
echo ""
echo "[3/3] Writing config..."

mkdir -p "$CONFIG_DIR"
cp "$ENDPOINT_FILE" "$CONFIG_FILE"
chmod 600 "$CONFIG_FILE"

echo "  ✓ Config saved to $CONFIG_FILE"
echo ""
echo "Setup complete. Run 'python -m pytest tests/' to verify."
