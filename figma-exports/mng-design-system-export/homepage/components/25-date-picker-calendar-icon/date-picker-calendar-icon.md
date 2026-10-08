---
name: "Date Picker Calendar Icon"
kind: component
group: homepage
order: 25
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3395:51892"
component_key: df272b86e43ca88b03e9da0e4ec2b5b072c19726
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Upcoming Events Calendar Glyph"]
built_into: ["Upcoming Events Widget"]
spec_json: date-picker-calendar-icon.json
skeleton: date-picker-calendar-icon.html
exported: 2026-10-08
---

# Date Picker Calendar Icon

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Upcoming Events atom. 50×50 date-strip calendar link; 25px production calendar glyph, #3B3B3B.

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Date Picker Calendar Icon](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3395-51892) · node `3395:51892` · key `df272b86e43ca88b03e9da0e4ec2b5b072c19726`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Date Picker Calendar Icon | [3395:51892](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3395-51892) | df272b86e43ca88b03e9da0e4ec2b5b072c19726 | 50×50 | ![Date Picker Calendar Icon](previews/date-picker-calendar-icon.png) |

## Properties

_None._

## Where it is used

- **Date Picker Calendar Icon** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1024 HomePage (via Upcoming Events Widget), Desktop HomePage (via Upcoming Events Widget), 768 HomePage (via Upcoming Events Widget), 1100 HomePage (via Upcoming Events Widget), Mobile HomePage (via Upcoming Events Widget), 340 HomePage (via Upcoming Events Widget); nested inside: Upcoming Events Widget / Device=1024 ×1, Upcoming Events Widget / Device=Desktop ×1, Upcoming Events Widget / Device=Tablet ×1, Upcoming Events Widget / Device=1100 ×1, Upcoming Events Widget / Device=Mobile ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Date Picker Calendar Icon |
| 360 | ≤639px (SM-Mobile, built 360) | Date Picker Calendar Icon |
| 768 | 640–799px (MD-TabletV) | Date Picker Calendar Icon |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Date Picker Calendar Icon |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Date Picker Calendar Icon |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Date Picker Calendar Icon |

## Responsive rules

- Date Picker Calendar Icon: 50×50, vertical gap 0 pad 13.5/0/0/0 main MIN cross CENTER — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- [Upcoming Events Calendar Glyph](../26-upcoming-events-calendar-glyph/upcoming-events-calendar-glyph.md) ×1

**Built into:**

- [Upcoming Events Widget](../../assemblies/29-upcoming-events-widget/upcoming-events-widget.md)

## Anatomy

**Date Picker Calendar Icon**

```
- Date Picker Calendar Icon — component 50×50 [vertical gap 0] (fixed/fixed)
  - Upcoming Events Calendar Glyph — instance 23.2×25 (fixed/fixed) → Upcoming Events Calendar Glyph
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Date Picker Calendar Icon | 50×50 | FIXED | FIXED | vertical gap 0 pad 13.5/0/0/0 main MIN cross CENTER |  |  |

## Typography

_No text._

## Color & effects

_None._

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

_None detected._

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `date-picker-calendar-icon.json` → `variants[].variantProperties`).
2. Start from `date-picker-calendar-icon.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
