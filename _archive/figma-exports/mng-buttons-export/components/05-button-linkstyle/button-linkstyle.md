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
built_into: [Form Field, InLineMessage, Modals, ModalsCenter]
spec_json: button-linkstyle.json
skeleton: button-linkstyle.html
exported: 2026-10-02
---

# Button Linkstyle

> Text-link styled button (used for disclosures and inline CTAs such as "Forgot password?"). Underlined brand-primary text at rest; a 1px brand-primary box appears on Hover/Pressed.

**Specification text from the Figma documentation frame** (verbatim, one text layer per line):

```text
Button Linkstyle
Last Updated: 2026.10.02
Components
UPDATED: 2026.09.30
Button Linkstyle
Updated: 2026.09.30
1 Row
Stacked
Default
Hover
Pressed
InFocus
Button Linkstyle
Updated: 2026.09.30
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
Default — resting appearance. Underlined text, no box border.
Hover — underline is removed; a 1px color/theme/primary border appears around the content area, corner radius 4px.
Pressed — same styling as Hover (1px color/theme/primary border, corner radius 4px). Now its own separate variant rather than combined with Hover.
InFocus — adds a 2px black focus ring, offset 1px outside, in addition to the 1px Hover-style border. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button Linkstyle` · 5428:3953](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3953) · key `f2989bf6601dd76f26f1ecd1ee39d25551450390`
- Documentation frame: [7075:7436](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-7436) · overview PNG: [previews/button-linkstyle--documentation.png](previews/button-linkstyle--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `1 Row / Default` | [5428:3880](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3880) | `20acea4b24fb…` | 157×38 | [png](previews/button-linkstyle--1-row-default.png) |
| `1 Row / Hover` | [5428:3882](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3882) | `b8943c851fa8…` | 157×38 | [png](previews/button-linkstyle--1-row-hover.png) |
| `1 Row / Pressed` | [7078:7616](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7616) | `5bb9e219c8ed…` | 157×38 | [png](previews/button-linkstyle--1-row-pressed.png) |
| `1 Row / InFocus` | [5428:3884](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3884) | `f5f60e210621…` | 157×38 | [png](previews/button-linkstyle--1-row-infocus.png) |
| `Stacked / Default` | [5428:3881](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3881) | `f2026049dee6…` | 91×60 | [png](previews/button-linkstyle--stacked-default.png) |
| `Stacked / Hover` | [5428:3883](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3883) | `e75af993aad5…` | 91×60 | [png](previews/button-linkstyle--stacked-hover.png) |
| `Stacked / Pressed` | [7078:7620](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7620) | `b3891886f3fd…` | 91×60 | [png](previews/button-linkstyle--stacked-pressed.png) |
| `Stacked / InFocus` | [5428:3885](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5428-3885) | `0b3538efc5f7…` | 91×60 | [png](previews/button-linkstyle--stacked-infocus.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Style | VARIANT | 1 Row | 1 Row, Stacked |
| State | VARIANT | Default | Default, Hover, InFocus, Pressed |

## Where it is used

Scope: local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **71**.

Nested inside (component sets / components): InLineMessage ×15, Modals ×14, ModalsCenter ×12, Form Field ×6.

Placed directly on pages: Modal Panels | 2025.12.29 ×14, In-Line Content Containers | 2026.01.02 ×3, Buttons | 2026.09.30 ×2.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `1 Row / Default` | 68 | 2 | Modals/Desktop ×2, Form Field ×6, InLineMessage/Desktop/none/StandAloneEmailPrefs/Panel ×6, Modals/Mobile/Login ×2, InLineMessage/FOLD/none/StandAloneEmailPrefs/Panel ×6, Modals/Desktop/Login ×2, Modals/TabletV/Login ×2, ModalsCenter ×12, InLineMessage ×3, Modals/TabletH/Login ×2, Modals/FOLD/Login ×2, Modals/MobileScroll/Login ×2 | Buttons \| 2026.09.30 ▸ Pop-Up Modal Close — Documentation ×2, Modal Panels \| 2025.12.29 ▸ Frame 12995 ×12, In-Line Content Containers \| 2026.01.02 ▸ Frame 8 ×3, Modal Panels \| 2025.12.29 ▸ Frame 12672 ×2 |
| `1 Row / Hover` | 1 | 1 | — | — |
| `1 Row / Pressed` | 1 | 1 | — | — |
| `1 Row / InFocus` | 1 | 1 | — | — |
| `Stacked / Default` | 0 | 0 | — | — |
| `Stacked / Hover` | 0 | 0 | — | — |
| `Stacked / Pressed` | 0 | 0 | — | — |
| `Stacked / InFocus` | 0 | 0 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint. No Breakpoint property. It stays compact (38px with one line), not 40px (Karl, 2026-10-02).
- `Style=1 Row` keeps the label on one line (157×38 with sample text). `Style=Stacked` fixes the text width at 75px so the label wraps to two lines (91×60), for narrow right-aligned slots.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (a 40px button reads as 46px with the ring). In CSS: `outline: 2px solid var(--color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Dependencies

**Built from:**

- nothing (no nested components).

**Built into:** Form Field, InLineMessage, Modals, ModalsCenter

## Anatomy

Every variant in the set has the same layer tree; InFocus only adds the `Focus Ring` frame. Hidden layers are marked.

Default variant `1 Row / Default`:

- **Style=1 Row, State=Default** `COMPONENT` — 157×38, horizontal, gap 8, pad 8/8/8/8, HUG×HUG
  - **Label** `TEXT` — 141×22, HUG×HUG, "Right Text Element" Noto Sans Regular 16px, align right

InFocus variant `1 Row / InFocus`:

- **Style=1 Row, State=InFocus** `COMPONENT` — 157×38, horizontal, gap 8, pad 8/8/8/8, HUG×HUG, r4 (radius/sm), stroke color/theme/primary, 1 inside
  - **Label** `TEXT` — 141×22, HUG×HUG, "Right Text Element" Noto Sans Regular 16px, align right
  - **Focus Ring** `FRAME` — 159×40, FIXED×FIXED, absolute at -1,-1, r4 (radius/sm), stroke color/gray/black, 2 outside

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `1 Row / Default` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | — | — | — |
| `1 Row / Hover` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `1 Row / Pressed` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `1 Row / InFocus` | 157×38 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 (radius/sm) | — | color/theme/primary |
| `Stacked / Default` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | — | — | — |
| `Stacked / Hover` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `Stacked / Pressed` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 | — | color/theme/primary |
| `Stacked / InFocus` | 91×60 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 (radius/sm) | — | color/theme/primary |

*Values are for the variant root.*

## Typography

| Font | Weight | Size | Line height | Case | Color | Align | Layers |
|---|---|---|---|---|---|---|---|
| Noto Sans | Regular | 16px | auto | — | color/theme/primary | right | Label |

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/theme/primary | #007580 | stroke on Style=1 Row, State=Hover; stroke on Style=1 Row, State=InFocus; stroke on Style=1 Row, State=Pressed; stroke on Style=Stacked, State=Hover; stroke on Style=Stacked, State=InFocus; stroke on Style=Stacked, State=Pressed; text on Label |
| color/gray/black | #000000 | stroke on Focus Ring |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **Margin not specified** (open spec gap, per the Figma Specifications column).
2. **4 of 8 variants have 0 instances** anywhere in the file: `Stacked / Default`, `Stacked / Hover`, `Stacked / Pressed`, `Stacked / InFocus`.
3. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `1 Row / Hover`, `1 Row / Pressed`, `1 Row / InFocus`.

## Rendering steps

1. Pick the variant from the Properties table (State comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `button-linkstyle.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. No nested components to resolve.
5. Draw the focus ring outside the element so it never changes layout (see Responsive rules).
6. Check against the preview PNG in `previews/`.
