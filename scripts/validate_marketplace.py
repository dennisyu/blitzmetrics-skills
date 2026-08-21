#!/usr/bin/env python3
"""Validate the local Local Service Spotlight Claude marketplace without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from standards_lib import (  # noqa: E402
    StandardError,
    load_standards,
    skill_scopes,
    standards_for,
)


EVERYTHING_PLUGIN = "lss-everything"
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_REFERENCE = re.compile(
    r"(?<![\w/])((?:references|scripts|assets)/[A-Za-z0-9_.\-/]+)"
)
CURRENT_SKILL_COUNT = (
    re.compile(
        r"\ball\s+(\d+)\s+(?:(?:expected|available|distributed)\s+)?"
        r"skill(?:s|\s+files)\b",
        re.IGNORECASE,
    ),
    re.compile(r"\bpack\s+contains\s+(\d+)\s+skills\b", re.IGNORECASE),
    re.compile(r"\bsame\s+(\d+)\s+directories\b", re.IGNORECASE),
    re.compile(
        rf"Skills in `{EVERYTHING_PLUGIN}`\s*\|\s*(\d+)\b",
        re.IGNORECASE,
    ),
)


def expected_blocks(root: Path) -> tuple[list[tuple[str, str]], list[str]]:
    """Return ([(slug, block)], errors) for every rule in standards/.

    Every rule is checked in every distributed skill, not one chosen rule.
    Hardcoding a single slug here was the second place propagation silently
    narrowed to a single file.
    """
    try:
        standards = load_standards(root / "standards")
    except StandardError as exc:
        return [], [f"standards/ is malformed: {exc}"]
    if not standards:
        return [], ["standards/ contains no rules"]
    return [(s.slug, s.block()) for s in standards], []


def blocks_for_skill(root: Path, skill_file: Path) -> list[tuple[str, str]]:
    standards = load_standards(root / "standards")
    keep = standards_for(standards, skill_scopes(skill_file))
    return [(s.slug, s.block()) for s in keep]


def _frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        value = match.group(2).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[match.group(1)] = value
    return values


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = root / ".claude-plugin" / "marketplace.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read {manifest_path.relative_to(root)}: {exc}"]

    plugins = manifest.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        return ["marketplace.json must contain a non-empty plugins array"]

    plugin_names: set[str] = set()
    bundle_counts: dict[str, int] = {}
    everything: list[str] | None = None
    everything_description = ""
    for index, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            errors.append(f"plugins[{index}] must be an object")
            continue
        name = plugin.get("name")
        if not isinstance(name, str) or not KEBAB.fullmatch(name):
            errors.append(f"plugins[{index}].name must be stable kebab-case")
        elif name in plugin_names:
            errors.append(f"duplicate plugin name: {name}")
        else:
            plugin_names.add(name)
        if plugin.get("source") != "./":
            errors.append(f"plugin {name!r} must use the local source './'")
        skills = plugin.get("skills")
        if not isinstance(skills, list) or not skills:
            errors.append(f"plugin {name!r} must have a non-empty skills array")
            continue
        if len(skills) != len(set(skills)):
            errors.append(f"plugin {name!r} lists a skill more than once")
        if isinstance(name, str):
            bundle_counts[name] = len(skills)
        description = plugin.get("description")
        if not isinstance(description, str) or not description:
            errors.append(f"plugin {name!r} must have a description")
        elif name != EVERYTHING_PLUGIN:
            described_count = re.search(r"\((\d+)\s+skills\)\s*$", description)
            if not described_count:
                errors.append(
                    f"plugin {name!r} description must end with its derived skill count"
                )
            elif int(described_count.group(1)) != len(skills):
                errors.append(
                    f"plugin {name!r} description advertises "
                    f"{described_count.group(1)} skills but lists {len(skills)}"
                )
        for skill_ref in skills:
            if not isinstance(skill_ref, str) or not skill_ref.startswith("./skills/"):
                errors.append(f"plugin {name!r} has invalid skill path: {skill_ref!r}")
                continue
            skill_path = root / skill_ref.removeprefix("./")
            if not (skill_path / "SKILL.md").is_file():
                errors.append(f"plugin {name!r} references missing {skill_ref}/SKILL.md")
        if name == EVERYTHING_PLUGIN:
            if everything is not None:
                errors.append(f"{EVERYTHING_PLUGIN} must appear exactly once")
            everything = skills
            everything_description = str(plugin.get("description", ""))

    if everything is None:
        errors.append(f"missing required {EVERYTHING_PLUGIN} plugin")
        everything_set: set[str] = set()
    else:
        everything_set = set(everything)

    skill_dirs = sorted(
        path for path in (root / "skills").iterdir() if path.is_dir()
    ) if (root / "skills").is_dir() else []
    actual_refs = {f"./skills/{path.name}" for path in skill_dirs}
    for missing in sorted(actual_refs - everything_set):
        errors.append(f"skill is not in {EVERYTHING_PLUGIN}: {missing}")
    for stale in sorted(everything_set - actual_refs):
        errors.append(f"{EVERYTHING_PLUGIN} has a stale skill path: {stale}")

    count_in_description = re.search(
        r"\ball\s+(\d+)\b[^.]*\bskills\b",
        everything_description,
        flags=re.IGNORECASE,
    )
    if count_in_description and int(count_in_description.group(1)) != len(skill_dirs):
        errors.append(
            f"{EVERYTHING_PLUGIN} description advertises "
            f"{count_in_description.group(1)} skills but found {len(skill_dirs)}"
        )

    metadata = manifest.get("metadata")
    source_version = metadata.get("version") if isinstance(metadata, dict) else None
    if not isinstance(source_version, str) or not source_version:
        errors.append("marketplace metadata.version is required")
    grok_path = root / ".grok-plugin" / "plugin.json"
    try:
        grok = json.loads(grok_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read .grok-plugin/plugin.json: {exc}")
        grok = {}
    if grok.get("name") != EVERYTHING_PLUGIN:
        errors.append(f"Grok adapter name must be {EVERYTHING_PLUGIN}")
    if grok.get("skills") != "./skills/":
        errors.append("Grok adapter must read the canonical ./skills/ directory")
    if source_version and grok.get("version") != source_version:
        errors.append(
            "adapter version drift: Claude marketplace is "
            f"{source_version!r}, Grok adapter is {grok.get('version')!r}"
        )

    blocks, block_errors = expected_blocks(root)
    errors.extend(block_errors)

    agents_file = root / "AGENTS.md"
    if not agents_file.is_file():
        errors.append("missing AGENTS.md with the shared house rules")
    else:
        agents_text = agents_file.read_text(encoding="utf-8")
        for slug, block in blocks:
            if block not in agents_text:
                errors.append(f"AGENTS.md has a missing or stale shared rule: {slug}")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing skills/{skill_dir.name}/SKILL.md")
            continue
        metadata = _frontmatter(skill_file)
        if metadata.get("name") != skill_dir.name:
            errors.append(
                f"{skill_file.relative_to(root)} name must be {skill_dir.name!r}, "
                f"found {metadata.get('name')!r}"
            )
        if not metadata.get("description"):
            errors.append(f"{skill_file.relative_to(root)} needs a description")
        skill_text = skill_file.read_text(encoding="utf-8")
        try:
            expected_here = blocks_for_skill(root, skill_file)
        except StandardError as exc:
            errors.append(str(exc))
            expected_here = []
        for slug, block in expected_here:
            if block not in skill_text:
                errors.append(
                    f"{skill_file.relative_to(root)} has a missing or stale "
                    f"shared rule: {slug}"
                )

        for markdown in skill_dir.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for relative in LOCAL_REFERENCE.findall(text):
                relative = relative.rstrip(".,:;!?)]}")
                candidates = (skill_dir / relative, root / relative)
                if not any(candidate.exists() for candidate in candidates):
                    errors.append(
                        f"{markdown.relative_to(root)} references missing {relative}"
                    )

    readme = (root / "README.md").read_text(encoding="utf-8")
    advertised = re.search(r"all (\d+) skills", readme, flags=re.IGNORECASE)
    if advertised and int(advertised.group(1)) != len(skill_dirs):
        errors.append(
            f"README advertises {advertised.group(1)} skills but found {len(skill_dirs)}"
        )
    current_fact_files = (
        root / "README.md",
        root / "CONTRIBUTING.md",
        root / "ACCEPTANCE.md",
        root / "HOW-KNOWLEDGE-PROPAGATES.md",
        root / "skills" / "skill-registry" / "SKILL.md",
        root / "skills" / "skill-registry" / "references" / "inventory.md",
    )
    for path in current_fact_files:
        if not path.is_file():
            errors.append(f"missing current-fact document: {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in CURRENT_SKILL_COUNT:
            for match in pattern.finditer(text):
                if int(match.group(1)) != len(skill_dirs):
                    errors.append(
                        f"{path.relative_to(root)} advertises {match.group(1)} current "
                        f"skills but found {len(skill_dirs)}"
                    )

    inventory_path = root / "skills" / "skill-registry" / "references" / "inventory.md"
    if inventory_path.is_file():
        inventory_text = inventory_path.read_text(encoding="utf-8")
        for bundle_name, expected_count in bundle_counts.items():
            row = re.search(
                rf"^\|\s*`{re.escape(bundle_name)}`\s*\|\s*(\d+)\s*\|\s*$",
                inventory_text,
                flags=re.MULTILINE,
            )
            if not row:
                errors.append(f"inventory is missing a count row for {bundle_name}")
            elif int(row.group(1)) != expected_count:
                errors.append(
                    f"inventory advertises {row.group(1)} skills for {bundle_name} "
                    f"but manifest lists {expected_count}"
                )
    return sorted(set(errors))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print(f"Marketplace validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    skill_count = sum(1 for path in (root / "skills").iterdir() if path.is_dir())
    print(f"Marketplace validation passed: {skill_count} skills, all references present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
