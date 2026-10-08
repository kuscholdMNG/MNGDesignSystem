---
name: "Form Field Assembly / Checkbox + Terms"
kind: assembly
group: form-fields
order: 45
figma_file: "MNG Design System (jFHYqhZbJjvWQmDI4myCsd)"
figma_node: "7003:29236"
component_key: 815cbc290cc86fc6abaf1b0fc9f441c19a79100d
variants: 2
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["CheckBox"]
built_into: []
spec_json: form-field-assembly-checkbox-terms.json
skeleton: form-field-assembly-checkbox-terms.html
exported: 2026-10-08
---

# Form Field Assembly / Checkbox + Terms

**Assembly · 2 variants** · Form Fields · source: MNG Design System ▸ Form Fields | 2026.09.24

**Designer notes on the canvas:**

- Checkbox + Terms

## Figma references

- File: MNG Design System (`jFHYqhZbJjvWQmDI4myCsd`) · Page: Form Fields | 2026.09.24 · Frame path: Form Field & Code Box — Documentation ▸ Frame 12919 ▸ Code Box — Documentation ▸ Frame 11535 ▸ Frame 11522 ▸ Assembly: Checkbox + Terms
- Main: [Form Field Assembly / Checkbox + Terms](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7003-29236) · node `7003:29236` · key `815cbc290cc86fc6abaf1b0fc9f441c19a79100d`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Size=Desktop | [7003:29229](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7003-29229) | 1dfa51a41ce9fb9aa721df7443ac8c4356cba33f | 388×77 | ![Size=Desktop](previews/form-field-assembly-checkbox-terms--desktop.png) |
| Size=Mobile | [7003:29235](https://www.figma.com/design/jFHYqhZbJjvWQmDI4myCsd/?node-id=7003-29235) | d3b94ff8f6757905109790cb8ef8fb1444537226 | 294×62 | ![Size=Mobile](previews/form-field-assembly-checkbox-terms--mobile.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Terms text | TEXT | I agree to the Terms of Service and Privacy Policy. |  |
| Show error | BOOLEAN | False |  |
| Error message | TEXT | Please accept terms and conditions. |  |
| Size | VARIANT | Desktop | Desktop, Mobile |

## Where it is used

- **Size=Desktop** — breakpoints: 768, 1024, 1100, 1280; nested inside: InLineMessage / Device=Desktop, Priority=none, Location=DashSubsCCupdate, PanelType=Panel ×1; other pages: Check Boxes | 2026.02.27 ▸ Frame 12791 ×5
- **Size=Mobile** — breakpoints: 340, 360; nested inside: InLineMessage / Device=Mobile, Priority=none, Location=DashSubscriptionCCinfo, PanelType=Panel ×1, InLineMessage / Device=FOLD, Priority=none, Location=DashSubscriptionCCinfo, PanelType=Panel ×1; other pages: Check Boxes | 2026.02.27 ▸ Frame 12791 ×4

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

- Size=Desktop: 388×77, vertical gap 8 pad 0/0/0/0 main MIN cross MIN — renders at 768, 1024, 1100, 1280
- Size=Mobile: 294×62, vertical gap 4 pad 0/0/0/0 main MIN cross MIN — renders at 340, 360

## Dependencies

**Built from:**

- CheckBox ×1 _(not in this export)_

**Built into:**

_Not used inside another exported item._

## Anatomy

**Size=Desktop**

```
- Size=Desktop — component 388×77 [vertical gap 8] (fixed/hug)
  - Fields — frame 388×44 [horizontal gap 8] (fill/hug)
    - CheckBox — instance 40×40 [horizontal gap 8] (fixed/fixed) → CheckBox [status=unselected, inFocus=False, interaction=Default]
    - I agree to the Terms of Service and Privacy Policy. — text 340×44 (fill/hug) "I agree to the Terms of Service and Priv"
  - Error Message Container (Shared) — frame 388×25 [horizontal gap 0] (fill/fixed)
    - Error Message Text. — text 388×25 (fixed/fixed) "Please accept terms and conditions." (hidden)
```

**Size=Mobile**

```
- Size=Mobile — component 294×62 [vertical gap 4] (fixed/hug)
  - Fields — frame 294×36 [horizontal gap 6] (fill/hug)
    - CheckBox — instance 28×28 [horizontal gap 8] (fixed/fixed) → CheckBox [status=unselected, inFocus=False, interaction=Default]
    - I agree to the Terms of Service and Privacy Policy. — text 260×36 (fill/hug) "I agree to the Terms of Service and Priv"
  - Error Message Container (Shared) — frame 294×22 [horizontal gap 0] (fill/fixed)
    - Error Message Text. — text 294×22 (fixed/fixed) "Please accept terms and conditions." (hidden)
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Size=Desktop | 388×77 | FIXED | HUG | vertical gap 8 pad 0/0/0/0 main MIN cross MIN |  | yes |
| Size=Mobile | 294×62 | FIXED | HUG | vertical gap 4 pad 0/0/0/0 main MIN cross MIN |  | yes |

## Typography

| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I agree to the Terms of Service and Privacy Policy. | Noto Sans | Regular | 16 | auto |  |  | #000000 | Colors/color/gray/black | font/size/16 |  | I agree to the Terms of Service and Privacy Policy | Size=Desktop |
| Error Message Text. | Noto Sans | Regular | 18 | auto |  |  | #CC2B27 | Colors/color/feedback/high-error | font/size/18 |  | Please accept terms and conditions. | Size=Desktop |
| I agree to the Terms of Service and Privacy Policy. | Noto Sans | Regular | 13 | auto |  |  | #000000 | Colors/color/gray/black | font/size/13 |  | I agree to the Terms of Service and Privacy Policy | Size=Mobile |
| Error Message Text. | Noto Sans | Regular | 16 | auto |  |  | #CC2B27 | Colors/color/feedback/high-error | font/size/16 |  | Please accept terms and conditions. | Size=Mobile |

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

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `form-field-assembly-checkbox-terms.json` → `variants[].variantProperties`).
2. Start from `form-field-assembly-checkbox-terms.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
