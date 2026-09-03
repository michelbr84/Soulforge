---
soul_version: 1
created: 2026-01-14
last_reviewed: 2026-01-14
---

# The Soul of pgtypes

> **Your database already knows the types. Stop typing them again.**

## Origin Story

In 2025 I was on call for a service with 41 tables and no generated types. A migration
added a nullable column on a Tuesday and we found out on Friday, in production, from a
customer. I tried three ORMs that week and dropped all of them for the same reason: each
one wanted to own my queries in exchange for knowing my schema. The trade was never worth
it. The first version of pgtypes was a 180-line script that read `information_schema` and
printed a file. I still have it in a gist.

## Why We Exist

Writing SQL was never the hard part. Keeping a type definition honest against a schema
that changes every week is, and the industry answered that with frameworks that take over
your data layer. There should be a version of this that just tells you the types and
leaves.

## Our Belief

Generated code is code. If a tool writes something into your repository, you should be
able to read it, diff it, and debug it without knowing anything about the tool.

## Principles

### Readable output over small output

The file we emit is one you will read in a code review. So when we must choose between a
more compact generated file and one a person can follow line by line, we choose the one a
person can follow — even when it means 40% more lines.

### Boring beats magic

No runtime, no proxies, no decorators. So when a feature would require us to be running
while your code runs, we don't build it, even when it would be more convenient.

## Promise to Users

- The output is yours. It is plain TypeScript with no imports from us.
- We never open a network connection except to the database url you give us.
- Removing pgtypes from a project takes one step: stop running it.

## What We Will Never Become

- We will never collect usage data. Not anonymized, not opt-out, not "just crash reports".
- We will never require an account to run the CLI.
- We will never make the generated output depend on a package we publish.

## The One-Sentence Soul

> **Your database already knows the types. Stop typing them again.**

---

## How This Document Was Written

- **Interviewed:** the author, on 2026-01-14, in English.
- **Repository state:** v0.3.0.
- **Drawn from the code rather than from a person:** none.
- **Still open:** the long-term dream.

## Amendments

Nothing above is ever deleted. When a section changes meaning, the text it replaced is
kept here, verbatim, with the date and the reason.
