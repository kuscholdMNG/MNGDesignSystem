---
name: "Article Status Badge"
kind: component
group: homepage
order: 1
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3344:63995"
component_key: a3c41dc84d271d8fadbefb86d033afe3706c21b6
variants: 3
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: []
built_into: ["Zone 1 Lead Article Card", "TopZone Article Card", "Latest Headlines List Item", "TOP ZONE Block", "1Col Article Card", "Photos Block"]
spec_json: article-status-badge.json
skeleton: article-status-badge.html
exported: 2026-09-24
---

# Article Status Badge

**Component · 3 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Type = None, Subscriber, Sponsored (replaces the old separate Subscriber Only Badge / Sponsored Content Tag atoms)

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Article Status Badge](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63995) · node `3344:63995` · key `a3c41dc84d271d8fadbefb86d033afe3706c21b6`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Type=None | [3344:63994](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63994) | 4bbcedebfb8a8e0b414d8217830d29de5fea2b5e | 0×0 | — (no preview: zero size) |
| Type=Subscriber | [3344:63989](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63989) | 3d7f0e03fdd71c7edddda24d4c13fadddb581fbd | 114×27 | ![Type=Subscriber](previews/article-status-badge--subscriber.png) |
| Type=Sponsored | [3344:63991](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63991) | 2cba7cf7dd45bbf3b7d1d71d53de2acd577e3217 | 138×27 | ![Type=Sponsored](previews/article-status-badge--sponsored.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Type | VARIANT | None | Subscriber, Sponsored, None |

## Where it is used

- **Type=None** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (direct): 768 HomePage ×7, Mobile HomePage ×10, 340 HomePage ×10, 1024 HomePage ×7, 1100 HomePage ×7, Desktop HomePage ×7; templates (via assembly): 1100 HomePage (via Latest Headlines List Item, Zone 1 Lead Article Card), 1024 HomePage (via Latest Headlines List Item, Zone 1 Lead Article Card), Mobile HomePage (via TopZone Article Card, Zone 1 Lead Article Card), 340 HomePage (via TopZone Article Card, Zone 1 Lead Article Card), Desktop HomePage (via Latest Headlines, Zone 1 Lead Article Card), 768 HomePage (via Zone 1 Lead Article Card); nested inside: Zone 1 Lead Article Card / Device=Mobile ×1, TOP ZONE Block / Device=Mobile ×10, TopZone Article Card / Device=Mobile ×1, Latest Headlines / Device=Desktop ×6, Latest Headlines / Device=Mobile ×6, TOP ZONE Block / Device=Desktop ×7, Zone 1 Lead Article Card / Device=Tablet ×1, TOP ZONE Block / Device=Tablet ×7, Latest Headlines / Device=Tablet ×6, Latest Headlines List Item / Type=First ×1, Latest Headlines List Item / Type=Standard ×1, Zone 1 Lead Article Card / Device=Desktop ×1
- **Type=Subscriber** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (direct): 768 HomePage ×1, Mobile HomePage ×1, 1024 HomePage ×1, Desktop HomePage ×1, 340 HomePage ×1, 1100 HomePage ×1; templates (via assembly): 768 HomePage (via Photos Block); nested inside: Photos Block / Device=Tablet ×1, 1Col Article Card ×1, Photos Block / Device=Mobile ×1
- **Type=Sponsored** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (direct): Desktop HomePage ×5, 1024 HomePage ×5, 1100 HomePage ×5, 340 HomePage ×1, Mobile HomePage ×1, 768 HomePage ×1; templates (via assembly): Desktop HomePage (via TOP ZONE Block), 768 HomePage (via TOP ZONE Block), Mobile HomePage (via TOP ZONE Block), 340 HomePage (via TOP ZONE Block), 1100 HomePage (via Latest Headlines List Item), 1024 HomePage (via Latest Headlines List Item); nested inside: TOP ZONE Block / Device=Desktop ×5, TOP ZONE Block / Device=Tablet ×1, TOP ZONE Block / Device=Mobile ×1, Latest Headlines / Device=Mobile ×1, Latest Headlines / Device=Desktop ×1, Latest Headlines / Device=Tablet ×1, TopZone Article Card / Device=Desktop ×1, Latest Headlines List Item / Type=Sponsored ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Type=None, Type=Subscriber, Type=Sponsored |
| 360 | ≤639px (SM-Mobile, built 360) | Type=None, Type=Subscriber, Type=Sponsored |
| 768 | 640–799px (MD-TabletV) | Type=None, Type=Subscriber, Type=Sponsored |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Type=None, Type=Subscriber, Type=Sponsored |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Type=None, Type=Subscriber, Type=Sponsored |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Type=None, Type=Subscriber, Type=Sponsored |

## Responsive rules

- Type=None: 0×0, horizontal gap 0 pad 0/0/0/0 main MIN cross MIN — renders at 340, 360, 768, 1024, 1100, 1280
- Type=Subscriber: 114×27, horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280
- Type=Sponsored: 138×27, horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- _nothing (leaf component)_

**Built into:**

- [Zone 1 Lead Article Card](../04-zone-1-lead-article-card/zone-1-lead-article-card.md)
- [TopZone Article Card](../05-topzone-article-card/topzone-article-card.md)
- [Latest Headlines List Item](../07-latest-headlines-list-item/latest-headlines-list-item.md)
- [TOP ZONE Block](../../assemblies/12-top-zone-block/top-zone-block.md)
- [1Col Article Card](../16-1col-article-card/1col-article-card.md)
- [Photos Block](../../assemblies/22-photos-block/photos-block.md)

## Anatomy

**Type=None**

```
- Type=None — component 0×0 [horizontal gap 0] (hug/hug)
```

**Type=Subscriber**

```
- Type=Subscriber — component 114×27 [horizontal gap 8] (hug/hug)
  - Subscriber Only — text 104×23 (hug/hug) "Subscriber Only"
```

**Type=Sponsored**

```
- Type=Sponsored — component 138×27 [horizontal gap 8] (hug/hug)
  - Sponsored content — text 128×23 (hug/hug) "Sponsored content"
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Type=None | 0×0 | HUG | HUG | horizontal gap 0 pad 0/0/0/0 main MIN cross MIN |  | yes |
| Type=Subscriber | 114×27 | HUG | HUG | horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER |  |  |
| Type=Sponsored | 138×27 | HUG | HUG | horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| Subscriber Only | Source Sans Pro | SemiBold | 13 | 22.652000427246094px |  | UPPER | #FFFFFF | Colors/color/gray/max |  | Subscriber Only |
| Sponsored content | Source Sans Pro | SemiBold | 13 | 22.652000427246094px |  | UPPER | #FFFFFF | Colors/color/gray/max |  | Sponsored content |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Type=Subscriber | fill | SOLID | #007580 | Colors/color/theme/primary |  |  |
| Type=Sponsored | fill | SOLID | #7D161E | ⚠ unbound |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- Variant `Type=None` is 0×0 (intentionally empty state?) — no preview exported.
- `Type=Subscriber`: fonts outside the production pair (Noto Sans / Noto Serif): Source Sans Pro SemiBold ×1.
- `Type=Sponsored`: fonts outside the production pair (Noto Sans / Noto Serif): Source Sans Pro SemiBold ×1.
- 1 solid paints are hard-coded (not bound to a color variable): #7D161E ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `article-status-badge.json` → `variants[].variantProperties`).
2. Start from `article-status-badge.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
