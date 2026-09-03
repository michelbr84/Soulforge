// We generate wide, boring, readable output on purpose.
// Someone is going to read this file in a diff at 2am. Clever is not a favor to them.
export async function emit(schema, out) {
  const lines = []
  for (const table of schema.tables) {
    lines.push(`export interface ${pascal(table.name)} {`)
    for (const col of table.columns) {
      lines.push(`  ${col.name}: ${tsType(col)}${col.nullable ? ' | null' : ''}`)
    }
    lines.push('}', '')
  }
  await write(out, lines.join('\n'))
}
