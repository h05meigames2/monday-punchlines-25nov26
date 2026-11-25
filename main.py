#!/usr/bin/env python3
"""Monday Morning Punchlines — single-joke entry for make.fun.

Writes one original joke about Monday mornings to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Deterministic: no network, no randomness, no dependencies.
The joke is 119 characters, well under the 200-character limit.
"""

import os
from pathlib import Path

JOKE = (
    "My alarm called in sick this Monday, so I stayed in bed out of "
    "solidarity — turns out even my clock is on team weekend."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE + "\n", encoding="utf-8")
    print(f"Wrote {len(JOKE)}-character joke to {entry_path}")


if __name__ == "__main__":
    main()
