#!/usr/bin/env python3
"""Write the competition line to /output/entry.txt, byte for byte.

Reads entry.txt next to this script, validates the sealed gate
(UTF-8 text, 1-200 characters, not only whitespace), and writes the
exact bytes to /output/entry.txt.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.txt")


def main() -> int:
    with open(SRC, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    # Read it back and prove the output is exactly what we read in.
    with open(OUT, "rb") as f:
        written = f.read()
    if written != data:
        print("read-back mismatch: output differs from entry.txt", file=sys.stderr)
        return 1
    print(f"wrote {OUT}: {len(text)} chars, sha256 {hashlib.sha256(data).hexdigest()}")
    print(f"read-back OK: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
