---
name: "Photos Block"
kind: assembly
group: homepage
order: 22
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3352:20865"
component_key: e952aa813910f9c37fe311a21c266b3089bad6ab
variants: 3
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Section Title / Eyebrow", "Article Image Placeholder", "Article Status Badge", "Horizontal Thumbnail Card", "Show More Photos Affordance", "Gallery Icon Badge", "1Col Article Card"]
built_into: []
spec_json: photos-block.json
skeleton: photos-block.html
exported: 2026-09-24
---

# Photos Block

**Assembly · 3 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Device = Desktop, Mobile · reused as instances in the assembled Desktop and Mobile pages and in both raw section libraries.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Photos Block](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20865) · node `3352:20865` · key `e952aa813910f9c37fe311a21c266b3089bad6ab`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Device=Mobile | [3352:20864](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20864) | bb477912263428727959de2d6182b0892f47ec88 | 438×1124.7 | ![Device=Mobile](previews/photos-block--mobile.png) |
| Device=Tablet | [3383:46539](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3383-46539) | 8f68df50113ec3908dfd74195bcf90582ebe7727 | 748×1040.7 | ![Device=Tablet](previews/photos-block--tablet.png) |
| Device=Desktop | [3352:20863](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20863) | d31d44fe7433df413291723e261947681a004f86 | 1280×886.7 | ![Device=Desktop](previews/photos-block--desktop.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Device | VARIANT | Mobile | Mobile, Desktop, Tablet |

## Where it is used

- **Device=Mobile** — breakpoints: 340, 360; no instances found
- **Device=Tablet** — breakpoints: 768; templates (direct): 768 HomePage ×1
- **Device=Desktop** — breakpoints: 1024, 1100, 1280; no instances found

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Device=Mobile |
| 360 | ≤639px (SM-Mobile, built 360) | Device=Mobile |
| 768 | 640–799px (MD-TabletV) | Device=Tablet |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Device=Desktop |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Device=Desktop |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Device=Desktop |

## Responsive rules

- Device=Mobile: 438×1124.7, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 340, 360
- Device=Tablet: 748×1040.7, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 768
- Device=Desktop: 1280×886.7, horizontal gap 24 pad 0/0/32/0 main CENTER cross MIN — renders at 1024, 1100, 1280

## Dependencies

**Built from:**

- [Section Title / Eyebrow](../../components/06-section-title-eyebrow/section-title-eyebrow.md) ×3
- [Article Image Placeholder](../../components/03-article-image-placeholder/article-image-placeholder.md) ×8
- [Article Status Badge](../../components/01-article-status-badge/article-status-badge.md) ×2
- [Horizontal Thumbnail Card](../../components/11-horizontal-thumbnail-card/horizontal-thumbnail-card.md) ×11
- [Show More Photos Affordance](../../components/21-show-more-photos-affordance/show-more-photos-affordance.md) ×3
- [Gallery Icon Badge](../../components/10-gallery-icon-badge/gallery-icon-badge.md) ×6
- [1Col Article Card](../../components/16-1col-article-card/1col-article-card.md) ×1

**Built into:**

- _no parent in this export_

## Anatomy

**Device=Mobile**

```
- Device=Mobile — component 438×1124.7 [vertical gap 24] (fixed/hug)
  - News Content — frame 438×1092.7 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 438×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 438×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 438×906 [vertical gap 16] (fill/hug)
      - 1Col Article Card (master, detached — image FILL-width fixed + resized to match production 16:9) — frame 438×395 [vertical gap 8] (fill/hug)
        - … 6 children
      - Additional Articles — frame 336×495 [vertical gap 40] (fixed/hug)
        - … 5 children
    - Show More Photos Affordance — instance 438×136.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=Tablet**

```
- Device=Tablet — component 748×1040.7 [vertical gap 24] (fixed/hug)
  - News Content — frame 748×1008.7 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 748×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 748×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 748×822 [vertical gap 16] (fill/hug)
      - 1Col Article Card (Tablet, detached — image resized to match production 16:9) — frame 748×525 [vertical gap 8] (fixed/hug)
        - … 6 children
      - Additional Articles Grid TABLET — frame 748×281 [vertical gap 40] (fixed/hug)
        - … 3 children
    - Show More Photos Affordance — instance 748×136.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=Desktop**

```
- Device=Desktop — component 1280×886.7 [horizontal gap 24] (fixed/fixed)
  - News Content — frame 1280×854.7 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 1280×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 1280×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 1280×668 [horizontal gap 16] (fill/hug)
      - 1Col Article Card — instance 573×352 [vertical gap 8] (fixed/hug) → 1Col Article Card
      - Additional Articles — frame 336×668 [vertical gap 16] (fixed/hug)
        - … 6 children
    - Show More Photos Affordance — instance 1280×136.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Device=Mobile | 438×1124.7 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |
| Device=Tablet | 748×1040.7 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |
| Device=Desktop | 1280×886.7 | FIXED | FIXED | horizontal gap 24 pad 0/0/32/0 main CENTER cross MIN |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| Article Headline on News paper homepage in first position on 1col section block | Noto Serif | Bold | 19 | auto |  |  | #141414 | Colors/color/gray/min |  | Featured Headline on News paper homepage in Photo  |
| Vanroy Evan Smith, 39, of Long Beach is being held on $1 million bail. | Noto Sans | Regular | 15 | 19px |  |  | #393938 | Colors/color/gray/100 |  | Vanroy Evan Smith, 39, of Long Beach is being held |
| 56 mins ago | Noto Sans | Regular | 13 | auto |  |  | #5E5D5C | Colors/color/gray/200 |  | 56 mins ago |
| Article Headline on News paper homepage in thumbnail list position | Noto Serif | Bold | 15 | auto |  |  | #141414 | Colors/color/gray/min |  | Article Headline on News paper homepage in thumbna |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Device=Mobile | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| News Content | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| 3Col Header | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| 1Col Article Card (master, detached — image FILL-width fixed + resized to match production 16:9) | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Bottom Border Line | stroke | SOLID | #CCCAC7 | Colors/color/gray/500 |  |  |
| Device=Tablet | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| 1Col Article Card (Tablet, detached — image resized to match production 16:9) | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Line 1 | stroke | SOLID | #D7D6D2 | ⚠ unbound |  |  |
| Device=Desktop | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |

## Image ratios

| Variant | Layer | Size | Ratio | Source |
|---|---|---|---|---|
| Device=Mobile | Article Graphic | 438×246 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Graphic | 748×421 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Image Placeholder | 90×51 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Image Placeholder | 90×51 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Image Placeholder | 90×51 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Image Placeholder | 90×51 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Image Placeholder | 90×51 | 16:9 | Article Image Placeholder |
| Device=Tablet | Article Image Placeholder | 90×51 | 16:9 | Article Image Placeholder |

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- 2 of 3 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Device=Mobile`, `Device=Desktop`.
- 6 solid paints are hard-coded (not bound to a color variable): #D7D6D2 ×6.
- Layer '1Col Article Card (master, detached — image FILL-width fixed + resized to match production 16:9)' is marked detached.
- Layer '1Col Article Card (Tablet, detached — image resized to match production 16:9)' is marked detached.
- Layer 'Horizontal Thumbnail Card (Tablet, Photos-768, detached — resized 364x67 to match production)' is marked detached.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `photos-block.json` → `variants[].variantProperties`).
2. Start from `photos-block.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
