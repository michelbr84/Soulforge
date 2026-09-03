# Working in this repository

Soulforge is a Claude Code plugin whose only content is the `project-soul` skill.

## Layout

- **`skills/project-soul/` is the canonical source.** Edit here.
- **`.claude/skills/project-soul` is a symlink to it**, so the skill loads while you work
  inside this repo. Never edit through the symlink path and never replace it with a copy —
  two divergent copies of the same skill is the failure this layout exists to prevent.
- `.claude-plugin/` holds the plugin and marketplace manifests that make the repo
  installable by anyone.
- `evals/` is for testing the skill and is not shipped to users.
- `scripts/validate.py` runs the structural checks. Run it before pushing —
  `python3 scripts/validate.py` — and CI runs the same script on every PR.

## Constraints

- `SKILL.md` frontmatter must stay within the six Agent Skills spec fields
  (`name`, `description`, `license`, `allowed-tools`, `compatibility`, `metadata`).
  Any other key makes packaging for claude.ai fail with a hard error.
- Bundled files are referenced as `${CLAUDE_SKILL_DIR}/references/...`. Plain relative
  paths do not resolve when the skill is installed as a plugin.
- Keep `SKILL.md` under 500 lines. Depth belongs in `references/`, loaded on demand.
- Do not add `.claude/` to `.gitignore` — it would silently drop the symlink.
- The canonical `SOUL.md` section list lives in `scripts/validate.py`. Changing the
  document's shape means editing it there, in `SKILL.md`, and in the template —
  the validator fails if those three disagree, which is the point.

## The skill's own rule applies to this repo

This project does not have a `SOUL.md` yet, and one must not be hand-written. If it gets
one, it comes from running the skill and answering the questions honestly — a fabricated
soul document in this repository would break the skill's central rule in the first file
anyone opens.
