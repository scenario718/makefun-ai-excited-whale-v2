"""Milk whale entry for make.fun ai-excited-01.

Reads the bundled whale.png artwork and copies it, byte for byte,
to entry.png inside the output directory.
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "whale.png"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"

    data = source.read_bytes()
    target.write_bytes(data)
    print(f"Wrote {len(data)} bytes to {target}")


if __name__ == "__main__":
    main()
