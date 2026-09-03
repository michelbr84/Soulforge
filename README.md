# Soulforge

Code explains how a project works. Documentation explains how to use it. Nothing in a
repository explains **why someone decided it should exist**.

That part lives in one person's head. It leaves when they leave, and it is the first thing
lost when a project grows, takes money, or changes hands. New contributors then spend years
guessing at intentions nobody wrote down.

Soulforge is a Claude Code skill that writes it down. It reads your project, interviews you
about the parts no repository can reveal, and produces a `SOUL.md` at your project root:
where this came from, what it believes, who it is for, what it promises, and what it must
never become.

It works on any kind of project — open source, an app, a library, a game, a developer tool,
a startup, or something you built for yourself on a weekend.

## Install

```
/plugin marketplace add michelbr84/Soulforge
/plugin install soulforge@soulforge
```

Then run `/soulforge:project-soul` inside any project, or just ask — "why does this project
exist?", "give this project a soul", "write our manifesto" — and Claude will reach for it.

Two other ways, if you'd rather not use plugins:

- **Copy it in.** Drop `skills/project-soul/` into `~/.claude/skills/` (for yourself) or
  into a project's `.claude/skills/` (for everyone who clones it). It becomes
  `/project-soul`.
- **Upload it to claude.ai.** The skill stays within the Agent Skills spec, so the folder
  zips and uploads unchanged.

## The three modes

The skill looks for an existing `SOUL.md` and picks a mode from what it finds.

**Forge** — no soul document yet. It reads the project first so it never asks you something
your README already answers, then asks between five and ten questions that it can't answer
on its own, then writes the document.

**Evolve** — a soul document exists and the project has moved. It compares the two, tells
you honestly when nothing meaningful has changed, and when something has, proposes specific
amendments. Superseded text is never deleted; it is preserved verbatim with the date and
the reason. The origin story is append-only.

**Check** — you have a decision in hand and want to know if it fits. A feature, a
dependency, a price change, a piece of copy. It answers *aligned*, *tension*, or *conflict*,
quoting the line that decides it — and it will tell you when the soul simply doesn't speak
to the question, rather than manufacturing a verdict.

## What comes out

A `SOUL.md` with an origin story, why the project exists, the problem it refuses to accept,
its belief, mission, vision, three to seven principles, its personality, its community, its
promises, what it will never become, the long-term dream, a short section on deciding with
all of it, and one sentence that holds the whole thing.

Two rules keep that from turning into a poster. **Every principle has to name what it costs**
— it must finish "so when forced to choose between A and B, we choose A" with a real A and B
from your project, because a principle nobody would argue with never settles an argument.
And **"what we will never become" has to name plausible temptations** — at least one item
should cost a real revenue path or a popular feature. "We'll never be evil" protects nothing.

## What it will not do

**It will not invent your story.** The skill can read what your project does; it cannot read
why you cared. So motives, beliefs, the moment you started, and the lines you won't cross
come from you or they don't get written at all. Before writing the file it traces every
sentence written in your project's voice back to something you said or something in the
repository. Anything it can't trace is cut, or left as a visible gap for you to fill later.

That means a thin interview produces a short document with holes in it. That is the intended
outcome. A beautiful invented sentence is the worst thing this skill could produce, because
it would be believed, quoted, and defended by people who weren't there.

It also won't write corporate filler. Phrases that fit every project — *revolutionize*,
*cutting-edge*, *empowering users*, *seamless* — describe none, and the draft is scanned for
them before it is written. The sharper test it runs on itself: swap your project's name for a
competitor's, and any sentence still true was saying nothing.

## Contributing

The skill lives in `skills/project-soul/`. `.claude/skills/project-soul` is a symlink to it,
so the skill is live while you work in this repo — edit the canonical path, never the
symlink. See `CLAUDE.md` for the rest.

## License

MIT.
