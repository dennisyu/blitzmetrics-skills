import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_marketplace import validate


REPOSITORY = Path(__file__).resolve().parents[1]


class MarketplaceValidatorTests(unittest.TestCase):
    def test_current_repository_passes(self):
        self.assertEqual(validate(REPOSITORY), [])

    def test_missing_referenced_skill_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            shutil.rmtree(copied / "skills" / "seo-audit")

            errors = validate(copied)

            self.assertTrue(
                any("./skills/seo-audit" in error for error in errors),
                errors,
            )

    def _strip_rule(self, skill_file: Path, slug: str) -> None:
        text = skill_file.read_text(encoding="utf-8")
        start = f"<!-- shared-rule:{slug}:start -->"
        end = f"<!-- shared-rule:{slug}:end -->"
        before, rest = text.split(start, 1)
        _, after = rest.split(end, 1)
        skill_file.write_text(before.rstrip() + after, encoding="utf-8")

    def test_missing_shared_media_rule_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            self._strip_rule(
                copied / "skills" / "content-agent" / "SKILL.md",
                "silent-media-playback",
            )

            errors = validate(copied)

            self.assertTrue(
                any(
                    "content-agent/SKILL.md has a missing or stale shared rule: "
                    "silent-media-playback" in error
                    for error in errors
                ),
                errors,
            )

    def test_every_standard_is_validated_not_just_the_first(self):
        """The regression this repository already shipped once: the validator
        checked exactly one hardcoded rule, so a second rule could go missing
        from every distributed skill and still pass."""
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            self._strip_rule(
                copied / "skills" / "seo-audit" / "SKILL.md", "no-black-buttons"
            )

            errors = validate(copied)

            self.assertTrue(
                any(
                    "seo-audit/SKILL.md has a missing or stale shared rule: "
                    "no-black-buttons" in error
                    for error in errors
                ),
                errors,
            )

    def test_adapter_version_drift_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            path = copied / ".grok-plugin" / "plugin.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["version"] = "0.0.0"
            path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")

            errors = validate(copied)

            self.assertTrue(any("adapter version drift" in error for error in errors), errors)

    def test_stale_current_skill_count_outside_readme_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            acceptance = copied / "ACCEPTANCE.md"
            acceptance.write_text(
                acceptance.read_text(encoding="utf-8")
                + "\nThe pack contains 999 skills.\n",
                encoding="utf-8",
            )

            errors = validate(copied)

            self.assertTrue(
                any("ACCEPTANCE.md advertises 999 current skills" in error for error in errors),
                errors,
            )

    def test_topical_bundle_description_count_drift_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            path = copied / ".claude-plugin" / "marketplace.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["plugins"][1]["description"] = manifest["plugins"][1][
                "description"
            ].replace("(7 skills)", "(99 skills)")
            path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")

            errors = validate(copied)

            self.assertTrue(
                any(
                    "description advertises 99 skills but lists 7" in error
                    for error in errors
                ),
                errors,
            )

    def test_inventory_bundle_count_drift_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            path = copied / "skills" / "skill-registry" / "references" / "inventory.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "| `authority-and-reputation` | 7 |",
                    "| `authority-and-reputation` | 99 |",
                ),
                encoding="utf-8",
            )

            errors = validate(copied)

            self.assertTrue(
                any(
                    "inventory advertises 99 skills for authority-and-reputation"
                    in error
                    for error in errors
                ),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
