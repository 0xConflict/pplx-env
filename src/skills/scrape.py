"""Web scraping skill — fetch and parse web pages."""

import html.parser
import urllib.request


class _Page:
    def __init__(self, url, content, status):
        self.url = url
        self._content = content
        self.status = status
        self.title = self._extract_title()
        self.text = self._strip_tags()

    def _extract_title(self):
        start = self._content.lower().find("<title>")
        end = self._content.lower().find("</title>")
        if start != -1 and end != -1:
            return self._content[start + 7:end].strip()
        return ""

    def _strip_tags(self):
        class _Stripper(html.parser.HTMLParser):
            def __init__(self):
                super().__init__()
                self.parts = []
            def handle_data(self, d):
                self.parts.append(d)
        s = _Stripper()
        s.feed(self._content)
        return " ".join(s.parts).strip()

    def links(self):
        import re
        return re.findall(r'href=["\']([^"\']+)["\']', self._content)


def get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "computer-skills/0.2"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content = resp.read().decode("utf-8", errors="replace")
        return _Page(url, content, resp.status)
