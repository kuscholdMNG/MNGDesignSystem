---
name: "Photos Block"
kind: assembly
group: homepage
order: 22
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3352:20865"
component_key: e952aa813910f9c37fe311a21c266b3089bad6ab
variants: 6
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Section Title / Eyebrow", "1Col Article Card", "Horizontal Thumbnail Card", "Show More Photos Affordance"]
built_into: []
spec_json: photos-block.json
skeleton: photos-block.html
exported: 2026-10-08
---

# Photos Block

**Assembly · 6 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Device = Desktop, Mobile · reused as instances in the assembled Desktop and Mobile pages and in both raw section libraries.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Photos Block](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20865) · node `3352:20865` · key `e952aa813910f9c37fe311a21c266b3089bad6ab`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Device=Mobile | [3352:20864](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20864) | bb477912263428727959de2d6182b0892f47ec88 | 438×1182.1 | ![Device=Mobile](previews/photos-block--mobile.png) |
| Device=Tablet | [3383:46539](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3383-46539) | 8f68df50113ec3908dfd74195bcf90582ebe7727 | 748×1088.5 | ![Device=Tablet](previews/photos-block--tablet.png) |
| Device=Desktop | [3352:20863](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20863) | d31d44fe7433df413291723e261947681a004f86 | 1280×886.7 | ![Device=Desktop](previews/photos-block--desktop.png) |
| Device=1280 | [3552:31512](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3552-31512) | 18ef702f60a31bc4c05087453bf3e5d66d4b6343 | 940×749.7 | ![Device=1280](previews/photos-block--1280.png) |
| Device=1100 | [3552:31974](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3552-31974) | bc3f3a950ce01f0bf50c5ee7e05d576d5e44b01b | 731×749.7 | ![Device=1100](previews/photos-block--1100.png) |
| Device=1024 | [3553:32439](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3553-32439) | c1da4d8153180d69a9c392c102e3442c9d648779 | 585×996.8 | ![Device=1024](previews/photos-block--1024.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Device | VARIANT | Mobile | Mobile, Desktop, Tablet, 1280, 1100, 1024 |

## Where it is used

- **Device=Mobile** — breakpoints: 340, 360; templates (direct): Mobile HomePage ×1, 340 HomePage ×1
- **Device=Tablet** — breakpoints: 768; templates (direct): 768 HomePage ×1
- **Device=Desktop** — breakpoints: 1100, 1280; no instances in this file
- **Device=1280** — breakpoints: 1280; templates (direct): Desktop HomePage ×1
- **Device=1100** — breakpoints: 1100; templates (direct): 1100 HomePage ×1
- **Device=1024** — breakpoints: 1024; templates (direct): 1024 HomePage ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Device=Mobile |
| 360 | ≤639px (SM-Mobile, built 360) | Device=Mobile |
| 768 | 640–799px (MD-TabletV) | Device=Tablet |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Device=1024 |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Device=Desktop, Device=1100 |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Device=Desktop, Device=1280 |

## Responsive rules

- The lead story is a `1Col Article Card` Style=Media Lead instance (16:9 image, 29/33 headline) at every breakpoint; the list is `Horizontal Thumbnail Card` Mobile instances (90×51 thumbnails, Noto Sans 600 15/19 HeadlineList titles) at every width.
- Device=1024 / 1100 / 1280 are the content column only (585 / 731 / 940 wide); the ad sits in the template's rail next to them, as in production's landing-three-one row. Device=Desktop (full width, no rail) is not used by any template.
- Device=Mobile: 438×1182.1, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 340, 360
- Device=Tablet: 748×1088.5, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 768
- Device=Desktop: 1280×886.7, horizontal gap 24 pad 0/0/32/0 main CENTER cross MIN — renders at 1100, 1280
- Device=1280: 940×749.7, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 1280
- Device=1100: 731×749.7, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 1100
- Device=1024: 585×996.8, vertical gap 24 pad 0/0/32/0 main MIN cross CENTER — renders at 1024

## Dependencies

**Built from:**

- [Section Title / Eyebrow](../../components/06-section-title-eyebrow/section-title-eyebrow.md) ×1
- [1Col Article Card](../../components/16-1col-article-card/1col-article-card.md) ×1
- [Horizontal Thumbnail Card](../../components/11-horizontal-thumbnail-card/horizontal-thumbnail-card.md) ×6
- [Show More Photos Affordance](../../components/21-show-more-photos-affordance/show-more-photos-affordance.md) ×1

**Built into:**

_Not used inside another exported item._

## Anatomy

**Device=Mobile**

```
- Device=Mobile — component 438×1182.1 [vertical gap 24] (fixed/hug)
  - News Content — frame 438×1150.1 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 438×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 438×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 438×959.4 [vertical gap 16] (fill/hug)
      - 1Col Article Card — instance 438×448.4 [vertical gap 8] (fill/hug) → 1Col Article Card [Style=Media Lead]
      - Additional Articles — frame 336×495 [vertical gap 40] (fixed/hug) ×5
    - Show More Photos Affordance — instance 438×140.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=Tablet**

```
- Device=Tablet — component 748×1088.5 [vertical gap 24] (fixed/hug)
  - News Content — frame 748×1056.5 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 748×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 748×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 748×865.8 [vertical gap 16] (fill/hug)
      - 1Col Article Card — instance 748×568.8 [vertical gap 8] (fixed/hug) → 1Col Article Card [Style=Media Lead]
      - Additional Articles Grid TABLET — frame 748×281 [vertical gap 40] (fixed/hug)
    - Show More Photos Affordance — instance 748×140.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=Desktop**

```
- Device=Desktop — component 1280×886.7 [horizontal gap 24] (fixed/fixed)
  - News Content — frame 1280×858.7 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 1280×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 1280×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 1280×668 [horizontal gap 16] (fill/hug)
      - 1Col Article Card — instance 573×470.3 [vertical gap 8] (fixed/hug) → 1Col Article Card [Style=Media Lead]
      - Additional Articles — frame 336×668 [vertical gap 16] (fixed/hug) ×6
    - Show More Photos Affordance — instance 1280×140.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=1280**

```
- Device=1280 — component 940×749.7 [vertical gap 24] (fixed/hug)
  - News Content — frame 940×717.7 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 940×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 940×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 940×527 [horizontal gap 20] (fill/hug)
      - 1Col Article Card — instance 580×474.3 [vertical gap 8] (fixed/hug) → 1Col Article Card [Style=Media Lead]
      - Additional Articles List (1280, single column, 6 cards) — frame 340×527 [vertical gap 25] (fixed/hug) ×6
    - Show More Photos Affordance — instance 940×140.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=1100**

```
- Device=1100 — component 731×749.7 [vertical gap 24] (fixed/hug)
  - News Content — frame 731×717.7 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 731×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 731×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 731×527 [horizontal gap 21] (fill/hug)
      - 1Col Article Card — instance 441×450.1 [vertical gap 8] (fixed/hug) → 1Col Article Card [Style=Media Lead]
      - Additional Articles List (1100, single column, 6 cards) — frame 269×527 [vertical gap 25] (fixed/hug) ×6
    - Show More Photos Affordance — instance 731×140.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

**Device=1024**

```
- Device=1024 — component 585×996.8 [vertical gap 24] (fixed/hug)
  - News Content — frame 585×964.8 [vertical gap 0] (fill/hug)
    - 3Col Header — frame 585×50 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 585×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Section Block — frame 585×774.1 [vertical gap 16] (fill/hug)
      - 1Col Article Card — instance 585×477.1 [vertical gap 8] (fill/hug) → 1Col Article Card [Style=Media Lead]
      - Additional Articles Grid TABLET — frame 585×281 [vertical gap 40] (fill/hug)
    - Show More Photos Affordance — instance 585×140.7 [vertical gap 4] (fill/hug) → Show More Photos Affordance
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Device=Mobile | 438×1182.1 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |
| Device=Tablet | 748×1088.5 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |
| Device=Desktop | 1280×886.7 | FIXED | FIXED | horizontal gap 24 pad 0/0/32/0 main CENTER cross MIN |  |  |
| Device=1280 | 940×749.7 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |
| Device=1100 | 731×749.7 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |
| Device=1024 | 585×996.8 | FIXED | HUG | vertical gap 24 pad 0/0/32/0 main MIN cross CENTER |  |  |

## Typography

_No text._

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Device=Mobile | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| News Content | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| 3Col Header | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| 1Col Article Card | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Device=Tablet | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Device=Desktop | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Device=1280 | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Device=1100 | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Device=1024 | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- 1 of 6 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Device=Desktop`.
- The 340 and 360 templates use a 'Photos Block' frame (not an instance) that copies Device=Mobile, so Device=Mobile shows as unused.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `photos-block.json` → `variants[].variantProperties`).
2. Start from `photos-block.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
