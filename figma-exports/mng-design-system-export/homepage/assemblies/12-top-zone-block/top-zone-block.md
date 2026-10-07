---
name: "TOP ZONE Block"
kind: assembly
group: homepage
order: 12
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3352:19482"
component_key: 7a4ff4e26dbe4cde51851d2fa71c64f0c4f6ddd1
variants: 3
breakpoints: [340, 360, 768, 1280]
built_from: ["Zone 1 Lead Article Card", "Article Image Placeholder", "TopZone Article Card", "Latest Headlines", "Ad Blocks", "Article Status Badge", "Horizontal Thumbnail Card"]
built_into: []
spec_json: top-zone-block.json
skeleton: top-zone-block.html
exported: 2026-10-07
---

# TOP ZONE Block

**Assembly · 3 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Device = Desktop, Mobile · reused as instances in the assembled Desktop and Mobile pages and in both raw section libraries (Home Page Sections, Frame 12027).

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [TOP ZONE Block](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-19482) · node `3352:19482` · key `7a4ff4e26dbe4cde51851d2fa71c64f0c4f6ddd1`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Device=Mobile | [3352:19481](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-19481) | 6f47ee23795007df62f06ec3ef7f576a1c87eb75 | 340×2378.7 | ![Device=Mobile](previews/top-zone-block--mobile.png) |
| Device=Desktop | [3352:19480](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-19480) | 36fdd688499b8f976a904d80a176e92d829057d4 | 1264×1123 | ![Device=Desktop](previews/top-zone-block--desktop.png) |
| Device=Tablet | [3383:46168](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3383-46168) | b4a1a32615aabad34160c7c1eb0c826d46033f51 | 748×1787 | ![Device=Tablet](previews/top-zone-block--tablet.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Device | VARIANT | Mobile | Desktop, Mobile, Tablet |

## Where it is used

- **Device=Mobile** — breakpoints: 340, 360; templates (direct): Mobile HomePage ×1, 340 HomePage ×1
- **Device=Desktop** — breakpoints: 1280; templates (direct): Desktop HomePage ×1
- **Device=Tablet** — breakpoints: 768; templates (direct): 768 HomePage ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Device=Mobile |
| 360 | ≤639px (SM-Mobile, built 360) | Device=Mobile |
| 768 | 640–799px (MD-TabletV) | Device=Tablet |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Device=Desktop |

## Responsive rules

- Desktop (checked against the preview): three columns. Left: Zone 1 lead card (headline + image side by side) over a 2×2 grid of TopZone cards. Middle: Latest Headlines rail with a sponsored item and newsletter signup. Right: a tall 300×1050 rail ad.
- Tablet: lead card and image across the top, then a 2×2 group of horizontal thumbnail cards, then Latest Headlines full width, with a 300×250 cube ad at the bottom.
- Mobile: one column. The lead card stacks headline → image → dek → related list, followed by four horizontal thumbnail cards, Latest Headlines, and a 300×250 cube ad.
- Device=Mobile: 340×2378.7, vertical gap 16 pad 0/0/0/0 main MIN cross MIN — renders at 340, 360
- Device=Desktop: 1264×1123, horizontal gap 16 pad 0/0/16/0 main CENTER cross MIN — renders at 1280
- Device=Tablet: 748×1787, vertical gap 16 pad 0/0/0/0 main MIN cross MIN — renders at 768

## Dependencies

**Built from:**

- [Zone 1 Lead Article Card](../../components/04-zone-1-lead-article-card/zone-1-lead-article-card.md) ×1
- [Article Image Placeholder](../../components/03-article-image-placeholder/article-image-placeholder.md) ×1
- [TopZone Article Card](../../components/05-topzone-article-card/topzone-article-card.md) ×3
- [Latest Headlines](../09-latest-headlines/latest-headlines.md) ×1
- Ad Blocks ×1 _(not in this export)_
- [Article Status Badge](../../components/01-article-status-badge/article-status-badge.md) ×4
- [Horizontal Thumbnail Card](../../components/11-horizontal-thumbnail-card/horizontal-thumbnail-card.md) ×4

**Built into:**

_Not used inside another exported item._

## Anatomy

**Device=Mobile**

```
- Device=Mobile — component 340×2378.7 [vertical gap 16] (fixed/hug)
  - TOP Zones 1-5 MOBILE — frame 340×1140.7 [vertical gap 16] (fill/hug)
    - Zone 1 Lead Article Card — instance 340×648.7 [vertical gap 8] (fixed/hug) → Zone 1 Lead Article Card [Device=Mobile]
    - TopZone Article Card MOBILE — frame 340×107 [vertical gap 16] (fill/hug)
      - Content — frame 340×75 [horizontal gap 8] (fill/hug)
      - Bottom Border Line — line 340×0 (fill/fixed)
    - TopZone Article Card — instance 340×107 [vertical gap 16] (fixed/hug) → TopZone Article Card [Device=Mobile] ×3
  - Latest Headlines — instance 340×956 [vertical gap 12] (fixed/hug) → Latest Headlines [Device=Mobile]
  - Ad Block Container — frame 340×250 [vertical gap 16] (fill/hug)
    - Ad Blocks — instance 300×250 [vertical gap 8] (fixed/fixed) → Ad Blocks [Device=All, Name=Cube 1 RRail ATF 300x250]
```

**Device=Desktop**

```
- Device=Desktop — component 1264×1123 [horizontal gap 16] (fixed/hug)
  - Lead Column — frame 706×1107 [vertical gap 0] (fixed/hug)
    - Zone 1 Lead Article Card — instance 706×349 [horizontal gap 20] (hug/hug) → Zone 1 Lead Article Card [Device=Desktop]
    - Top Zones 2-5 — frame 706×379 [horizontal gap 16] (fill/hug)
      - TopZone Article Card — frame 336×363 [vertical gap 8] (hug/fixed)
      - TopZone Article Card — frame 336×363 [vertical gap 8] (hug/fixed)
    - Top Zones 2-5 — frame 706×379 [horizontal gap 16] (fill/hug)
      - TopZone Article Card — frame 336×363 [vertical gap 8] (hug/fixed)
      - TopZone Article Card — frame 336×363 [vertical gap 8] (hug/fixed)
  - Latest Headlines — instance 226×1072 [vertical gap 12] (fixed/hug) → Latest Headlines [Device=Desktop]
  - Right Rail — frame 300×1050 [vertical gap 16] (fixed/hug)
    - Ad Blocks — instance 300×1050 [vertical gap 8] (fixed/fixed) → Ad Blocks [Device=Desktop, Name=Cube 1 RRail ATF 300x1050]
```

**Device=Tablet**

```
- Device=Tablet — component 748×1787 [vertical gap 16] (fixed/hug)
  - TOP Zones 1-5 TABLET — frame 748×549 [vertical gap 16] (fill/hug)
    - Zone 1 Lead Article Card — instance 748×349 [horizontal gap 32] (hug/hug) → Zone 1 Lead Article Card [Device=Tablet]
    - TopZone Secondary Grid TABLET — frame 748×184 [vertical gap 16] (fixed/hug)
      - Row 1 — frame 748×84 [horizontal gap 32] (hug/hug) ×2
      - Row 2 — frame 748×84 [horizontal gap 32] (hug/hug) ×2
  - Latest Headlines — instance 748×956 [vertical gap 12] (fixed/hug) → Latest Headlines [Device=Tablet]
  - Ad Block Container — frame 748×250 [vertical gap 16] (fill/hug)
    - Ad Blocks — instance 300×250 [vertical gap 8] (fixed/fixed) → Ad Blocks [Device=All, Name=Cube 1 RRail ATF 300x250]
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Device=Mobile | 340×2378.7 | FIXED | HUG | vertical gap 16 pad 0/0/0/0 main MIN cross MIN |  |  |
| Device=Desktop | 1264×1123 | FIXED | HUG | horizontal gap 16 pad 0/0/16/0 main CENTER cross MIN |  |  |
| Device=Tablet | 748×1787 | FIXED | HUG | vertical gap 16 pad 0/0/0/0 main MIN cross MIN |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Article Headline on News paper homepage in second zone posit | Noto Serif | Bold | 18 | auto |  |  | #141414 | Colors/color/gray/min |  |  | Article Headline on News paper homepage in second  | Device=Mobile |
| ARTICLE IMAGE | Noto Serif | Bold | 16 | auto | 10% |  | #141414 | Colors/color/gray/min |  |  | GRAPHIC / IMAGE | Device=Desktop |
| Article Headline on News paper homepage in second zone posit | Noto Serif | Bold | 20 | auto |  |  | #141414 | Colors/color/gray/min |  |  | Article Headline on News paper homepage in second  | Device=Desktop |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Zone 1 Lead Article Card | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| TopZone Article Card MOBILE | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Article Image Placeholder | fill | SOLID | #E1A1FF |  |  | image placeholder fill |
| Article Image Placeholder | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| Bottom Border Line | stroke | SOLID | #CCCAC7 | Colors/color/gray/500 |  |  |
| TopZone Article Card | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Latest Headlines | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Ad Blocks | fill | SOLID | #85FF9B |  |  |  |
| Ad Blocks | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| Device=Desktop | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Placeholder X | fill | SOLID | #141414 | Colors/color/gray/min |  |  |
| Diagonal 1 | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| Diagonal 2 | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| Article Status Badge | fill | SOLID | #7D161E |  |  |  |

## Image ratios

| Variant | Layer | Size | Ratio | Source |
|---|---|---|---|---|
| Device=Mobile | Article Image Placeholder | 100×67 | 3:2 | Article Image Placeholder |
| Device=Desktop | Article Image Placeholder | 336×189 | 16:9 | frame |
| Device=Desktop | Article Image Placeholder | 336×189 | 16:9 | frame |
| Device=Desktop | Article Image Placeholder | 336×189 | 16:9 | frame |
| Device=Desktop | Article Image Placeholder | 336×189 | 16:9 | frame |

## Ad slots

| Variant | Layer | Unit | Size |
|---|---|---|---|
| Device=Mobile | Ad Block Container |  | 340×250 |
| Device=Mobile | Ad Blocks | Cube 1 RRail ATF 300x250 | 300×250 |
| Device=Desktop | Ad Blocks | Cube 1 RRail ATF 300x1050 | 300×1050 |
| Device=Tablet | Ad Block Container |  | 748×250 |
| Device=Tablet | Ad Blocks | Cube 1 RRail ATF 300x250 | 300×250 |

## Production references

_None found in descriptions or layer names._

## Known issues

- 4 solid paints are hard-coded (not bound to a color variable): #E1A1FF ×4.
- The 1024 and 1100 HomePage templates use detached, resized copies ('TOP ZONE Block (Desktop, detached+resized for 1024…)' and 'TOP ZONE Block (detached, resized for 1100…)') instead of instances, so those breakpoints are not counted above. Reattaching them is on the status list.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `top-zone-block.json` → `variants[].variantProperties`).
2. Start from `top-zone-block.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
