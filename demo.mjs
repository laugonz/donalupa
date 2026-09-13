import { placementError, boardComplete, culpritFor } from './demo-engine.mjs';

const data = JSON.parse(document.getElementById('case-data').textContent);
const { puzzle, copy } = data;
const ids = [...puzzle.suspects.map(s => s.id), puzzle.victim.id];
const game = document.querySelector('[data-case-game]');
const status = game.querySelector('[data-status]');
const tray = [...game.querySelectorAll('[data-person]')];
const cells = [...game.querySelectorAll('[data-cell]')];
const accusation = game.querySelector('[data-accusation]');
const result = game.querySelector('[data-result]');
const undo = game.querySelector('[data-undo]');
let positions = {}, history = [], selected = ids[0], won = false;
const name = id => copy.characters[ids.indexOf(id)];
function draw() {
  const complete = boardComplete(puzzle, positions);
  game.querySelector('[data-current-clue]').textContent = complete ? copy.accusePrompt : (copy.clues[ids.indexOf(selected)] || copy.itemPrompt);
  game.querySelector('[data-progress]').textContent = `${Object.keys(positions).length} / ${ids.length}`;
  tray.forEach(button => {
    const id = button.dataset.person;
    button.setAttribute('aria-pressed', String(id === selected));
    button.classList.toggle('is-placed', Boolean(positions[id]));
    button.disabled = won;
  });
  cells.forEach(button => {
    const cell = button.dataset.cell.split(',').map(Number);
    const actor = Object.keys(positions).find(id => positions[id][0] === cell[0] && positions[id][1] === cell[1]);
    const slot = button.querySelector('[data-piece]');
    slot.replaceChildren();
    if (actor) {
      const source = tray.find(b => b.dataset.person === actor).querySelector('[data-portrait]');
      const portrait = source.cloneNode(true);
      if (portrait.tagName === 'IMG') portrait.alt = '';
      slot.append(portrait);
    }
    button.classList.toggle('has-piece', Boolean(actor));
    button.setAttribute('aria-label', `${copy.row} ${cell[0] + 1}, ${copy.col} ${cell[1] + 1}. ${button.dataset.room}. ${actor ? name(actor) : button.dataset.label}`);
    button.disabled = won;
  });
  game.querySelectorAll('[data-clue]').forEach((clue, i) => {
    clue.classList.toggle('is-current', ids[i] === selected && !complete);
    clue.classList.toggle('is-solved', Boolean(positions[ids[i]]));
  });
  accusation.hidden = !complete || won;
  if (!complete) game.querySelector('[data-accusation-message]').textContent = '';
  result.hidden = !won;
  undo.disabled = history.length === 0;
  game.querySelector('[data-hint]').disabled = complete;
}
function announce(message) { status.textContent = message; }
tray.forEach(button => button.addEventListener('click', () => {
  selected = button.dataset.person;
  announce(selected === puzzle.victim.id ? copy.itemPrompt : `${name(selected)}. ${copy.choose}`);
  draw();
}));
cells.forEach(button => button.addEventListener('click', () => {
  const cell = button.dataset.cell.split(',').map(Number);
  const error = placementError(puzzle, positions, selected, cell);
  if (error) { announce(copy[error]); return; }
  history.push({ positions: structuredClone(positions), selected });
  positions[selected] = cell;
  selected = ids.find(id => !positions[id]) || selected;
  if (boardComplete(puzzle, positions)) announce(copy.accusePrompt);
  else if (selected === puzzle.victim.id) announce(copy.itemPrompt);
  else announce(`${copy.placed} ${name(selected)}. ${copy.choose}`);
  draw();
}));
game.querySelector('[data-hint]').addEventListener('click', () => announce(copy.hints[ids.indexOf(selected)]));
undo.addEventListener('click', () => {
  const last = history.pop();
  if (!last) return;
  positions = last.positions; selected = last.selected; won = false;
  announce(`${name(selected)}. ${copy.choose}`); draw();
} );
game.querySelector('[data-reset]').addEventListener('click', () => {
  positions = {}; history = []; selected = ids[0]; won = false;
  announce(copy.choose); draw(); tray[0].focus({ preventScroll: true });
});
game.querySelectorAll('[data-accuse]').forEach(button => button.addEventListener('click', () => {
  if (button.dataset.accuse !== culpritFor(puzzle, positions)) {
    game.querySelector('[data-accusation-message]').textContent = copy.wrongCulprit;
    return;
  }
  won = true; draw(); announce(copy.solved);
  result.querySelector('h2').focus({ preventScroll: true });
}));
draw();
game.querySelectorAll('[data-needs-js]').forEach(node => { node.hidden = false; });
