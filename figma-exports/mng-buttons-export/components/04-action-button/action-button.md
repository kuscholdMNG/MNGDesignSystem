---
name: Action Button
kind: component
order: 4
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Action Button
figma_node: "7075:6357"
component_key: f2d61dd8cfa1619da4987e7b90ac60f2fbb6c102
variants: 4
breakpoints: [all (single size)]
built_from: [Icons]
built_into: []
spec_json: action-button.json
skeleton: action-button.html
exported: 2026-10-01
---

# Action Button

> Small icon + label utility action (documented example: "Copy Link"). No box at rest; a 1px black border appears on Hover/Pressed.

**Specification text from the Figma documentation frame** (verbatim, ` | ` separates text layers):

```text
Action Button
Last Updated: 2026.09.30
Components
UPDATED: 2026.09.30
Action Button
Updated: 2026.09.30
Default
Hover
Pressed
InFocus
Action Button
Updated: 2026.09.30
Copy Link
Action Button
Size: 97×34px outer, 95×32px content area
Corner Radius: 4px (radius/sm)
Padding: 8px all sides within the content area
Spacing between icon and label: 4px
Icon: 16px square, fixed to the left of the label
Text: Noto Sans Bold 12px, center align
Text Color: color/gray/min / #141414
Border: 
none by default; 
1px black border appears on Hover/Pressed; 
InFocus adds a 2px black focus ring, offset 1px outside the border

Note: This is a simplified, single-purpose reference derived from the shared "Button Action" library component (kept separate and unchanged so existing designs on other files aren't affected). That source component bundles many additional pre-built icon+label combinations as hidden layers within the same component — Resend Invitation, Link Copied, Share (Android/Apple/Unknown), Preview Most Recent, Save/Saved, Gift Article, Remove, Cancel, and Delete — none of which are exposed as pickable Figma variants there. This documented version isolates just the "Copy Link" example. To use a different label/icon, duplicate this component and swap its icon instance and label text.

Margin: not yet established for this component (unlike the CTA buttons' 8px min left/right margin) — flagging as an open spec gap.
States
Updated: 2026.09.30
Copy Link
Default — resting appearance. No border; icon and label only.
Copy Link
Hover — pointer is over the button; a 1px black border appears around the content area.
Copy Link
Pressed — same visual treatment as Hover. No distinct pressed color token exists yet.
Copy Link
InFocus — adds a 2px black focus ring, offset 1px outside the 1px border. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Action Button` · 7075:6357](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6357) · key `f2d61dd8cfa1619da4987e7b90ac60f2fbb6c102`
- Documentation frame: [7075:6715](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6715) · overview PNG: [previews/action-button--documentation.png](previews/action-button--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `Default` | [7075:6358](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6358) | `d527026b821c…` | 97×34 | [png](previews/action-button--default.png) |
| `Hover` | [7075:6415](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6415) | `b570062e77c4…` | 97×34 | [png](previews/action-button--hover.png) |
| `InFocus` | [7075:6464](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6464) | `e137200747fb…` | 97×34 | [png](previews/action-button--infocus.png) |
| `Pressed` | [7075:6513](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6513) | `4c6105826870…` | 97×34 | [png](previews/action-button--pressed.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| state | VARIANT | Default | Default, Hover, InFocus, Pressed |

## Where it is used

Scope: Local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **4**.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `Default` | 1 | 1 | — | — |
| `Hover` | 1 | 1 | — | — |
| `InFocus` | 1 | 1 | — | — |
| `Pressed` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint (97×34 outer, HUG). No Breakpoint property.
- Width hugs icon + label; swapping the label changes the width.

## Dependencies

**Built from:**

- Icons ([4693:5](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=4693-5)) ×8 — not in this export

Icon variants used: `content_copy` ×8.

**Built into:** nothing yet (standalone).

## Anatomy

Default variant `Default`:

- **state=Default** `COMPONENT` — 97×34, horizontal gap 1 pad 1/1/1/1, HUG×HUG, r5
  - **options** `FRAME` — 95×32, horizontal gap 8 pad 8/8/8/8, HUG×HUG, r4
    - **Sharing** `FRAME` — 79×16, vertical gap 8 pad 0/0/0/0, HUG×HUG
      - **Copy Link** `FRAME` — 79×16, horizontal gap 4 pad 0/0/0/0, HUG×HUG
        - **Icons** `INSTANCE` — 16×16, horizontal gap 8 pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy)
        - **Details** `TEXT` — 59×9, HUG×HUG, text color/gray/min, "Copy Link" Noto Sans Bold 12px align left
        - **Icons** `INSTANCE` *(hidden)* — 16×16, horizontal gap 8 pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy)

InFocus variant `InFocus` (focus-ring structure):

- **state=InFocus** `COMPONENT` — 97×34, horizontal gap 1 pad 1/1/1/1, HUG×HUG, r5, stroke color/gray/black, stroke 2 outside
  - **options** `FRAME` — 95×32, horizontal gap 8 pad 8/8/8/8, HUG×HUG, r4, stroke color/gray/black, stroke 1 inside
    - **Sharing** `FRAME` — 79×16, vertical gap 8 pad 0/0/0/0, HUG×HUG
      - **Copy Link** `FRAME` — 79×16, horizontal gap 4 pad 0/0/0/0, HUG×HUG
        - **Icons** `INSTANCE` — 16×16, horizontal gap 8 pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy)
        - **Details** `TEXT` — 59×9, HUG×HUG, text color/gray/min, "Copy Link" Noto Sans Bold 12px align left
        - **Icons** `INSTANCE` *(hidden)* — 16×16, horizontal gap 8 pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy)

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `Default` | 97×34 | HUG×HUG | horizontal, gap 1, pad 1/1/1/1 | 4 | — | — |
| `Hover` | 97×34 | HUG×HUG | horizontal, gap 1, pad 1/1/1/1 | 4 | — | — |
| `InFocus` | 97×34 | HUG×HUG | horizontal, gap 1, pad 1/1/1/1 | 4 | — | color/gray/black |
| `Pressed` | 97×34 | HUG×HUG | horizontal, gap 1, pad 1/1/1/1 | 4 | — | — |

*Values are for the variant root. Most families wrap the visible button in an inner frame; see Anatomy.*

## Typography

| Font | Weight | Size | Line height | Case | Decoration | Color token | Layers |
|---|---|---|---|---|---|---|---|
| Noto Sans | Bold | 12px | auto | — | — | color/gray/min | Details |

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/gray/min | #141414 | text on Details |
| color/gray/black | #000000 | stroke on options; stroke on state=InFocus |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **Single-purpose reference.** This set only documents "Copy Link". The shared "Button Action" library component (other files) bundles Resend Invitation, Link Copied, Share (Android/Apple/Unknown), Preview Most Recent, Save/Saved, Gift Article, Remove, Cancel and Delete as hidden layers, none exposed as variants. To render another action, swap the icon instance and the label text.
2. **Hidden trailing icon.** Every variant carries a second, hidden `Icons` (content_copy) instance after the label. It is never shown; ignore it when rendering.
3. **Margin not specified** (open spec gap, per the Figma Specifications column).
4. **4 variants are placed only in their own documentation frame** (not yet used in any real layout): `Default`, `Hover`, `InFocus`, `Pressed`.

## Rendering steps

1. Pick the variant from the Properties table (state comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `action-button.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the color tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Check against the preview PNG in `previews/`.
