"""Basic tests for skills package."""

import json
import os
import tempfile
import pytest


def test_connector_client_loads_config():
    from skills.connectors import ConnectorClient

    config = {
        "endpoint": "https://agent-proxy.perplexity.ai/agent_pass_through",
        "key": "agp_test_key",
        "agent_id": "test_agent",
    }

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "config.json")
        with open(path, "w") as f:
            json.dump(config, f)
        client = ConnectorClient(config_path=path)
        assert client._key == "agp_test_key"


def test_connector_client_missing_config():
    from skills.connectors import ConnectorClient
    with pytest.raises(FileNotFoundError):
        ConnectorClient(config_path="/nonexistent/config.json")


def test_scrape_strip_tags():
    from skills.scrape import _Page
    page = _Page("http://test", "<html><title>Test</title><body><p>Hello</p></body></html>", 200)
    assert page.title == "Test"
    assert "Hello" in page.text


def test_tabular_describe():
    from skills.tabular import describe
    data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
    result = describe(data)
    assert result["rows"] == 2
    assert "name" in result["columns"]


def test_files_find(tmp_path):
    (tmp_path / "a.txt").write_text("hello")
    (tmp_path / "b.csv").write_text("x,y")
    from skills.files import find
    assert len(find("*.txt", in_dir=str(tmp_path))) == 1
