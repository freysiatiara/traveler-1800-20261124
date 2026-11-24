#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) that explains the
modern internet to a time traveler from the year 1800, using only
words and pictures that a person of that year could hold in their
head: letters, horses, lightning, wires, tea.

The sentence goes to the path the grader names: ENTRY_OUTPUT when
set, else OUTPUT_DIR / MAKEFUN_OUTPUT_DIR joined with entry.txt,
else /output/entry.txt.
"""

import os
import sys

SENTENCE = (
    "Imagine every letter ever written, carried not by horse but by "
    "lightning through wires, so any man may read the whole world's "
    "words before his tea cools."
)


def output_path():
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
