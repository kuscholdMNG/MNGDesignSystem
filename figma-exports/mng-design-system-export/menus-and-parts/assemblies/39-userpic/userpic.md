---
name: "UserPic"
kind: assembly
group: menus-and-parts
order: 39
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "456:5674"
component_key: b0a98e06e6e220ea1c7d4a247494ff5525fe0dd7
variants: 6
breakpoints: []
built_from: ["UserImage", "AlertLevel"]
built_into: ["UserStatus"]
spec_json: userpic.json
skeleton: userpic.html
exported: 2026-10-08
---

# UserPic

**Assembly · 6 variants** · Menus and Parts · source: WordPress Elements ▸ Menus and Parts

**Designer notes on the canvas:**

- User Type
- UserPic
- UserPic | Sample Model; do not use

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Menus and Parts · Frame path: Frame 12800 ▸ Frame 416 ▸ Frame 11820 ▸ Frame 12776 ▸ Frame 12636 ▸ User Status ▸ Frame 12757
- Main: [UserPic](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5674) · node `456:5674` · key `b0a98e06e6e220ea1c7d4a247494ff5525fe0dd7`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Size=Small, Status=Default | [456:5675](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5675) | 10b073ddb31cc0cbd22bf85c71f892fc5dde0905 | 30×30 | ![Size=Small, Status=Default](previews/userpic--small-default.png) |
| Size=Small, Status=Active | [712:6222](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=712-6222) | 8279faee5686897d37c9e5a43b5e41ef6b281a12 | 30×30 | ![Size=Small, Status=Active](previews/userpic--small-active.png) |
| Size=Medium, Status=Default | [456:5678](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5678) | f19e521ce487bfcd3ebe2771e7fdbd0b5808f62c | 40×40 | ![Size=Medium, Status=Default](previews/userpic--medium-default.png) |
| Size=Medium, Status=Active | [712:6292](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=712-6292) | aac53a11e2bcf0004e9bd15d6583c5f61059cb8b | 40×40 | ![Size=Medium, Status=Active](previews/userpic--medium-active.png) |
| Size=Large, Status=Default | [712:6226](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=712-6226) | 4e3f6f9cea921e03a619965b61b83314cc2a4ce1 | 64×64 | ![Size=Large, Status=Default](previews/userpic--large-default.png) |
| Size=Large, Status=Active | [712:6295](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=712-6295) | 4811301ef6ab5bbc7d2eec6a6797664a5405257a | 64×64 | ![Size=Large, Status=Active](previews/userpic--large-active.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Size | VARIANT | Small | Small, Large, Medium |
| Status | VARIANT | Default | Default, Active |

## Where it is used

- **Size=Small, Status=Default** — breakpoints: —; nested inside: UserStatus / Device=Desktop, status=subscriber ×1, UserStatus / Device=Desktop, status=nonSub ×1, UserStatus / Device=mobile, status=none ×1
- **Size=Small, Status=Active** — breakpoints: —; no instances in this file
- **Size=Medium, Status=Default** — breakpoints: —; no instances in this file
- **Size=Medium, Status=Active** — breakpoints: —; other pages: Menus and Parts ▸ Frame 12800 ×1
- **Size=Large, Status=Default** — breakpoints: —; no instances in this file
- **Size=Large, Status=Active** — breakpoints: —; no instances in this file

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| — | not placed in any homepage template | — |

## Responsive rules

- Size=Small, Status=Default: 30×30, horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER — no breakpoint (not placed in a template)
- Size=Small, Status=Active: 30×30, horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER — no breakpoint (not placed in a template)
- Size=Medium, Status=Default: 40×40, horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER — no breakpoint (not placed in a template)
- Size=Medium, Status=Active: 40×40, horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER — no breakpoint (not placed in a template)
- Size=Large, Status=Default: 64×64, horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER — no breakpoint (not placed in a template)
- Size=Large, Status=Active: 64×64, horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER — no breakpoint (not placed in a template)

## Dependencies

**Built from:**

- [UserImage](../../components/34-userimage/userimage.md) ×1
- [AlertLevel](../../components/33-alertlevel/alertlevel.md) ×2

**Built into:**

- [UserStatus](../41-userstatus/userstatus.md)

## Anatomy

**Size=Small, Status=Default**

```
- Size=Small, Status=Default — component 30×30 [horizontal gap 8] (fixed/fixed)
  - UserImage — instance 30×30 [horizontal gap 0] (fixed/fixed) → UserImage [Size=small, Graphic=social]
  - AlertLevel — instance 8×8 (fixed/fixed) → AlertLevel [Level=low, Size=Small]
  - AlertLevel — instance 8×8 (fixed/fixed) → AlertLevel [Level=none, Size=Small]
```

**Size=Small, Status=Active**

```
- Size=Small, Status=Active — component 30×30 [horizontal gap 8] (fixed/fixed)
  - UserImage — instance 30×30 [horizontal gap 0] (fixed/fixed) → UserImage [Size=small, Graphic=social]
  - AlertLevel — instance 8×8 (fixed/fixed) → AlertLevel [Level=low, Size=Small] ×2
```

**Size=Medium, Status=Default**

```
- Size=Medium, Status=Default — component 40×40 [horizontal gap 8] (fixed/fixed)
  - UserImage — instance 40×40 [horizontal gap 0] (fixed/fixed) → UserImage [Size=medium, Graphic=social]
  - AlertLevel — instance 8×8 (fixed/fixed) → AlertLevel [Level=low, Size=Small]
  - AlertLevel — instance 8×8 (fixed/fixed) → AlertLevel [Level=none, Size=Small]
```

**Size=Medium, Status=Active**

```
- Size=Medium, Status=Active — component 40×40 [horizontal gap 8] (fixed/fixed)
  - UserImage — instance 40×40 [horizontal gap 0] (fixed/fixed) → UserImage [Size=medium, Graphic=social]
  - AlertLevel — instance 8×8 (fixed/fixed) → AlertLevel [Level=low, Size=Small] ×2
```

**Size=Large, Status=Default**

```
- Size=Large, Status=Default — component 64×64 [horizontal gap 8] (fixed/fixed)
  - UserImage — instance 64×64 [horizontal gap 0] (fixed/fixed) → UserImage [Size=large, Graphic=social]
  - AlertLevel — instance 16×16 (fixed/fixed) → AlertLevel [Level=low, Size=Large]
  - AlertLevel — instance 16×16 (fixed/fixed) → AlertLevel [Level=none, Size=Large]
```

**Size=Large, Status=Active**

```
- Size=Large, Status=Active — component 64×64 [horizontal gap 8] (fixed/fixed)
  - UserImage — instance 64×64 [horizontal gap 0] (fixed/fixed) → UserImage [Size=large, Graphic=social]
  - AlertLevel — instance 16×16 (fixed/fixed) → AlertLevel [Level=low, Size=Large] ×2
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Size=Small, Status=Default | 30×30 | FIXED | FIXED | horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Size=Small, Status=Active | 30×30 | FIXED | FIXED | horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Size=Medium, Status=Default | 40×40 | FIXED | FIXED | horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Size=Medium, Status=Active | 40×40 | FIXED | FIXED | horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Size=Large, Status=Default | 64×64 | FIXED | FIXED | horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Size=Large, Status=Active | 64×64 | FIXED | FIXED | horizontal gap 8 pad 0/0/0/0 main MIN cross CENTER |  |  |

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

- 4 of 6 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Size=Small, Status=Active`, `Size=Medium, Status=Default`, `Size=Large, Status=Default`, `Size=Large, Status=Active`.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `userpic.json` → `variants[].variantProperties`).
2. Start from `userpic.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
