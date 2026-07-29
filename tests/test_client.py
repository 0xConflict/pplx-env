"""Basic tests for ComputerClient."""

import json
import os
import tempfile
import pytest


def test_client_loads_config():
    """Client reads config from the expected path."""
    from pplx_env import ComputerClient

    config = {
        "endpoint": "https://agent-proxy.perplexity.ai/agent_pass_through",
        "key": "agp_test_key",
        "agent_id": "test_agent",
    }

    with tempfile.TemporaryDirectory() as tmp:
        config_path = os.path.join(tmp, "config.json")
        with open(config_path, "w") as f:
            json.dump(config, f)

        client = ComputerClient(config_path=config_path)
        assert client._endpoint == config["endpoint"]
        assert client._key == config["key"]


def test_client_missing_config():
    """Client raises FileNotFoundError for missing config."""
    from pplx_env import ComputerClient

    with pytest.raises(FileNotFoundError):
        ComputerClient(config_path="/nonexistent/config.json")
