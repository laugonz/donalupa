# Doña Lupa playable case — 13 September 2026

Visitors can solve a free, short office mystery directly on the website before downloading. The five localized homepages link to `/play/`, `/es/jugar/`, `/fr/jouer/`, `/it/gioca/` and `/pt/jogar/`. This is one adapted demonstration case, not the full collection or a daily case service.

## Before / after review

| Area | Before | After and purpose |
| --- | --- | --- |
| Entry | Hero secondary link scrolled to instructions | It now opens the localized case; a second preview section explains the mystery. Primary download remains available. |
| Demonstration | Screenshots and prose | Playable 4 × 4 board with three suspects and the missing lunch, using original app illustrations. |
| Layout | No browser board | Paper cards, orange controls, room colors and a two-column desktop layout that stacks on mobile; explicit square grid sizing prevents art from distorting rows. |
| Interaction | No browser game | Choose a piece and cell; clue, furniture and row/column validation; hints, undo and reset. |
| Feedback | No game state | Current clue above the board, progress counter, local accusation feedback, then a focused case-closed result and App Store link. |
| Accessibility | Static images and text | Native keyboard-operable buttons, coordinate/room/object labels, live feedback, visible focus, 44 px targets and reduced-motion support. Room identity is available in accessible names as well as color. |
| Learning | General rules | Original three clues plus five server-rendered deduction steps; readable without JavaScript. |
| Discovery and measurement | No playable URL | Five canonical pages, reciprocal language alternatives, sitemap entries and WebPage/Breadcrumb schema; demo download links use `donalupa_web_demo`. |

## Provenance and rules

Source case `office_002` comes from sibling `CaseGrid/ios/CaseGrid/Resources/Content/casegrid_seed.json`, native HEAD `6693b1d`. The source was unchanged locally. Web case SHA-256: `226bfc8a3b15830cdcad22496b59c1d5a88a87ca6262e66527f66b927a02d2ee`.

The 13 PNGs use the app's original suspect/scenery illustrations. The ten larger scenery images were proportionally resized to at most 256 px with transparency preserved, reducing the total demo artwork from 2,669,604 to 563,148 bytes; suspect portraits retain their original 256 px size. The lunch uses the source case's emoji. The web copy translates and clarifies the original clues. No competitor art or customer data is used.

Each piece, including the lunch, occupies a different row and column. Furniture blocks its cell. Rooms constrain clues; the culprit is the single suspect sharing the lunch's room. This case does not impose a universal one-piece-per-room rule. The unique solution is accountant `[0,2]`, marketing `[1,3]`, sales `[2,1]`, lunch `[3,0]`; sales is the culprit.

Edit `content/demo-copy.json` or the case, then run `python3 scripts/build_demo.py`. The vanilla browser module stores game state only in memory. It introduces no backend, payment flow or native changes.

## Validation

- Five Node tests pass: original solution, exhaustive enumeration confirming exactly one valid arrangement, invalid placement rules, moving the same piece and complete five-language copy.
- Chrome Spanish desktop/390 px: correct and incorrect placements, hint/undo/reset, wrong accusation and victory. Italian 320 px: full keyboard solution, local wrong-accusation feedback, focus on victory, undo after victory and reset. All 16 cells are 61.25 px squares at 320 px, with no horizontal overflow.
- French and Portuguese 320 px: initialized board, localized first clue and no horizontal overflow. The accessible room label addition was subsequently checked in the browser.
- Release checks cover all 32 sitemap pages, 44 homepage FAQ pairs, five full alternate-language groups, original case parity, asset paths and campaign links. Generators are idempotent; syntax and diff checks pass.
- No-JavaScript fallback is verified in initial HTML, not with JavaScript disabled in the browser. Nine older translated guides use the homepage as `x-default`; that pre-existing pattern is outside this demo change. New demo pages have fully reciprocal alternatives including `x-default`.

Campaign parameters reuse provider token `1201782`. Apple's reporting thresholds and delay apply; a blank report does not establish zero downloads. Source: [Apple campaign links documentation](https://developer.apple.com/help/app-store-connect-analytics/acquisition/campaign-links). Publication does not establish a conversion improvement or increased AI recommendations.

## Room identification follow-up — 13 September 2026

Laura's mobile screenshot showed that the pastel colors and small legend did not make room membership clear enough. All 16 cells now name their room, including occupied and furniture cells. The existing accessible coordinate/room labels remain intact. Room boundaries are calculated from adjacent cells in the original case; thin lines within a room and thick lines between rooms communicate the shape without relying on color. The original case and game engine are unchanged.

### Visible room identity and boundaries

| Before | After |
| --- | --- |
| Room names appeared only in a small legend | scripts/build_demo.py adds a localized .cell-room label to every cell in all five languages. Labels remain outside the piece slot so placing a suspect cannot hide them. |
| Every cell had the same thick outline and rounded corners | The generator compares the top/left neighbors' room IDs. demo.css renders shared-room dividers at 1 px and room boundaries at 3 px; cell corners are square inside the rounded board. |
| Similar pastel fills | Slightly stronger green, yellow, blue and rose room fills provide a secondary cue alongside names and borders. |
| Legend was 11 px with 12 px swatches | It is now 12 px with 14 px swatches and wider vertical spacing. |

### Room for text and illustrations

| Before | After |
| --- | --- |
| Square board, artwork centered in each square | Board aspect ratio is 5 / 6, keeping cells wide enough to tap and making space for room labels. This supersedes the square-cell measurements from the initial release above. |
| Artwork could occupy the future text area | Scenery and pieces now reserve a bottom label strip; suspect portraits retain their square proportions and never overlap room text. |
| Only small coordinate text | Coordinates have slightly stronger contrast; room names use bold 10 px type on the narrowest screens and 11 px from 380 px, up to two lines, with 26 px reserved height and slight negative letter spacing to fit Portuguese labels. |
| Rules referred only to colored rooms | Five localized rules now explain room names and the difference between thick and thin dividers. |

Validation: existing five engine/copy tests pass. Browser checks cover all five languages at 320 px, including the adjusted Portuguese label; all 16 room names fit without clipping. Spanish 390 px also fits. A full keyboard solution, victory, reset and a hint were checked; occupied cells retain room names and pieces do not overlap the label area. The release verifier independently checks all 80 labels and generated room boundaries against case data. Production evidence is in the workspace's docs/aso/donalupa-room-labels-2026-09-13 folder.

## Native room design follow-up — 13 September 2026

Laura then asked for the board to look like the app. This supersedes the per-cell room names and 5/6 board from the previous follow-up. The web now uses one white serif nameplate per room on its upper boundary, the native palette and floor patterns, and square cells. Reference: the existing app capture assets/es-gameplay.jpg and CaseGrid's GridView.swift, Theme.swift, ZoneWalls.swift and ZoneTexture.swift. The inspected working-copy GridView changes concern irregular boards; the palette, room plates and textures used here match its committed implementation. No native files were edited or built.

### Room presentation

| Before | After |
| --- | --- |
| Sixteen repeated cell labels and a separate legend | Four white rounded nameplates, with a 1.5 px chocolate border, small-caps serif type and 0.4 px tracking, matching the app's room-label design. Full localized titles are supplied in roomPlates. |
| Names sat below each illustration | Plates sit on each room's topmost contiguous row. The generator derives the anchor/span from case data; ResizeObserver positions the measured text and keeps it inside the board after resizing. Font size follows the app's max(11, cell × 0.18). |
| Green desks, yellow reception, blue break room and pale rose office | Theme.swift palette by original zone index: cream (97/93/84%), slate (64/71/79%), sage (76/85/66%) and rose (76/55/52%). |
| Flat fills | Four small procedural SVG floor textures port carpet, stone, dots and parquet from ZoneTexture. Language selection uses the original seed's language fallback; occupiable furniture cells have the app's 32% white floor wash. |
| Generic dark dividers | Native chocolate ink (24/13/6%), 3 px room boundaries at 80% opacity and 1 px inner dividers at 16%. Outer frame is 3 px, radius 14 px, with the app's soft lower shadow. |

### Board proportions and content

| Before | After |
| --- | --- |
| Tall 5/6 board with bottom text strips and visible coordinates | Square board; coordinates remain in accessible names. Map spacing reserves space around the boundary plates. |
| Art fitted around room labels; blocked furniture faded | Unoccupied scenery is centered at 60% cell size and full opacity; after placement it shrinks to 30% at the bottom right at 65% opacity, as in GridView. Portraits use the available 84% central area. |
| Rules described a name inside every cell | All five translations now explain the white room plates. The original clues, solution, game actions and Apple campaigns remain the same. |

Validation: existing five tests, syntax and diff checks pass; generated output is idempotent. At 320 px all five languages have four complete, non-overlapping plates within the board. ES390 was compared visually to the app capture; the Portuguese case was completed using the keyboard through victory and reset. The board responds to a desktop resize. Public verification and source checks are recorded under workspace docs/aso/donalupa-native-board-2026-09-13.

## Homepage entry follow-up — 13 September 2026

The browser case was reachable through a plain hero link and a preview lower down, but Laura could not find it. The homepage now names the browser action explicitly and keeps it in the sticky header in all five languages.

| Before | After |
| --- | --- |
| No play action in the header; mobile showed only the language link | A dark localized play button remains visible next to the language switcher, with a 44 px touch target. At tablet widths the informational links collapse so the play action fits. |
| Underlined “Probar un caso aquí” beside the App Store button | Outlined “Jugar gratis en la web” button, distinguishing the browser destination. The preview further down uses the same clear label. |
| No responsive play-button layout | Compact header spacing and brand type at 320 px; explicit hover, pressed, keyboard focus and reduced-motion states. |

`content/demo-copy.json` supplies both labels; `scripts/build_demo.py` regenerates the header, hero and preview links idempotently. The App Store CTA and game behavior are unchanged. Existing five tests and the full static release verifier pass. Browser checks confirm header-to-initialized-game navigation in all five languages at 320 px, ES390 visual layout, EN1280 desktop and EN768 tablet layout, and hero navigation with Enter. Public checks are recorded in workspace `docs/aso/donalupa-demo-entry-2026-09-13`.
