#!/usr/bin/env python3
"""Copy entry.png to the requested output path.

This is the entrypoint for the news-image-20261118 submission: one
picture summing up Wednesday 18 November 2026 (36 stories). It uses
only the Python standard library. Run it as:

    python3 main.py [output-path]

With no argument it writes ./entry.png. The copy is byte-for-byte
identical to the bundled entry.png.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("entry.png not found next to main.py\n")
        sys.exit(1)
    dest = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    shutil.copyfile(src, dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
