---
name: "Most Popular List Item"
kind: component
group: homepage
order: 13
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3352:24171"
component_key: 7af31a2e303ffc881a654e1094cbc7d622d2da3f
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: []
built_into: ["Blueconic Block (Most Popular)"]
spec_json: most-popular-list-item.json
skeleton: most-popular-list-item.html
exported: 2026-10-08
---

# Most Popular List Item

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Standalone component · freely resizable, no variants · the numbered rank badge + headline pattern used in Blueconic Block's Most Popular list (10 per device).

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Most Popular List Item](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-24171) · node `3352:24171` · key `7af31a2e303ffc881a654e1094cbc7d622d2da3f`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Most Popular List Item | [3352:24171](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-24171) | 7af31a2e303ffc881a654e1094cbc7d622d2da3f | 963×32 | ![Most Popular List Item](previews/most-popular-list-item.png) |

## Properties

_None._

## Where it is used

- **Most Popular List Item** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1100 HomePage (via Blueconic Block (Most Popular)), 768 HomePage (via Blueconic Block (Most Popular)), Desktop HomePage (via Blueconic Block (Most Popular)), 1024 HomePage (via Blueconic Block (Most Popular)), Mobile HomePage (via Blueconic Block (Most Popular)), 340 HomePage (via Blueconic Block (Most Popular)); nested inside: Blueconic Block (Most Popular) / Device=1100 ×10, Blueconic Block (Most Popular) / Device=Tablet ×10, Blueconic Block (Most Popular) / Device=1280 ×10, Blueconic Block (Most Popular) / Device=1024 ×10, Blueconic Block (Most Popular) / Device=Desktop ×10, Blueconic Block (Most Popular) / Device=Mobile ×10

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Most Popular List Item |
| 360 | ≤639px (SM-Mobile, built 360) | Most Popular List Item |
| 768 | 640–799px (MD-TabletV) | Most Popular List Item |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Most Popular List Item |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Most Popular List Item |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Most Popular List Item |

## Responsive rules

- Most Popular List Item: 963×32, horizontal gap 12 pad 0/0/0/0 main MIN cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

_Nothing — leaf component._

**Built into:**

- [Blueconic Block (Most Popular)](../../assemblies/14-blueconic-block-most-popular/blueconic-block-most-popular.md)

## Anatomy

**Most Popular List Item**

```
- Most Popular List Item — component 963×32 [horizontal gap 12] (fixed/hug)
  - Bullet Number — frame 32×32 [vertical gap 8] (fixed/fixed)
    - 1 — text 13×15 (hug/hug) "1"
  - Headline Container — frame 919×22 [horizontal gap 8] (fill/hug)
    - Dear Abby: My clothes make her cry, and I feel like I can’t win — text 919×22 (fill/hug) "Dear Abby: My clothes make her cry, and "
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Most Popular List Item | 963×32 | FIXED | HUG | horizontal gap 12 pad 0/0/0/0 main MIN cross CENTER |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Noto Sans | SemiBold | 21 | 32px |  |  | #FFFFFF | Colors/color/gray/max | font/size/21 |  | 1 | all |
| Dear Abby: My clothes make her cry, and I feel like I can’t  | Noto Serif | Bold | 16 | auto |  |  | #141414 | Colors/color/gray/min | font/size/16 |  | Dear Abby: My clothes make her cry, and I feel lik | all |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Most Popular List Item | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Bullet Number | fill | SOLID | #007580 | Colors/color/theme/primary |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

_None detected._

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `most-popular-list-item.json` → `variants[].variantProperties`).
2. Start from `most-popular-list-item.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
