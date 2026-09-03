import pg from 'pg'

// One query, one connection, closed immediately. We ask for read access to
// information_schema and nothing else, and we should not need anything else.
export async function introspect(url) {
  const client = new pg.Client({ connectionString: url })
  await client.connect()
  try {
    const { rows } = await client.query(COLUMNS_QUERY)
    return { tables: group(rows) }
  } finally {
    await client.end()
  }
}
