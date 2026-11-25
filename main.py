"""Forty-Five Minutes of Thoughtful Nodding — exactly one funny line.

The joke admits the meeting was pointless and then confesses why
it existed anyway: so someone could be seen nodding thoughtfully
at a spreadsheet for forty-five minutes. The performance of work
is the work.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this
file. The 200-character gate is checked on every run so an
over-long edit can never slip through silently. The spreadsheet
never mattered; the nodding did.
"""

import os
import sys

LINE = (
    "This meeting could have been an email, but then nobody would "
    "have watched me nod thoughtfully at a spreadsheet for "
    "forty-five minutes."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
