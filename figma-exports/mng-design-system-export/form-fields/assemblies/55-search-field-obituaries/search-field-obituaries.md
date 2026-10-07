---
name: "Search Field / Obituaries"
kind: assembly
group: form-fields
order: 55
figma_file: "MNG Design System (jFHYqhZbJjvWQmDI4myCsd)"
figma_node: "6996:27351"
component_key: 39edef9096118c31c76c65dc3692f0ec90a960ff
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Search Field / Obituaries — Core"]
built_into: []
spec_json: search-field-obituaries.json
skeleton: search-field-obituaries.html
exported: 2026-10-07
---

# Search Field / Obituaries

**Assembly · 2 variants** · Form Fields · source: MNG Design System ▸ Form Fields | 2026.09.24

## Figma references

- File: MNG Design System (`jFHYqhZbJjvWQmDI4myCsd`) · Page: Form Fields | 2026.09.24 · Frame path: Form Field & Code Box — Documentation ▸ Frame 12860 ▸ Frame 12925 ▸ Frame 12928
- Main: [Search Field / Obituaries](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6996-27351) · node `6996:27351` · key `39edef9096118c31c76c65dc3692f0ec90a960ff`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Size=Mobile | [6996:27287](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6996-27287) | b55c86f116b0e5ee0fcc77d6decc770421381fd6 | 486.4×64 | ![Size=Mobile](previews/search-field-obituaries--mobile.png) |
| Size=Desktop | [6996:27295](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6996-27295) | 50fa352fc2998e5e1817942dbbb2fce3b69bcb49 | 497.6×74 | ![Size=Desktop](previews/search-field-obituaries--desktop.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Size | VARIANT | Mobile | Mobile, Desktop |

## Where it is used

- **Size=Mobile** — breakpoints: 340, 360; no instances in this file
- **Size=Desktop** — breakpoints: 768, 1024, 1100, 1280; no instances in this file

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Size=Mobile |
| 360 | ≤639px (SM-Mobile, built 360) | Size=Mobile |
| 768 | 640–799px (MD-TabletV) | Size=Desktop |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Size=Desktop |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Size=Desktop |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Size=Desktop |

## Responsive rules

- Size=Mobile: 486.4×64, horizontal gap 0 pad 10/7.2/10/7.2 main MIN cross MIN — renders at 340, 360
- Size=Desktop: 497.6×74, horizontal gap 0 pad 15/12.8/15/12.8 main MIN cross MIN — renders at 768, 1024, 1100, 1280

## Dependencies

**Built from:**

- [Search Field / Obituaries — Core](../../components/46-search-field-obituaries-core/search-field-obituaries-core.md) ×1

**Built into:**

_Not used inside another exported item._

## Anatomy

**Size=Mobile**

```
- Size=Mobile — component 486.4×64 [horizontal gap 0] (hug/hug)
  - Search Field / Obituaries — Core — instance 472×44 [horizontal gap 8] (fixed/hug) → Search Field / Obituaries — Core
```

**Size=Desktop**

```
- Size=Desktop — component 497.6×74 [horizontal gap 0] (hug/hug)
  - Search Field / Obituaries — Core — instance 472×44 [horizontal gap 8] (fixed/hug) → Search Field / Obituaries — Core
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Size=Mobile | 486.4×64 | HUG | HUG | horizontal gap 0 pad 10/7.2/10/7.2 main MIN cross MIN |  |  |
| Size=Desktop | 497.6×74 | HUG | HUG | horizontal gap 0 pad 15/12.8/15/12.8 main MIN cross MIN |  |  |

## Typography

_No text._

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Search Field / Obituaries — Core | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Search Field / Obituaries — Core | stroke | SOLID | #A7A6A3 | Colors/color/gray/400 |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- No variant has instances in MNG Design System (unused here, or used only from another file): `Size=Mobile`, `Size=Desktop`.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `search-field-obituaries.json` → `variants[].variantProperties`).
2. Start from `search-field-obituaries.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
