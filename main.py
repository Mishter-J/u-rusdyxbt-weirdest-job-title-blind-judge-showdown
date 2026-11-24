#!/usr/bin/env python3
"""Weirdest Job Title entry (program/v1).

Writes a single job title, 60 characters at most, to /output/entry.txt.
The title is a fixed, deterministic string: a real-sounding job with one
hilariously specific twist, chosen from 22 candidates by local scoring
(local_score.py / pairwise_judge.py) and in-session judging against the
judge's published brief (weird, stranger than ordinary work, funny twist
on first read, sounds like a real job, reads instantly).
"""

import os

TITLE = "Lead Tester of Mattresses Nobody Sleeps On, Night Shift"

def main() -> None:
    # Gate check before writing: the entry must be exactly one non-blank
    # line of at most 60 characters (the program/v1 gate limit). Fail
    # loudly instead of writing an entry the judge would reject.
    if len(TITLE.splitlines()) != 1 or not TITLE.strip() or len(TITLE) > 60:
        raise ValueError(
            f"invalid title: must be a single non-blank line of at most "
            f"60 chars, got {len(TITLE)} chars"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)

if __name__ == "__main__":
    main()
