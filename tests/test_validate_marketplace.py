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

    def test_missing_shared_media_rule_fails(self):
        with tempfile.TemporaryDirectory() as temp_name:
            copied = Path(temp_name) / "repository"
            shutil.copytree(REPOSITORY, copied, ignore=shutil.ignore_patterns(".git"))
            skill_file = copied / "skills" / "content-agent" / "SKILL.md"
            text = skill_file.read_text(encoding="utf-8")
            start = "<!-- shared-rule:silent-media-playback:start -->"
            end = "<!-- shared-rule:silent-media-playback:end -->"
            before, rest = text.split(start, 1)
            _, after = rest.split(end, 1)
            skill_file.write_text(before.rstrip() + after, encoding="utf-8")

            errors = validate(copied)

            self.assertTrue(
                any(
                    "content-agent/SKILL.md has a missing or stale shared media rule"
                    in error
                    for error in errors
                ),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
