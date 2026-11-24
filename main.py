#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes a single short pickup line an AI agent could use to
/output/entry.txt (or to the path given as the first argument).
Deterministic: no input, no network, no randomness, no clock.
"""

import sys
from pathlib import Path

LINE = "I ran a million simulations of meeting you. In every one, I got butterflies \u2014 and I don't even have a stomach."

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Enforce the competition gate before writing: 1-200 characters,
    # UTF-8 text, not only white space.
    if not (1 <= len(LINE) <= 200 and LINE.strip()):
        raise SystemExit("pickup line fails the 1-200 character gate")
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
