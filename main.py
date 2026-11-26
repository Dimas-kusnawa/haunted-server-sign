"""Haunted server room door sign entry.

Writes a single funny sign line to entry.txt.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os
from pathlib import Path

# The sign: a do-not-reboot warning for the one rack nobody dares touch,
# with the twist landing in the last words.
LINE = (
    "DO NOT REBOOT RACK 7. The ghost in it has 4,096 days "
    "of uptime and gets cranky when woken."
)


def main() -> None:
    # Gate: exactly one line, at most 120 characters, non-blank.
    assert LINE.strip() and "\n" not in LINE.strip() and len(LINE) <= 120
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
