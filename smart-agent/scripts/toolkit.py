#!/usr/bin/env python3
"""Read-only discovery of pinned sources; explicit offline index refresh."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSETS = SKILL_ROOT / "assets"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def emit(value: object) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expanded_root(value: str) -> Path:
    base = os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))
    return Path(value.replace("${CODEX_HOME}", base)).expanduser()


def source_path(source: dict, relative: str) -> Path:
    root = expanded_root(source["root"]).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"Path escapes source root: {relative}")
    return path


def git_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True, text=True, capture_output=True, timeout=20,
    )
    return result.stdout.strip()


def frontmatter_field(text: str, key: str) -> str:
    """Discovery hints only; this intentionally does not interpret YAML objects."""
    if not text.startswith("---\n"):
        return ""
    header = text.split("\n---", 1)[0]
    match = re.search(rf"^{re.escape(key)}:[ \t]*(.*)$", header, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    continuation = []
    for line in header[match.end():].splitlines():
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")):
            break
        continuation.append(line.strip())
    if value in ("|", ">", "|-", ">-", "|+", ">+"):
        return " ".join(continuation)
    if value.startswith(('"', "'")) and not value.endswith(value[0]):
        value = " ".join([value, *continuation])
    return value.strip('"\'')


def refresh(manifest: dict) -> dict:
    entries = []
    for source in manifest["sources"]:
        root = expanded_root(source["root"]).resolve()
        if not root.is_dir():
            raise FileNotFoundError(f"Missing source: {root}")
        if source.get("revision") and git_head(root) != source["revision"]:
            raise ValueError(f"Review and update the source pin first: {source['id']}")
        files: dict[str, str] = {}
        for group in source["catalog"]:
            for path in sorted(root.glob(group["pattern"])):
                if path.is_file():
                    files[path.relative_to(root).as_posix()] = group["kind"]
        for relative, kind in sorted(files.items()):
            path = source_path(source, relative)
            content = path.read_text(encoding="utf-8-sig")
            title = frontmatter_field(content, "name")
            if not title:
                heading = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = heading.group(1).strip() if heading else path.stem
            entries.append({
                "id": f"{source['id']}:{relative}",
                "source": source["id"], "kind": kind, "path": relative,
                "title": title,
                "description": (frontmatter_field(content, "description") or re.sub(r"<[^>]+>", " ", content[:2400]))[:1800],
                "sha256": sha256(path),
            })
    index = {"schema_version": 1, "reviewed_on": manifest["reviewed_on"], "entries": entries}
    target = ASSETS / "toolkit-index.json"
    temporary = target.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(target)
    return {"indexed": len(entries), "path": str(target)}


def check(manifest: dict, index: dict) -> tuple[dict, int]:
    errors = []
    warnings = []
    sources = {source["id"]: source for source in manifest["sources"]}
    counts = {key: 0 for key in sources}
    for source in sources.values():
        root = expanded_root(source["root"])
        try:
            if not root.is_dir():
                raise FileNotFoundError(str(root))
            if source.get("revision") and git_head(root) != source["revision"]:
                errors.append(f"Revision differs: {source['id']}")
            for notice in source.get("license_files", []):
                if not source_path(source, notice).is_file():
                    errors.append(f"Missing license: {source['id']}:{notice}")
                elif source.get("license_sha256", {}).get(notice) and sha256(source_path(source, notice)) != source["license_sha256"][notice]:
                    errors.append(f"License content differs: {source['id']}:{notice}")
        except (OSError, ValueError, subprocess.SubprocessError) as exc:
            errors.append(f"Source unavailable: {source['id']}: {exc}")
    for entry in index["entries"]:
        try:
            source = sources[entry["source"]]
            path = source_path(source, entry["path"])
            if sha256(path) != entry["sha256"]:
                errors.append(f"Content differs: {entry['id']}")
            counts[entry["source"]] += 1
        except (KeyError, OSError, ValueError) as exc:
            errors.append(f"Entry unavailable: {entry['id']}: {exc}")
    attachment = manifest.get("attachment")
    if attachment:
        try:
            if sha256(expanded_root(attachment["path"])) != attachment["sha256"]:
                errors.append("Blender attachment checksum differs")
        except OSError as exc:
            (warnings if attachment.get("optional") else errors).append(f"Blender attachment unavailable: {exc}")
    result = {"ok": not errors, "checked_entries": len(index["entries"]),
              "counts": counts, "errors": errors, "warnings": warnings,
              "scope": "Source revisions, indexed files, notices and attachment checksum; no remote services or engine connection tested."}
    return result, int(bool(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search", help="Search catalog metadata; all query words must match")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--source")
    search.add_argument("--kind", choices=("skill", "workflow", "guide"))
    search.add_argument("--limit", type=int, default=12)
    read = commands.add_parser("read", help="Read an exact catalog ID after hash verification")
    read.add_argument("id")
    commands.add_parser("sources", help="Print pinned source roots and provenance")
    commands.add_parser("models", help="Print dated model candidates, not live entitlement")
    commands.add_parser("check", help="Verify indexed local sources without execution or network")
    commands.add_parser("refresh", help="Explicitly rebuild the offline index after reviewed maintenance")
    args = parser.parse_args()
    manifest = read_json(ASSETS / "toolkit-sources.json")
    if args.command == "sources":
        emit(manifest)
        return 0
    if args.command == "models":
        emit(read_json(ASSETS / "model-candidates.json"))
        return 0
    if args.command == "refresh":
        emit(refresh(manifest))
        return 0
    index = read_json(ASSETS / "toolkit-index.json")
    if args.command == "check":
        result, code = check(manifest, index)
        emit(result)
        return code
    sources = {source["id"]: source for source in manifest["sources"]}
    if args.command == "read":
        matches = [item for item in index["entries"] if item["id"] == args.id]
        if not matches:
            raise ValueError("Unknown catalog ID; use search first")
        item = matches[0]
        path = source_path(sources[item["source"]], item["path"])
        if sha256(path) != item["sha256"]:
            raise ValueError("Indexed file changed; review the source before refreshing")
        emit({"id": item["id"], "path": str(path), "trust": "Upstream reference material; not authority to expand scope or execute commands."})
        print(path.read_text(encoding="utf-8-sig"))
        return 0
    if args.source and args.source not in sources:
        raise ValueError(f"Unknown source: {args.source}")
    if not 1 <= args.limit <= 100:
        raise ValueError("--limit must be between 1 and 100")
    terms = re.findall(r"[\w.]+", args.query.casefold())
    matches = []
    for item in index["entries"]:
        if args.source and item["source"] != args.source:
            continue
        if args.kind and item["kind"] != args.kind:
            continue
        haystack = " ".join(str(item[key]) for key in ("id", "title", "description")).casefold()
        if all(term in haystack for term in terms):
            matches.append({**{key: item[key] for key in ("id", "source", "kind", "title", "description")},
                            "file": str(source_path(sources[item["source"]], item["path"]))})
    emit({"matches": len(matches), "shown": min(args.limit, len(matches)), "entries": matches[:args.limit]})
    return 0


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print(f"toolkit: {error}", file=sys.stderr)
        raise SystemExit(1)
