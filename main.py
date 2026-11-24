"""One-Liner Laugh Lab entry.

The program writes one short funny line to /output/entry.txt: the excuse
a robot vacuum gives after eating a sock. The gate allows 1 to 200
characters of UTF-8 text, not whitespace-only, on a single line.
Standard library only.
"""

import os
from pathlib import Path

LINE = "The dog eats your shoes, gets treats. I eat one sock, get the third degree."

MAX_CHARS = 200  # gate cap from the competition rules (1-200 characters)


def main() -> None:
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} non-whitespace characters"
        )
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
