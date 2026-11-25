"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt. The gate allows 1 to 200 characters, so
the line is checked before writing.
"""

import os

LIMIT = 200
OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Tip: The bug isn't in the last place you'd look. "
    "It's in the first place you checked, nodded at, "
    "and said 'can't be that' about."
)


def check_line(line: str) -> None:
    """Enforce the gate exactly: UTF-8 text, 1..LIMIT chars, not only white space."""
    assert line.strip(), "entry must not be only white space"
    assert 1 <= len(line) <= LIMIT, f"line is {len(line)} chars, limit is {LIMIT}"
    assert "\n" not in line, "entry must be a single line"


def main() -> None:
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    # Read back what actually landed on disk, so a bad write cannot slip through.
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        written = fh.read()
    check_line(written)
    assert written == LINE, "written file does not match the intended line"
    print(f"wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
