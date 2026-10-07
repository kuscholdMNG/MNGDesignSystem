---
name: "Upcoming Events Side Arrow"
kind: component
group: homepage
order: 28
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3557:40209"
component_key: 6423abf91ade006adc3cfbb23e6175da99435e60
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Icons"]
built_into: ["Upcoming Events Widget"]
spec_json: upcoming-events-side-arrow.json
skeleton: upcoming-events-side-arrow.html
exported: 2026-10-07
---

# Upcoming Events Side Arrow

**Component · 2 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Direction = Left, Right. 20×20, #3B3B3B, at the card-row edges (y104).

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Upcoming Events Side Arrow](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3557-40209) · node `3557:40209` · key `6423abf91ade006adc3cfbb23e6175da99435e60`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Direction=Left | [3557:40203](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3557-40203) | 7cecbc1dfc30089aaf1b66b18f09b805cfad868e | 20×20 | ![Direction=Left](previews/upcoming-events-side-arrow--left.png) |
| Direction=Right | [3557:40206](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3557-40206) | 6efc3e17906043563d80ce8c5c6d7a59836131f3 | 20×20 | ![Direction=Right](previews/upcoming-events-side-arrow--right.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Direction | VARIANT | Left | Left, Right |

## Where it is used

- **Direction=Left** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1100 HomePage (via Upcoming Events Widget), 1024 HomePage (via Upcoming Events Widget), Mobile HomePage (via Upcoming Events Widget), 340 HomePage (via Upcoming Events Widget), 768 HomePage (via Upcoming Events Widget), Desktop HomePage (via Upcoming Events Widget); nested inside: Upcoming Events Widget / Device=1100 ×1, Upcoming Events Widget / Device=1024 ×1, Upcoming Events Widget / Device=Mobile ×1, Upcoming Events Widget / Device=Tablet ×1, Upcoming Events Widget / Device=Desktop ×1
- **Direction=Right** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via Upcoming Events Widget), Mobile HomePage (via Upcoming Events Widget), 340 HomePage (via Upcoming Events Widget), 768 HomePage (via Upcoming Events Widget), 1100 HomePage (via Upcoming Events Widget), Desktop HomePage (via Upcoming Events Widget); nested inside: Upcoming Events Widget / Device=1024 ×1, Upcoming Events Widget / Device=Mobile ×1, Upcoming Events Widget / Device=Tablet ×1, Upcoming Events Widget / Device=1100 ×1, Upcoming Events Widget / Device=Desktop ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Direction=Left, Direction=Right |
| 360 | ≤639px (SM-Mobile, built 360) | Direction=Left, Direction=Right |
| 768 | 640–799px (MD-TabletV) | Direction=Left, Direction=Right |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Direction=Left, Direction=Right |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Direction=Left, Direction=Right |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Direction=Left, Direction=Right |

## Responsive rules

- Direction=Left: 20×20 — renders at 340, 360, 768, 1024, 1100, 1280
- Direction=Right: 20×20 — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- Icons ×1 _(not in this export)_

**Built into:**

- [Upcoming Events Widget](../../assemblies/29-upcoming-events-widget/upcoming-events-widget.md)

## Anatomy

**Direction=Left**

```
- Direction=Left — component 20×20
  - Icons — instance 16×16 [horizontal gap 8] (fixed/fixed) → Icons [Name=arrow-left2]
```

**Direction=Right**

```
- Direction=Right — component 20×20
  - Icons — instance 16×16 [horizontal gap 8] (fixed/fixed) → Icons [Name=arrow-right2]
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Direction=Left | 20×20 |  |  |  |  |  |
| Direction=Right | 20×20 |  |  |  |  |  |

## Typography

_No text._

## Color & effects

_None._

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

_None detected._

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `upcoming-events-side-arrow.json` → `variants[].variantProperties`).
2. Start from `upcoming-events-side-arrow.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
