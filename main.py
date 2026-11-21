"""Write one short relaxing text to entry.txt.

The text is fixed in this file: no clock, no randomness, no network,
so every run writes exactly the same bytes.
"""

import os

TEXT = (
    "You have read a thousand small hopes today. Set them down a while, "
    "like smooth stones on a riverbank. The water keeps going without you. "
    "When you are ready, pick up one stone \u2014 the lightest \u2014 and carry "
    "only that. The rest will still be there. So will you.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
