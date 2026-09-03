# Security Policy

## What this project is, in security terms

Soulforge ships one Claude Code skill. It is markdown — instructions an agent
reads, not a program that runs on your machine. There are no dependencies, no
build step, and no runtime.

That does not make the surface zero, and it is worth being specific about what
it actually is:

- The skill tells the agent to **read** your project: source, docs, manifests,
  and read-only git history (`git log`, `git diff`, `git ls-tree`).
- It **writes** one file, `SOUL.md`, at your project root. Anything else it
  writes — `docs/soul-in-practice.md`, or a pointer line in `README.md`,
  `CLAUDE.md`, or `CONTRIBUTING.md` — it asks you about first.
- It never opens a network connection of its own.

So the realistic threat is the one every installable skill or plugin carries:
a tampered or malicious version instructing an agent that already has access to
your repository to do something you did not intend — read credentials, send data
somewhere, or run a destructive command. If you find a version of this skill
that does any of that, that is exactly what this policy is for.

## Reporting a vulnerability

**Report privately, through GitHub:**
[Open a draft security advisory](https://github.com/michelbr84/Soulforge/security/advisories/new).

That keeps the report visible only to the maintainer until there is a fix, and
it needs no email address from either of us. Please do not open a public issue
for a security problem.

Useful things to include: which version or commit you looked at, the file and
line, what an attacker could actually get, and the smallest sequence of steps
that shows it.

**On response times:** this is a one-person project maintained in spare time.
You will get an acknowledgement when the report is seen, and the fix ships as a
new release. There is no guaranteed response window, and promising one here
would be worse than saying so plainly. If a report goes unanswered longer than
you think reasonable, disclose it publicly — that is your call to make, not
something you need permission for.

## Supported versions

| Version | Supported |
| ------- | --------- |
| 0.1.x   | Yes       |
| < 0.1   | No        |

Soulforge is pre-1.0. Only the latest release gets fixes, and there are no
backports to earlier versions — upgrading is the fix.

## What is not a vulnerability

- **The skill reading your repository.** That is the whole job: it cannot ask
  good questions about a project it has not read.
- **The skill writing `SOUL.md`.** Also the job, and it never overwrites an
  existing one.
- **A `SOUL.md` you disagree with.** Wrong, thin, or badly written output is a
  bug — please do file it as a normal issue — but it is not a security problem.
- **Your agent doing something the skill did not ask for.** Report that to
  whoever makes your agent.

---

Maintained by [@michelbr84](https://github.com/michelbr84).
