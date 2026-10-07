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
exported: 2026-10-07
---

# Video Tile Image Placeholder

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Standalone component · vertical 160×287 video tile (background, play/masthead badge, caption) used in the Videos from OCRegister Carousel tile row.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Video Tile Image Placeholder](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55114) · node `3419:55114` · key `a7a988a13b00a06452e5bc8345274ca7b07af36a`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Video Tile Image Placeholder | [3419:55114](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55114) | a7a988a13b00a06452e5bc8345274ca7b07af36a | 160×287 | ![Video Tile Image Placeholder](previews/video-tile-image-placeholder.png) |

## Properties

_None._

## Where it is used

- **Video Tile Image Placeholder** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via Videos from OCRegister Carousel), 1100 HomePage (via Videos from OCRegister Carousel), 340 HomePage (via Videos from OCRegister Carousel), 768 HomePage (via Videos from OCRegister Carousel), Mobile HomePage (via Videos from OCRegister Carousel), Desktop HomePage (via Videos from OCRegister Carousel); nested inside: Videos from OCRegister Carousel ×9

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

_Nothing — leaf component._

**Built into:**

- [Videos from OCRegister Carousel](../../assemblies/20-videos-from-ocregister-carousel/videos-from-ocregister-carousel.md)

## Anatomy

**Video Tile Image Placeholder**

```
- Video Tile Image Placeholder — component 160×287 [vertical gap 8] (fixed/fixed)
  - Tile Background — rectangle 160×287 (fixed/fixed)
  - Label — frame 60×22 [horizontal gap 8] (hug/hug)
    - ARTICLE IMAGE — text 60×22 (hug/hug) "VIDEO"
  - Masthead Badge — text 43×12 (fixed/fixed) "REGISTER"
  - Caption Background — rectangle 148×48 (fixed/fixed)
  - Caption Text — text 136×32 (fixed/fixed) "Watch our journalists cover local news i"
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Video Tile Image Placeholder | 160×287 | FIXED | FIXED | vertical gap 8 pad 0/0/0/0 main CENTER cross CENTER |  | yes |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ARTICLE IMAGE | Noto Serif | Bold | 16 | auto | 10% |  | #141414 | Colors/color/gray/min |  |  | VIDEO | all |
| Masthead Badge | Noto Sans | Bold | 9 | auto |  |  | #FFFFFF | Colors/color/gray/max |  |  | REGISTER | all |
| Caption Text | Noto Sans | Regular | 9 | auto |  |  | #FFFFFF | Colors/color/gray/max |  |  | Watch our journalists cover local news in these cl | all |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Video Tile Image Placeholder | fill | SOLID | #E1A1FF |  |  | image placeholder fill |
| Video Tile Image Placeholder | stroke | SOLID | #141414 | Colors/color/gray/min |  |  |
| Tile Background | fill | SOLID | #FFC76B |  |  | video placeholder accent |
| Caption Background | fill | SOLID | #000000 | Colors/color/gray/black |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- 2 solid paints are hard-coded (not bound to a color variable): #E1A1FF ×1, #FFC76B ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `video-tile-image-placeholder.json` → `variants[].variantProperties`).
2. Start from `video-tile-image-placeholder.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
