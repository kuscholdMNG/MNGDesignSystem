---
name: "Videos from OCRegister Carousel"
kind: assembly
group: homepage
order: 20
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3419:55122"
component_key: 8440dab024c062758ef2eefdac32320283804015
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Video Tile Image Placeholder"]
built_into: []
spec_json: videos-from-ocregister-carousel.json
skeleton: videos-from-ocregister-carousel.html
exported: 2026-09-24
---

# Videos from OCRegister Carousel

**Assembly · 2 components** · Homepage components · source: WordPress Elements ▸ Homepage

> Instagram video carousel (header + Video Tile Image Placeholder row + scroll indicator), instanced on every homepage breakpoint. Two main components share this name: the populated one used by the templates, and an empty 1245×100 shell with no layers that no template references — flagged for review/removal.

> Real production content block: 'Videos from @OCRegister' (prod selector .dfm-page-middle-flex-container), a Flourish-embedded horizontal video carousel that sits between the four-across/category row and the Photos block on every breakpoint. Built as a FILL-width header/subtitle/tile-row/scroll-indicator stack; the Tile Row uses clipsContent=true to simulate horizontal scroll — extra tiles beyond the visible width are intentionally clipped, not a layout bug. Placed as instances in all 6 homepage assemblies (Mobile/340/768/1024/Desktop/1100), each set to layoutSizingHorizontal=FILL to match its container's content width. See homepage-template-audit.md section on the video carousel build for full detail.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Videos from OCRegister Carousel](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55122) · node `3419:55122` · key `8440dab024c062758ef2eefdac32320283804015`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Videos from OCRegister Carousel | [3419:55122](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55122) | 8440dab024c062758ef2eefdac32320283804015 | 1245×404 | ![Videos from OCRegister Carousel](previews/videos-from-ocregister-carousel.png) |
| Videos from OCRegister Carousel | [3419:55120](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3419-55120) | b83dd4446cceb462b97bb4c4cd9a3487566cd7aa | 1245×100 | ![Videos from OCRegister Carousel](previews/videos-from-ocregister-carousel-2.png) |

## Properties

_None._

## Where it is used

- **Videos from OCRegister Carousel** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (direct): 1024 HomePage ×1, 1100 HomePage ×1, 340 HomePage ×1, 768 HomePage ×1, Mobile HomePage ×1, Desktop HomePage ×1
- **Videos from OCRegister Carousel** — breakpoints: —; no instances found

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Videos from OCRegister Carousel |
| 360 | ≤639px (SM-Mobile, built 360) | Videos from OCRegister Carousel |
| 768 | 640–799px (MD-TabletV) | Videos from OCRegister Carousel |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Videos from OCRegister Carousel |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Videos from OCRegister Carousel |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Videos from OCRegister Carousel |

## Responsive rules

- Videos from OCRegister Carousel: 1245×404, vertical gap 8 pad 16/0/16/0 main MIN cross MIN — renders at 340, 360, 768, 1024, 1100, 1280
- Videos from OCRegister Carousel: 1245×100, vertical gap 8 pad 16/0/16/0 main MIN cross MIN — renders at (no breakpoint evidence)

## Dependencies

**Built from:**

- [Video Tile Image Placeholder](../../components/19-video-tile-image-placeholder/video-tile-image-placeholder.md) ×9

**Built into:**

- _no parent in this export_

## Anatomy

**Videos from OCRegister Carousel**

```
- Videos from OCRegister Carousel — component 1245×404 [vertical gap 8] (fixed/hug)
  - Videos from @OCRegister — text 1245×35 (fill/hug) "Videos from @OCRegister"
  - Watch as our journalists report on our local news coverage in these Instagram videos. — text 1245×20 (fill/hug) "Watch as our journalists report on our l"
  - Tile Row — frame 1245×287 [horizontal gap 8] (fill/fixed)
    - Video Tile Image Placeholder — instance 160×287 [vertical gap 8] (fixed/fixed) → Video Tile Image Placeholder ×9
  - Scroll Indicator Track — frame 1245×6 (fill/fixed)
    - Scroll Indicator Thumb — rectangle 224.1×6
```

**Videos from OCRegister Carousel**

```
- Videos from OCRegister Carousel — component 1245×100 [vertical gap 8] (fixed/hug)
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Videos from OCRegister Carousel | 1245×404 | FIXED | HUG | vertical gap 8 pad 16/0/16/0 main MIN cross MIN |  |  |
| Videos from OCRegister Carousel | 1245×100 | FIXED | HUG | vertical gap 8 pad 16/0/16/0 main MIN cross MIN |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| Videos from @OCRegister | Noto Serif | Bold | 26 | auto |  |  | #141414 |  |  | Videos from @OCRegister |
| Videos from @OCRegister | Noto Serif | Bold | 26 | auto |  |  | #1651BA |  |  | Videos from @OCRegister |
| Watch as our journalists report on our local news coverage in these Instagram videos. | Noto Sans | Regular | 15 | auto |  |  | #393938 |  |  | Watch as our journalists report on our local news  |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Videos from OCRegister Carousel | fill | SOLID | #FFFFFF | ⚠ unbound |  |  |
| Scroll Indicator Track | fill | SOLID | #E5E4E1 | ⚠ unbound |  |  |
| Scroll Indicator Thumb | fill | SOLID | #B2B1AD | ⚠ unbound |  |  |

## Image ratios

| Variant | Layer | Size | Ratio | Source |
|---|---|---|---|---|
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |
| Videos from OCRegister Carousel | Video Tile Image Placeholder | 160×287 | 9:16 | Video Tile Image Placeholder |

## Ad slots

_None._

## Production references

- `.dfm-page-middle-flex-container`

## Known issues

- 1 of 2 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Videos from OCRegister Carousel`.
- 7 solid paints are hard-coded (not bound to a color variable): #FFFFFF ×2, #141414 ×1, #1651BA ×1, #393938 ×1, #E5E4E1 ×1, #B2B1AD ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `videos-from-ocregister-carousel.json` → `variants[].variantProperties`).
2. Start from `videos-from-ocregister-carousel.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
