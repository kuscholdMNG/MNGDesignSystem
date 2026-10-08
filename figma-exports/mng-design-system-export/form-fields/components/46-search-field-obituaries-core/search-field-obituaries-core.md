---
name: "Search Field / Obituaries — Core"
kind: component
group: form-fields
order: 46
figma_file: "MNG Design System (jFHYqhZbJjvWQmDI4myCsd)"
figma_node: "6995:27285"
component_key: 1c628d329332b07f539d85317b98689e64fbfc81
variants: 1
breakpoints: []
built_from: []
built_into: ["Search Field / Obituaries"]
spec_json: search-field-obituaries-core.json
skeleton: search-field-obituaries-core.html
exported: 2026-10-08
---

# Search Field / Obituaries — Core

**Component · Standalone** · Form Fields · source: MNG Design System ▸ Form Fields | 2026.09.24

**Designer notes on the canvas:**

- Core visual (used internally by both Size variants above — not for direct use)

## Figma references

- File: MNG Design System (`jFHYqhZbJjvWQmDI4myCsd`) · Page: Form Fields | 2026.09.24 · Frame path: Form Field & Code Box — Documentation ▸ Frame 12860 ▸ Frame 12925 ▸ Frame 12931
- Main: [Search Field / Obituaries — Core](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6995-27285) · node `6995:27285` · key `1c628d329332b07f539d85317b98689e64fbfc81`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Search Field / Obituaries — Core | [6995:27285](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=6995-27285) | 1c628d329332b07f539d85317b98689e64fbfc81 | 472×44 | ![Search Field / Obituaries — Core](previews/search-field-obituaries-core.png) |

## Properties

_None._

## Where it is used

- **Search Field / Obituaries — Core** — breakpoints: —; nested inside: Search Field / Obituaries / Size=Desktop ×1, Search Field / Obituaries / Size=Mobile ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| — | not placed in any homepage template | — |

## Responsive rules

- Search Field / Obituaries — Core: 472×44, horizontal gap 8 pad 8/16/8/16 main SPACE_BETWEEN cross CENTER — no breakpoint (not placed in a template)

## Dependencies

**Built from:**

_Nothing — leaf component._

**Built into:**

- [Search Field / Obituaries](../../assemblies/55-search-field-obituaries/search-field-obituaries.md)

## Anatomy

**Search Field / Obituaries — Core**

```
- Search Field / Obituaries — Core — component 472×44 [horizontal gap 8] (fixed/hug)
  - Placeholder Text — text 205×22 (hug/hug) "Search Obituaries by Name"
  - Search Icons — frame 66×26 [horizontal gap 16] (hug/hug)
    - 135-search 1 — frame 26×26 (fixed/fixed)
      - Search Glyph — vector 26×26
    - equalizer2 1 — frame 24×24 (fixed/fixed)
      - Filter Glyph — vector 21×24
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Search Field / Obituaries — Core | 472×44 | FIXED | HUG | horizontal gap 8 pad 8/16/8/16 main SPACE_BETWEEN cross CENTER | 3 |  |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Placeholder Text | Noto Sans | Regular | 16 | auto |  |  | #141414 | Colors/color/gray/min | font/size/16 |  | Search Obituaries by Name | all |

## Color & effects

| Layer | Role | Type | Hex | Token | Opacity | Note |
|---|---|---|---|---|---|---|
| Search Field / Obituaries — Core | fill | SOLID | #FFFFFF | Colors/color/gray/max |  |  |
| Search Field / Obituaries — Core | stroke | SOLID | #A7A6A3 | Colors/color/gray/400 |  |  |
| Search Glyph | fill | SOLID | #141414 | Colors/color/gray/min |  |  |
| Filter Glyph | fill | SOLID | #141414 | Colors/color/gray/min |  |  |

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

_None detected._

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `search-field-obituaries-core.json` → `variants[].variantProperties`).
2. Start from `search-field-obituaries-core.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
