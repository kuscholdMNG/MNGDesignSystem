---
name: Pop-Up Modal Close
kind: component
order: 6
figma_file: jFHYqhZbJjvWQmDI4myCsd
figma_set_name: Button ModalClose
figma_node: "5335:16196"
component_key: 790ce7e08b7c4a4da2f4c22f29a5525fdcbea997
variants: 4
breakpoints: [all (single size)]
built_from: [Icons]
built_into: [Modals, ModalsCenter]
spec_json: pop-up-modal-close.json
skeleton: pop-up-modal-close.html
exported: 2026-10-01
---

# Pop-Up Modal Close

> Circular 32px close (X) button for pop-up modals (ModalsCenter, Modals/*). Light-gray circle at rest, white on Hover/Pressed.

**Specification text from the Figma documentation frame** (verbatim, ` | ` separates text layers):

```text
Pop-Up Modal Close
Last Updated: 2026.09.30
Components
UPDATED: 2026.09.30
Pop-Up Modal Close
Updated: 2026.09.30
Default
Hover
Pressed
InFocus
Pop-Up Modal Close Button
Pop-Up Modal Title
Sub-Title Text
Body Section (As Needed)
Field Label 
Place holder text
Error message text.
We’ve encountered an error
We are unable to process your request at this time. To continue, please call us, or try again later.
Update Payment Info
CTA Hyperlink
CTA button
CTA Hyperlink
Pop-Up Modal Close
Updated: 2026.09.30
Pop-Up Modal Close
Size: 32×32px (34×34px on InFocus, from the added focus ring)
Corner Radius: fully rounded (circle)
Padding: 10px all sides (12px icon centered in the 32px circle)
Icon: 12px square, "close" (X) icon
Icon Color: color/gray/min / #141414 in every state — does not shift between Default, Hover, Pressed, or InFocus
Fill: color/gray/600 (Default); color/gray/max / white (Hover, Pressed); none (InFocus)
Border: 1px color/gray/400 (Default); 1px color/gray/500 (Hover, Pressed); InFocus adds a 2px black focus ring, offset 1px outside, no inner border

Margin: not yet established for this component (unlike the CTA buttons' 8px min left/right margin) — flagging as an open spec gap.
States
Updated: 2026.09.30
Default — resting appearance. Light gray fill (color/gray/600), 1px gray border (color/gray/400), near-black icon.
Hover — fill switches to white, border darkens to color/gray/500. Icon color stays the same.
Pressed — matches Hover exactly: white fill, color/gray/500 border. No separate pressed-only styling.
InFocus — removes the fill entirely and adds a 2px black focus ring, offset 1px outside the 32px circle. Appears on keyboard (Tab) focus for accessibility.
```

## Figma references

- File: **MNG Design System** (`jFHYqhZbJjvWQmDI4myCsd`), page **Buttons | 2026.09.30**
- Component set: [`Button ModalClose` · 5335:16196](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16196) · key `790ce7e08b7c4a4da2f4c22f29a5525fdcbea997`
- Documentation frame: [7078:7807](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7807) · overview PNG: [previews/pop-up-modal-close--documentation.png](previews/pop-up-modal-close--documentation.png)

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| `default` | [5335:16193](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16193) | `45a9fbb66f65…` | 32×32 | [png](previews/pop-up-modal-close--default.png) |
| `Hover` | [5335:16194](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16194) | `3003a972adb7…` | 32×32 | [png](previews/pop-up-modal-close--hover.png) |
| `Pressed` | [7078:7686](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7078-7686) | `be3d5493da1f…` | 32×32 | [png](previews/pop-up-modal-close--pressed.png) |
| `InFocus` | [5335:16195](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=5335-16195) | `0d2629a282e1…` | 34×34 | [png](previews/pop-up-modal-close--infocus.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| state | VARIANT | default | Hover, InFocus, default, Pressed |

## Where it is used

Scope: Local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.

Total instances: **26**.

Nested inside (component sets / components): Modals ×7, ModalsCenter ×6.

Placed directly on pages: Modal Panels | 2025.12.29 ×7.

| Variant | Total | Doc frame | In components | Other placements |
|---|---|---|---|---|
| `default` | 23 | 3 | 13 | Modal Panels \| 2025.12.29 ▸ Frame 12995 ×6, Modal Panels \| 2025.12.29 ▸ Frame 12672 ×1 |
| `Hover` | 1 | 1 | — | — |
| `Pressed` | 1 | 1 | — | — |
| `InFocus` | 1 | 1 | — | — |

## Breakpoints

No Breakpoint property: one size at every viewport.

## Responsive rules

- Single size at every breakpoint (32×32; 34×34 on InFocus because of the ring wrapper). No Breakpoint property.
- Sits in the modal header, top-right; see ModalsCenter in the main file.

## Dependencies

**Built from:**

- Icons ([4693:5](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=4693-5)) ×4 — not in this export

Icon variants used: `close` ×4.

**Built into:** Modals, ModalsCenter

## Anatomy

Default variant `default`:

- **state=default** `COMPONENT` — 32×32, horizontal gap 0 pad 0/0/0/0, FIXED×FIXED, r40, fill color/gray/600, stroke color/gray/400, stroke 1 inside
  - **Icons** `INSTANCE` — 12×12, horizontal gap 8 pad 0/0/0/0, FIXED×FIXED, → Icons (Name=close)

InFocus variant `InFocus` (focus-ring structure):

- **state=InFocus** `COMPONENT` — 34×34, horizontal gap 8 pad 1/1/1/1, HUG×HUG, r24, stroke color/gray/black, stroke 2 outside
  - **Close Button** `FRAME` — 32×32, horizontal gap 0 pad 0/0/0/0, FIXED×FIXED, r40, fill color/gray/600, stroke color/gray/400, stroke 1 inside
    - **Icons** `INSTANCE` — 12×12, horizontal gap 8 pad 0/0/0/0, FIXED×FIXED, → Icons (Name=close)

Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).

## Size & layout

| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |
|---|---|---|---|---|---|---|
| `default` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/600 | color/gray/400 |
| `Hover` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/max | color/gray/500 |
| `Pressed` | 32×32 | FIXED×FIXED | horizontal, gap 0, pad 0/0/0/0 | 40 | color/gray/max | color/gray/500 |
| `InFocus` | 34×34 | HUG×HUG | horizontal, gap 8, pad 1/1/1/1 | 24 | — | color/gray/black |

*Values are for the variant root. Most families wrap the visible button in an inner frame; see Anatomy.*

## Typography

No text layers (icon-only).

## Color & effects

| Token | Hex | Used as |
|---|---|---|
| color/gray/600 | #F1EFEB | fill on Close Button; fill on state=default |
| color/gray/400 | #A7A6A3 | stroke on Close Button; stroke on state=default |
| color/gray/max | #FFFFFF | fill on state=Hover; fill on state=Pressed |
| color/gray/500 | #CCCAC7 | stroke on state=Hover; stroke on state=Pressed |
| color/gray/black | #000000 | stroke on state=InFocus |

Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.

## Image ratios

N/A: no image fills or placeholders.

## Ad slots

N/A.

## Production references

None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.

## Known issues

1. **InFocus description disagrees with the component.** The Figma spec text says InFocus "removes the fill entirely … no inner border", but the InFocus variant still contains the Default circle (color/gray/600 fill + 1px color/gray/400 border) inside the 2px black ring. The preview confirms the gray fill is visible. Either the text or the variant needs to change (Karl to decide).
2. **Lower-case variant value.** The resting state is `state=default` (lower case); every other button family uses `Default`. Renaming it to `Default` is safe (Figma links by ID), but any code mapping state names should treat them the same.
3. **Figma set name differs from the doc title**: the component set is `Button ModalClose`.
4. **Margin not specified** (open spec gap, per the Figma Specifications column).
5. **3 variants are placed only in their own documentation frame** (not yet used in any real layout): `Hover`, `Pressed`, `InFocus`.

## Rendering steps

1. Pick the variant from the Properties table (state comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).
2. Copy that variant's structure from `pop-up-modal-close.html` (or build it from `variants[].layerTree` in the JSON).
3. Use the color tokens from `../../tokens.css`, never the hex, so the site theme applies.
4. Replace icon placeholders with the named `Icons` variant (see Dependencies).
5. Check against the preview PNG in `previews/`.
