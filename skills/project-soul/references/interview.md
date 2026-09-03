# The interview

Read this before Stage 2. Everything worth putting in a `SOUL.md` that you could not have
written yourself comes out of this conversation, so the way it is run matters as much as
the questions themselves.

Three rules shape the design: never ask a blank question when you could offer a
correction, never drip one question per turn, and never let the person feel processed.

## The shape

| Step | What happens | User turns |
|---|---|---|
| Stage 1 analysis | You read. No questions. | 0 |
| **Round 1** | One message: your reading of the project, the positions you want corrected, and 4–6 questions | 1 |
| **Round 2** | 1–4 follow-ups that exist only because of Round 1 | 1 |
| Draft review | You show the draft, they correct it | 1 |

Three user turns, four at the outside. Five questions if five are enough; up to ten when
the project genuinely needs them.

**The analysis and the first questions go in the same message.** Sending the summary alone,
or a menu about how deep to go, spends a round trip before the user has said one thing about
their project. The depth choice is offered as a sentence inside Round 1, not as a turn of its
own — and it is more honest that way, since nobody can sensibly pick "five questions or ten"
before seeing what the questions feel like.

Never send a message containing one question and nothing else — that is an interrogation, and
people start giving short answers to make it end.

## Which questions get a hypothesis and which don't

**Attach your guess** to anything the project can suggest: what it does, who it is for,
what it is competing with, its technical stance, its stage. Correcting is far cheaper than
composing, and a wrong guess produces a better answer than a blank line ever does.

**Ask blank** — no hypothesis, no candidates, nothing to nod at:

- the origin moment
- the belief
- what it must never become
- what is at stake if it works

These four cannot be inferred, and they carry Origin Story, Our Belief, What We Will Never
Become, and Why We Exist. A hypothesis here does not jog the memory; it hands the person
your invention and invites them to agree with it. What you get back will read well and be
worthless.

## Selection rule

Always ask the four blank ones. Add up to six more only where Stage 1 left a real hole.
Never ask anything on the already-answered list — the fastest way to lose someone is to
ask what their README says on line three.

## Opening the interview

Show your reading first. It proves you looked, it gives them something easy to react to,
and their corrections are usually the most revealing thing in the session.

> I read the repo first so I don't ask you things it already answers. Here's what I think
> I know:
>
> - It's a CLI that turns a Postgres schema into typed clients.
> - It's for people who don't want an ORM but are tired of writing types by hand.
> - It's early — three months, no releases, one contributor.
> - Two decisions look like a philosophy rather than taste: you generate code you can read
>   and commit instead of doing it at runtime, and you refused a config file until v0.4.
>
> Correct anything wrong there. What I can't get from the code is why you started and what
> you refuse to let this become — so:
>
> 1. What was the moment you thought "this should exist"? Not the reason, the moment.
> 2. What do you believe about this problem that most people building similar things don't?
> 3. What would this have to do for you to stop recognizing it?
> 4. If it works, what changes for the people using it?
> 5. Who do you want around this — not users, the people who'd argue about it with you?
> 6. My guess is you're fighting tools that treat the user as the thing that's broken. Is
>    that it, or is it something else?
>
> Answer as short as you like — half a sentence is fine, and "skip" is fine. If you'd rather
> I just draft the whole thing from the code and you correct it, say so and skip all six.

## The question bank

Eight themes. Adapt the wording to the project; asking these verbatim will feel like a
form. The parenthetical variants show how the same question changes shape by project type.

### A · Origin — always ask, always blank

- What was the moment you thought "this should exist"? Not the reason — the moment.
- What were you doing right before you started? What had just gone wrong?
- What did the first version look like, and what did it not do?
- *(Library)* What were you doing by hand that you finally refused to do again?
- *(Game)* What did you want to play that didn't exist?
- *(Startup)* Who did you talk to before you wrote any code, and what did they say?

### B · Stakes — ask at least one

- If this works, what changes for the people who use it?
- Who is worse off today because this doesn't exist yet?
- What would someone stop doing if they adopted this?

### C · Belief — always ask, always blank

- What do you believe about this problem that most people building similar things don't?
- What's the unpopular opinion baked into how you built it?
- Finish this: "Most tools like this assume ___. That's wrong because ___."

### D · Identity and personality

- If this project were a person, how would they talk? Blunt, patient, funny, formal?
- When a user makes a mistake, is the project apologetic, matter-of-fact, or does it
  assume they know what they're doing?
- Is there a project — in any field — whose personality you'd want people to compare
  this to?

### E · People and community

- Who do you want around this? Not users — the people who'd contribute or argue about it.
- Who is this explicitly *not* for? (This one is often more useful than its opposite.)
- What kind of first pull request would make you happy? What kind would make you tired?

### F · Boundaries — always ask, always blank

- What would this project have to do for you to stop recognizing it?
- If someone offered to buy or fund it, what condition would you refuse?
- Is there a feature you'll never build, even though people ask for it?
- What's the version of success you would not want?

### G · Horizon

- Best case, five or ten years out — what does that actually look like?
- What would you want someone to say about this after using it for years?
- When it gets hard and you want to stop, what do you tell yourself to keep going?

### H · Contrast

- What exists already that does something like this, and why wasn't it enough?
- What do those alternatives get right that you'd never want to lose?
- What is this project, in a sense, fighting against?

## Wording patterns

**A question with a hypothesis and an exit.** The exit matters — without it people agree
out of politeness.

> **3. What you're fighting against.** From the README and the way your errors are worded,
> my guess is you're fighting tools that treat the user as the thing that's broken. Is that
> it, or is it something else?

**Probing an abstract answer for the scene.** One probe per abstract answer, at most two
in the whole interview. Past that you are badgering, and the answers get worse.

> You said you wanted it "simpler." When did you last hit the un-simple version? I want the
> scene — a day, a bug, a tool you gave up on — not the principle. The story is what someone
> repeats in five years; the principle is what they skim.

**Turning a generic audience answer into a person.**

> Think of one specific person who used this. What could they do afterward that they
> couldn't before?

**Getting a principle to name its cost.**

> What would you refuse even if it made the project slower to adopt, or less popular?

**Getting a "never" with teeth.**

> Which of those would actually be tempting? I'm looking for the one that would cost you
> something real to keep.

## When to use AskUserQuestion

Only where two to four options genuinely span the space. Soul questions need prose, and
forcing them into options destroys the thing you are collecting.

Use it for exactly three things:

1. **Turning an "I don't know" into a choice**, offering two or three candidates drawn from
   the project — always with a fourth option meaning "none of these, I'll say it myself."
2. **The language of the interview**, if it isn't obvious which one the person prefers.
3. **The final go-ahead** before writing the file.

Not for how deep to go. That is offered as a sentence in Round 1, because a tool call there
costs a whole turn and asks people to choose a depth before they have seen a single question.

Never use it for the origin story, the dream, the promise, or the personality.

## Difficult cases

**One-word answers.** Probe once. If it stays thin, keep it thin. Three words become three
words in the document. Inflating them into a paragraph is invention wearing the user's voice.

**"I don't know."** Convert it into a choice between candidates you can point at in the
project. If still nothing, it becomes a marked gap in the document and an open question in
the provenance section. Never fill it in yourself.

**"You decide" / "just do it fast."** Switch to draft-and-correct: produce the whole
`SOUL.md` **in the conversation, not on disk**, with every inferred claim marked as inferred,
and ask for one correction pass. That is one round trip and it keeps a human in the loop —
which is the part that cannot be skipped.

**They answer four of six.** Don't re-ask the skipped ones. Note them as open questions and
move on. People skip questions they don't have an answer to yet, and pressing produces
invention rather than memory.

**They go quiet mid-interview.** Write nothing. If they come back, resume from what was
answered.

**A team project with one person answering.** Say once, plainly, that this captures one
person's view, and record whose in the provenance section. A future contributor should know
whether they are reading a consensus or a founder.

**They start describing features.** Redirect gently — features belong in the README. Ask
what made that feature worth building when others weren't.

**They contradict something in the code.** Say what you saw and ask about it directly. The
gap between what a project does and what its author believes it does is often where the most
interesting part of the soul is hiding.
