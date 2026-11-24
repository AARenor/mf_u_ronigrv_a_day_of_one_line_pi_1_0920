"""Write the make.fun bounty entry text to entry.txt.

Bounty: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3
The entry is a single short text; this program writes its exact bytes
(UTF-8, no trailing newline) into the output folder and reports the
character count on stderr.
"""

import os
import sys

TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)

assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"


def output_dir() -> str:
    """Folder from MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
