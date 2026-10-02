---
name: Non-Button Hyperlink
kind: component
order: 8
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Hyperlink
figma_node: "6282:5568"
component_key: 121a469eea7d108efe028d82b734c60ffbbf6aab
variants: 4
breakpoints: [all (single size)]
built_from: []
built_into: [InLineMessage]
spec_json: non-button-hyperlink.json
skeleton: non-button-hyperlink.html
exported: 2026-10-02
---

# Non-Button Hyperlink

> Plain in-text hyperlink (not a button). Brand-primary text with a 1px bottom border: dashed at rest, solid on Hover/Pressed, 2px teal box on InFocus. Figma set name: `Hyperlink`.

**Specification text from the Figma documentation frame** (verbatim, one text layer per line):

```text
Non-Button Hyperlink
Last Updated: 2026.10.02
Components
UPDATED: 2026.09.30
Non-Button Hyperlink
Updated: 2026.09.30
Default
Hover
Pressed
InFocus
Non-Button Hyperlink
Default — dashed teal underline (subtle at normal reading size); cursor is a plain pointer, not yet over the link.
Hover — underline becomes solid teal; cursor changes to a hand pointer, confirming it reads as interactive.
Non-Button Hyperlink
Updated: 2026.09.30
Non-Button Hyperlink

Size: hugs to its text content — no fixed box, no padding chrome

Text: Noto Sans Regular 16.5px

Text Color: color/theme/primary / #007580 in every state — does not shift

Underline: not text-decoration — implemented as a bottom border instead. Default: 1px dashed teal (very subtle at normal size, reads as almost invisible). Hover: 1px solid teal. Pressed: matches Hover exactly (1px solid teal). InFocus: adds a 2px solid teal box border, corner radius 4px, around the whole link

InFocus also keeps the inner 1px dashed teal underline inside the box border (a slightly heavier bottom edge). This matches production and is intentional (Karl, 2026-10-02).

Focus ring color: teal (color/theme/primary), not the black ring used on the button families. This matches production and is intentional for plain text links, as is the 16.5px text size (Karl, 2026-10-02).
States
Updated: 2026.09.30
Default — resting appearance. Teal text with a barely-visible 1px dashed teal underline.
Hover — the underline becomes a solid 1px teal line.
Pressed — matches Hover exactly (solid 1px teal underline). No separate pressed-only styling.
InFocus — adds a 2px solid teal box border (4px corner radius) around the whole link, plus still shows the inner dashed underline nested inside it. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Hyperlink` · 6282:5568](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5568) · key `121a469eea7d108efe028d82b734c60ffbbf6aab`
- Documentation frame: [7078:8121](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-8121) · overview PNG: [previews/non-button-hyperlink--documentation.png](previews/non-button-hyperlink--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `Default` | [6282:5569](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5569) | `fd7b8e9029b1…` | 133×23 | [png](previews/non-button-hyperlink--default.png) |
| `Hover` | [6282:5577](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5577) | `e139df490024…` | 133×23 | [png](previews/non-button-hyperlink--hover.png) |
| `Pressed` | [7078:7681](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7681) | `e95a7c55f26a…` | 133×23 | [png](previews/non-button-hyperlink--pressed.png) |
| `InFocus` | [6282:5585](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5585) | `ad4861554ebf…` | 133×25 | [png](previews/non-button-hyperlink--infocus.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| State | VARIANT | Default | Default, Hover, InFocus, Pressed |

## Where it is used

Scope: local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **8**.

Nested inside (component sets / components): InLineMessage ×3.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `Default` | 4 | 1 | InLineMessage ×3 | — |
| `Hover` | 2 | 2 | — | — |
| `Pressed` | 1 | 1 | — | — |
| `InFocus` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Hugs its text at every breakpoint. No Breakpoint property.
- Implement the underline as `border-bottom`, not `text-decoration` (that is how Figma builds it).
- **Intentional, matches production (Karl, 2026-10-02):** 16.5px text, a teal (color/theme/primary) 2px focus box with 4px corners instead of the black ring, and the dashed underline kept inside the InFocus box (`Underline` › `Label`). Because the focus box is part of the layout, InFocus is 2px taller (25 vs 23px). Do not "fix" these.

## Dependencies

**Built from:**

- nothing (no nested components).

**Built into:** InLineMessage

## Anatomy

Every variant in the set has the same layer tree; InFocus only adds the `Focus Ring` frame. Hidden layers are marked.

Default variant `Default`:

- **State=Default** `COMPONENT` — 133×23, horizontal, gap 0, pad 0/0/1/0, HUG×HUG, stroke color/theme/primary, 0/0/1/0 center dashed
  - **Label** `TEXT` — 133×22, HUG×HUG, "...hyperlink text..." Noto Sans Regular 16.5px, align right

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT` — 133×25, horizontal, gap 0, pad 0/0/2/0, HUG×HUG, r4, stroke color/theme/primary, 2 center
  - **Underline** `FRAME` — 133×23, horizontal, gap 0, pad 0/0/1/0, HUG×HUG, stroke color/theme/primary, 0/0/1/0 center dashed
    - **Label** `TEXT` — 133×22, HUG×HUG, "...hyperlink text..." Noto Sans Regular 16.5px, align right

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `Default` | 133×23 | HUG×HUG | horizontal, gap 0, pad 0/0/1/0 | — | — | color/theme/primary |
| `Hover` | 133×23 | HUG×HUG | horizontal, gap 0, pad 0/0/1/0 | — | — | color/theme/primary |
| `Pressed` | 133×23 | HUG×HUG | horizontal, gap 0, pad 0/0/1/0 | — | — | color/theme/primary |
| `InFocus` | 133×25 | HUG×HUG | horizontal, gap 0, pad 0/0/2/0 | 4 | — | color/theme/primary |

*Values are for the variant root.*

## Typography

| Font | Weight | Size | Line height | Case | Color | Align | Layers |
|---|---|---|---|---|---|---|---|
| Noto Sans | Regular | 16.5px | auto | — | color/theme/primary | right | Label |

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/theme/primary | #007580 | stroke on State=Default; stroke on State=Hover; stroke on State=InFocus; stroke on State=Pressed; stroke on Underline; text on Label |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `Hover`, `Pressed`, `InFocus`.

## Rendering steps

1. Pick the variant from the Properties table (State comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `non-button-hyperlink.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. No nested components to resolve.
5. Draw the focus ring outside the element so it never changes layout (see Responsive rules).
6. Check against the preview PNG in `previews/`.
