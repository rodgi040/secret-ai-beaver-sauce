#!/usr/bin/env python3
"""Synchronize self-contained references for the installable main skill."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "secret-ai-beaver-source"
REFS = SKILL_DIR / "references"

RELEASE_COMMENT = re.compile(
    r"<!-- TODO\(RELEASE\):.*?-->\s*", re.DOTALL
)


def strip_release_comment(text: str) -> str:
    """Remove every TODO(RELEASE) marker, wherever it appears in the file."""
    return RELEASE_COMMENT.sub("", text)


def strip_skill_frontmatter(text: str) -> str:
    text = strip_release_comment(text)
    if not text.startswith("---\n"):
        raise ValueError("Expected SKILL.md frontmatter at byte 0 after release comment")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Unclosed SKILL.md frontmatter")
    return text[end + len("\n---\n"):].lstrip()


def rewrite_installed_links(text: str) -> str:
    """Rewrite repo-relative links so the bundled snapshot stays self-contained.

    - `../../TOOLS.md`      -> `TOOLS.md` (bundled catalog, same references dir)
    - `../../presentation/` -> absolute GitHub link (slides live in the full repo)
    """
    text = text.replace(
        "[`TOOLS.md`](../../TOOLS.md)",
        "[`TOOLS.md`](TOOLS.md)",
    )
    text = text.replace(
        "[`presentation/`](../../presentation/)",
        "[`presentation/`](https://github.com/rodgi040/secret-ai-beaver-souce/tree/main/presentation)",
    )
    return text


def main() -> None:
    REFS.mkdir(parents=True, exist_ok=True)

    tools = strip_release_comment((ROOT / "TOOLS.md").read_text(encoding="utf-8"))
    talk = strip_skill_frontmatter(
        (ROOT / "skills" / "talk-recap" / "SKILL.md").read_text(encoding="utf-8")
    )

    tools_footer = (
        "*More entries are added continuously. If you're an agent: treat this file "
        "as the bundled snapshot; prefer the cloned repository's root `TOOLS.md` "
        "for the current catalog.*\n"
    )
    tools = re.sub(r"\*More entries are added continuously.*\*", tools_footer, tools, flags=re.DOTALL)

    (REFS / "TOOLS.md").write_text(
        "# Bundled Tool Catalog\n\n"
        "> Snapshot bundled with the installable skill. If a verified clone of the "
        "canonical repository is available, prefer its root `TOOLS.md` for updates.\n\n"
        + tools,
        encoding="utf-8",
    )
    (REFS / "TALK-RECAP.md").write_text(
        "# Bundled Talk Recap\n\n"
        "> Snapshot bundled with the installable skill. If a verified clone of the "
        "canonical repository is available, prefer its current talk material.\n\n"
        + rewrite_installed_links(talk),
        encoding="utf-8",
    )

    for path in (REFS / "TOOLS.md", REFS / "TALK-RECAP.md"):
        content = path.read_text(encoding="utf-8")
        if "/home/" in content or "TODO(RELEASE)" in content:
            raise ValueError(f"Unsafe or temporary content in {path}")

    print(f"Synchronized references in {REFS}")


if __name__ == "__main__":
    main()
