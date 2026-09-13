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
