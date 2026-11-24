#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes exactly one line (110 characters, no trailing newline) to
/output/entry.txt, then reads it back and asserts it matches.
"""
import os
from pathlib import Path

ENTRY = "It worked on my machine — production is the same code, only now it has an audience, stage fright, and a pager."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, "read-back mismatch"
    assert len(back) == 110, f"expected 110 chars, got {len(back)}"
    assert not back.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
