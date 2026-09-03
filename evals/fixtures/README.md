# Test fixtures

Synthetic projects used by `../evals.json`. They are not real software — `pgtypes` does
not exist, and the source files are illustrative fragments, not working code. They exist
so the skill can be tested against a project with enough texture to analyze: a README that
states a position, a changelog that records a reversal, error messages someone clearly
thought about, and a comment explaining a deliberate trade-off.

- **`typed-pg-cli/`** — no `SOUL.md`. Used for Forge-mode tests.
- **`with-existing-soul/`** — the same project plus a `SOUL.md` at version 1, one open gap
  recorded in its provenance, and an absolute "no telemetry" line. Used for the
  no-overwrite, Evolve, and Check tests.

To run a test, copy a fixture to a scratch directory and `git init` it first — the analysis
and drift-detection steps read git history.
