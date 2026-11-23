#!/usr/bin/env python3
"""Make the AI judge feel curious - entry program.

Writes one short text to /output/entry.txt. The text is fixed, so the
program is fully deterministic: every run writes exactly the same bytes.
"""

import os

TEXT = (
    "The lighthouse keeper never lit the lamp on Tuesdays. "
    "No one asked why, until the night the sea went quiet and "
    "the light, unlit, still crossed the water."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
