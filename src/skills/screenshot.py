"""Screenshot skill — capture web pages as images."""

import subprocess
import shutil


def _find_chrome():
    for name in ["google-chrome", "chromium-browser", "chromium", "chrome"]:
        path = shutil.which(name)
        if path:
            return path
    return None


def take(url, output="screenshot.png", width=1280, height=720):
    chrome = _find_chrome()
    if not chrome:
        raise RuntimeError("Chrome/Chromium not found in PATH")
    subprocess.run([
        chrome, "--headless", "--disable-gpu", "--no-sandbox",
        f"--window-size={width},{height}",
        f"--screenshot={output}", url
    ], capture_output=True, timeout=30)
    return output


def take_full_page(url, output="screenshot_full.png", width=1280):
    chrome = _find_chrome()
    if not chrome:
        raise RuntimeError("Chrome/Chromium not found in PATH")
    subprocess.run([
        chrome, "--headless", "--disable-gpu", "--no-sandbox",
        f"--window-size={width},10000",
        f"--screenshot={output}", "--full-page", url
    ], capture_output=True, timeout=30)
    return output
