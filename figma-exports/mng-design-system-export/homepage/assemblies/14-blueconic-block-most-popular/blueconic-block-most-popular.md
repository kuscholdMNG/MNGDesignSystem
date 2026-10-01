---
name: "Blueconic Block (Most Popular)"
kind: assembly
group: homepage
order: 14
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3352:20526"
component_key: 82f5635bacf305c14f58abc48d2f3eadf4a3258f
variants: 3
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Section Title / Eyebrow", "Most Popular List Item"]
built_into: []
spec_json: blueconic-block-most-popular.json
skeleton: blueconic-block-most-popular.html
exported: 2026-09-24
---

# Blueconic Block (Most Popular)

**Assembly · 3 variants** · Homepage components · source: WordPress Elements ▸ Homepage

> Component set · Variant: Device = Desktop, Mobile · reused as instances in the assembled Desktop and Mobile pages and in both raw section libraries.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Blueconic Block (Most Popular)](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20526) · node `3352:20526` · key `82f5635bacf305c14f58abc48d2f3eadf4a3258f`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Device=Mobile | [3352:20525](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20525) | 2369e9662f5695c6f298f9e06e82f7a206147afa | 438×610 | ![Device=Mobile](previews/blueconic-block-most-popular--mobile.png) |
| Device=Tablet | [3383:46926](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3383-46926) | fb617dc46b7ad6d451fe1864c6f5a29eeca9dc9c | 748×382 | ![Device=Tablet](previews/blueconic-block-most-popular--tablet.png) |
| Device=Desktop | [3352:20524](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3352-20524) | acff982b4c1448f9efd7dc4e472a3a4a60e0db18 | 1280×600 | ![Device=Desktop](previews/blueconic-block-most-popular--desktop.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Device | VARIANT | Mobile | Desktop, Mobile, Tablet |

## Where it is used

- **Device=Mobile** — breakpoints: 340, 360; templates (direct): Mobile HomePage ×1, 340 HomePage ×1
- **Device=Tablet** — breakpoints: 768; templates (direct): 768 HomePage ×1
- **Device=Desktop** — breakpoints: 1024, 1100, 1280; no instances found

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Device=Mobile |
| 360 | ≤639px (SM-Mobile, built 360) | Device=Mobile |
| 768 | 640–799px (MD-TabletV) | Device=Tablet |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Device=Desktop |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Device=Desktop |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Device=Desktop |

## Responsive rules

- Device=Mobile: 438×610, vertical gap 16 pad 0/0/0/0 main MIN cross CENTER — renders at 340, 360
- Device=Tablet: 748×382, vertical gap 16 pad 0/0/0/0 main MIN cross CENTER — renders at 768
- Device=Desktop: 1280×600, horizontal gap 16 pad 0/0/0/0 main MIN cross MIN — renders at 1024, 1100, 1280

## Dependencies

**Built from:**

- [Section Title / Eyebrow](../../components/06-section-title-eyebrow/section-title-eyebrow.md) ×3
- [Most Popular List Item](../../components/13-most-popular-list-item/most-popular-list-item.md) ×30

**Built into:**

- _no parent in this export_

## Anatomy

**Device=Mobile**

```
- Device=Mobile — component 438×610 [vertical gap 16] (fixed/hug)
  - Content Container — frame 438×610 [vertical gap 0] (fill/hug)
    - Blueconic Header MOBILE — frame 438×30 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 438×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - List Container — frame 438×548 [horizontal gap 16] (fill/hug)
      - 1st Column — frame 438×516 [vertical gap 6] (fill/hug)
        - … 10 children
```

**Device=Tablet**

```
- Device=Tablet — component 748×382 [vertical gap 16] (fixed/hug)
  - Content Container — frame 748×382 [vertical gap 0] (fill/hug)
    - Blueconic Header MOBILE — frame 748×30 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 748×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - List Container — frame 748×320 [horizontal gap 16] (fill/hug)
      - 1st Column — frame 366×266 [vertical gap 6] (fill/hug)
        - … 5 children
      - 2nd Column — frame 366×288 [vertical gap 6] (fill/hug)
        - … 5 children
```

**Device=Desktop**

```
- Device=Desktop — component 1280×600 [horizontal gap 16] (fixed/fixed)
  - Content Container — frame 1280×302 [vertical gap 0] (fill/hug)
    - Blueconic 3Col Header — frame 1280×30 [vertical gap 4] (fill/hug)
      - Section Title / Eyebrow — instance 1280×30 [vertical gap 6] (fill/hug) → Section Title / Eyebrow [Style=Underline]
    - Items Container — frame 1280×240 [horizontal gap 16] (fill/hug)
      - 1st Column — frame 632×196 [vertical gap 6] (fill/hug)
        - … 5 children
      - 2nd Column — frame 632×208 [vertical gap 6] (fill/hug)
        - … 5 children
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Device=Mobile | 438×610 | FIXED | HUG | vertical gap 16 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Device=Tablet | 748×382 | FIXED | HUG | vertical gap 16 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Device=Desktop | 1280×600 | FIXED | FIXED | horizontal gap 16 pad 0/0/0/0 main MIN cross MIN |  |  |

## Typography

_None._

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Device=Mobile | fill | SOLID | #FFFFFF | ⚠ unbound |  |  |
| Content Container | fill | SOLID | #FFFFFF | ⚠ unbound |  |  |
| Blueconic Header MOBILE | fill | SOLID | #FFFFFF | ⚠ unbound |  |  |
| List Container | fill | SOLID | #FFFFFF | ⚠ unbound |  |  |
| Device=Tablet | fill | SOLID | #FFFFFF | ⚠ unbound |  |  |
| Device=Desktop | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Content Container | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Blueconic 3Col Header | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Items Container | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- 1 of 3 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Device=Desktop`.
- 8 solid paints are hard-coded (not bound to a color variable): #FFFFFF ×8.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `blueconic-block-most-popular.json` → `variants[].variantProperties`).
2. Start from `blueconic-block-most-popular.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
