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
built_into: ["Zone 1 Lead Article Card", "TopZone Article Card", "Latest Headlines List Item", "1Col Article Card"]
spec_json: article-status-badge.json
skeleton: article-status-badge.html
exported: 2026-10-08
---

# Article Status Badge

**Component · 3 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Type = None, Subscriber, Sponsored (replaces the old separate Subscriber Only Badge / Sponsored Content Tag atoms)

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Article Status Badge](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63995) · node `3344:63995` · key `a3c41dc84d271d8fadbefb86d033afe3706c21b6`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Type=None | [3344:63994](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63994) | 4bbcedebfb8a8e0b414d8217830d29de5fea2b5e | 0×0 | _none (0×0)_ |
| Type=Subscriber | [3344:63989](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63989) | 3d7f0e03fdd71c7edddda24d4c13fadddb581fbd | 127×27 | ![Type=Subscriber](previews/article-status-badge--subscriber.png) |
| Type=Sponsored | [3344:63991](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3344-63991) | 2cba7cf7dd45bbf3b7d1d71d53de2acd577e3217 | 153×27 | ![Type=Sponsored](previews/article-status-badge--sponsored.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Type | VARIANT | None | Subscriber, Sponsored, None |

## Where it is used

- **Type=None** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1100 HomePage (via Latest Headlines List Item, TopZone Article Card, Zone 1 Lead Article Card), 1024 HomePage (via Latest Headlines List Item, Zone 1 Lead Article Card), Mobile HomePage (via Latest Headlines List Item, TopZone Article Card, Zone 1 Lead Article Card), 340 HomePage (via Latest Headlines List Item, TopZone Article Card, Zone 1 Lead Article Card), Desktop HomePage (via Latest Headlines List Item, Zone 1 Lead Article Card), 768 HomePage (via Latest Headlines List Item, Zone 1 Lead Article Card); nested inside: Zone 1 Lead Article Card / Device=Mobile ×1, TopZone Article Card / Device=1100 ×1, Latest Headlines List Item / Type=Standard ×1, Zone 1 Lead Article Card / Device=Desktop ×1, Zone 1 Lead Article Card / Device=Tablet ×1, Latest Headlines List Item / Type=First ×1, TopZone Article Card / Device=Mobile ×1
- **Type=Subscriber** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via 1Col Article Card), Mobile HomePage (via 1Col Article Card), 340 HomePage (via 1Col Article Card), 1100 HomePage (via 1Col Article Card), 768 HomePage (via 1Col Article Card), Desktop HomePage (via 1Col Article Card); nested inside: 1Col Article Card / Style=Media Lead ×1, 1Col Article Card / Style=Standard ×1
- **Type=Sponsored** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via Latest Headlines List Item, TopZone Article Card), Desktop HomePage (via Latest Headlines List Item, TopZone Article Card), 1100 HomePage (via Latest Headlines List Item), Mobile HomePage (via Latest Headlines List Item), 340 HomePage (via Latest Headlines List Item), 768 HomePage (via Latest Headlines List Item); nested inside: TopZone Article Card / Device=1024 ×1, TopZone Article Card / Device=Desktop ×1, Latest Headlines List Item / Type=Sponsored ×1

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
- Type=Subscriber: 127×27, horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280
- Type=Sponsored: 153×27, horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

_Nothing — leaf component._

**Built into:**

- [Zone 1 Lead Article Card](../04-zone-1-lead-article-card/zone-1-lead-article-card.md)
- [TopZone Article Card](../05-topzone-article-card/topzone-article-card.md)
- [Latest Headlines List Item](../07-latest-headlines-list-item/latest-headlines-list-item.md)
- [1Col Article Card](../16-1col-article-card/1col-article-card.md)

## Anatomy

**Type=None**

```
- Type=None — component 0×0 [horizontal gap 0] (hug/hug)
```

**Type=Subscriber**

```
- Type=Subscriber — component 127×27 [horizontal gap 8] (hug/hug)
  - Subscriber Only — text 117×23 (hug/hug) "Subscriber Only"
```

**Type=Sponsored**

```
- Type=Sponsored — component 153×27 [horizontal gap 8] (hug/hug)
  - Sponsored content — text 143×23 (hug/hug) "Sponsored content"
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Type=None | 0×0 | HUG | HUG | horizontal gap 0 pad 0/0/0/0 main MIN cross MIN |  | yes |
| Type=Subscriber | 127×27 | HUG | HUG | horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER |  |  |
| Type=Sponsored | 153×27 | HUG | HUG | horizontal gap 8 pad 2/5/2/5 main CENTER cross CENTER |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Subscriber Only | Noto Sans | SemiBold | 13 | 22.65px |  | UPPER | #FFFFFF | Colors/color/gray/max | font/size/13 |  | Subscriber Only | Type=Subscriber |
| Sponsored content | Noto Sans | SemiBold | 13 | 22.65px |  | UPPER | #FFFFFF | Colors/color/gray/max | font/size/13 |  | Sponsored content | Type=Sponsored |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Type=Subscriber | fill | SOLID | #007580 | Colors/color/theme/primary |  |  |
| Type=Sponsored | fill | SOLID | #7D161E |  |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- Variant `Type=None` is 0×0 (intentionally empty state?) — no preview exported.
- 1 solid paints are hard-coded (not bound to a color variable): #7D161E ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `article-status-badge.json` → `variants[].variantProperties`).
2. Start from `article-status-badge.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
