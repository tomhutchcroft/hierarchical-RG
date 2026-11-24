#!/usr/bin/env python3
"""Reserve assertion tags in wiki/tags.json and print them.

Usage: python3 tools/new_tag.py [count]

Reservations are permanent: a tag is never removed or reused, and an unused
reservation is harmless. Reserve before inserting an anchor; the checker fails on
an anchor whose tag is not reserved.
"""
from __future__ import annotations

import json
import secrets
import sys
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "wiki" / "tags.json"
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> int:
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    ledger = json.loads(LEDGER.read_text())
    reserved = {e["tag"] for e in ledger["tags"]}
    fresh = []
    while len(fresh) < count:
        tag = "".join(secrets.choice(ALPHABET) for _ in range(4))
        if tag not in reserved and tag not in fresh:
            fresh.append(tag)
    for tag in fresh:
        ledger["tags"].append({"tag": tag, "state": "allocated"})
    LEDGER.write_text(json.dumps(ledger, indent=2) + "\n")
    print("\n".join(fresh))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
