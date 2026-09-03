# Evolving a soul without erasing it

Read this in Evolve mode. A `SOUL.md` that is quietly rewritten every time the project
changes direction is worse than none at all — it becomes a document that always agrees
with the present, which means it can never hold anyone to anything.

The contract this file enforces: **a project may change its mind, but it does not get to
pretend it never thought otherwise.**

## Detect before you ask

Look at what actually changed before deciding there is anything to discuss. The baseline
is `last_reviewed` in the document's frontmatter; if it is missing, use the date of the
commit that added `SOUL.md`.

```bash
BASE=$(git rev-list -1 --before="<last_reviewed>" HEAD)

git log --oneline "$BASE"..HEAD | wc -l
git diff --stat "$BASE"..HEAD | tail -1
diff <(git ls-tree -d --name-only "$BASE") <(git ls-tree -d --name-only HEAD)
git diff "$BASE"..HEAD -- package.json pyproject.toml Cargo.toml go.mod composer.json
git diff "$BASE"..HEAD -- README.md | head -60
git diff "$BASE"..HEAD -- LICENSE | head -20
git tag --contains "$BASE" | head
git shortlog -sn "$BASE"..HEAD
```

If the project isn't a git repository, compare the document against the current state
directly: does it still describe what the README claims, the dependencies present, and the
directories that exist?

## Signals, roughly by weight

1. **The README tagline changed.** The strongest pivot signal there is. What a project
   calls itself is the last thing to change and the first thing that matters.
2. **A new top-level directory named for a new surface** — `billing/`, `enterprise/`,
   `mobile/`, `cloud/`, `api/`. New surfaces bring new pressures.
3. **Auth, pricing, or billing code appearing.** Monetization is now real, and every
   promise written before it was real is now under load.
4. **A license change.** Almost always a change in what the author is afraid of.
5. **Contributors going from one to many.** The Community section was written about a
   different project.
6. **First release tag, or 0.x → 1.0.** A promise of stability was just made to strangers.
7. **A framework or core dependency added or removed.** Sometimes philosophy, often not —
   check whether it changes what the project can promise.
8. **A dropped platform or an abandoned feature area.** What was given up says as much as
   what was added.

## Four classes, four behaviors

| Class | What you see | What you do |
|---|---|---|
| **No material change** | Docs and dependency churn, ordinary fixes | Say so plainly. Offer to bump `last_reviewed` and nothing else. **Ask no questions.** |
| **Growth** | Same identity, more of it — more users, more features in the same direction | Propose additions only. One or two questions |
| **Drift** | Audience, scope, monetization, or tagline changed | Propose amendments. Two to four questions |
| **Pivot** | It does a different thing now | Never rewrite the Origin. Append a Second Beginning; amend Mission and Vision with the old text preserved |

**No material change is the common case, and handling it well is most of the value of this
mode.** Manufacturing work here — inventing drift so there is something to do — teaches
the user that running this skill produces churn, and they will stop running it. Say
nothing changed, and stop.

In the Drift and Pivot classes, always ask one specific question: **is anything in "What
We Will Never Become" under pressure now?** That section is the one quietly betrayed
first, usually by a decision nobody framed as a betrayal at the time.

## Diff and propose, before touching anything

Show a table. Let the user accept or reject rows. Ask questions only about accepted rows.

| What changed | What it implies for the soul | Proposal |
|---|---|---|
| `billing/` added, Stripe dependency, pricing page | Monetization is real; the promises were written when it wasn't | **Amend** — needs your answer |
| Contributors 1 → 9, `CODE_OF_CONDUCT.md` added | Community section describes a solo project | **Amend** — I can draft it |
| Vite replaced with Rspack | Implementation detail | **Keep** — no soul change |

Most rows should be "keep". A table where everything needs amending usually means you are
reading ordinary progress as identity change.

## The preservation contract

**Nothing is deleted.** When a section's meaning changes, its previous text moves verbatim
into the Amendments section, and the section gains a marker:

```markdown
## What We Will Never Become

*(amended 2027-03-11 — see Amendments)*
```

**Origin Story is append-only.** It records what happened, and what happened does not
change because the project did. Correct it only for factual errors — a wrong year, a
misspelled tool. If the project began again, that is a *Second Beginning*, added as a
subsection under the Origin, dated, in the same voice:

```markdown
### The Second Beginning — 2027

<What made it start over, told the same way the first beginning was told.>
```

**Trivial corrections** — a typo, a renamed technology, a moved link — are made inline and
noted in one line in the amendment entry. Don't ceremonialize them.

**`soul_version` increments** with every amendment. `last_reviewed` updates on every run,
including runs that change nothing.

## Amendment entry format

```markdown
### 2027-03-11 — v2

**What changed in the project:** paid tier shipped; team grew from 1 to 9 contributors.
**Sections amended:** What We Will Never Become; Community.
**Why:** <in the user's own words, quoted from the conversation>
**Superseded text, kept verbatim:**

> We will never charge for the core CLI.

**Answered by:** <who>, in conversation, 2027-03-11.
```

The "Why" is quoted, not summarized. A future reader needs to know that a person said
this, and roughly how they said it.

## Open questions from earlier runs

The provenance section lists what was left unanswered. Evolve is the natural moment to
pick one or two of them up — a question someone couldn't answer in year one is often easy
in year three. Ask at most two, and only if the person seems to have room for them; a
drift review that turns into a second full interview will not get finished.

## The same rules still apply

Everything from Forge holds here. The sourcing pass runs before writing. Nothing is
inferred that the human did not say. Thin answers stay thin. New text passes the same
self-check — including the portability test, which amended sections fail more often than
original ones, because it is easy to write a vague update.
