---
name: "Upcoming Events Calendar Glyph"
kind: component
group: homepage
order: 26
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "3557:40167"
component_key: 5406d0073387de6c154488bd6b4260333e411b1e
variants: 1
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: []
built_into: ["Date Picker Calendar Icon", "Upcoming Events Header Button"]
spec_json: upcoming-events-calendar-glyph.json
skeleton: upcoming-events-calendar-glyph.html
exported: 2026-10-07
---

# Upcoming Events Calendar Glyph

**Component · Standalone** · Homepage components · source: WordPress Elements ▸ Homepage

> Production calendar icon from the CitySpark widget icon font (icomoon U+E603); not in the MNG icon font. Box is one em; used at 25px (date strip) and 12px (See All Events button).

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Homepage
- Main: [Upcoming Events Calendar Glyph](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3557-40167) · node `3557:40167` · key `5406d0073387de6c154488bd6b4260333e411b1e`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Upcoming Events Calendar Glyph | [3557:40167](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=3557-40167) | 5406d0073387de6c154488bd6b4260333e411b1e | 23.2×25 | ![Upcoming Events Calendar Glyph](previews/upcoming-events-calendar-glyph.png) |

## Properties

_None._

## Where it is used

- **Upcoming Events Calendar Glyph** — breakpoints: 340, 360, 768, 1024, 1100, 1280; templates (via assembly): 1100 HomePage (via Date Picker Calendar Icon, Upcoming Events Header Button), 768 HomePage (via Date Picker Calendar Icon, Upcoming Events Header Button), 1024 HomePage (via Date Picker Calendar Icon, Upcoming Events Header Button), Desktop HomePage (via Date Picker Calendar Icon, Upcoming Events Header Button), Mobile HomePage (via Date Picker Calendar Icon, Upcoming Events Header Button), 340 HomePage (via Date Picker Calendar Icon, Upcoming Events Header Button); nested inside: Date Picker Calendar Icon ×1, Upcoming Events Header Button / Type=See All Events, Label=Off ×1, Upcoming Events Header Button / Type=See All Events, Label=On ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Upcoming Events Calendar Glyph |
| 360 | ≤639px (SM-Mobile, built 360) | Upcoming Events Calendar Glyph |
| 768 | 640–799px (MD-TabletV) | Upcoming Events Calendar Glyph |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Upcoming Events Calendar Glyph |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Upcoming Events Calendar Glyph |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Upcoming Events Calendar Glyph |

## Responsive rules

- Upcoming Events Calendar Glyph: 23.2×25 — renders at 340, 360, 768, 1024, 1100, 1280

## Dependencies

**Built from:**

_Nothing — leaf component._

**Built into:**

- [Date Picker Calendar Icon](../25-date-picker-calendar-icon/date-picker-calendar-icon.md)
- [Upcoming Events Header Button](../27-upcoming-events-header-button/upcoming-events-header-button.md)

## Anatomy

**Upcoming Events Calendar Glyph**

```
- Upcoming Events Calendar Glyph — component 23.2×25
  - Calendar (CitySpark icomoon U+E603) — vector 23.2×25
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Upcoming Events Calendar Glyph | 23.2×25 |  |  |  |  |  |

## Typography

_No text._

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Calendar (CitySpark icomoon U+E603) | fill | SOLID | #3B3B3B |  |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

- `.svg`
- `cityspark.com/cdn/widget/fonts/icomoon`

## Known issues

- 1 solid paints are hard-coded (not bound to a color variable): #3B3B3B ×1.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `upcoming-events-calendar-glyph.json` → `variants[].variantProperties`).
2. Start from `upcoming-events-calendar-glyph.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
