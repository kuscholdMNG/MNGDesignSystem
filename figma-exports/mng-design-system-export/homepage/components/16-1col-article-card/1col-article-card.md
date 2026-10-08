---
name: "1Col Article Card"
kind: component
group: homepage
order: 16
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3536:39065"
component_key: d527b9d45b9d427355fa4f71183d2232ca6eaf27
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Article Image Placeholder", "Article Status Badge"]
built_into: ["Feature + List Content Block", "Section Rail Card", "Photos Block"]
spec_json: 1col-article-card.json
skeleton: 1col-article-card.html
exported: 2026-10-08
---

# 1Col Article Card

**Component · 2 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Style=Standard (4:3 image, CardQuaternary headline, ExcerptCompact excerpt — section-highlight lead cards) and Style=Media Lead (16:9 image, TitleMedia headline, Excerpt excerpt — the Photos lead) · Boolean props: Show Image, Show Subscriber Badge, Show Excerpt, Show Meta · uses instances of Article Image Placeholder and Article Status Badge internally. Shared atom for the lead + secondary items inside Photos Block and Section Rail Card (Wide + Narrow).

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [1Col Article Card](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3536-39065) · node `3536:39065` · key `d527b9d45b9d427355fa4f71183d2232ca6eaf27`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Style=Standard | [3352:24163](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-24163) | 480dedb94931bf80d85b41c0a7e921311b39dc0d | 296×372 | ![Style=Standard](previews/1col-article-card--standard.png) |
| Style=Media Lead | [3536:39050](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3536-39050) | 7e0ce7008b41fed7d8afb5279eca363f9e338674 | 296×413.5 | ![Style=Media Lead](previews/1col-article-card--media-lead.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Show Image | BOOLEAN | True |  |
| Show Subscriber Badge | BOOLEAN | False |  |
| Show Excerpt | BOOLEAN | True |  |
| Show Meta | BOOLEAN | False |  |
| Style | VARIANT | Standard | Standard, Media Lead |

## Where it is used

- **Style=Standard** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1100 HomePage (via Feature + List Content Block, Section Rail Card), Mobile HomePage (via Section Rail Card), 340 HomePage (via Section Rail Card), 1024 HomePage (via Feature + List Content Block, Section Rail Card), 768 HomePage (via Feature + List Content Block, Section Rail Card), Desktop HomePage (via Feature + List Content Block, Section Rail Card); nested inside: Section Rail Card / Device=1100, Layout=Narrow ×4, Section Rail Card / Device=Mobile, Layout=Narrow ×4, Section Rail Card / Device=1024, Layout=Narrow ×4, Feature + List Content Block / Size=Narrow ×3, Section Rail Card / Device=Tablet, Layout=Narrow ×4, Section Rail Card / Device=Desktop, Layout=Narrow ×4, Feature + List Content Block / Size=Default ×3
- **Style=Media Lead** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via Photos Block), Mobile HomePage (via Photos Block), 340 HomePage (via Photos Block), 1100 HomePage (via Photos Block), 768 HomePage (via Photos Block), Desktop HomePage (via Photos Block); nested inside: Photos Block / Device=1024 ×1, Photos Block / Device=Mobile ×1, Photos Block / Device=1100 ×1, Photos Block / Device=Tablet ×1, Photos Block / Device=1280 ×1, Photos Block / Device=Desktop ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Style=Standard, Style=Media Lead |
| 360 | ≤639px (SM-Mobile, built 360) | Style=Standard, Style=Media Lead |
| 768 | 640–799px (MD-TabletV) | Style=Standard, Style=Media Lead |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Style=Standard, Style=Media Lead |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Style=Standard, Style=Media Lead |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Style=Standard, Style=Media Lead |

## Responsive rules

- Style=Standard: 4:3 image, CardQuaternary headline (Noto Sans 600 19/24 −0.665 via small-headline-family) and ExcerptCompact excerpt (15/19, small-headline-family) — production section-highlight lead cards (feature-medium.feature-large, 300×225 image at 1280).
- Style=Media Lead: 16:9 image at every width (production crops the image to a 16:9 frame: 340×191 at 360, 580×326 at 1280), TitleMedia headline (Noto Serif 700 29/33 −1.16) and Excerpt excerpt (15/21) — the Photos lead (feature-media feature-large).
- Style=Standard: 296×372, vertical gap 8 pad 0/0/16/0 main MIN cross MIN — renders at 340, 360, 768, 1024, 1100, 1280
- Style=Media Lead: 296×413.5, vertical gap 8 pad 0/0/16/0 main MIN cross MIN — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- [Article Image Placeholder](../03-article-image-placeholder/article-image-placeholder.md) ×1
- [Article Status Badge](../01-article-status-badge/article-status-badge.md) ×1

**Built into:**

- [Feature + List Content Block](../../assemblies/17-feature-list-content-block/feature-list-content-block.md)
- [Section Rail Card](../../assemblies/18-section-rail-card/section-rail-card.md)
- [Photos Block](../../assemblies/22-photos-block/photos-block.md)

## Anatomy

**Style=Standard**

```
- Style=Standard — component 296×372 [vertical gap 8] (fixed/hug)
  - Article Graphic — instance 296×222 [vertical gap 8] (fill/fixed) → Article Image Placeholder
  - SubsOnlyBadge — instance 127×27 [horizontal gap 8] (hug/hug) → Article Status Badge [Type=Subscriber] (hidden)
  - Headline Container — frame 296×72 [vertical gap 15] (fill/hug)
    - Article Headline on News paper homepage in first position on 1col section block — text 296×72 (fill/hug) "Article Headline on News paper homepage "
  - Excerpt Container — frame 296×38 [horizontal gap 8] (fill/hug)
    - Vanroy Evan Smith, 39, of Long Beach is being held on $1 million bail. — text 296×38 (fill/hug) "Vanroy Evan Smith, 39, of Long Beach is "
  - Meta Container — frame 296×18 [vertical gap 8] (fixed/hug) (hidden)
    - 56 mins ago — text 296×18 (fill/hug) "56 mins ago"
  - Bottom Border Line — line 296×0 (fill/fixed)
```

**Style=Media Lead**

```
- Style=Media Lead — component 296×413.5 [vertical gap 8] (fixed/hug)
  - Article Graphic — instance 296×166.5 [vertical gap 8] (fill/fixed) → Article Image Placeholder
  - SubsOnlyBadge — instance 127×27 [horizontal gap 8] (hug/hug) → Article Status Badge [Type=Subscriber] (hidden)
  - Headline Container — frame 296×165 [vertical gap 15] (fill/hug)
    - Article Headline on News paper homepage in first position on 1col section block — text 296×165 (fill/hug) "Article Headline on News paper homepage "
  - Excerpt Container — frame 296×42 [horizontal gap 8] (fill/hug)
    - Vanroy Evan Smith, 39, of Long Beach is being held on $1 million bail. — text 296×42 (fill/hug) "Vanroy Evan Smith, 39, of Long Beach is "
  - Meta Container — frame 296×18 [vertical gap 8] (fixed/hug) (hidden)
    - 56 mins ago — text 296×18 (fill/hug) "56 mins ago"
  - Bottom Border Line — line 296×0 (fill/fixed)
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Style=Standard | 296×372 | FIXED | HUG | vertical gap 8 pad 0/0/16/0 main MIN cross MIN |  |  |
| Style=Media Lead | 296×413.5 | FIXED | HUG | vertical gap 8 pad 0/0/16/0 main MIN cross MIN |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Article Headline on News paper homepage in first position on | Noto Sans | SemiBold | 19 | 24px | -0.665px |  | #141414 | Colors/color/gray/min | Editorial/Titles/CardQuaternary |  | Article Headline on News paper homepage in first p | Style=Standard |
| Vanroy Evan Smith, 39, of Long Beach is being held on $1 mil | Noto Sans | Regular | 15 | 19px |  |  | #393938 | Colors/color/gray/100 | Editorial/Body/ExcerptCompact |  | Vanroy Evan Smith, 39, of Long Beach is being held | Style=Standard |
| 56 mins ago | Noto Sans | Regular | 13 | auto |  |  | #5E5D5C | Colors/color/gray/200 | font/size/13 |  | 56 mins ago | all |
| Article Headline on News paper homepage in first position on | Noto Serif | Bold | 29 | 33px | -1.16px |  | #141414 | Colors/color/gray/min | Editorial/Titles/TitleMedia |  | Article Headline on News paper homepage in first p | Style=Media Lead |
| Vanroy Evan Smith, 39, of Long Beach is being held on $1 mil | Noto Sans | Regular | 15 | 21px |  |  | #393938 | Colors/color/gray/100 | Editorial/Body/Excerpt |  | Vanroy Evan Smith, 39, of Long Beach is being held | Style=Media Lead |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Style=Standard | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Article Graphic | fill | SOLID | #E1A1FF |  |  | image placeholder fill |
| Article Graphic | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| SubsOnlyBadge | fill | SOLID | #007580 | Colors/color/theme/primary |  |  |
| Bottom Border Line | stroke | SOLID | #CCCAC7 | Colors/color/gray/500 |  |  |
| Style=Media Lead | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |

## Image ratios

| Variant | Layer | Size | Ratio | Source |
|---|---|---|---|---|
| Style=Standard | Article Graphic | 296×222 | 4:3 | Article Image Placeholder |
| Style=Media Lead | Article Graphic | 296×166.5 | 16:9 | Article Image Placeholder |

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

_None detected._

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `1col-article-card.json` → `variants[].variantProperties`).
2. Start from `1col-article-card.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
