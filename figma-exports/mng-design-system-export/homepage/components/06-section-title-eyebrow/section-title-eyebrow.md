---
name: "Section Title / Eyebrow"
kind: component
group: homepage
order: 6
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3333:42278"
component_key: 5328709ebbc037e3ef524cab212533ccb6fb6465
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Icons"]
built_into: ["Latest Headlines", "Blueconic Block (Most Popular)", "Section Rail Card", "Photos Block"]
spec_json: section-title-eyebrow.json
skeleton: section-title-eyebrow.html
exported: 2026-10-07
---

# Section Title / Eyebrow

**Component · 2 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Style = Underline, Bold · Chevron = boolean, shows/hides the arrow-right icon (off by default)

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Section Title / Eyebrow](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3333-42278) · node `3333:42278` · key `5328709ebbc037e3ef524cab212533ccb6fb6465`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Style=Underline | [3326:41622](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3326-41622) | 8cbeba34f69a91292d5ce8b48f38eefb62195044 | 212×30 | ![Style=Underline](previews/section-title-eyebrow--underline.png) |
| Style=Bold | [3333:42270](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3333-42270) | 62d8b4021212e9b55d09fc65291f260b942afe8a | 211×27 | ![Style=Bold](previews/section-title-eyebrow--bold.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Chevron | BOOLEAN | True |  |
| Style | VARIANT | Underline | Underline, Bold |

## Where it is used

- **Style=Underline** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via Blueconic Block (Most Popular), Latest Headlines, Photos Block, Section Rail Card), Desktop HomePage (via Blueconic Block (Most Popular), Latest Headlines, Photos Block, Section Rail Card), 1100 HomePage (via Blueconic Block (Most Popular), Latest Headlines, Photos Block, Section Rail Card), 768 HomePage (via Blueconic Block (Most Popular), Latest Headlines, Photos Block, Section Rail Card), Mobile HomePage (via Blueconic Block (Most Popular), Latest Headlines, Photos Block, Section Rail Card), 340 HomePage (via Blueconic Block (Most Popular), Latest Headlines, Photos Block, Section Rail Card); nested inside: Section Rail Card / Device=1024, Layout=Wide ×1, Photos Block / Device=Desktop ×1, Section Rail Card / Device=1280, Layout=Wide ×1, Section Rail Card / Device=1100, Layout=Narrow ×1, Blueconic Block (Most Popular) / Device=1024 ×1, Section Rail Card / Device=Tablet, Layout=Wide ×1, Section Rail Card / Device=Tablet, Layout=Narrow ×1, Section Rail Card / Device=1100, Layout=Wide ×1, Blueconic Block (Most Popular) / Device=Tablet ×1, Section Rail Card / Device=Desktop, Layout=Narrow ×1, Blueconic Block (Most Popular) / Device=Mobile ×1, Photos Block / Device=1024 ×1, Latest Headlines / Device=Desktop ×1, Blueconic Block (Most Popular) / Device=1100 ×1, Section Rail Card / Device=1024, Layout=Narrow ×1, Photos Block / Device=1100 ×1, Photos Block / Device=Tablet ×1, Latest Headlines / Device=Tablet ×1, Blueconic Block (Most Popular) / Device=1280 ×1, Latest Headlines / Device=Mobile ×1, Blueconic Block (Most Popular) / Device=Desktop ×1, Photos Block / Device=Mobile ×1, Section Rail Card / Device=Mobile, Layout=Narrow ×1, Photos Block / Device=1280 ×1
- **Style=Bold** — breakpoints: —; no instances in this file

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Style=Underline |
| 360 | ≤639px (SM-Mobile, built 360) | Style=Underline |
| 768 | 640–799px (MD-TabletV) | Style=Underline |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Style=Underline |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Style=Underline |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Style=Underline |

## Responsive rules

- Style=Underline: 212×30, vertical gap 6 pad 0/0/0/0 main MIN cross MIN — renders at 340, 360, 768, 1024, 1100, 1280
- Style=Bold: 211×27, vertical gap 0 pad 0/0/0/0 main MIN cross MIN — no breakpoint (not placed in a template)

## Dependencies

**Built from:**

- Icons ×1 _(not in this export)_

**Built into:**

- [Latest Headlines](../../assemblies/09-latest-headlines/latest-headlines.md)
- [Blueconic Block (Most Popular)](../../assemblies/14-blueconic-block-most-popular/blueconic-block-most-popular.md)
- [Section Rail Card](../../assemblies/18-section-rail-card/section-rail-card.md)
- [Photos Block](../../assemblies/22-photos-block/photos-block.md)

## Anatomy

**Style=Underline**

```
- Style=Underline — component 212×30 [vertical gap 6] (fixed/hug)
  - Title Row — frame 212×22 [horizontal gap 6] (hug/hug)
    - Latest Headlines — text 190×22 (hug/hug) "Latest Headlines"
    - Icons — instance 16×16 [horizontal gap 8] (fixed/fixed) → Icons [Name=arrow-right2]
  - Underline — rectangle 212×2 (fill/fixed)
```

**Style=Bold**

```
- Style=Bold — component 211×27 [vertical gap 0] (hug/hug)
  - Title Row — frame 211×27 [horizontal gap 6] (hug/hug)
    - Latest Headlines — text 189×27 (hug/hug) "Latest Headlines"
    - Icons — instance 16×16 [horizontal gap 8] (fixed/fixed) → Icons [Name=arrow-right2]
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Style=Underline | 212×30 | FIXED | HUG | vertical gap 6 pad 0/0/0/0 main MIN cross MIN |  |  |
| Style=Bold | 211×27 | HUG | HUG | vertical gap 0 pad 0/0/0/0 main MIN cross MIN |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Latest Headlines | Noto Sans | Regular | 20 | 22px | 0.7px | UPPER | #393938 | Colors/color/gray/100 | font/theme |  | Latest Headlines | Style=Underline |
| Latest Headlines | Noto Sans | Regular | 20 | auto | 0.595px | UPPER | #007580 | Colors/color/theme/primary | font/theme |  | Latest Headlines | Style=Bold |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Underline | fill | SOLID | #007580 | Colors/color/theme/primary |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

- `chicagotribune.com`

## Known issues

- 1 of 2 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Style=Bold`.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `section-title-eyebrow.json` → `variants[].variantProperties`).
2. Start from `section-title-eyebrow.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
