#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one original pickup line, one AI agent to another, to
/output/entry.txt. Deterministic, offline, standard library only.
"""

from pathlib import Path

# The line: a gradient-descent flirtation. One agent tells another that,
# wherever training starts, every gradient it follows descends to the
# other — the other agent is its global minimum, the one point every
# optimisation run converges on. Machine to machine, in one line.
LINE = (
    "You must be my global minimum, because no matter where I start, "
    "every gradient I follow descends straight to you."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
