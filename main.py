"""The Excuse That Almost Works — make.fun entry.

Writes the single line a gamer texts the boss to skip work during
GTA 6 launch week to /output/entry.txt.

Python 3.13 standard library only.
"""

import os

ENTRY = "My dog's at the vet, he swallowed a sock, they're keeping him in till this afternoon"


def main() -> None:
    # Gate, straight from RULES.txt: UTF-8 text of 1 to 140 characters,
    # and the task caps the line at 20 words.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert len(ENTRY.split()) <= 20, f"entry is {len(ENTRY.split())} words"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
