# Writing each section

Read this while drafting. Every section below gives what it is for, how long it should
be, and a weak version next to a strong one. The examples come from deliberately
different kinds of project — a CLI, a game, a library, a hosted product — so that none
of them can be lifted whole. Use them for calibration, never for phrasing.

The failure mode is the same in every section: writing something no one could disagree
with. Agreeable text feels safe and carries no information. If a sentence would be
equally true of a competitor, it is not about this project.

## Contents

Epigraph · Origin Story · Why We Exist · The Problem We Refuse to Accept · Our Belief ·
Mission · Vision · Principles · Personality · Community · Promise to Users ·
What We Will Never Become · The Long-Term Dream · Deciding With This ·
The One-Sentence Soul · How This Document Was Written · Amendments

---

## Epigraph

The One-Sentence Soul, in a blockquote, directly under the title. It appears twice on
purpose: this is the copy people paste into READMEs, `--help` output, and slides, and
the closing one is what a reader carries away. Repetition in a manifesto is structure,
not redundancy.

## Origin Story

**Purpose:** the true account of how this began. It is the only section that cannot be
reconstructed later, which is why it is append-only forever after.

**Length:** two to five paragraphs.

It should read like something a person would say out loud. Dates, places, the specific
tool that failed, the specific job that was miserable. Those details are the difference
between a story and a press release, and they are also what makes it survive — people
remember the Sunday afternoon, not the value proposition.

> **Weak:** "Born from a desire to simplify database access for modern developers, the
> project began as an exploration of how tooling could be made more intuitive."
>
> **Strong:** "In 2023 I was maintaining a service with 40 tables and no types. Every
> schema change broke something at runtime, in production, usually on a Friday. I tried
> three ORMs and gave up on all of them for the same reason: they wanted to own my
> queries. I wanted to keep writing SQL and stop writing types by hand. The first
> version was a 200-line script that read `information_schema` and printed a TypeScript
> file. I still have it."

The weak one could be about any database tool written in the last decade. The strong one
could only be about this one, and it tells you something about the author's taste before
it states a single principle.

If the project pivoted later, the pivot goes in a *Second Beginning* subsection here.
Never edit the original.

## Why We Exist

**Purpose:** the short, forceful answer to "why does this deserve to exist when other
things already do?"

**Length:** two to four sentences. This is the section most likely to be quoted alone,
so it should survive being quoted alone.

It has to be a claim, not a description. "We make X easier" is a description; "X was
never hard — it was just badly served, and everyone accepted that" is a claim.

## The Problem We Refuse to Accept

**Purpose:** the situation the creator looked at and decided was not acceptable. This
is where the project's anger lives, and a project without any is usually a project
without a direction.

**Length:** one or two paragraphs.

Make it concrete enough that a reader can picture it happening to them. A problem stated
at the level of "inefficiency in the industry" cannot motivate anyone.

> **Weak:** "Existing solutions are complex and difficult to use."
>
> **Strong:** "A new contributor to a mid-size game project spends their first two days
> not writing gameplay but getting the engine to build. We refuse to accept that the
> price of entry to making a game is a week of build systems."

## Our Belief

**Purpose:** one claim about the world that this project is a bet on.

**Length:** one to three sentences, sometimes a single line.

The test: **a reasonable person must be able to disagree with it.** "We believe in
quality software" fails — nobody is against quality. "We believe most software should
be readable by the people who depend on it, even if that costs performance" is a real
position, and it predicts what this project will do when the two conflict.

## Mission

**Purpose:** what the project is doing now, in the present tense.

**Length:** one to three sentences.

Bounded and current. If it could have been written before any code existed, it is too
vague to be useful. The Mission is the sentence that should become false and need
updating when the project succeeds — that is the point of keeping it separate from
Vision.

## Vision

**Purpose:** where it is trying to get to.

**Length:** one to three sentences.

Different from The Long-Term Dream: Vision is the destination the current work is aimed
at, plausibly reachable. The Dream is the version with no constraints.

## Principles

**Purpose:** to let a developer choose between two reasonable alternatives without
asking anyone.

**Length:** three to seven. Fewer than three is not a set of principles; more than seven
means none of them are load-bearing.

**Each principle must complete this sentence with a real A and B from this project:**
*so when we are forced to choose between A and B, we choose A.* If you cannot fill in
the trade-off, it is not a principle — it is a mood, and it will never settle an
argument.

> **Weak:** "**Simplicity.** We value simple, elegant solutions."
>
> **Strong:** "**Readable output over clever output.** The code we generate is code you
> will read in a diff and debug at 2am. So when we must choose between a smaller
> generated file and one a human can follow, we choose the one a human can follow —
> even when it means shipping 40% more lines."

Notice what the strong version does: it names the cost. A principle that costs nothing
protects nothing.

Format each as a bold name, one or two lines of explanation, then the trade-off.

If you derived a principle from the code rather than from the interview, say so at the head
of the section and write it in the observed past tense — what this project has chosen before,
not what it promises to choose. Then list confirming them as an open question. Principles are
the section most likely to be quoted back at someone in an argument, which is exactly why
none of them should be words the author never said.

## Personality

**Purpose:** how the project behaves — which decides how docs are written, how errors
are worded, how issues are answered, and what the whole thing feels like to be around.

**Length:** six short entries, one line each.

Cover language, attitude, how it treats users, how it treats contributors, where it
stands technically, and how formal it is. Be specific enough to settle a copy decision.

> **Weak:** "Friendly and professional, with a focus on user experience."
>
> **Strong:** "**With users** — assumes you are competent and busy. Never explains what
> a terminal is; never makes you read three paragraphs to find the flag. When something
> fails, the error says what to do next, and it does not apologize."

The strong version can be handed to someone writing an error message tomorrow.

## Community

**Purpose:** who the project wants around it, and how it should feel to be one of them.

**Length:** one or two paragraphs.

Say who it is *for* — and, where it is honest, who it is not for. "Everyone is welcome"
describes no community and attracts no one in particular. A project that says "this is
for people who like reading source code and dislike magic" tells the right people they
have found their place.

## Promise to Users

**Purpose:** the things users can count on, breaking which would be a betrayal rather
than a change.

**Length:** three to six items.

Promises must be checkable. "We promise a great experience" cannot be broken because it
cannot be tested. "Your data stays on your machine unless you explicitly export it" can
be broken, which is what makes it worth writing down.

## What We Will Never Become

**Purpose:** to protect the identity from the pressures that arrive with success —
growth, money, acquisition, scale.

**Length:** three to six items.

**Every item must name a plausible temptation.** The test: could this project realistically
drift into it? "We will never be evil" is decoration. "We will never sell a version where
the free tier stops receiving security fixes" is a lock on a door someone will one day
try.

At least one item should cost something real — a revenue path, a popular feature, a
growth tactic. If every promise on the list is free to make, the section is theater.

This is the section that gets quietly betrayed first, which is why Evolve mode asks about
it specifically every time.

## The Long-Term Dream

**Purpose:** the most ambitious honest version of where this goes.

**Length:** one or two paragraphs.

Ambitious is not the same as grandiose. "Every developer on earth uses this" is a number,
not a dream. The dream should describe a changed situation: what is different in the world
if this works completely.

This section is often the one left open after a first interview. A marked gap here is fine.

## Deciding With This

**Purpose:** to give the soul an edge. Without it the document is a poster.

**Length:** 15–20 lines.

The alignment question, then three to six concrete "when in doubt" rules that follow
directly from the Principles above. Each rule should be usable by someone who has not
read the rest of the document.

> "When a feature would make the tool easier to start with but harder to understand
> later, we don't ship it. When a dependency would save us a week but we could not
> explain what it does, we write the week."

If a longer operational guide exists, link `docs/soul-in-practice.md` here in one line.

## The One-Sentence Soul

**Purpose:** the line that outlives the document.

**Length:** under about fifteen words.

It has to work with no context around it — on a sticker, in a talk, in the first line of
a README. No stacked conjunctions; one idea. It should be the sentence someone repeats
when explaining, years later, why they still work on this.

> **Weak:** "Empowering developers to build better software faster with modern tooling."
>
> **Strong:** "Your database already knows the types. Stop typing them again."

Write five and pick one. The first is almost never the one.

## How This Document Was Written

**Purpose:** to make the sourcing rule auditable, and to give Evolve mode a baseline.

Record who was interviewed, when, in what language, which sections came from reading the
code rather than from a person, and which questions are still open. If one person spoke
for a team, say so — it is honest, and it tells a future reader whose voice this is.

## Amendments

Empty at version 1, with its contract stated in one line: nothing above is ever deleted;
superseded text is preserved here, verbatim, with the date and the reason.
