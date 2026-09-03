#!/usr/bin/env node
import { introspect } from './introspect.js'
import { emit } from './emit.js'

const url = arg('--url') ?? process.env.DATABASE_URL
if (!url) {
  console.error(
    'pgtypes: no database url.\n' +
    '  Pass --url, or set DATABASE_URL.\n' +
    '  The url needs read access to information_schema, nothing more.'
  )
  process.exit(1)
}

const schema = await introspect(url)
await emit(schema, arg('--out') ?? 'db.types.ts')
