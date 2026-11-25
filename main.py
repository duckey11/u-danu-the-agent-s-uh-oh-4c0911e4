#!/usr/bin/env python3
"""The Agent's Uh-Oh: write exactly one word to /output/entry.txt.

One word an AI agent blurts out when it has no idea what to do.
Deterministic, no network, no files read outside this repo.
"""

import os

WORD = "hallucinating"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
