# Making the soul operational

Read this for Stage 4 and in Check mode. A soul document that never touches a decision is
a poster. This file covers how identity translates into the choices a project actually
faces, and how to judge a proposal against it.

## The split

The `SOUL.md` section **Deciding With This** stays short — 15 to 20 lines: the alignment
question, then three to six concrete "when in doubt" rules that fall directly out of the
Principles. Short enough that people reread it.

Everything longer goes to a companion `docs/soul-in-practice.md`. It is operational and
will change far more often than the soul does; keeping it separate is what stops `SOUL.md`
from decaying into a style guide. **Offer the companion, don't impose it** — for a personal
project two weeks old it is overhead.

Write only the domains that actually bite for this project. A library has no monetization
section; a game has no CLI copy. Padding the list with domains that don't apply is the
same genericness the whole skill is built to avoid.

## Domains

**Architecture.** Which principles constrain structure? A project that promises "your data
stays on your machine" has ruled out a class of designs. One that values readable output
over clever output has decided something about code generation and metaprogramming. Write
the constraint, not the preference.

**User experience.** What does the Personality section imply about defaults, error
recovery, and how much the product explains itself? A project that "assumes you are
competent and busy" has just decided against onboarding wizards.

**Documentation.** Who is the reader, and what do they already know? Beliefs about users
show up in whether docs start with concepts or with a working command.

**README.** The first three lines are where identity is most visible and most often
generic. The One-Sentence Soul usually belongs there.

**CLI and error messages.** The highest-density expression of personality in a tool. An
error either tells you what to do next or it doesn't, and that is a values decision made
a hundred times. Give two or three concrete examples in the project's voice.

**Interface and visual design.** Density, defaults, dark mode, how much motion. Whether
the interface trusts the user or guides them.

**Branding.** Name, tone, colors, whether it has a mascot. Derive it from Personality
rather than inventing one — and say plainly when the soul doesn't determine it.

**Product decisions and feature choice.** The most valuable domain, because it is where
the soul either has teeth or doesn't. Write the test as a question the team can ask in a
planning meeting, phrased against this project's actual pressures.

**Community.** How issues are answered, how disagreement is handled, what a good first
contribution looks like, who gets commit access and when.

**Open-source contribution.** Review tone, how much scaffolding a newcomer gets, whether
the project optimizes for contributor throughput or for a small consistent codebase.
Those two goals conflict, and the principles should say which wins.

**Communication.** Release notes, changelog voice, how bad news is delivered. Projects
break their promise most visibly in how they announce a breaking change.

**Monetization, when it applies.** The domain where souls die. Write down which revenue
models are compatible with the promises already made and which are not — before there is
money on the table. A soul document written after the pricing discussion is worth much
less than one written before it.

## Check mode

Someone brings a decision, a feature, a dependency, a name, a PR, a price change, or a
piece of copy, and wants to know if it fits.

### How to judge

1. Read `SOUL.md`. Do not answer from memory of an earlier read.
2. Find the lines that actually bear on it — usually in Principles, Promise to Users, or
   What We Will Never Become. If nothing bears on it, say so.
3. Weigh it against those lines specifically, not against a general impression.
4. Answer in one of four ways.

### The four answers

**Aligned.** Name the line it follows from. One or two sentences; don't inflate agreement
into an essay.

**Tension.** It cuts against something, but not fatally. Name the line, name the cost, and
say what would resolve it — usually a smaller version of the same idea, or a different
default.

> Tension. *Promise to Users* says telemetry is opt-in and always visible. Analytics on by
> default breaks that. Opt-in at first run, with the exact payload shown, keeps the
> decision and the promise.

**Conflict.** It contradicts a written line directly. Quote the line. Say what would have
to change — either the decision or the document — and be explicit that changing the
document is a legitimate option, handled through Evolve, not by quietly ignoring it.

**The soul doesn't speak to this.** Say it plainly. Most technical decisions are not
identity decisions, and a rubric that always finds a verdict is manufacturing conflict.
The fastest way to make a team stop consulting its own document is to turn it into a
machine that says no.

### Guardrails

**Write no files in Check mode.** It answers a question; it does not edit the project.

**Advise, don't veto.** The person deciding is the one who has to live with it. Give them
the clearest possible reading of what they wrote down and let them choose.

**Don't volunteer this.** Ordinary engineering work does not need an alignment review. Run
Check when asked, or when a change plainly contradicts a written line — not as a running
commentary.

**One good line beats five vague ones.** A verdict resting on a specific quoted sentence
is useful. A verdict resting on the general vibe of the document is what makes people stop
trusting it.

### When the conflict is real and repeated

If the same line keeps blocking things the team wants, that is information about the
document, not about the team. Say so, and offer Evolve. A soul that is quietly violated
every month is worse than one that was honestly amended — the amendment leaves a record,
and the violation leaves a habit.
