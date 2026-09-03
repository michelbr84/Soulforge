---
name: project-soul
description: >-
  Discover, define, and preserve a project's soul — its origin story, purpose, beliefs,
  principles, personality, and promises — and write it to SOUL.md at the project root. Use
  whenever someone wants to articulate why a project exists rather than how it works: "give this
  project a soul", "define our identity", "write our manifesto", "what's our mission and vision",
  "why does this project exist", "what do we believe", "what should this project never become",
  "write a SOUL.md", "define our voice and personality", and non-English equivalents ("alma do
  projeto", "manifesto", "propósito", "princípios", "identidade"). Also use it when SOUL.md
  already exists and the user wants to update, evolve, or amend it after the project changed, or
  wants to check whether a decision, feature, dependency, price change, or piece of copy is
  aligned with the project's soul. Do not use it for ordinary README, API reference, CONTRIBUTING,
  or changelog work with no identity question behind it.
license: MIT
---

# Project Soul

Code explains how a project works. Documentation explains how to use it. Nothing in a repository explains why someone decided it should exist — that lives in one person's head, leaves when they leave, and is the first thing lost when a project grows, takes money, or changes hands.

This skill puts it in writing. It reads the project, interviews the person who made it, and writes `SOUL.md`: origin, purpose, beliefs, principles, personality, promises, and the lines the project must never cross. Then it protects that document — amending it as the project changes without erasing what came before, and answering the question every later decision should face: *is this still us?*

The whole thing rests on one rule. **The soul comes from the human, not from you.** You can read what a project does; you cannot read why anyone cared. A beautiful invented sentence is the worst thing this skill can produce, because it will be believed, quoted, and defended by people who weren't there.

## Pick the mode first

Before any analysis and before any question, find out whether a soul document already exists. One glob: `SOUL.md` at the project root, then `docs/SOUL.md` and `.github/SOUL.md`.

| Situation | Mode |
|---|---|
| No soul document | **Forge** — the full five stages below |
| Document exists, and the request is to update, revisit, evolve, or amend it, or says the project changed | **Evolve** |
| Document exists, and the request names something concrete to judge — a feature, decision, dependency, name, PR, price, piece of copy — or asks "should we…", "does this fit…", "is this aligned…" | **Check** |
| Document exists, and the request is to create one | Do **not** overwrite. Say it exists, summarize it in two lines, offer Evolve |
| Ambiguous | Read the existing document, then ask once with `AskUserQuestion` |

Say which mode you picked in one line before you start, so the user can redirect you cheaply.

Forge never overwrites an existing `SOUL.md`. If the user insists on starting over after you've told them one exists, the old text is preserved as an amendment record, never deleted. A project only gets one origin.

---

## Forge

### Stage 1 — Read the project before you ask anything

Nothing costs you the user's trust faster than asking something the README answers on line three. Read first.

Read `${CLAUDE_SKILL_DIR}/references/project-analysis.md` before this stage. It gives the reading order, the signals that carry philosophy rather than just facts, and what the same evidence means in a library versus a game versus a startup.

You are looking for two things. First, the answerable facts: what it does, its stack, who it's plausibly for, what stage it's at. Second — and this is what makes the interview good — **the decisions that already reveal a belief**. A license choice, a refusal to add telemetry, zero dependencies, error messages someone clearly agonized over, a feature conspicuously absent. Those are positions, and naming them back to the creator is what makes them realize you actually read their work.

Come out of this stage with a written list of what the project already answers. You will not ask any of it.

If the project is empty or nearly empty, don't fake an analysis. Say the project is still an idea and run a more open interview — here the soul precedes the code, which is a fine place to be.

### Stage 2 — Interview the person who made it

Read `${CLAUDE_SKILL_DIR}/references/interview.md` before this stage. It holds the question bank by theme, the exact wording patterns, and how to handle thin answers.

The shape, which matters as much as the questions:

- **Round 1 is one message containing everything:** what you learned in Stage 1, the two or three decisions you read as positions for them to correct, and 4–6 questions. Do not spend a turn on a menu before it — a user who has to answer a process question before saying anything about their project has spent a round trip on nothing. Offer the escape hatch inline instead: if they would rather you draft the whole document from the code and have them correct it, one sentence tells them so.
- **Round 2: 1–4 follow-ups** that exist only because of what Round 1 said, plus any remaining questions if they are clearly engaged.
- Then a draft review turn. Three user turns, ceiling of four. Five questions if five are enough; up to ten when the project genuinely needs them.

Never drip one question per turn. It feels like an interrogation, and it burns the goodwill you need for the honest answers.

Every question about something inferable ships with your guess attached, because correcting is far cheaper than composing. But the four things you cannot infer get asked **blank**, with no hypothesis to anchor them: the origin moment, the belief, what the project refuses to become, and what's at stake if it works. A hypothesis there doesn't help the user remember — it hands them your invention to nod at.

Ask for scenes, not principles. "I wanted it simpler" is not an origin story; "the third time I rewrote the same 200 lines of boilerplate on a Sunday" is. One probe per abstract answer, at most two in the whole interview — past that you're badgering.

`AskUserQuestion` is for genuinely discrete choices only: turning an "I don't know" into a choice between candidates drawn from the project, and the final go-ahead before writing the file. Origin, dream, promise, and personality need prose — forcing them into four options destroys the exact thing you're trying to collect, and spending one on how deep to go costs a turn you could have spent asking.

### Stage 3 — Write the soul

Read `${CLAUDE_SKILL_DIR}/references/soul-sections.md` for what each section is for and what a good and a bad version of it look like, and `${CLAUDE_SKILL_DIR}/references/voice.md` for the language to avoid and what to write instead. Copy the skeleton from `${CLAUDE_SKILL_DIR}/assets/SOUL.template.md`.

The sections, in order:

Origin Story · Why We Exist · The Problem We Refuse to Accept · Our Belief · Mission · Vision · Principles (3–7) · Personality · Community · Promise to Users · What We Will Never Become · The Long-Term Dream · Deciding With This · The One-Sentence Soul · How This Document Was Written · Amendments

Two of those carry most of the document's usefulness, and both fail the same way — by being agreeable:

**Principles have to be able to cost something.** Each one must complete the sentence *"so when we are forced to choose between A and B, we choose A"* with a real A and B from this project. A principle nobody would argue with isn't a principle, it's a mood, and it will never help anyone pick between two implementations at 11pm.

**"What We Will Never Become" has to name plausible temptations.** At least one item should cost a real revenue path, a popular feature, or a growth tactic. "We'll never be evil" is decoration. "We'll never require an account to run the CLI" is a lock someone will one day want to pick.

Length: 200–400 lines. Longer goes unread; shorter is a list of slogans.

### Stage 4 — Make it operational

A soul with no edge is a poster. Translate it into guidance for the decisions this project actually faces — architecture, UX, documentation, README, CLI and error copy, interface, branding, product and feature choices, community, contribution, communication, and monetization where it applies.

Read `${CLAUDE_SKILL_DIR}/references/soul-in-practice.md` for how each of those follows from the soul.

Split it asymmetrically. Inside `SOUL.md`, the **Deciding With This** section stays short — 15–20 lines, the alignment question plus three to six concrete "when in doubt" rules that fall directly out of the Principles. The long version goes to a companion `docs/soul-in-practice.md`, which will change far more often than the soul does; keeping it separate is what stops `SOUL.md` from decaying into a style guide. Offer that companion, don't impose it — for a two-week personal project it's overkill.

Then offer the pointers, each one separately and never written without permission:

- `README.md` — two to four lines near the top: why this exists → `SOUL.md`.
- `CLAUDE.md` — one line, and this is the highest-leverage of the three: *"Read SOUL.md before product, UX, naming, or copy decisions."* It's what makes every future Claude session in that repository consult the document instead of ignoring it. Create the file if it doesn't exist.
- `CONTRIBUTING.md` for open-source projects — one line, so contributors meet the identity before the style rules.

### Stage 5 — Write the file

`SOUL.md` at the project root. Run the self-check below first, and report its result to the user in two lines rather than hiding it.

---

## Evolve

The project moved and the document didn't. Read `${CLAUDE_SKILL_DIR}/references/evolution.md` for the drift-detection commands and the amendment format.

Detect before you ask. Using `last_reviewed` from the document's frontmatter as the baseline, look at what actually changed: commit volume, new top-level directories, manifest diffs, README tagline changes, release tags, license changes, contributor count. Then place it in one of four classes, because they call for four different behaviors:

| Class | What you see | What you do |
|---|---|---|
| **No material change** | docs and dependency churn | Say so plainly, offer to bump `last_reviewed`, **ask nothing**. This is the common case, and manufacturing work here is a failure |
| **Growth** | same identity, more of it | Propose additions only. One or two questions |
| **Drift** | audience, scope, monetization, or tagline changed | Propose amendments. Two to four questions, always including whether anything in *What We Will Never Become* is now under pressure — that section is the one quietly betrayed first |
| **Pivot** | it does a different thing now | Never rewrite the Origin. Append a *Second Beginning* under it, and amend Mission and Vision with the old text preserved |

Show a diff-and-propose table before touching anything — what changed in the project, what that implies for the soul, and whether you propose to amend or keep. Let the user accept or reject rows, and only ask questions about the rows they accepted.

**The preservation contract is absolute.** Amended text is never deleted; it moves verbatim into the amendment entry, and the section gains a pointer to it. `Origin Story` is append-only. A project is allowed to change its mind; it is not allowed to pretend it never thought otherwise.

---

## Check

Someone has a decision in hand and wants to know if it fits. The rubric is in `${CLAUDE_SKILL_DIR}/references/soul-in-practice.md`.

Read `SOUL.md`, then answer short: **Aligned**, **Tension**, or **Conflict**, citing the specific line that supports the verdict, and — when there's tension — what would resolve it.

Three guardrails. **Write no files in this mode.** Advise, don't veto; the person deciding is the one who has to live with it. And *"the soul doesn't speak to this"* is a real answer that you should be willing to give — a rubric that always finds a verdict is manufacturing conflict, and the fastest way to make a project stop consulting its own document is to turn it into a machine that says no.

---

## The rule that holds all of this together

**You may infer from the repository:** what the project does, its stack, its apparent audience, its stage, observable architectural and product decisions and the trade-offs they imply, timeline facts from git history, and values already stated in the README, CONTRIBUTING, or CODE_OF_CONDUCT — quoted and credited, not paraphrased into new beliefs.

**You may never infer:** the origin moment, the motive, any emotion, any belief, what the project refuses to become, the dream, the promise, the chosen personality, any claim about what the creator intended, or anything containing a date, a place, a person's name, a user quote, a metric, or a claim about a competitor.

**Principles sit exactly on that line, so handle them carefully.** A principle is read off decisions you can see in the repository — which is allowed — but it is also a forward commitment, and only a person can make one of those. So a principle nobody confirmed is written as observed past behavior ("this project has chosen X over Y, repeatedly"), marked as a candidate awaiting confirmation, and listed as an open question. Never in the project's voice as a promise. The difference sounds small and isn't: one describes what happened, the other binds people who never agreed to it.

**Don't merge identities either.** The person you interviewed, the person who wrote the README, and the name in the commits may not be the same person. If you haven't established that they are, don't write a sentence that assumes it.

Before you write the file, do the **sourcing pass**. Go through the draft claim by claim. For every sentence written in the project's voice — *we believe*, *we started because*, *we will never* — name where it came from: which answer, or which file. If you can't name one, you invented it. Cut it, or turn it into a marked gap:

```markdown
## The Long-Term Dream

> _Not yet answered: what does this look like in ten years if it works?
> Written before this question was answered — add it and delete this note._
```

A visible gap is worth more than a beautiful lie. It nags someone into filling it, and Evolve will pick it up later. Record the same open question in the provenance section.

When the user gives thin answers, keep them thin. Three words stay three words. Inflating them into a paragraph is invention wearing the user's voice.

Two things help when the interview was thin overall:

- **Say so at the top of the document, and drop the "we".** A soul document is normally written in the project's collective voice, but "we believe" over material nobody supplied puts invented conviction in someone's mouth. Quote and credit what was actually said, leave gaps for the rest, and open with a short note explaining why the document reads that way. A reader who knows which parts were decided out loud is better served than one handed a confident document built on four short answers.
- **Record declined candidates as questions, never as commitments.** When you offered choices and the user picked "none of these", the candidates are still the best starting point for a later pass — write them down as open questions so the next run has somewhere to begin, and make it unmistakable that nobody has agreed to them.

## Language

The document is written in English — it is a project artifact meant to be read by future contributors, not a reply to the person you're talking to.

**Conduct the interview in whatever language the user is speaking.** People tell the story of why they started far better in their own language, and that story is the one thing you cannot get anywhere else. Translate at write time, and keep their concrete nouns intact — the specific tool, the specific bug, the specific year. Those survive translation; adjectives don't, and don't matter.

## Before you write the file

Run this against the draft, and tell the user how it went in two lines.

1. **The portability test.** Swap the project's name for a competitor's. Every sentence that stays true is generic. Origin Story, The Problem We Refuse to Accept, Principles, and What We Will Never Become *must* break under the swap. If a whole section survives it, rewrite it with something from the interview.
2. **Banned-phrase scan.** Zero hits — the list and the replacements are in `${CLAUDE_SKILL_DIR}/references/voice.md`.
3. **The sourcing pass**, above. Every first-person claim traces to an answer or a file.
4. **Principle discrimination.** Each principle completes the A/B sentence with a real trade-off from this project.
5. **Teeth.** At least one item in *What We Will Never Become* costs something real.
6. **The stranger test.** Would someone who has never seen this repository learn one specific, surprising thing? Name it out loud. If you can't, the draft is empty.
7. **The five-year test.** Anything that dates the document to this month — a version number, a current dependency, a named competitor — moves to the companion `docs/soul-in-practice.md` in the user's project, or goes.
8. **The one sentence.** Under about fifteen words, no stacked conjunctions, quotable with no context around it.

A check can fail because a section is an honest gap — the teeth test cannot pass when nobody answered the question. Report the failure and leave the gap. A failing check is a reason to go back to the person, never a reason to write something that makes it pass.

## Reference files

Read each one at the stage that needs it, not up front.

| File | Read it when |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/project-analysis.md` | Stage 1, before reading the project |
| `${CLAUDE_SKILL_DIR}/references/interview.md` | Stage 2, before asking anything |
| `${CLAUDE_SKILL_DIR}/references/soul-sections.md` | Stage 3, before drafting |
| `${CLAUDE_SKILL_DIR}/references/voice.md` | Stage 3, while drafting and during the self-check |
| `${CLAUDE_SKILL_DIR}/references/soul-in-practice.md` | Stage 4, and in Check mode |
| `${CLAUDE_SKILL_DIR}/references/evolution.md` | Evolve mode |
| `${CLAUDE_SKILL_DIR}/assets/SOUL.template.md` | Stage 3, as the skeleton to fill |
