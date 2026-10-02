---
name: In-Line Close
kind: component
order: 7
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Button In-Line Close
figma_node: "5335:16200"
component_key: f0d7dc9ffa766ef6e54c1d46416a37d1405acaa6
variants: 4
breakpoints: [all (single size)]
built_from: [Icons]
built_into: [InLineMessage, ModalsOffset]
spec_json: in-line-close.json
skeleton: in-line-close.html
exported: 2026-10-02
---

# In-Line Close

> Close (X) button for in-line panels and alerts (InLineMessage, ModalsOffset). Bare 12px icon in a 40px hit area at rest; the 28px `Box` gets a white fill and 1px near-black border on Hover/Pressed.

**Specification text from the Figma documentation frame** (verbatim, one text layer per line):

```text
In-Line Close
Last Updated: 2026.10.02
Components
UPDATED: 2026.09.30
In-Line Close
Updated: 2026.09.30
Default
Hover
Pressed
InFocus
In-Line Close Button
In-Line Close
Updated: 2026.09.30
In-Line Close
Size: 40×40px hit area; visible box is 28×28px (Hover, Pressed only)
Corner Radius: 4px (radius/sm) on the Hover/Pressed box and on the InFocus focus ring — not a circle like Modal Close
Padding: 8px all sides (12px icon centered in the 28px box, on Hover/Pressed); Default and InFocus have no box, so the icon sits directly in the 40px hit area
Icon: 12px square, "close" (X) icon, color/gray/min / #141414 in every state — does not shift between states
Fill: none (Default); color/gray/max / white box (Hover, Pressed); none (InFocus)
Border: none (Default); 1px color/gray/min box border (Hover, Pressed); InFocus adds a 2px color/gray/black focus ring with 4px corners, offset 1px outside the 40px hit area, no inner box
Default intentionally has no visible box, fill, or border — just the bare icon in the 40px hit area. It stays this way at rest and only gains the box on Hover/Pressed.

Margin: not yet established for this component (unlike the CTA buttons' 8px min left/right margin) — flagging as an open spec gap.
States
Updated: 2026.09.30
Default — resting appearance. No visible box, fill, or border by design; just the bare icon in the 40px hit area.
Hover — a white 28×28px box with a 1px color/gray/min border and 4px corner radius appears around the icon.
Pressed — matches Hover exactly (same white box, border, and icon color). No separate pressed-only styling.
InFocus — removes the box and adds a 2px black focus ring with 4px corners (matching the Hover/Pressed box), offset 1px outside the full 40px hit area. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button In-Line Close` · 5335:16200](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16200) · key `f0d7dc9ffa766ef6e54c1d46416a37d1405acaa6`
- Documentation frame: [7078:7975](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7975) · overview PNG: [previews/in-line-close--documentation.png](previews/in-line-close--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `Default` | [5335:16197](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16197) | `209eeb588c83…` | 40×40 | [png](previews/in-line-close--default.png) |
| `Hover` | [5335:16198](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16198) | `75ad5b6822e7…` | 40×40 | [png](previews/in-line-close--hover.png) |
| `Pressed` | [7078:7697](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7697) | `ee6e9976a5cf…` | 40×40 | [png](previews/in-line-close--pressed.png) |
| `InFocus` | [5335:16199](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16199) | `1f8cafef65fc…` | 40×40 | [png](previews/in-line-close--infocus.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| State | VARIANT | Default | Default, Hover, Pressed, InFocus |

## Where it is used

Scope: local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **100**.

Nested inside (component sets / components): InLineMessage ×59, ModalsOffset ×9.

Placed directly on pages: In-Line Content Containers | 2026.01.02 ×5, Alerts and Icons ×3, Buttons | 2026.09.30 ×1.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `Default` | 96 | 2 | InLineMessage/Desktop/none/StandAloneEmailPrefs/Panel ×1, InLineMessage ×51, ModalsOffset ×9, InLineMessage/FOLD/Medium/DashSubsAcctShareALL/HeaderAlert ×1, InLineMessage/Mobile/none/StandAloneEmailPrefs/Panel ×2, InLineMessage/FOLD/none/StandAloneEmailPrefs/Panel ×2, InLineMessage/Desktop/Medium/DashSubsAcctShareALL/HeaderAlert ×1, InLineMessage/FOLD/Confirmation/Footer/Panel ×1 | In-Line Content Containers \| 2026.01.02 ▸ Frame 8 ×5, Alerts and Icons ▸ Proposed MNG Icon Set ×3, Buttons \| 2026.09.30 ▸ Frame 13001 ×1 |
| `Hover` | 2 | 2 | — | — |
| `Pressed` | 1 | 1 | — | — |
| `InFocus` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint (40×40 hit area). No Breakpoint property.
- Every state has the same layers (`Button` › `Box` › `Icon`); the `Box` has no fill or border in Default and InFocus.
- Usually placed top-right of an InLineMessage panel, with the hit area aligned to the panel padding.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (the ring surrounds the 40px hit area with 4px corners, matching the Hover/Pressed box). In CSS: `outline: 2px solid var(--color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Dependencies

**Built from:**

- Icons ([4693:5](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=4693-5)) ×4 — not in this export

Icon variants used: `close` ×4.

**Built into:** InLineMessage, ModalsOffset

## Anatomy

Every variant in the set has the same layer tree; InFocus only adds the `Focus Ring` frame. Hidden layers are marked.

Default variant `Default`:

- **State=Default** `COMPONENT` — 40×40, horizontal, gap 8, pad 0/0/0/0, HUG×HUG
  - **Button** `FRAME` — 40×40, horizontal, gap 0, pad 0/0/0/0, FIXED×FIXED, r40
    - **Box** `FRAME` — 28×28, horizontal, gap 8, pad 8/8/8/8, HUG×HUG, r4 (radius/sm)
      - **Icon** `INSTANCE` — 12×12, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=close)

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT` — 40×40, horizontal, gap 8, pad 0/0/0/0, HUG×HUG
  - **Button** `FRAME` — 40×40, horizontal, gap 0, pad 0/0/0/0, FIXED×FIXED, r40
    - **Box** `FRAME` — 28×28, horizontal, gap 8, pad 8/8/8/8, HUG×HUG, r4 (radius/sm)
      - **Icon** `INSTANCE` — 12×12, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=close)
  - **Focus Ring** `FRAME` — 42×42, FIXED×FIXED, absolute at -1,-1, r4 (radius/sm), stroke color/gray/black, 2 outside

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `Default` | 40×40 | HUG×HUG | horizontal, gap 8, pad 0/0/0/0 | — | — | — |
| `Hover` | 40×40 | HUG×HUG | horizontal, gap 8, pad 0/0/0/0 | — | — | — |
| `Pressed` | 40×40 | HUG×HUG | horizontal, gap 8, pad 0/0/0/0 | — | — | — |
| `InFocus` | 40×40 | HUG×HUG | horizontal, gap 8, pad 0/0/0/0 | — | — | — |

*Values are for the variant root.*

## Typography

No text layers (icon-only).

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/gray/max | #FFFFFF | fill on Box |
| color/gray/min | #141414 | stroke on Box |
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
2. **17 instances are nested inside other instances** (counted in the total, not per parent, in "Where it is used").
3. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `Hover`, `Pressed`, `InFocus`.

## Rendering steps

1. Pick the variant from the Properties table (State comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `in-line-close.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Draw the focus ring outside the element so it never changes layout (see Responsive rules).
6. Check against the preview PNG in `previews/`.
