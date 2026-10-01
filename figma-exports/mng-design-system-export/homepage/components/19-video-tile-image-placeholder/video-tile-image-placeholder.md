---
name: "Video Tile Image Placeholder"
kind: component
group: homepage
order: 19
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3419:55114"
component_key: a7a988a13b00a06452e5bc8345274ca7b07af36a
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: []
built_into: ["Videos from OCRegister Carousel"]
spec_json: video-tile-image-placeholder.json
skeleton: video-tile-image-placeholder.html
exported: 2026-09-24
---

# Video Tile Image Placeholder

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Standalone component · vertical 160×287 video tile (background, play/masthead badge, caption) used in the Videos from OCRegister Carousel tile row.

> Placeholder tile for the 'Videos from @OCRegister' carousel (160×287, portrait). Solid-color background (no boolean-op graphic — a plain rect, unlike the landscape Article Image Placeholder it was cloned from, since the diagonal-X vector distorted badly at this aspect ratio and was removed). Overlay children (Masthead Badge, Caption Background, Caption Text) use ABSOLUTE layout positioning so they don't get swept into the parent's VERTICAL auto-layout stack — this is required, not optional: AUTO positioning here silently overrides any explicit x/y.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Video Tile Image Placeholder](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55114) · node `3419:55114` · key `a7a988a13b00a06452e5bc8345274ca7b07af36a`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Video Tile Image Placeholder | [3419:55114](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55114) | a7a988a13b00a06452e5bc8345274ca7b07af36a | 160×287 | ![Video Tile Image Placeholder](previews/video-tile-image-placeholder.png) |

## Properties

_None._

## Where it is used

- **Video Tile Image Placeholder** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (direct): 1024 HomePage ×9, 1100 HomePage ×9, Mobile HomePage ×9, 340 HomePage ×9, 768 HomePage ×9, Desktop HomePage ×9; nested inside: Videos from OCRegister Carousel ×9

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Video Tile Image Placeholder |
| 360 | ≤639px (SM-Mobile, built 360) | Video Tile Image Placeholder |
| 768 | 640–799px (MD-TabletV) | Video Tile Image Placeholder |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Video Tile Image Placeholder |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Video Tile Image Placeholder |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Video Tile Image Placeholder |

## Responsive rules

- Video Tile Image Placeholder: 160×287, vertical gap 8 pad 0/0/0/0 main CENTER cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- _nothing (leaf component)_

**Built into:**

- [Videos from OCRegister Carousel](../../assemblies/20-videos-from-ocregister-carousel/videos-from-ocregister-carousel.md)

## Anatomy

**Video Tile Image Placeholder**

```
- Video Tile Image Placeholder — component 160×287 [vertical gap 8] (fixed/fixed)
  - Tile Background — rectangle 160×287 (fixed/fixed)
  - Frame 11643 — frame 65×19 [horizontal gap 8] (hug/hug)
    - ARTICLE IMAGE — text 65×19 (hug/hug) "VIDEO"
  - Masthead Badge — text 43×12 (fixed/fixed) "REGISTER"
  - Caption Background — rectangle 148×48 (fixed/fixed)
  - Caption Text — text 136×32 (fixed/fixed) "Watch our journalists cover local news i"
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Video Tile Image Placeholder | 160×287 | FIXED | FIXED | vertical gap 8 pad 0/0/0/0 main CENTER cross CENTER |  | yes |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| ARTICLE IMAGE | New York | Black | 16 | auto | 10% |  | #141414 | Colors/color/gray/min |  | VIDEO |
| Masthead Badge | Noto Sans | Bold | 9 | auto |  |  | #FFFFFF |  |  | REGISTER |
| Caption Text | Noto Sans | Regular | 9 | auto |  |  | #FFFFFF |  |  | Watch our journalists cover local news in these cl |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Video Tile Image Placeholder | fill | SOLID | #E1A1FF | ⚠ unbound |  |  |
| Video Tile Image Placeholder | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| Tile Background | fill | SOLID | #FFC76B | ⚠ unbound |  |  |
| ARTICLE IMAGE | stroke | SOLID | #F1EFEB | Colors/color/gray/600 |  |  |
| Caption Background | fill | SOLID | #000000 | ⚠ unbound | 0.55 |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- `Video Tile Image Placeholder`: fonts outside the production pair (Noto Sans / Noto Serif): New York Black ×1.
- 5 solid paints are hard-coded (not bound to a color variable): #FFFFFF ×2, #E1A1FF ×1, #FFC76B ×1, #000000 ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `video-tile-image-placeholder.json` → `variants[].variantProperties`).
2. Start from `video-tile-image-placeholder.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
