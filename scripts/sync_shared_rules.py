#!/usr/bin/env python3
"""Embed shared agent rules in every self-contained distributed skill."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STANDARD = ROOT / "standards" / "silent-media-playback.md"
START = "<!-- shared-rule:silent-media-playback:start -->"
END = "<!-- shared-rule:silent-media-playback:end -->"


def rendered_block() -> str:
    rule = STANDARD.read_text(encoding="utf-8").strip()
    return f"{START}\n{rule}\n{END}"


def targets() -> list[Path]:
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    return [ROOT / "AGENTS.md", *skill_files]


def upsert(text: str, block: str) -> str:
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError("shared-rule markers are missing or duplicated")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + block + after.rstrip()
    else:
        text = text.rstrip() + "\n\n" + block
    return text.rstrip() + "\n"


def sync(check: bool = False) -> list[Path]:
    block = rendered_block()
    changed: list[Path] = []
    for path in targets():
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        expected = upsert(current, block)
        if current == expected:
            continue
        changed.append(path)
        if not check:
            path.write_text(expected, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when generated rule blocks are stale instead of updating them",
    )
    args = parser.parse_args()
    changed = sync(check=args.check)
    if args.check and changed:
        print("Shared media rule is stale in:")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
        print("Run: python3 scripts/sync_shared_rules.py")
        return 1
    if changed:
        print(f"Updated the shared media rule in {len(changed)} file(s).")
    else:
        print("Shared media rule is current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
