# Reading a project before you ask about it

Read this before Stage 1. The goal is not an inventory of files. It is to arrive at the
interview already knowing what the project does, and — more importantly — carrying two
or three decisions that reveal what its author believes. Naming those back to someone is
what convinces them you actually read their work, and it is what makes them answer the
hard questions honestly instead of politely.

Come out of this stage with two artifacts:

1. **The already-answered list.** Everything the project states plainly. You will not ask
   about any of it. Asking someone what their project does, when the README says so in
   the first line, tells them you didn't look.
2. **Two or three observed positions**, phrased as hypotheses to be corrected.

## Reading order

Stop when you have enough; a small project does not need all of this.

1. `README` — what it claims to be, who it addresses, and its tone.
2. The manifest — `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Gemfile`,
   `*.csproj`, `composer.json`. Name, description, dependency count, scripts, version.
3. `LICENSE` — see below; this one carries more than people expect.
4. `CONTRIBUTING`, `CODE_OF_CONDUCT`, `GOVERNANCE` — who the project thinks it is for.
5. `CHANGELOG`, `ROADMAP`, release tags — what it has been trying to become.
6. `docs/`, ADRs, RFCs, design notes — where reasoning is written down, if anywhere.
7. `CLAUDE.md`, `.cursorrules`, editor configs — instructions the author gives to tools
   often say plainly what they care about.
8. Directory structure, then the entry point and one or two core modules.
9. `git log --oneline | head -40`, `git log --reverse | head -20`, `git shortlog -sn`.

## Signals that carry philosophy

Facts tell you what a project is. These tell you what it believes. Two or three of them,
named specifically, are worth more than a full inventory.

**The license.** It says what the author is afraid of. AGPL guards against someone
running a closed service on their work. MIT says adoption matters more than control.
No license at all usually means it hasn't occurred to them that anyone else would use it —
which is itself a fact about the project's stage.

**Dependency count.** Zero dependencies is a position, and a costly one. Two hundred is
also a position. Which way it leans predicts a dozen future arguments.

**Where the data lives.** Local-first, self-hosted, or someone else's server is the most
political decision in software. It usually maps directly onto a belief about who should
be in control.

**Telemetry, mandatory accounts, paywalls.** Present or conspicuously absent. An analytics
package that someone deliberately did not add is a strong signal, and you can often find
the issue where they said no.

**Error messages.** Errors are the part of a codebase nobody is forced to make good. When
they are careful, specific, and tell the user what to do next, someone decided the person
on the other end deserved that. When they are stack traces, that decision was made too.

**Where unpaid effort went.** Tests, types, accessibility, docs, CI, performance work,
onboarding scripts. Nobody is required to do these. Whichever one is disproportionately
good is where the author's taste lives.

**What is deliberately missing.** A closed issue that says "not doing this, here's why"
is the single richest artifact in a repository. Search closed issues and PRs for refusals.

**Commit history.** One person or many. Bursts or steady. Messages that explain reasoning
or messages that say "fix". The first twenty commits often show what the project was
before it knew what it was.

**Naming.** What things are called — modules, flags, error types — shows who the author
imagined reading them.

## The same evidence means different things

| Project type | What to look for | What it usually means |
|---|---|---|
| **Library / SDK** | API surface size, breaking-change history, deprecation policy | A small surface guarded over years is a promise to users; frequent breakage means velocity was chosen over stability |
| **CLI / dev tool** | Flags, defaults, `--help` copy, error text, install path | Defaults reveal who the author pictured typing this at 2am |
| **Application / SaaS** | Auth, billing, data ownership, export paths, offline behavior | Whether the user or the vendor holds the leverage |
| **Game** | Monetization hooks, mod support, save-file format, engine choice | Mod support and open save formats say the player is trusted |
| **Community / OSS project** | Governance, contributor ladder, review tone in PRs, issue templates | How power is shared, and whether newcomers are a cost or the point |
| **Personal project** | Commit rhythm, unfinished branches, README voice | Often built to solve one person's real problem; the soul is usually sharper, not vaguer |
| **Startup / commercial** | Pricing page, free tier boundaries, enterprise features | Where the line between generosity and revenue was drawn |

Read the type off the evidence, not off a label. A "personal project" with a pricing page
is a startup that hasn't admitted it yet, and that tension is worth asking about.

## What you may and may not conclude

You may state, as observation: what it does, its stack, its apparent audience, its stage,
the decisions above and the trade-offs they imply, timeline facts from git, and values
already written in the README or CONTRIBUTING — quoted and credited, never paraphrased
into a belief the author didn't state.

You may not conclude motive. A project with no telemetry might be privacy-minded, or the
author might simply not have gotten to it. That difference is the entire interview.

## Stage

Name it, because it changes which questions are worth asking.

- **Idea** — little or no code. The soul precedes the work; run a more open interview.
- **Prototype** — it runs for the author. Ask what they are trying to prove.
- **Used by others** — issues from strangers, releases. Ask what surprised them about
  how people actually use it.
- **Mature** — stable API, many contributors, a deprecation policy. Ask what they have
  already refused.
- **Maintenance** — commits are fixes and dependency bumps. Ask what would make them
  care about it again, and what they want preserved if they hand it over.

## Closing the stage

Give the user five to eight lines: what it is, who it seems to be for, what stage it is
at, and the two or three decisions that look like a philosophy rather than an accident.
Ask them to correct it.

**This summary is not a turn of its own.** It opens the Round 1 message and is followed
immediately by the questions, in the same message. Sending it alone and waiting spends a
round trip on something the user cannot act on.

Frame it as a hypothesis, always. Being told "no, that's not why I did that" is a good
outcome — the correction is usually the most revealing thing they say all session.

State what you could not read, too — a file imported but missing, a directory you skipped.
It costs one line, and it stops you from quietly building a conclusion on a gap.

## When there is almost nothing to read

An empty or near-empty repository is a legitimate starting point, and pretending to have
analyzed it is worse than admitting there is nothing yet. Say so, and run a fuller
interview — a project at this stage has a soul and no code, which is the easiest case to
get honest answers from and the hardest to fake.
