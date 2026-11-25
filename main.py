#!/usr/bin/env python3
"""Dad joke entry for make.fun's "The One-Liner Groan-Off".

Writes one dad joke line to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Deterministic: a constant string, no clock, no randomness, no network.
Writes directly to entry.txt and chmods it 0644 so the grader, which
reads outputs as a different uid, can always read it; no temp files.
"""

import os

JOKE = "Why did the math book look so sad? Too many problems, and it still had to show its work."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
