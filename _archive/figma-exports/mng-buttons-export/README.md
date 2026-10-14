# Buttons and links: MNG Design System export

**Exported 2026-10-02** from the **Buttons | 2026.09.30** page. It reflects Karl's 2026-10-02 review: 40px CTAs, focus rings drawn outside the element, the set renames and the layer-name cleanup. It replaces the 2026-10-01 export.

This is a portable, AI-readable spec export from the **MNG Design System** Figma file (`jFHYqhZbJjvWQmDI4myCsd`), page [Buttons | 2026.09.30](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=1079-34282). It holds 8 component sets with 96 variants in total. Design (Figma) is the source of truth. Values here are design values, not production values.

## How an agent should use this folder

1. Read `index.json` first. It lists the 8 components in order, with paths to every file.
2. For context (description, the verbatim Figma spec text, where it's used, known issues), read the component's `.md`.
3. For exact data (hex and token per layer, sizes, per-variant layer trees, usage counts), read the `.json` twin (`schema: mng-design-system/component-spec@1`).
4. To see the structure rendered, open the `.html` skeleton. It has one `<section>` per variant and uses `tokens.css`. Compare it with the PNGs in `previews/`: one per variant at 2×, plus `<slug>--documentation.png`, the whole Figma documentation frame at 0.5×.
5. Always use the **tokens** (`var(--color-theme-primary)`, `var(--radius-sm)` and so on), never the hex. Theme colors change per site.

## Components (build order)

| # | Component | Figma set name | Node | Variants | Breakpoints | Instances in file | Built from | Built into |
|---|---|---|---|---|---|---|---|---|
| 01 | [Button Primary](components/01-button-primary/button-primary.md) | Button Primary | `5328:15928` | 24 | Desktop, Mobile | 111 | Icons | InLineMessage, Modals, ModalsCenter, Page Body Templates, ReaderDash Tempates |
| 02 | [Button Secondary](components/02-button-secondary/button-secondary.md) | Button Secondary | `5333:16013` | 24 | Mobile, Desktop | 4 | Icons | — |
| 03 | [Button Tertiary](components/03-button-tertiary/button-tertiary.md) | Button Tertiary | `5333:16089` | 24 | Desktop, Mobile | 18 | Icons | InLineMessage |
| 04 | [Action Button](components/04-action-button/action-button.md) | Button Action | `7075:6357` | 4 | single size | 4 | Icons | — |
| 05 | [Button Linkstyle](components/05-button-linkstyle/button-linkstyle.md) | Button Linkstyle | `5428:3953` | 8 | single size | 71 | — | Form Field, InLineMessage, Modals, ModalsCenter |
| 06 | [Pop-Up Modal Close](components/06-pop-up-modal-close/pop-up-modal-close.md) | Button Modal Close | `5335:16196` | 4 | single size | 26 | Icons | Modals, ModalsCenter |
| 07 | [In-Line Close](components/07-in-line-close/in-line-close.md) | Button In-Line Close | `5335:16200` | 4 | single size | 100 | Icons | InLineMessage, ModalsOffset |
| 08 | [Non-Button Hyperlink](components/08-non-button-hyperlink/non-button-hyperlink.md) | Hyperlink | `6282:5568` | 4 | single size | 8 | — | InLineMessage |

The component name is the documentation-frame title; the Figma set name is what you search for in the Assets panel. Note the 2026-10-02 swap: the documented utility button is the set **`Button Action`**, and the older library set on the same page (`5417:3876`, used by Reader Dashboard files) is **`Action Button`**. That older set is not in this export.

All 8 are leaf components: none is built from another one in this export. The only dependency is the shared **Icons** set (`4693:5`), which isn't in this export. Instance counts cover this file only; library instances in WordPress Elements and Reader Dashboard v2.0 aren't counted.

```mermaid
flowchart LR
  Icons(["Icons 4693:5 (not exported)"])
  P[Button Primary] & S[Button Secondary] & T[Button Tertiary] & AB[Action Button] & MC[Pop-Up Modal Close] & IC[In-Line Close] --> Icons
  LS[Button Linkstyle]
  HL[Non-Button Hyperlink]
  P --> ILM[[InLineMessage]] & MOD[[ModalsCenter / Modals]]
  T --> ILM
  LS --> MOD & ILM & FF[[Form Field]]
  MC --> MOD
  IC --> ILM & MO[[ModalsOffset]]
  HL --> ILM
```

## Layer structure

Every variant in a set has the same layer tree, so text and icon overrides carry across variant swaps. InFocus adds only a `Focus Ring` frame.

| Family | Layers |
|---|---|
| Primary, Secondary, Tertiary | variant root (8px side margin) › `Button` › `Content` › `Icon Left` / `Label` / `Icon Right` |
| Action Button (`Button Action`) | `Button` › `Content` › `Icon Left` / `Label` / `Icon Right` (hidden) |
| Button Linkstyle | `Label` |
| Pop-Up Modal Close | `Icon` |
| In-Line Close | `Button` › `Box` › `Icon` |
| Non-Button Hyperlink | `Label` (InFocus: `Underline` › `Label`) |

## States (shared by all families)

- **Default:** resting appearance.
- **Hover:** pointer over the button. The fill or border changes to the family's hover token.
- **Pressed:** mouse down or tap. It's currently the same as Hover everywhere, because no pressed token exists yet.
- **InFocus:** keyboard focus. The Default look plus a 2px `color/gray/black` focus ring, 1px outside the element. The ring never changes the component's size or moves anything (a 40px button reads as 46px with the ring). The exception is Non-Button Hyperlink: its teal 2px focus box is part of the layout, which matches production and is intentional.

## Breakpoints

Only the three CTA families (Primary, Secondary, Tertiary) have a `Breakpoint` property:

| Value | Viewport (export convention) | Behavior |
|---|---|---|
| Desktop | ≥640px (768, 1024, 1100 and 1280 templates) | The button hugs its label and icon. Gap in a row or stack is 16px. |
| Mobile | ≤639px (340 XS-Fold and 360 SM-Mobile templates) | The button fills the container with an 8px side margin. Stacked gap is 8px. |

The other five families are a single size at every viewport.

## Sizes

- **CTAs:** 40px tall in every state: 8px top/bottom padding (`spacing/100`), 16px left/right (`spacing/200`), 40px min-height so a wrapped label can grow. 16px icons. 4px corners (`radius/sm`).
- **Action Button:** 95×32 (compact by design), 16px icon. **Linkstyle:** 38px for one line (compact by design). **Modal Close:** 32×32 circle, 12px icon. **In-Line Close:** 40×40 hit area, 28px box, 12px icon.

## Tokens summary

Colors (default mode, see `tokens.json` and `tokens.css`): `color/gray/400` #A7A6A3, `color/gray/500` #CCCAC7, `color/gray/600` #F1EFEB, `color/gray/black` #000000, `color/gray/max` #FFFFFF, `color/gray/min` #141414, `color/theme/primary` #007580, `color/theme/primary-dark` #0A5962, `color/theme/primary-light` #00838F. Every color in the 8 sets is bound to a variable. Radius and spacing are bound to `radius/sm` (4px), `spacing/100` (8px) and `spacing/200` (16px).

Type: Noto Sans only. CTA buttons use Bold 16px Title Case. Action Button uses Bold 12px. Linkstyle uses Regular 16px. Hyperlink uses Regular 16.5px (matches production).

## Known issues

Each component's `.md` lists its own under **Known issues**. The open ones across the page:

- **Margin not specified** for Action Button, Linkstyle, Modal Close and In-Line Close (open spec gap in Figma).
- **Low adoption:** most Hover, Pressed, InFocus, Mobile and icon variants appear only in their documentation frame, or nowhere. The stacked Linkstyle variants and the Action Button aren't used anywhere yet.

## Folder layout

```
mng-buttons-export/
  README.md  index.json  tokens.json  tokens.css
  components/
    01-button-primary/       button-primary.md  .json  .html  previews/ (24 variants + documentation)
    02-button-secondary/     button-secondary.md  .json  .html  previews/ (24 variants + documentation)
    03-button-tertiary/      button-tertiary.md  .json  .html  previews/ (24 variants + documentation)
    04-action-button/        action-button.md  .json  .html  previews/ (4 variants + documentation)
    05-button-linkstyle/     button-linkstyle.md  .json  .html  previews/ (8 variants + documentation)
    06-pop-up-modal-close/   pop-up-modal-close.md  .json  .html  previews/ (4 variants + documentation)
    07-in-line-close/        in-line-close.md  .json  .html  previews/ (4 variants + documentation)
    08-non-button-hyperlink/ non-button-hyperlink.md  .json  .html  previews/ (4 variants + documentation)
```

Not included: the Icons set, the older `Action Button` / `Button ActionMenu` / `Button Pay` / social and save button sets on the same page, and page templates.
