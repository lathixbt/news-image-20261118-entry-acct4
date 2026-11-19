#!/usr/bin/env python3
"""Copy the bundled entry.png to the grader's output directory.

The entry image lives next to this script in the repo. The grader runs
this program in a sandbox where the repo is read-only, so the copy must
go to the output directory named by the MAKEFUN_OUTPUT_DIR environment
variable (defaulting to /output), never to the current working directory.
The copy is byte-for-byte, and it is verified twice: its size is checked
against the source, and the first eight bytes must be the PNG signature.
"""

import os
import shutil
import sys


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        print("error: size mismatch after copy: %d != %d" % (dst_size, src_size), file=sys.stderr)
        return 1
    with open(dst, "rb") as f:
        header = f.read(8)
    if header != b"\x89PNG\r\n\x1a\n":
        print("error: copied file is not a PNG (bad signature)", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, dst_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
