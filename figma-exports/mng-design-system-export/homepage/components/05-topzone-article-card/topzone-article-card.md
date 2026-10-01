---
name: "TopZone Article Card"
kind: component
group: homepage
order: 5
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3336:46079"
component_key: 4daecb8ad8cafb30916853070665c768d1fc18e8
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Article Image Placeholder", "Article Status Badge"]
built_into: ["TOP ZONE Block"]
spec_json: topzone-article-card.json
skeleton: topzone-article-card.html
exported: 2026-09-24
---

# TopZone Article Card

**Component · 2 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Device = Desktop, Mobile (badge defaults to None on both)

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [TopZone Article Card](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3336-46079) · node `3336:46079` · key `4daecb8ad8cafb30916853070665c768d1fc18e8`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Device=Mobile | [3336:46078](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3336-46078) | 997b110ba5e030bfc5ba916de350fbd24160af6f | 340×107 | ![Device=Mobile](previews/topzone-article-card--mobile.png) |
| Device=Desktop | [3336:46077](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3336-46077) | 8dcd8a244e91736a663d21060039986716abae71 | 336×363 | ![Device=Desktop](previews/topzone-article-card--desktop.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Device | VARIANT | Mobile | Desktop, Mobile |

## Where it is used

- **Device=Mobile** — breakpoints: 340, 360, 768; templates (direct): Mobile HomePage ×3, 340 HomePage ×3; templates (via assembly): Mobile HomePage (via TOP ZONE Block), 340 HomePage (via TOP ZONE Block); nested inside: TOP ZONE Block / Device=Mobile ×3
- **Device=Desktop** — breakpoints: 768, 1024, 1100, 1280; no instances found

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Device=Mobile |
| 360 | ≤639px (SM-Mobile, built 360) | Device=Mobile |
| 768 | 640–799px (MD-TabletV) | Device=Mobile, Device=Desktop |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Device=Desktop |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Device=Desktop |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Device=Desktop |

## Responsive rules

- Device=Mobile: 340×107, vertical gap 16 pad 0/0/16/0 main MIN cross MIN — renders at 340, 360, 768
- Device=Desktop: 336×363, vertical gap 8 pad 0/0/16/0 main MIN cross MIN — renders at 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- [Article Image Placeholder](../03-article-image-placeholder/article-image-placeholder.md) ×2
- [Article Status Badge](../01-article-status-badge/article-status-badge.md) ×2

**Built into:**

- [TOP ZONE Block](../../assemblies/12-top-zone-block/top-zone-block.md)

## Anatomy

**Device=Mobile**

```
- Device=Mobile — component 340×107 [vertical gap 16] (fixed/hug)
  - Content — frame 340×75 [horizontal gap 8] (fill/hug)
    - Article Image Placeholder — instance 100×67 [vertical gap 8] (fixed/fixed) → Article Image Placeholder
    - Headline — frame 232×75 [vertical gap 15] (fixed/hug)
      - Article Status Badge — instance 0×0 [horizontal gap 0] (hug/hug) → Article Status Badge [Type=None] (hidden)
      - Article Headline on News paper homepage in second zone position — text 232×75 (fill/hug) "Article Headline on News paper homepage "
  - Line 1 — line 340×0 (fill/fixed)
```

**Device=Desktop**

```
- Device=Desktop — component 336×363 [vertical gap 8] (hug/fixed)
  - Article Image Placeholder — instance 336×223 [vertical gap 8] (fixed/fixed) → Article Image Placeholder
  - Article Status Badge — instance 138×27 [horizontal gap 8] (hug/hug) → Article Status Badge [Type=Sponsored] (hidden)
  - Headline — frame 336×81 [vertical gap 15] (fill/hug)
    - Article Headline on News paper homepage in second zone position — text 336×81 (fill/hug) "Article Headline on News paper homepage "
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Device=Mobile | 340×107 | FIXED | HUG | vertical gap 16 pad 0/0/16/0 main MIN cross MIN |  |  |
| Device=Desktop | 336×363 | HUG | FIXED | vertical gap 8 pad 0/0/16/0 main MIN cross MIN |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| Article Headline on News paper homepage in second zone position | Noto Serif | Bold | 18 | auto |  |  | #141414 | Colors/color/gray/min |  | Article Headline on News paper homepage in second  |
| Article Headline on News paper homepage in second zone position | Noto Serif | Bold | 20 | auto |  |  | #141414 | Colors/color/gray/min |  | Article Headline on News paper homepage in second  |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Device=Mobile | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Line 1 | stroke | SOLID | #D7D6D2 | ⚠ unbound |  |  |
| Device=Desktop | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |

## Image ratios

| Variant | Layer | Size | Ratio | Source |
|---|---|---|---|---|
| Device=Mobile | Article Image Placeholder | 100×67 | 3:2 | Article Image Placeholder |
| Device=Desktop | Article Image Placeholder | 336×223 | 3:2 | Article Image Placeholder |

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- 1 of 2 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Device=Desktop`.
- 1 solid paints are hard-coded (not bound to a color variable): #D7D6D2 ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `topzone-article-card.json` → `variants[].variantProperties`).
2. Start from `topzone-article-card.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
