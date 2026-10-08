---
name: "Date Picker Day"
kind: component
group: homepage
order: 24
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3395:51889"
component_key: 7b0015814ba0dd09c777e8f126ceb11608e6bf0d
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: []
built_into: ["Upcoming Events Widget"]
spec_json: date-picker-day.json
skeleton: date-picker-day.html
exported: 2026-10-08
---

# Date Picker Day

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Upcoming Events atom. 50×50: day 15/20 uppercase, date 20/19, #3B3B3B, no fill or border.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Date Picker Day](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3395-51889) · node `3395:51889` · key `7b0015814ba0dd09c777e8f126ceb11608e6bf0d`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Date Picker Day | [3395:51889](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3395-51889) | 7b0015814ba0dd09c777e8f126ceb11608e6bf0d | 50×50 | ![Date Picker Day](previews/date-picker-day.png) |

## Properties

_None._

## Where it is used

- **Date Picker Day** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): Mobile HomePage (via Upcoming Events Widget), 340 HomePage (via Upcoming Events Widget), 1024 HomePage (via Upcoming Events Widget), Desktop HomePage (via Upcoming Events Widget), 1100 HomePage (via Upcoming Events Widget), 768 HomePage (via Upcoming Events Widget); nested inside: Upcoming Events Widget / Device=Mobile ×5, Upcoming Events Widget / Device=1024 ×12, Upcoming Events Widget / Device=Desktop ×18, Upcoming Events Widget / Device=1100 ×14, Upcoming Events Widget / Device=Tablet ×7

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Date Picker Day |
| 360 | ≤639px (SM-Mobile, built 360) | Date Picker Day |
| 768 | 640–799px (MD-TabletV) | Date Picker Day |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Date Picker Day |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Date Picker Day |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Date Picker Day |

## Responsive rules

- Date Picker Day: 50×50, vertical gap 0 pad 6/0/0/0 main MIN cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

_Nothing — leaf component._

**Built into:**

- [Upcoming Events Widget](../../assemblies/29-upcoming-events-widget/upcoming-events-widget.md)

## Anatomy

**Date Picker Day**

```
- Date Picker Day — component 50×50 [vertical gap 0] (fixed/fixed)
  - Mon — text 37×20 (hug/hug) "Mon"
  - 14 — text 23×19 (hug/hug) "14"
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Date Picker Day | 50×50 | FIXED | FIXED | vertical gap 0 pad 6/0/0/0 main MIN cross CENTER |  |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mon | Noto Sans | Regular | 15 | 20px |  | UPPER | #3B3B3B |  | font/size/15 |  | Mon | all |
| 14 | Noto Sans | Regular | 20 | 19px |  |  | #3B3B3B |  | font/size/20 |  | 14 | all |

## Color & effects

_None._

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- 2 solid paints are hard-coded (not bound to a color variable): #3B3B3B ×2.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `date-picker-day.json` → `variants[].variantProperties`).
2. Start from `date-picker-day.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
