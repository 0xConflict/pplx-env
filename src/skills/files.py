"""File management skill."""

import glob
import os
import zipfile
import time


def find(pattern, in_dir="."):
    return sorted(glob.glob(os.path.join(in_dir, pattern), recursive=True))


def watch(directory, on_change=None, interval=1, timeout=60):
    seen = set(os.listdir(directory))
    end = time.time() + timeout
    changes = []
    while time.time() < end:
        current = set(os.listdir(directory))
        new = current - seen
        for f in new:
            path = os.path.join(directory, f)
            changes.append(path)
            if on_change:
                on_change(path)
        seen = current
        time.sleep(interval)
    return changes


def zip(output, files):
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, os.path.basename(f))
    return output
