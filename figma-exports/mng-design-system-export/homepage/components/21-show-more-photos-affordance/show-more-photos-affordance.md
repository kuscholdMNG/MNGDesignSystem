---
name: "Show More Photos Affordance"
kind: component
group: homepage
order: 21
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3352:24180"
component_key: df4464b15997ef2b7b310ca9cd6a8b427de277a7
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: []
built_into: ["Photos Block"]
spec_json: show-more-photos-affordance.json
skeleton: show-more-photos-affordance.html
exported: 2026-09-24
---

# Show More Photos Affordance

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Standalone component · freely resizable, no variants · the divider + "Show More Photos" affordance at the bottom of Photos Block.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Show More Photos Affordance](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-24180) · node `3352:24180` · key `df4464b15997ef2b7b310ca9cd6a8b427de277a7`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Show More Photos Affordance | [3352:24180](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-24180) | df4464b15997ef2b7b310ca9cd6a8b427de277a7 | 793×136.7 | ![Show More Photos Affordance](previews/show-more-photos-affordance.png) |

## Properties

_None._

## Where it is used

- **Show More Photos Affordance** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (direct): Desktop HomePage ×1, 1100 HomePage ×1, 1024 HomePage ×1, Mobile HomePage ×1, 340 HomePage ×1, 768 HomePage ×1; templates (via assembly): 768 HomePage (via Photos Block); nested inside: Photos Block / Device=Mobile ×1, Photos Block / Device=Desktop ×1, Photos Block / Device=Tablet ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Show More Photos Affordance |
| 360 | ≤639px (SM-Mobile, built 360) | Show More Photos Affordance |
| 768 | 640–799px (MD-TabletV) | Show More Photos Affordance |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Show More Photos Affordance |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Show More Photos Affordance |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Show More Photos Affordance |

## Responsive rules

- Show More Photos Affordance: 793×136.7, vertical gap 4 pad 0/0/40/0 main MIN cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- _nothing (leaf component)_

**Built into:**

- [Photos Block](../../assemblies/22-photos-block/photos-block.md)

## Anatomy

**Show More Photos Affordance**

```
- Show More Photos Affordance — component 793×136.7 [vertical gap 4] (fixed/hug)
  - Frame 342 — frame 793×70.7 [horizontal gap 0] (fill/hug)
    - Line 1 — line 361.1×0 (fill/fixed)
    - Rectangle 11 — rectangle 50×50 (fixed/fixed)
    - Line 2 — line 361.1×0 (fill/fixed)
  - Show More Photos — text 193×22 (hug/hug) "Show More Photos"
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Show More Photos Affordance | 793×136.7 | FIXED | HUG | vertical gap 4 pad 0/0/40/0 main MIN cross CENTER |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| Show More Photos | Droid Sans | Bold | 19 | auto |  | UPPER | #007580 | Colors/color/theme/primary |  | Show More Photos |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Line 1 | stroke | SOLID | #CCCAC7 | Colors/color/gray/500 |  |  |
| Rectangle 11 | fill | SOLID | #F1EFEB | Colors/color/gray/600 |  |  |
| Rectangle 11 | stroke | SOLID | #CCCAC7 | Colors/color/gray/500 |  |  |
| Line 2 | stroke | SOLID | #CCCAC7 | Colors/color/gray/500 |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- `Show More Photos Affordance`: fonts outside the production pair (Noto Sans / Noto Serif): Droid Sans Bold ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `show-more-photos-affordance.json` → `variants[].variantProperties`).
2. Start from `show-more-photos-affordance.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
