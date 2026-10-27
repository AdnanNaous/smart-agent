from pathlib import Path
import tempfile
import unittest

from tools.validate_skill import check_links, load_frontmatter, validate


class ValidationTests(unittest.TestCase):
    def test_missing_and_external_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "reference.md"
            doc.write_text("[source](https://example.com/x)\n[missing](gone.md)\n")
            findings = check_links(doc, root)
            self.assertEqual(len(findings), 1)
            self.assertIn("missing link target", findings[0])

    def test_relative_link_and_fenced_example(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "assets").mkdir()
            (root / "assets/state.md").write_text("state")
            (root / "references").mkdir()
            doc = root / "references/work.md"
            doc.write_text("[state](../assets/state.md)\n```text\n[example](absent.md)\n```\n")
            self.assertEqual(check_links(doc, root), [])

    def test_repository_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "reference.md"
            doc.write_text("[outside](../outside.md)\n")
            self.assertIn("escapes repository", check_links(doc, root)[0])

    def test_invalid_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            doc = Path(directory) / "metadata.md"
            for content in ("no frontmatter", "---\n- unexpected-list\n---\nbody"):
                doc.write_text(content)
                with self.assertRaises(ValueError):
                    load_frontmatter(doc)

    def test_maintenance_and_evaluation_links_are_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "smart-agent"
            (bundle / "agents").mkdir(parents=True)
            (bundle / "SKILL.md").write_text(
                '---\nname: smart-agent\ndescription: "Verified work"\n---\n'
            )
            (bundle / "agents/openai.yaml").write_text(
                'interface:\n  display_name: SMART AGENT\n'
                '  short_description: Capability-first verified engineering\n'
                '  default_prompt: Use $smart-agent\n'
            )
            (root / "README.md").write_text("Project\n")
            self.assertEqual(validate(root), [])
            for relative in ("AGENTS.md", "docs/nested/maintenance.md", "tests/evaluation.md"):
                with self.subTest(relative=relative):
                    doc = root / relative
                    doc.parent.mkdir(parents=True, exist_ok=True)
                    doc.write_text("[missing](absent.md)\n")
                    findings = validate(root)
                    self.assertTrue(any(relative in item and "missing link" in item for item in findings))
                    doc.unlink()


if __name__ == "__main__":
    unittest.main()
