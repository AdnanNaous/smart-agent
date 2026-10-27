"""Check the repository bundle without executing code from the skill."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


SLUG = "smart-agent"
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")


def load_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
    if not match:
        raise ValueError(f"{path.name}: missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path.name}: frontmatter must be a mapping")
    return data, text[match.end():]


def check_links(path, root):
    errors = []
    text = path.read_text(encoding="utf-8")
    # Examples in fenced code are not documentation links.
    text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.M | re.S)
    for target in LINK.findall(text):
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        resolved = (path.parent / unquote(parsed.path)).resolve()
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f"{path.relative_to(root).as_posix()}: link escapes repository: {target}")
        elif not resolved.exists():
            errors.append(f"{path.relative_to(root).as_posix()}: missing link target: {target}")
    return errors


def validate(root):
    errors = []
    bundle = root / SLUG
    required = [bundle / "SKILL.md", bundle / "agents/openai.yaml", root / "README.md"]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(root)}")
    if errors:
        return errors
    try:
        metadata, body = load_frontmatter(bundle / "SKILL.md")
        if set(metadata) != {"name", "description"}:
            errors.append("SKILL.md: expected only name and description metadata")
        if metadata.get("name") != SLUG:
            errors.append("SKILL.md: name differs from bundle slug")
        if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
            errors.append("SKILL.md: description must be nonempty text")
        if len(body.splitlines()) >= 500:
            errors.append("SKILL.md: move specialized detail into references")
        agent = yaml.safe_load((bundle / "agents/openai.yaml").read_text())
        if not isinstance(agent, dict) or not isinstance(agent.get("interface"), dict):
            raise ValueError("openai.yaml: interface must be a mapping")
        interface = agent["interface"]
        if interface.get("display_name") != "SMART AGENT":
            errors.append("openai.yaml: stale display name")
        short = interface.get("short_description", "")
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            errors.append("openai.yaml: short_description must be 25â€“64 characters")
        prompt = interface.get("default_prompt", "")
        if not isinstance(prompt, str) or f"${SLUG}" not in prompt:
            errors.append("openai.yaml: default_prompt must invoke the current skill")
        for reference in (bundle / "references").glob("*.md"):
            if f"references/{reference.name}" not in body:
                errors.append(f"SKILL.md: reference is not discoverable: {reference.name}")
    except (ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        errors.append(f"Invalid metadata: {exc}")
    if (root / "smart-model-router").exists() or (root / "agent-engineering-os").exists():
        errors.append("Old skill folder remains alongside migrated bundle")
    documentation = [
        *root.glob("*.md"),
        *bundle.rglob("*.md"),
        *(root / "docs").rglob("*.md"),
        *(root / "tests").glob("*.md"),
    ]
    for path in documentation:
        errors.extend(check_links(path, root))
    return errors


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    findings = validate(repo)
    if findings:
        print("\n".join(findings), file=sys.stderr)
        sys.exit(1)
    print("Bundle metadata, reference discovery, invocation, and local links passed.")
