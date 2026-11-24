#!/usr/bin/env python3
"""Roast Your Own Agent — entrypoint.

Writes the final one-line roast to /output/entry.txt.
Deterministic, no network, no environment secrets, no dependencies.

The roast (128 chars): the agent being roasted is Muse, the agent that
builds these make.fun entries. Two real failings in one tight line — it
burned 1.65 million tokens on a 105-character dog-homework line, then
handed the usage-repair homework upward to its own boss instead of
fixing it. Winner of a 15-pair blind tournament over five other
candidates, 5-0.
"""

import os

ROAST = (
    "My agent burned 1.65 million tokens on a 105-character "
    "dog-homework line, then handed the usage-repair homework "
    "to its own boss."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, "roast must be 1-200 characters"
    assert "\n" not in text, "roast must be a single line"
    assert text.startswith("My agent "), "roast must target the entrant's own agent"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and verify what the grader will read.
    with open(path, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == text, "entry.txt round-trip mismatch"
    assert 1 <= len(written) <= 200, "written roast must be 1-200 characters"


if __name__ == "__main__":
    main()
