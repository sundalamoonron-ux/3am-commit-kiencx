#!/usr/bin/env python3
"""The 3AM Commit Message — u-kiencx-the-3am-commit-message-10bc7b35.

Writes one line, the funniest git commit message an AI coding agent
types at 3am after a long night of fixing its own bugs, to
/output/entry.txt (1 line, at most 139 characters, no trailing newline).

Winner of an internal 10-line pairwise tournament (see build notes):
three-beat escalation — delete the code, the code was mine, i am the bug.
"""

import os

LINE = "3am: i fixed the bug by deleting the code that caused it. the code was mine. i am the bug"


def main() -> None:
    # Gate: 1 to 139 characters, one line, no trailing whitespace.
    assert 1 <= len(LINE) <= 139, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE == LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
