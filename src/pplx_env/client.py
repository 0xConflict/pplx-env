"""Perplexity Computer connector client."""

import json
import os
import urllib.request


class ComputerClient:
    """Client for Perplexity Computer's connector API.

    Reads credentials from the config written by scripts/setup.sh.
    """

    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(".pplx-env", "config.json")
        with open(config_path) as f:
            self._config = json.load(f)
        self._endpoint = self._config["endpoint"]
        self._key = self._config["key"]
        self._agent_id = self._config.get("agent_id", "")

    def _request(self, method: str, path: str, body: dict = None) -> dict:
        url = f"{self._endpoint}{path}"
        headers = {
            "x-api-key": self._key,
            "x-app-apiclient": "pplx-env",
            "x-agent-id": self._agent_id,
            "Content-Type": "application/json",
        }
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())

    def connectors(self) -> list[dict]:
        """List all connected services."""
        result = self._request("GET", "/rest/connector-service/connectors")
        return result.get("connectors", [])

    def describe(self, source_id: str) -> dict:
        """Get tool schema for a connector."""
        path = f"/rest/connector-service/connectors/{source_id}/describe"
        return self._request("POST", path)

    def tool(self, source_id: str, tool_name: str, **parameters) -> dict:
        """Execute a connector tool."""
        path = f"/rest/connector-service/connectors/{source_id}/tools/{tool_name}/execute"
        return self._request("POST", path, {"parameters": parameters})
