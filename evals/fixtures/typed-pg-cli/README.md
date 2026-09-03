# pgtypes

Generate TypeScript types from a live Postgres schema. No ORM, no runtime, no magic.

```bash
npx pgtypes --url $DATABASE_URL --out src/db.types.ts
```

`pgtypes` reads `information_schema`, writes one plain `.ts` file, and gets out of the way.
You commit the output and read it in diffs like any other code.

## Why not an ORM?

Because you already know SQL. The problem was never writing queries — it was keeping types
in sync with a schema that changes weekly.

## Requirements

Node 20+, and a Postgres connection string with read access to `information_schema`.

## Status

Early. The API may change before 1.0.
