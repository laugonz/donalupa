import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { placementError, boardComplete, culpritFor } from '../demo-engine.mjs';
const puzzle = JSON.parse(readFileSync(new URL('../content/demo-case.json', import.meta.url)));
const copy = JSON.parse(readFileSync(new URL('../content/demo-copy.json', import.meta.url)));

test('the original app solution obeys the demo rules and identifies the same culprit', () => {
  assert.equal(boardComplete(puzzle, puzzle.solution), true);
  assert.equal(culpritFor(puzzle, puzzle.solution), puzzle.culprit);
  assert.equal(culpritFor(puzzle, {}), null);
  assert.equal(boardComplete(puzzle, {s_accountant: [0, 2]}), false);
});
test('every complete arrangement satisfying the visible clues has one solution', () => {
  // Compare every playable arrangement against the native app's stored solution.
  const solutions = [];
  const cells = [];
  for (let row = 0; row < 4; row++) for (let col = 0; col < 4; col++) {
    if (!puzzle.scenery.some(s=>s.row === row && s.col === col && !s.occupiable)) cells.push([row,col]);
  }
  for (const a of cells) for (const b of cells) for (const c of cells) for (const d of cells) {
    const positions = {s_accountant:a,s_marketing:b,s_sales:c,case_item:d};
    if (boardComplete(puzzle, positions)) solutions.push(positions);
  }
  assert.equal(solutions.length, 1);
  assert.deepEqual(solutions[0], puzzle.solution);
});
test('furniture, repeated rows/columns and contradictory clues reject placements', () => {
  assert.equal(placementError(puzzle, {}, 's_accountant', [0,3]), 'blocked');
  assert.equal(placementError(puzzle, {s_accountant:[0,2]}, 'case_item', [0,0]), 'line');
  assert.equal(placementError(puzzle, {s_sales:[2,1]}, 'case_item', [3,1]), 'line');
  assert.equal(placementError(puzzle, {}, 's_accountant', [0,1]), 'clueError');
  assert.equal(placementError(puzzle, {}, 's_marketing', [0,0]), 'clueError');
  assert.equal(placementError(puzzle, {}, 'case_item', [-1,0]), 'blocked');
  assert.equal(placementError(puzzle, {}, 'not-a-suspect', [0,0]), 'blocked');
});
test('a piece can be selected again without colliding with itself', () => {
  assert.equal(placementError(puzzle, puzzle.solution, 's_accountant', [0,2]), null);
  assert.equal(placementError(puzzle, {}, 'case_item', [0,0]), null);
});
test('every language has complete controls, clues, hints and a distinct canonical route', () => {
  const keys = Object.keys(copy.en).sort();
  assert.equal(new Set(Object.values(copy).map(c=>c.path)).size, 5);
  for (const c of Object.values(copy)) {
    assert.deepEqual(Object.keys(c).sort(), keys);
    assert.equal(c.characters.length, 4);
    assert.equal(c.clues.length, 3);
    assert.equal(c.hints.length, 4);
    assert.equal(c.solution.length, 5);
    for (const s of puzzle.scenery) assert.ok(c.scenery[s.key]);
  }
});
