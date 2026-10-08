---
name: "Gallery Icon Badge"
kind: component
group: homepage
order: 10
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3362:2959"
component_key: 0a14bf42a7c1ff5db7aea4dedb38ebea41c76862
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Icons"]
built_into: ["Horizontal Thumbnail Card"]
spec_json: gallery-icon-badge.json
skeleton: gallery-icon-badge.html
exported: 2026-10-08
---

# Gallery Icon Badge

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Small dark circular badge (28x28) with a white gallery/slideshow icon, used as an optional overlay on the bottom-right corner of Article Image Placeholder instances to indicate multi-photo content. Used inside Horizontal Thumbnail Card, toggled by its "Show Gallery Icon" property.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Gallery Icon Badge](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3362-2959) · node `3362:2959` · key `0a14bf42a7c1ff5db7aea4dedb38ebea41c76862`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Gallery Icon Badge | [3362:2959](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3362-2959) | 0a14bf42a7c1ff5db7aea4dedb38ebea41c76862 | 28×28 | ![Gallery Icon Badge](previews/gallery-icon-badge.png) |

## Properties

_None._

## Where it is used

- **Gallery Icon Badge** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 768 HomePage (via Horizontal Thumbnail Card), 1100 HomePage (via Horizontal Thumbnail Card), Desktop HomePage (via Horizontal Thumbnail Card), 1024 HomePage (via Horizontal Thumbnail Card), Mobile HomePage (via Horizontal Thumbnail Card), 340 HomePage (via Horizontal Thumbnail Card); nested inside: Horizontal Thumbnail Card / Device=Desktop ×1, Horizontal Thumbnail Card / Device=Tablet ×1, Horizontal Thumbnail Card / Device=Mobile ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Gallery Icon Badge |
| 360 | ≤639px (SM-Mobile, built 360) | Gallery Icon Badge |
| 768 | 640–799px (MD-TabletV) | Gallery Icon Badge |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Gallery Icon Badge |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Gallery Icon Badge |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Gallery Icon Badge |

## Responsive rules

- Gallery Icon Badge: 28×28, horizontal gap 0 pad 0/0/0/0 main CENTER cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- Icons ×1 _(not in this export)_

**Built into:**

- [Horizontal Thumbnail Card](../11-horizontal-thumbnail-card/horizontal-thumbnail-card.md)

## Anatomy

**Gallery Icon Badge**

```
- Gallery Icon Badge — component 28×28 [horizontal gap 0] (fixed/fixed)
  - Icons — instance 16×16 [horizontal gap 8] (fixed/fixed) → Icons [Name=slideshow]
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Gallery Icon Badge | 28×28 | FIXED | FIXED | horizontal gap 0 pad 0/0/0/0 main CENTER cross CENTER | 14 |  |

## Typography

_No text._

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Gallery Icon Badge | fill | SOLID | #000000 | Colors/color/gray/black |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

_None detected._

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `gallery-icon-badge.json` → `variants[].variantProperties`).
2. Start from `gallery-icon-badge.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
