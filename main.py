"""Entry for make.fun bounty: Two Days of Quiet Dread.

Writes a single-line code review approval (<= 140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.
"""

import os

MAX_CHARS = 140
LINE = "Approved. The tests pass, the logic holds, and none of it will matter in a hundred years — merge it before the void notices us back."


def write_entry(out_dir):
    """Validate LINE and write it to entry.txt in out_dir."""
    if not LINE or LINE != LINE.strip():
        raise ValueError("entry must be a single non-empty line")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
