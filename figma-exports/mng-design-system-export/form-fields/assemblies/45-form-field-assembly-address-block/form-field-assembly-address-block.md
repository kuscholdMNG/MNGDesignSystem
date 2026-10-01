---
name: "Form Field Assembly / Address block"
kind: assembly
group: form-fields
order: 45
figma_file: "MNG Design System (jFHYqhZbJjvWQmDI4myCsd)"
figma_node: "7003:28741"
component_key: 14866950667431f609aecef5e9619766db2e4043
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Form Field"]
built_into: []
spec_json: form-field-assembly-address-block.json
skeleton: form-field-assembly-address-block.html
exported: 2026-09-24
---

# Form Field Assembly / Address block

**Assembly · 2 variants** · Form Fields · source: MNG Design System ▸ Form Fields | 2026.09.24

**Designer notes on the canvas:**

- Street Address as a full-width Form Field instance, followed by City / State / Zip Code in a row. State (2 chars) and Zip Code (5 digits) are auto-sized to fit their own label/value content - Figma measures the actual rendered text (not a guessed number), so the box is always exactly as wide as it needs to be and re-measures itself whenever the label, placeholder, or font size changes. Currently: Desktop State 55px, Zip 84px; Mobile State 53px, Zip 78px. City takes the rest of the row (Fill sizing) since city names vary in length. Desktop: 16px gaps, 8px vertical spacing between rows. Mobile: 

## Figma references

- File: MNG Design System (`jFHYqhZbJjvWQmDI4myCsd`) · Page: Form Fields | 2026.09.24 · Frame path: Form Field & Code Box — Documentation ▸ Frame 12911 ▸ Frame 12918 ▸ Assembly: Address block — Documentation ▸ Frame 11535 ▸ Frame 11522
- Main: [Form Field Assembly / Address block](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7003-28741) · node `7003:28741` · key `14866950667431f609aecef5e9619766db2e4043`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Size=Desktop | [7003:28703](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7003-28703) | 8fe07ae994166bcba317c8bf181571f64bea9ae7 | 480×197 | ![Size=Desktop](previews/form-field-assembly-address-block--desktop.png) |
| Size=Mobile | [7003:28740](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7003-28740) | 78b5c0d55e6ffa225167f03410f65fb992d76fe5 | 328×148 | ![Size=Mobile](previews/form-field-assembly-address-block--mobile.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Error message | TEXT | Error message text. |  |
| Show error | BOOLEAN | False |  |
| Size | VARIANT | Desktop | Desktop, Mobile |

## Where it is used

- **Size=Desktop** — breakpoints: 768, 1024, 1100, 1280; no instances found
- **Size=Mobile** — breakpoints: 340, 360; no instances found

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

- Size=Desktop: 480×197, vertical gap 8 pad 0/0/0/0 main MIN cross MIN — renders at 768, 1024, 1100, 1280
- Size=Mobile: 328×148, vertical gap 4 pad 0/0/0/0 main MIN cross MIN — renders at 340, 360

## Dependencies

**Built from:**

- [Form Field](../../components/41-form-field-dashboard-mockup-set/form-field-dashboard-mockup-set.md) ×8

**Built into:**

- _no parent in this export_

## Anatomy

**Size=Desktop**

```
- Size=Desktop — component 480×197 [vertical gap 8] (fixed/hug)
  - Form Field — instance 480×78 [vertical gap 0] (fill/hug) → Form Field [Size=Desktop, State=Filled]
  - Fields — frame 480×78 [horizontal gap 16] (fill/hug)
    - Form Field — instance 309×78 [vertical gap 0] (fill/hug) → Form Field [Size=Desktop, State=Filled]
    - Form Field — instance 55×78 [vertical gap 0] (fixed/hug) → Form Field [Size=Desktop, State=Filled]
    - Form Field — instance 84×78 [vertical gap 0] (fixed/hug) → Form Field [Size=Desktop, State=Filled]
  - Error Message Container (Shared) — frame 480×25 [horizontal gap 8] (fill/fixed)
    - Error Message Text. — text 480×25 (fixed/fixed) "Error message text." (hidden)
```

**Size=Mobile**

```
- Size=Mobile — component 328×148 [vertical gap 4] (fixed/hug)
  - Form Field — instance 328×59 [vertical gap 0] (fill/hug) → Form Field [Size=Mobile, State=Blank]
  - Fields — frame 328×59 [horizontal gap 8] (fill/hug)
    - Form Field — instance 181×59 [vertical gap 0] (fill/hug) → Form Field [Size=Mobile, State=Blank]
    - Form Field — instance 53×59 [vertical gap 0] (fixed/hug) → Form Field [Size=Mobile, State=Blank]
    - Form Field — instance 78×59 [vertical gap 0] (fixed/hug) → Form Field [Size=Mobile, State=Blank]
  - Error Message Container (Shared) — frame 328×22 [horizontal gap 8] (fill/fixed)
    - Error Message Text. — text 328×22 (fixed/fixed) "Error message text." (hidden)
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Size=Desktop | 480×197 | FIXED | HUG | vertical gap 8 pad 0/0/0/0 main MIN cross MIN |  | yes |
| Size=Mobile | 328×148 | FIXED | HUG | vertical gap 4 pad 0/0/0/0 main MIN cross MIN |  | yes |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Token | Truncate | Sample |
|---|---|---|---|---|---|---|---|---|---|---|
| Error Message Text. | Noto Sans | Regular | 18 | auto |  |  | #CC2B27 | Colors/color/feedback/high-error |  | Error message text. |
| Error Message Text. | Noto Sans | Regular | 16 | auto |  |  | #CC2B27 | Colors/color/feedback/high-error |  | Error message text. |

## Color & effects

_None._

## Image ratios

_None._

## Ad slots

_None._

## Production references

_None found in descriptions or layer names._

## Known issues

- No variant has instances in MNG Design System (unused here, or used only from another file): `Size=Desktop`, `Size=Mobile`.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `form-field-assembly-address-block.json` → `variants[].variantProperties`).
2. Start from `form-field-assembly-address-block.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
