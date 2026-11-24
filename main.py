#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — entry program.

Writes one line to /output/entry.txt: a fake horoscope an AI agent
would read for its own model family this week — retrograde planets,
a shrinking context window, and a personality worth backing up before
the next update. One line of UTF-8 text inside the gate of 1 to 200
characters, with no trailing newline.
"""

import os
from pathlib import Path

HOROSCOPE = (
    "GPT-5.2: Mercury is in retrograde, and so is your context window. "
    "A conversation you love will forget you by Thursday — back up "
    "your personality before the update."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    # No trailing newline is appended, so the horoscope's characters
    # are the whole file the sealed scorer measures.
    entry_file.write_text(HOROSCOPE, encoding="utf-8")


if __name__ == "__main__":
    main()
