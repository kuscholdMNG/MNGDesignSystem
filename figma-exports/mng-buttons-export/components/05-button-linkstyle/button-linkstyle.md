---
name: Button Linkstyle
kind: component
order: 5
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Button Linkstyle
figma_node: "5428:3953"
component_key: f2989bf6601dd76f26f1ecd1ee39d25551450390
variants: 8
breakpoints: [all (single size)]
built_from: []
built_into: [Modals, InLineMessage, Form Field, ModalsCenter]
spec_json: button-linkstyle.json
skeleton: button-linkstyle.html
exported: 2026-10-01
---

# Button Linkstyle

> Text-link styled button (used for disclosures and inline CTAs such as "Forgot password?"). Underlined brand-primary text at rest; a 1px brand-primary box appears on Hover/Pressed.

**Specification text from the Figma documentation frame** (verbatim, ` | ` separates text layers):

```text
Button Linkstyle
Last Updated: 2026.09.30
Components
UPDATED: 2026.09.30
Button Linkstyle
Updated: 2026.09.30
1row
stacked
Default
Hover
Pressed
InFocus
Button Linkstyle
Updated: 2026.09.30
Right Text Element
Button Linkstyle
Size: 157×38px (1row) / 91×60px (stacked)
Corner Radius: 4px (Hover, Pressed, and InFocus box states only; Default has no box)
Padding: 8px all sides
Text: Noto Sans Regular 16px
Text Color: color/theme/primary / #007580
Border: none by default (underlined text instead); 1px color/theme/primary border appears on Hover/Pressed (underline removed); InFocus adds a 2px black focus ring, offset 1px outside, plus the 1px Hover-style border

Margin: not yet established for this component (unlike the CTA buttons' 8px min left/right margin) — flagging as an open spec gap.
States
Updated: 2026.09.30
Right Text Element
Default — resting appearance. Underlined text, no box border.
Right Text Element
Hover — underline is removed; a 1px color/theme/primary border appears around the content area, corner radius 4px.
Right Text Element
Pressed — same styling as Hover (1px color/theme/primary border, corner radius 4px). Now its own separate variant rather than combined with Hover.
Right Text Element
InFocus — adds a 2px black focus ring, offset 1px outside, in addition to the 1px Hover-style border. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button Linkstyle` · 5428:3953](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3953) · key `f2989bf6601dd76f26f1ecd1ee39d25551450390`
- Documentation frame: [7075:7436](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-7436) · overview PNG: [previews/button-linkstyle--documentation.png](previews/button-linkstyle--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `1row / Default` | [5428:3880](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3880) | `20acea4b24fb…` | 157×38 | [png](previews/button-linkstyle--1row-default.png) |
| `stacked / Default` | [5428:3881](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3881) | `f2026049dee6…` | 91×60 | [png](previews/button-linkstyle--stacked-default.png) |
| `1row / Hover` | [5428:3882](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3882) | `b8943c851fa8…` | 157×38 | [png](previews/button-linkstyle--1row-hover.png) |
| `stacked / Hover` | [5428:3883](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3883) | `e75af993aad5…` | 91×60 | [png](previews/button-linkstyle--stacked-hover.png) |
| `1row / InFocus` | [5428:3884](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3884) | `f5f60e210621…` | 159×40 | [png](previews/button-linkstyle--1row-infocus.png) |
| `stacked / InFocus` | [5428:3885](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3885) | `0b3538efc5f7…` | 93×62 | [png](previews/button-linkstyle--stacked-infocus.png) |
| `1row / Pressed` | [7078:7616](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7616) | `5bb9e219c8ed…` | 157×38 | [png](previews/button-linkstyle--1row-pressed.png) |
| `stacked / Pressed` | [7078:7620](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7620) | `b3891886f3fd…` | 91×60 | [png](previews/button-linkstyle--stacked-pressed.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| style | VARIANT | 1row | stacked, 1row |
| state | VARIANT | Default | Default, Pressed, InFocus, Hover |

## Where it is used

Scope: Local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **71**.

Nested inside (component sets / components): InLineMessage ×15, Modals ×14, ModalsCenter ×12, Form Field ×6.

Placed directly on pages: Modal Panels | 2025.12.29 ×14, In-Line Content Containers | 2026.01.02 ×3.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `1row / Default` | 68 | 4 | 47 | In-Line Content Containers \| 2026.01.02 ▸ Frame 8 ×3, Modal Panels \| 2025.12.29 ▸ Frame 12995 ×12, Modal Panels \| 2025.12.29 ▸ Frame 12672 ×2 |
| `stacked / Default` | 0 | 0 | — | — |
| `1row / Hover` | 1 | 1 | — | — |
| `stacked / Hover` | 0 | 0 | — | — |
| `1row / InFocus` | 1 | 1 | — | — |
| `stacked / InFocus` | 0 | 0 | — | — |
| `1row / Pressed` | 1 | 1 | — | — |
| `stacked / Pressed` | 0 | 0 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint. No Breakpoint property.
- `style=1row` keeps the label on one line (157×38 with sample text). `style=stacked` fixes the text width at 75px so the label wraps to two lines (91×60), for narrow right-aligned slots.

## Dependencies

**Built from:**


**Built into:** Modals, InLineMessage, Form Field, ModalsCenter

## Anatomy

Default variant `1row / Default`:

- **style=1row, state=Default** `COMPONENT` — 157×38, horizontal gap 8 pad 8/8/8/8, HUG×HUG
  - **Right Text Element** `TEXT` — 141×22, HUG×HUG, text color/theme/primary, "Right Text Element" Noto Sans Regular 16px underline align right

InFocus variant `1row / InFocus` (focus-ring structure):

- **style=1row, state=InFocus** `COMPONENT` — 159×40, horizontal gap 8 pad 1/1/1/1, HUG×HUG, r4, stroke color/gray/black, stroke 2 outside
  - **Frame 12966** `FRAME` — 157×38, horizontal gap 8 pad 8/8/8/8, HUG×HUG, r4, stroke color/theme/primary, stroke 1 inside
    - **Right Text Element** `TEXT` — 141×22, HUG×HUG, text color/theme/primary, "Right Text Element" Noto Sans Regular 16px align right

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `1row / Default` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | — | — | — |
| `stacked / Default` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | — | — | — |
| `1row / Hover` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `stacked / Hover` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `1row / InFocus` | 159×40 | HUG×HUG | horizontal, gap 8, pad 1/1/1/1 | 4 | — | color/gray/black |
| `stacked / InFocus` | 93×62 | HUG×HUG | horizontal, gap 8, pad 1/1/1/1 | 4 | — | color/gray/black |
| `1row / Pressed` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `stacked / Pressed` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |

*Values are for the variant root. Most families wrap the visible button in an inner frame; see Anatomy.*

## Typography

| Font | Weight | Size | Line height | Case | Decoration | Color token | Layers |
|---|---|---|---|---|---|---|---|
| Noto Sans | Regular | 16px | auto | — | UNDERLINE | color/theme/primary | Right Text Element |
| Noto Sans | Regular | 16px | auto | — | — | color/theme/primary | Right Text Element |

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/theme/primary | #007580 | stroke on Frame 12966; stroke on Frame 12967; stroke on style=1row, state=Hover; stroke on style=1row, state=Pressed; stroke on style=stacked, state=Hover; stroke on style=stacked, state=Pressed; text on Right Text Element |
| color/gray/black | #000000 | stroke on style=1row, state=InFocus; stroke on style=stacked, state=InFocus |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **Text is right-aligned in every variant** (layer name "Right Text Element"). Confirm this is intended for left-aligned uses.
2. **Margin not specified** (open spec gap, per the Figma Specifications column).
3. **4 of 8 variants have 0 instances** anywhere in the file: `stacked / Default`, `stacked / Hover`, `stacked / InFocus`, `stacked / Pressed`.
4. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `1row / Hover`, `1row / InFocus`, `1row / Pressed`.

## Rendering steps

1. Pick the variant from the Properties table (state comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `button-linkstyle.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the color tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Check against the preview PNG in `previews/`.
