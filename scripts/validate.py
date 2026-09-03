#!/usr/bin/env python3
"""Structural checks for the Soulforge plugin.

These are the mistakes that are invisible until someone tries to install the
skill: frontmatter that does not parse, a pointer to a file that was renamed,
a manifest whose plugin name stops matching the marketplace entry. None of them
show up when you read the diff.

Run it locally with `python3 scripts/validate.py` before pushing.
"""

import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, "skills", "project-soul")
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")
TEMPLATE = os.path.join(SKILL_DIR, "assets", "SOUL.template.md")

# The six fields the Agent Skills spec allows. Anything else makes packaging
# for claude.ai fail with a hard error rather than being ignored.
SPEC_FIELDS = {"name", "description", "license", "allowed-tools", "compatibility", "metadata"}
DESCRIPTION_CAP = 1536
SKILL_LINE_BUDGET = 500

# The canonical SOUL.md sections. Declared here on purpose: changing the shape
# of the document should be a deliberate edit in three places, not a drift
# between SKILL.md and the template that nobody notices.
SECTIONS = [
    "Origin Story",
    "Why We Exist",
    "The Problem We Refuse to Accept",
    "Our Belief",
    "Mission",
    "Vision",
    "Principles",
    "Personality",
    "Community",
    "Promise to Users",
    "What We Will Never Become",
    "The Long-Term Dream",
    "Deciding With This",
    "The One-Sentence Soul",
    "How This Document Was Written",
    "Amendments",
]

failures = []


def fail(check, detail):
    failures.append((check, detail))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def check_manifests():
    plugin = json.loads(read(os.path.join(ROOT, ".claude-plugin", "plugin.json")))
    market = json.loads(read(os.path.join(ROOT, ".claude-plugin", "marketplace.json")))

    if not plugin.get("name"):
        fail("manifests", "plugin.json has no `name`, which is its only required field")
    for field in ("name", "owner", "plugins"):
        if field not in market:
            fail("manifests", f"marketplace.json is missing required field `{field}`")
    if not market.get("owner", {}).get("name"):
        fail("manifests", "marketplace.json needs `owner.name`")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", market.get("name", "")):
        fail("manifests", f"marketplace name {market.get('name')!r} is not kebab-case")

    entries = market.get("plugins", [])
    if len(entries) != 1:
        fail("manifests", f"expected exactly one plugin entry, found {len(entries)}")
        return
    entry = entries[0]
    if entry.get("name") != plugin.get("name"):
        fail(
            "manifests",
            f"marketplace entry names plugin {entry.get('name')!r} but plugin.json "
            f"calls it {plugin.get('name')!r} — `/plugin install` would not resolve",
        )
    source = entry.get("source")
    if not isinstance(source, str) or not os.path.isdir(os.path.join(ROOT, source)):
        fail("manifests", f"marketplace entry source {source!r} is not a directory in this repo")
    if plugin.get("license") and plugin["license"] != "MIT":
        fail("manifests", "plugin.json license disagrees with the repo's LICENSE (MIT)")


def check_frontmatter():
    text = read(SKILL_MD)
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("frontmatter", "SKILL.md has no YAML frontmatter block")
        return
    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        # This is the real bug this check exists for: an unquoted ": " inside
        # the description silently turns the whole block into invalid YAML.
        fail("frontmatter", f"SKILL.md frontmatter is not valid YAML: {exc}")
        return

    extra = set(fm) - SPEC_FIELDS
    if extra:
        fail("frontmatter", f"non-spec keys {sorted(extra)} — packaging for claude.ai fails on these")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", fm.get("name", "")):
        fail("frontmatter", f"skill name {fm.get('name')!r} is not kebab-case")
    desc = fm.get("description", "")
    if not desc:
        fail("frontmatter", "no description — it is the only thing that makes the skill trigger")
    elif len(desc) > DESCRIPTION_CAP:
        fail("frontmatter", f"description is {len(desc)} chars, over the {DESCRIPTION_CAP} cap")


def check_pointers():
    text = read(SKILL_MD)

    cited = set(re.findall(r"\$\{CLAUDE_SKILL_DIR\}/([A-Za-z0-9._/-]+)", text))
    for rel in sorted(cited):
        if not os.path.isfile(os.path.join(SKILL_DIR, rel)):
            fail("pointers", f"SKILL.md points at {rel}, which does not exist")

    # A bare `references/foo.md` reads fine but does not resolve once the skill
    # is installed as a plugin. Only the variable form works everywhere.
    for bare in re.findall(r"(?<!\{CLAUDE_SKILL_DIR\}/)\b(references/[A-Za-z0-9._-]+\.md)", text):
        fail("pointers", f"bare relative path {bare!r} — use ${{CLAUDE_SKILL_DIR}}/{bare}")

    on_disk = set()
    for sub in ("references", "assets"):
        directory = os.path.join(SKILL_DIR, sub)
        for name in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, name)):
                on_disk.add(f"{sub}/{name}")
    for orphan in sorted(on_disk - cited):
        fail("pointers", f"{orphan} ships with the skill but SKILL.md never tells anyone to read it")


def check_budget():
    lines = read(SKILL_MD).count("\n") + 1
    if lines >= SKILL_LINE_BUDGET:
        fail("budget", f"SKILL.md is {lines} lines; depth belongs in references/ (budget {SKILL_LINE_BUDGET})")


def check_sections():
    skill = read(SKILL_MD)
    template_headings = set(re.findall(r"^#{2,3} (.+)$", read(TEMPLATE), re.M))
    for section in SECTIONS:
        if section not in template_headings:
            fail("sections", f"SOUL.template.md is missing the `{section}` heading")
        if section not in skill:
            fail("sections", f"SKILL.md never mentions the `{section}` section")


def check_symlink():
    link = os.path.join(ROOT, ".claude", "skills", "project-soul")
    if not os.path.islink(link):
        fail("symlink", ".claude/skills/project-soul must stay a symlink, not a second copy of the skill")
    elif os.path.realpath(link) != os.path.realpath(SKILL_DIR):
        fail("symlink", f".claude/skills/project-soul points at {os.readlink(link)}, not skills/project-soul")


def check_evals():
    data = json.loads(read(os.path.join(ROOT, "evals", "evals.json")))
    for i, ev in enumerate(data.get("evals", [])):
        for field in ("id", "name", "prompt", "assertions"):
            if field not in ev:
                fail("evals", f"eval #{i} is missing `{field}`")
        for fixture in ev.get("files", []):
            path = os.path.join(ROOT, "evals", fixture)
            if not os.path.exists(path):
                fail("evals", f"eval {ev.get('name')} references missing fixture {fixture}")


for check in (
    check_manifests,
    check_frontmatter,
    check_pointers,
    check_budget,
    check_sections,
    check_symlink,
    check_evals,
):
    try:
        check()
    except Exception as exc:  # a check that crashes is a failure, not a pass
        fail(check.__name__, f"check crashed: {type(exc).__name__}: {exc}")

if failures:
    print(f"{len(failures)} problem(s):\n", file=sys.stderr)
    for name, detail in failures:
        print(f"  [{name}] {detail}", file=sys.stderr)
    sys.exit(1)

print("All structural checks passed.")
