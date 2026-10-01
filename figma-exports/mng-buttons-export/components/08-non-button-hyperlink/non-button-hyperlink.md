---
name: Non-Button Hyperlink
kind: component
order: 8
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: nonButton Hyperlink
figma_node: "6282:5568"
component_key: 121a469eea7d108efe028d82b734c60ffbbf6aab
variants: 4
breakpoints: [all (single size)]
built_from: []
built_into: [InLineMessage]
spec_json: non-button-hyperlink.json
skeleton: non-button-hyperlink.html
exported: 2026-10-01
---

# Non-Button Hyperlink

> Plain in-text hyperlink (not a button). Brand-primary text with a 1px bottom border: dashed at rest, solid on Hover/Pressed, 2px teal box on InFocus.

**Specification text from the Figma documentation frame** (verbatim, ` | ` separates text layers):

```text
Non-Button Hyperlink
Last Updated: 2026.09.30
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
...hyperlink text...
Non-Button Hyperlink

Size: hugs to its text content — no fixed box, no padding chrome

Text: Noto Sans Regular 16.5px

Text Color: color/theme/primary / #007580 in every state — does not shift

Underline: not text-decoration — implemented as a bottom border instead. Default: 1px dashed teal (very subtle at normal size, reads as almost invisible). Hover: 1px solid teal. Pressed: matches Hover exactly (1px solid teal). InFocus: adds a 2px solid teal box border, corner radius 4px, around the whole link

InFocus also still carries the inner 1px dashed teal underline nested inside the box border (visible as a slightly heavier bottom edge) — likely a leftover from how Default's structure was reused rather than an intentional double-border. Flagging rather than cleaning it up silently.

Focus ring color: teal (color/theme/primary), not the black focus ring used on every other button family — worth confirming this is intentional for plain text links.
States
Updated: 2026.09.30
...hyperlink text...
Default — resting appearance. Teal text with a barely-visible 1px dashed teal underline.
...hyperlink text...
Hover — the underline becomes a solid 1px teal line.
...hyperlink text...
Pressed — matches Hover exactly (solid 1px teal underline). No separate pressed-only styling.
...hyperlink text...
InFocus — adds a 2px solid teal box border (4px corner radius) around the whole link, plus still shows the inner dashed underline nested inside it. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`nonButton Hyperlink` · 6282:5568](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5568) · key `121a469eea7d108efe028d82b734c60ffbbf6aab`
- Documentation frame: [7078:8121](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-8121) · overview PNG: [previews/non-button-hyperlink--documentation.png](previews/non-button-hyperlink--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `Default` | [6282:5569](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5569) | `fd7b8e9029b1…` | 133×23 | [png](previews/non-button-hyperlink--default.png) |
| `Hover` | [6282:5577](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5577) | `e139df490024…` | 133×23 | [png](previews/non-button-hyperlink--hover.png) |
| `InFocus` | [6282:5585](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6282-5585) | `ad4861554ebf…` | 133×25 | [png](previews/non-button-hyperlink--infocus.png) |
| `Pressed` | [7078:7681](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7681) | `e95a7c55f26a…` | 133×23 | [png](previews/non-button-hyperlink--pressed.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| state | VARIANT | Default | Default, Hover, InFocus, Pressed |

## Where it is used

Scope: Local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **8**.

Nested inside (component sets / components): InLineMessage ×3.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `Default` | 4 | 1 | 3 | — |
| `Hover` | 2 | 2 | — | — |
| `InFocus` | 1 | 1 | — | — |
| `Pressed` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Hugs its text at every breakpoint. No Breakpoint property.
- Implement the underline as `border-bottom`, not `text-decoration` (that is how Figma builds it).

## Dependencies

**Built from:**


**Built into:** InLineMessage

## Anatomy

Default variant `Default`:

- **state=Default** `COMPONENT` — 133×23, horizontal gap 0 pad 0/0/1/0, HUG×HUG, stroke color/theme/primary, stroke [0, 0, 1, 0] center dashed
  - **...hyperlink text...** `TEXT` — 133×22, HUG×HUG, text color/theme/primary, "...hyperlink text..." Noto Sans Regular 16.5px align right

InFocus variant `InFocus` (focus-ring structure):

- **state=InFocus** `COMPONENT` — 133×25, horizontal gap 0 pad 0/0/2/0, HUG×HUG, r4, stroke color/theme/primary, stroke 2 center
  - **Frame 12966** `FRAME` — 133×23, horizontal gap 0 pad 0/0/1/0, HUG×HUG, stroke color/theme/primary, stroke [0, 0, 1, 0] center dashed
    - **...hyperlink text...** `TEXT` — 133×22, HUG×HUG, text color/theme/primary, "...hyperlink text..." Noto Sans Regular 16.5px align right

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `Default` | 133×23 | HUG×HUG | horizontal, gap 0, pad 0/0/1/0 | — | — | color/theme/primary |
| `Hover` | 133×23 | HUG×HUG | horizontal, gap 0, pad 0/0/1/0 | — | — | color/theme/primary |
| `InFocus` | 133×25 | HUG×HUG | horizontal, gap 0, pad 0/0/2/0 | 4 | — | color/theme/primary |
| `Pressed` | 133×23 | HUG×HUG | horizontal, gap 0, pad 0/0/1/0 | — | — | color/theme/primary |

*Values are for the variant root. Most families wrap the visible button in an inner frame; see Anatomy.*

## Typography

| Font | Weight | Size | Line height | Case | Decoration | Color token | Layers |
|---|---|---|---|---|---|---|---|
| Noto Sans | Regular | 16.5px | auto | — | — | color/theme/primary | ...hyperlink text... |

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/theme/primary | #007580 | stroke on Frame 12966; stroke on state=Default; stroke on state=Hover; stroke on state=InFocus; stroke on state=Pressed; text on ...hyperlink text... |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **Font size 16.5px** is off the type scale (every other family uses 16px or 12px). Likely should be `font/size/16`.
2. **Teal focus ring** (color/theme/primary) instead of the black ring every other family uses. Flagged in Figma as "worth confirming".
3. **InFocus keeps the dashed underline** inside the 2px box border, likely left over from copying Default. Flagged in Figma, not cleaned up.
4. **Text is right-aligned** in every variant (no effect when hugging, but it matters if the frame is stretched).
5. **Figma set name differs from the doc title**: the component set is `nonButton Hyperlink`.
6. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `Hover`, `InFocus`, `Pressed`.

## Rendering steps

1. Pick the variant from the Properties table (state comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `non-button-hyperlink.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the color tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Check against the preview PNG in `previews/`.
