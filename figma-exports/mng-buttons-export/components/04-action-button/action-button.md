---
name: Action Button
kind: component
order: 4
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Button Action
figma_node: "7075:6357"
component_key: f2d61dd8cfa1619da4987e7b90ac60f2fbb6c102
variants: 4
breakpoints: [all (single size)]
built_from: [Icons]
built_into: []
spec_json: action-button.json
skeleton: action-button.html
exported: 2026-10-02
---

# Action Button

> Small icon + label utility action (documented example: "Copy Link"). No box at rest; a 1px black border appears on Hover/Pressed. Figma set name: `Button Action`.

**Specification text from the Figma documentation frame** (verbatim, one text layer per line):

```text
Action Button
Last Updated: 2026.10.02
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
Size: 95×32px in every state (the InFocus ring is drawn outside and doesn't change the size)
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

Note: This is a simplified, single-purpose reference derived from the older shared "Action Button" library component (renamed from "Button Action" on 2026-10-02) (kept separate and unchanged so existing designs on other files aren't affected). That source component bundles many additional pre-built icon+label combinations as hidden layers within the same component — Resend Invitation, Link Copied, Share (Android/Apple/Unknown), Preview Most Recent, Save/Saved, Gift Article, Remove, Cancel, and Delete — none of which are exposed as pickable Figma variants there. This documented version isolates just the "Copy Link" example. To use a different label/icon, duplicate this component and swap its icon instance and label text.

Margin: not yet established for this component (unlike the CTA buttons' 8px min left/right margin) — flagging as an open spec gap.
States
Updated: 2026.09.30
Default — resting appearance. No border; icon and label only.
Hover — pointer is over the button; a 1px black border appears around the content area.
Pressed — same visual treatment as Hover. No distinct pressed color token exists yet.
InFocus — adds a 2px black focus ring, offset 1px outside the 1px border. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button Action` · 7075:6357](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6357) · key `f2d61dd8cfa1619da4987e7b90ac60f2fbb6c102`
- Documentation frame: [7075:6715](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6715) · overview PNG: [previews/action-button--documentation.png](previews/action-button--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `Default` | [7075:6358](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6358) | `d527026b821c…` | 95×32 | [png](previews/action-button--default.png) |
| `Hover` | [7075:6415](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6415) | `b570062e77c4…` | 95×32 | [png](previews/action-button--hover.png) |
| `Pressed` | [7075:6513](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6513) | `4c6105826870…` | 95×32 | [png](previews/action-button--pressed.png) |
| `InFocus` | [7075:6464](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7075-6464) | `e137200747fb…` | 95×32 | [png](previews/action-button--infocus.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| State | VARIANT | Default | Default, Hover, InFocus, Pressed |

## Where it is used

Scope: local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **4**.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `Default` | 1 | 1 | — | — |
| `Hover` | 1 | 1 | — | — |
| `Pressed` | 1 | 1 | — | — |
| `InFocus` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint (95×32, HUG). No Breakpoint property. It stays compact (32px), not 40px (Karl, 2026-10-02).
- Width hugs icon + label; swapping the label changes the width.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (a 40px button reads as 46px with the ring). In CSS: `outline: 2px solid var(--color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Dependencies

**Built from:**

- Icons ([4693:5](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=4693-5)) ×8 — not in this export

Icon variants used: `content_copy` ×8.

**Built into:** nothing yet (standalone).

## Anatomy

Every variant in the set has the same layer tree; InFocus only adds the `Focus Ring` frame. Hidden layers are marked.

Default variant `Default`:

- **State=Default** `COMPONENT` — 95×32, horizontal, gap 1, pad 0/0/0/0, HUG×HUG, r4 (radius/sm)
  - **Button** `FRAME` — 95×32, horizontal, gap 8, pad 8/8/8/8, HUG×HUG, r4 (radius/sm)
    - **Content** `FRAME` — 79×16, horizontal, gap 4, pad 0/0/0/0, HUG×HUG
      - **Icon Left** `INSTANCE` — 16×16, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy)
      - **Label** `TEXT` — 59×9, HUG×HUG, "Copy Link" Noto Sans Bold 12px, align left
      - **Icon Right** `INSTANCE` — 16×16, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy), **hidden**

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT` — 95×32, horizontal, gap 1, pad 0/0/0/0, HUG×HUG, r4 (radius/sm)
  - **Button** `FRAME` — 95×32, horizontal, gap 8, pad 8/8/8/8, HUG×HUG, r4 (radius/sm), stroke color/gray/black, 1 inside
    - **Content** `FRAME` — 79×16, horizontal, gap 4, pad 0/0/0/0, HUG×HUG
      - **Icon Left** `INSTANCE` — 16×16, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy)
      - **Label** `TEXT` — 59×9, HUG×HUG, "Copy Link" Noto Sans Bold 12px, align left
      - **Icon Right** `INSTANCE` — 16×16, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=content_copy), **hidden**
  - **Focus Ring** `FRAME` — 97×34, FIXED×FIXED, absolute at -1,-1, r4 (radius/sm), stroke color/gray/black, 2 outside

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `Default` | 95×32 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 (radius/sm) | — | — |
| `Hover` | 95×32 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 (radius/sm) | — | color/gray/black |
| `Pressed` | 95×32 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 (radius/sm) | — | color/gray/black |
| `InFocus` | 95×32 | HUG×HUG | horizontal, gap 8, pad 8/8/8/8 | 4 (radius/sm) | — | color/gray/black |

*Values are for the `Button` frame.*

## Typography

| Font | Weight | Size | Line height | Case | Color | Align | Layers |
|---|---|---|---|---|---|---|---|
| Noto Sans | Bold | 12px | auto | — | color/gray/min | left | Label |

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/gray/min | #141414 | text on Label |
| color/gray/black | #000000 | stroke on Button; stroke on Focus Ring |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **Name swap (2026-10-02).** This documented set is `Button Action` (`7075:6357`). The older library set on the same page (`5417:3876`, formerly `Button Action`, kept for Reader Dashboard files) is now `Action Button`. The documentation frame keeps the page title "Action Button".
2. **Single-purpose reference.** This set only documents "Copy Link". The older `Action Button` library set bundles Resend Invitation, Link Copied, Share (Android/Apple/Unknown), Preview Most Recent, Save/Saved, Gift Article, Remove, Cancel and Delete as hidden layers, none exposed as variants. To render another action, swap the icon instance and the label text.
3. **Hidden trailing icon.** Every variant carries a hidden `Icon Right` (content_copy) after the label. It is never shown; ignore it when rendering.
4. **Margin not specified** (open spec gap, per the Figma Specifications column).
5. **4 variants are placed only in their own documentation frame** (not yet used in any real layout): `Default`, `Hover`, `Pressed`, `InFocus`.

## Rendering steps

1. Pick the variant from the Properties table (State comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `action-button.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Draw the focus ring outside the element so it never changes layout (see Responsive rules).
6. Check against the preview PNG in `previews/`.
