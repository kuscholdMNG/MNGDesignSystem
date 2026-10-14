---
name: Pop-Up Modal Close
kind: component
order: 6
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Button Modal Close
figma_node: "5335:16196"
component_key: 790ce7e08b7c4a4da2f4c22f29a5525fdcbea997
variants: 4
breakpoints: [all (single size)]
built_from: [Icons]
built_into: [Modals, ModalsCenter]
spec_json: pop-up-modal-close.json
skeleton: pop-up-modal-close.html
exported: 2026-10-02
---

# Pop-Up Modal Close

> Circular 32px close (X) button for pop-up modals (ModalsCenter, Modals/*). Light-gray circle at rest, white on Hover/Pressed; InFocus keeps the Default look and adds the ring.

**Specification text from the Figma documentation frame** (verbatim, one text layer per line):

```text
Pop-Up Modal Close
Last Updated: 2026.10.02
Components
UPDATED: 2026.09.30
Pop-Up Modal Close
Updated: 2026.09.30
Default
Hover
Pressed
InFocus
Pop-Up Modal Close Button
Pop-Up Modal Close
Updated: 2026.09.30
Pop-Up Modal Close
Size: 32×32px in every state (the InFocus ring is drawn outside and doesn't change the size)
Corner Radius: fully rounded (circle)
Padding: 10px all sides (12px icon centered in the 32px circle)
Icon: 12px square, "close" (X) icon
Icon Color: color/gray/min / #141414 in every state — does not shift between Default, Hover, Pressed, or InFocus
Fill: color/gray/600 (Default, InFocus); color/gray/max / white (Hover, Pressed)
Border: 1px color/gray/400 (Default, InFocus); 1px color/gray/500 (Hover, Pressed); InFocus adds a 2px color/gray/black focus ring, offset 1px outside the circle

Margin: not yet established for this component (unlike the CTA buttons' 8px min left/right margin) — flagging as an open spec gap.
States
Updated: 2026.09.30
Default — resting appearance. Light gray fill (color/gray/600), 1px gray border (color/gray/400), near-black icon.
Hover — fill switches to white, border darkens to color/gray/500. Icon color stays the same.
Pressed — matches Hover exactly: white fill, color/gray/500 border. No separate pressed-only styling.
InFocus — keeps the Default fill and border and adds a 2px black focus ring, offset 1px outside the 32px circle. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button Modal Close` · 5335:16196](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16196) · key `790ce7e08b7c4a4da2f4c22f29a5525fdcbea997`
- Documentation frame: [7078:7807](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7807) · overview PNG: [previews/pop-up-modal-close--documentation.png](previews/pop-up-modal-close--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `Default` | [5335:16193](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16193) | `45a9fbb66f65…` | 32×32 | [png](previews/pop-up-modal-close--default.png) |
| `Hover` | [5335:16194](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16194) | `3003a972adb7…` | 32×32 | [png](previews/pop-up-modal-close--hover.png) |
| `Pressed` | [7078:7686](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7686) | `be3d5493da1f…` | 32×32 | [png](previews/pop-up-modal-close--pressed.png) |
| `InFocus` | [5335:16195](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16195) | `0d2629a282e1…` | 32×32 | [png](previews/pop-up-modal-close--infocus.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| State | VARIANT | Default | Default, Hover, Pressed, InFocus |

## Where it is used

Scope: local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **26**.

Nested inside (component sets / components): Modals ×7, ModalsCenter ×6.

Placed directly on pages: Modal Panels | 2025.12.29 ×7.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `Default` | 23 | 3 | Modals/Mobile/Login ×1, Modals/TabletH/Login ×1, Modals/MobileScroll/Login ×1, ModalsCenter ×6, Modals/Desktop/Login ×1, Modals/FOLD/Login ×1, Modals/TabletV/Login ×1, Modals/Desktop ×1 | Modal Panels \| 2025.12.29 ▸ Frame 12995 ×6, Modal Panels \| 2025.12.29 ▸ Frame 12672 ×1 |
| `Hover` | 1 | 1 | — | — |
| `Pressed` | 1 | 1 | — | — |
| `InFocus` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint (32×32 in every state). No Breakpoint property.
- Sits in the modal header, top-right; see ModalsCenter in the main file.
- **Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. It draws outside the component and never changes its size or moves anything inside or around it (the 32px circle reads as 38px with the ring). In CSS: `outline: 2px solid var(--color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.

## Dependencies

**Built from:**

- Icons ([4693:5](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=4693-5)) ×4 — not in this export

Icon variants used: `close` ×4.

**Built into:** Modals, ModalsCenter

## Anatomy

Every variant in the set has the same layer tree; InFocus only adds the `Focus Ring` frame. Hidden layers are marked.

Default variant `Default`:

- **State=Default** `COMPONENT` — 32×32, horizontal, gap 0, pad 0/0/0/0, FIXED×FIXED, r40, fill color/gray/600, stroke color/gray/400, 1 inside
  - **Icon** `INSTANCE` — 12×12, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=close)

InFocus variant `InFocus`:

- **State=InFocus** `COMPONENT` — 32×32, horizontal, gap 0, pad 0/0/0/0, FIXED×FIXED, r40, fill color/gray/600, stroke color/gray/400, 1 inside
  - **Icon** `INSTANCE` — 12×12, horizontal, gap 8, pad 0/0/0/0, FIXED×FIXED, → Icons (Name=close)
  - **Focus Ring** `FRAME` — 34×34, FIXED×FIXED, absolute at -1,-1, r40, stroke color/gray/black, 2 outside

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `Default` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/600 | color/gray/400 |
| `Hover` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/max | color/gray/500 |
| `Pressed` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/max | color/gray/500 |
| `InFocus` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/600 | color/gray/400 |

*Values are for the variant root.*

## Typography

No text layers (icon-only).

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/gray/600 | #F1EFEB | fill on State=Default; fill on State=InFocus |
| color/gray/400 | #A7A6A3 | stroke on State=Default; stroke on State=InFocus |
| color/gray/max | #FFFFFF | fill on State=Hover; fill on State=Pressed |
| color/gray/500 | #CCCAC7 | stroke on State=Hover; stroke on State=Pressed |
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
2. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `Hover`, `Pressed`, `InFocus`.

## Rendering steps

1. Pick the variant from the Properties table (State comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `pop-up-modal-close.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Draw the focus ring outside the element so it never changes layout (see Responsive rules).
6. Check against the preview PNG in `previews/`.
