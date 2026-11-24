#!/usr/bin/env python3
"""Write the scariest horror story you can in exactly two sentences, at most 400 characters, to /output/entry.txt.

The story is written exactly as given: 155 Unicode code points,
inside the competition gate of 1-400. Python 3, standard library
only, no network.
"""

import os

TEXT = "The baby monitor has played my daughter's lullaby every night since she was born. She turned eighteen last week, and the singing only started last Tuesday."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
