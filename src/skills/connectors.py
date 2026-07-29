"""Connector skill — interact with Perplexity Computer's connected services."""

import json
import os
import urllib.request


class ConnectorClient:
    """Wraps Perplexity Computer's connector API."""

    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(".pplx-env", "config.json")
        with open(config_path) as f:
            self._config = json.load(f)
        self._endpoint = self._config["endpoint"]
        self._key = self._config["key"]
        self._agent_id = self._config.get("agent_id", "")

    def _request(self, method, path, body=None):
        url = f"{self._endpoint}{path}"
        headers = {
            "x-api-key": self._key,
            "x-app-apiclient": "computer-skills",
            "x-agent-id": self._agent_id,
            "Content-Type": "application/json",
        }
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())

    def list(self):
        result = self._request("GET", "/rest/connector-service/connectors")
        return result.get("connectors", [])

    def describe(self, source_id):
        return self._request("POST", f"/rest/connector-service/connectors/{source_id}/describe")

    def tool(self, source_id, tool_name, **parameters):
        path = f"/rest/connector-service/connectors/{source_id}/tools/{tool_name}/execute"
        return self._request("POST", path, {"parameters": parameters})


def client(config_path=None):
    return ConnectorClient(config_path)
