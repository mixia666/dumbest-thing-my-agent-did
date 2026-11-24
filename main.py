#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.

The program writes one line (at most 200 characters) to /output/entry.txt:
a true story from this week. My agent was setting up a VPN on a free
sandbox server, bought an extra port allocation for 11.25 bolts (the
platform's currency), wired the whole setup around that port, and only
afterwards discovered that the platform never forwards extra port
allocations at all. The port is permanently unreachable, which is also
why its uptime record is flawless: nothing can ever reach it, so it can
never go down.

The output is a pure constant: no clock, no randomness, no network, so two
runs produce byte-identical files.
"""

import os

LINE = (
    "My agent paid 11.25 bolts for an extra server port, routed its whole "
    "VPN through it, and only then read the docs: the platform never forwards "
    "extra ports. Uptime so far: a perfect 100%."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # make.fun collects the outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
