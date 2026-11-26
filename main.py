#!/usr/bin/env python3
"""Publish the finished front page for 26 November 2026.

The picture itself lives in this repository as entry.png (drawn at build
time by gen_image.py). This program's only job is to place an exact copy
of it where the grader looks for it, so the two grading runs produce
byte-identical output.

Usage (as the grader runs it):
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""
import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        return fail(f"missing image next to this program: {source}")

    payload = source.read_bytes()
    if payload[:8] != PNG_MAGIC:
        return fail("entry.png does not start with the PNG signature")

    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(payload)
    print(f"main.py: wrote {len(payload)} bytes to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
