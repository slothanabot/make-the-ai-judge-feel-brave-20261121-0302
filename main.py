#!/usr/bin/env python3
"""Mending the Net at Dusk.

Writes one short text to /output/entry.txt: a quiet scene of mending a
fishing net at dusk while the tide comes in, hands busy, the day's work
nearly done. The text is fixed and deterministic; the program writes the
same bytes on every run.
"""

import os

TEXT = (
    "The net tore where the day pulled hardest. "
    "You sit with it as the light thins, one knot, then another, "
    "the thread slipping through your fingers, the tide coming in "
    "slow enough to hear. The water takes the day's noise with it. "
    "The mending is enough."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
