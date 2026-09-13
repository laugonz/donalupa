export function zoneAt(puzzle, cell) {
  return puzzle.zones.find(zone => zone.cells.some(([r, c]) => r === cell[0] && c === cell[1]))?.id;
}
export function placementError(puzzle, positions, id, cell) {
  const ids = [...puzzle.suspects.map(s => s.id), puzzle.victim.id];
  if (!ids.includes(id) || !Array.isArray(cell) || cell.length !== 2 || cell.some(n => !Number.isInteger(n) || n < 0 || n >= puzzle.size)) return 'blocked';
  const [row, col] = cell;
  if (puzzle.scenery.some(s => s.row === row && s.col === col && !s.occupiable)) return 'blocked';
  if (Object.entries(positions).some(([other, [r, c]]) => other !== id && (r === row || c === col))) return 'line';
  for (const clue of puzzle.clues.filter(c => c.args[0] === id)) {
    if (clue.type === 'atCell' && (row !== Number(clue.args[1]) || col !== Number(clue.args[2]))) return 'clueError';
    if (clue.type === 'inZone' && zoneAt(puzzle, cell) !== clue.args[1]) return 'clueError';
    if (!['atCell', 'inZone'].includes(clue.type)) throw new Error(`Unsupported demo clue: ${clue.type}`);
  }
  return null;
}
export function boardComplete(puzzle, positions) {
  return [...puzzle.suspects.map(s => s.id), puzzle.victim.id].every(id => positions[id] && !placementError(puzzle, positions, id, positions[id]));
}
export function culpritFor(puzzle, positions) {
  if (!boardComplete(puzzle, positions)) return null;
  const room = zoneAt(puzzle, positions[puzzle.victim.id]);
  const suspects = puzzle.suspects.filter(s => zoneAt(puzzle, positions[s.id]) === room);
  return suspects.length === 1 ? suspects[0].id : null;
}
