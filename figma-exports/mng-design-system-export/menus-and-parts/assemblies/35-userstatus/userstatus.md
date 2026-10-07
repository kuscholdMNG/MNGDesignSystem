---
name: "UserStatus"
kind: assembly
group: menus-and-parts
order: 35
figma_file: "WordPress Elements (b1iZxkFwtAYq9rElmnCAzd)"
figma_node: "456:5728"
component_key: 4c1b4132e858b8a7bef12375fa03f44cb6177947
variants: 4
breakpoints: [340, 360, 768, 1024, 1100, 1280]
built_from: ["Button Primary", "UserPic"]
built_into: []
spec_json: userstatus.json
skeleton: userstatus.html
exported: 2026-10-07
---

# UserStatus

**Assembly · 4 variants** · Menus and Parts · source: WordPress Elements ▸ Menus and Parts

**Designer notes on the canvas:**

- User Status

## Figma references

- File: WordPress Elements (`b1iZxkFwtAYq9rElmnCAzd`) · Page: Menus and Parts · Frame path: Frame 12800 ▸ Frame 416 ▸ Frame 11820 ▸ Frame 12776 ▸ Frame 12636 ▸ User Status ▸ Frame 12758
- Main: [UserStatus](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5728) · node `456:5728` · key `4c1b4132e858b8a7bef12375fa03f44cb6177947`

| Variant | Node | Key | Size | Preview |
|---|---|---|---|---|
| Device=Desktop, status=none | [456:5729](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5729) | 75b4401360410294816486ed741541f190d57a15 | 207×32 | ![Device=Desktop, status=none](previews/userstatus--desktop-none.png) |
| Device=Desktop, status=nonSub | [456:5734](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5734) | b1450066e455f63c00d44b22d7233ece876e6bea | 155×40 | ![Device=Desktop, status=nonSub](previews/userstatus--desktop-nonsub.png) |
| Device=Desktop, status=subscriber | [456:5738](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5738) | 774aab6ad900098fa1bf1534ded01481389de847 | 30×32 | ![Device=Desktop, status=subscriber](previews/userstatus--desktop-subscriber.png) |
| Device=mobile, status=none | [456:5740](https://www.figma.com/design/b1iZxkFwtAYq9rElmnCAzd/?node-id=456-5740) | 3352e98cb29762532d3f6e6926f75fb1bb5f15a2 | 30×32 | ![Device=mobile, status=none](previews/userstatus--mobile-none.png) |

## Properties

| Property | Type | Default | Options |
|---|---|---|---|
| Device | VARIANT | Desktop | Desktop, mobile |
| status | VARIANT | none | none, nonSub, subscriber |

## Where it is used

- **Device=Desktop, status=none** — breakpoints: 1024, 1100, 1280; nested inside: AccountMenu / Status=loggedOut, View=Closed, Device=XL-Desktop, UserType=loggedOut ×1
- **Device=Desktop, status=nonSub** — breakpoints: 1024, 1100, 1280; no instances in this file
- **Device=Desktop, status=subscriber** — breakpoints: 1024, 1100, 1280; nested inside: AccountMenu/loggedIn/Closed/MD-TabletV/loggedIn ×1, AccountMenu / Status=loggedIn, View=Open, Device=SM-Mobile, UserType=PremSub ×1, AccountMenu / Status=loggedIn, View=Closed, Device=LG-TabletH, UserType=loggedIn ×1, AccountMenu / Status=alert, View=Open, Device=XS-Fold, UserType=PremSub ×1, AccountMenu / Status=loggedIn, View=Open, Device=XL-Desktop, UserType=PremSub ×1, AccountMenu / Status=loggedIn, View=Open, Device=XL-Desktop, UserType=BasicSub ×1, AccountMenu / Status=loggedIn, View=Closed, Device=MD-TabletV, UserType=loggedIn ×1, AccountMenu / Status=loggedIn, View=Closed, Device=XL-Desktop, UserType=loggedIn ×1, AccountMenu / Status=loggedIn, View=Open, Device=XL-Desktop, UserType=nonSub ×1, AccountMenu / Status=alert, View=Open, Device=SM-Mobile, UserType=PremSub ×1, AccountMenu / Status=loggedIn, View=Closed, Device=SM-Mobile, UserType=loggedIn ×1, AccountMenu / Status=alert, View=Open, Device=XL-Desktop, UserType=PremSub ×1, AccountMenu / Status=loggedIn, View=Open, Device=XL-Desktop, UserType=groupSub ×1, AccountMenu / Status=alert, View=Open, Device=MD-TabletV, UserType=PremSub ×1, AccountMenu / Status=loggedIn, View=Open, Device=SM-Mobile, UserType=nonSub ×1; other pages: Menus and Parts ▸ Frame 12800 ×12
- **Device=mobile, status=none** — breakpoints: 340, 360, 768; nested inside: AccountMenu / Status=loggedOut, View=Closed, Device=SM-Mobile, UserType=loggedOut ×1, AccountMenu / Status=loggedOut, View=Closed, Device=MD-TabletV, UserType=loggedOut ×1, AccountMenu / Status=loggedOut, View=Closed, Device=LG-TabletH, UserType=loggedOut ×1

## Breakpoints

| Key | Viewport | Variant(s) |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | Device=mobile, status=none |
| 360 | ≤639px (SM-Mobile, built 360) | Device=mobile, status=none |
| 768 | 640–799px (MD-TabletV) | Device=mobile, status=none |
| 1024 | 800–1039px (LG-TabletH, built 1009) | Device=Desktop, status=none, Device=Desktop, status=nonSub, Device=Desktop, status=subscriber |
| 1100 | ≥1040px (XL-Desktop, built 1085) | Device=Desktop, status=none, Device=Desktop, status=nonSub, Device=Desktop, status=subscriber |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Device=Desktop, status=none, Device=Desktop, status=nonSub, Device=Desktop, status=subscriber |

## Responsive rules

- Device=Desktop, status=none: 207×32, horizontal gap 15 pad 0/0/0/0 main CENTER cross CENTER — renders at 1024, 1100, 1280
- Device=Desktop, status=nonSub: 155×40, horizontal gap 15 pad 0/0/0/0 main CENTER cross CENTER — renders at 1024, 1100, 1280
- Device=Desktop, status=subscriber: 30×32, horizontal gap 15 pad 0/0/0/0 main MIN cross CENTER — renders at 1024, 1100, 1280
- Device=mobile, status=none: 30×32, horizontal gap 15 pad 0/0/0/0 main MIN cross CENTER — renders at 340, 360, 768

## Dependencies

**Built from:**

- Button Primary ×2 _(not in this export)_
- [UserPic](../33-userpic/userpic.md) ×1

**Built into:**

_Not used inside another exported item._

## Anatomy

**Device=Desktop, status=none**

```
- Device=Desktop, status=none — component 207×32 [horizontal gap 15] (hug/fixed)
  - Button Primary — instance 110×40 [vertical gap 8] (hug/hug) → Button Primary [Icon=None, State=Default, Breakpoint=Desktop]
  - Button Primary — instance 82×40 [vertical gap 8] (hug/hug) → Button Primary [Icon=None, State=Default, Breakpoint=Desktop]
```

**Device=Desktop, status=nonSub**

```
- Device=Desktop, status=nonSub — component 155×40 [horizontal gap 15] (hug/hug)
  - Button Primary — instance 110×40 [vertical gap 8] (hug/hug) → Button Primary [Icon=None, State=Default, Breakpoint=Desktop]
  - UserPic — instance 30×30 [horizontal gap 8] (fixed/fixed) → UserPic [Size=Small, Status=Default]
```

**Device=Desktop, status=subscriber**

```
- Device=Desktop, status=subscriber — component 30×32 [horizontal gap 15] (hug/fixed)
  - UserPic — instance 30×30 [horizontal gap 8] (fixed/fixed) → UserPic [Size=Small, Status=Default]
```

**Device=mobile, status=none**

```
- Device=mobile, status=none — component 30×32 [horizontal gap 15] (hug/fixed)
  - UserPic — instance 30×30 [horizontal gap 8] (fixed/fixed) → UserPic [Size=Small, Status=Default]
```

## Size & layout

| Variant | Size | Width | Height | Auto-layout | Radius | Clip |
|---|---|---|---|---|---|---|
| Device=Desktop, status=none | 207×32 | HUG | FIXED | horizontal gap 15 pad 0/0/0/0 main CENTER cross CENTER |  |  |
| Device=Desktop, status=nonSub | 155×40 | HUG | HUG | horizontal gap 15 pad 0/0/0/0 main CENTER cross CENTER |  |  |
| Device=Desktop, status=subscriber | 30×32 | HUG | FIXED | horizontal gap 15 pad 0/0/0/0 main MIN cross CENTER |  |  |
| Device=mobile, status=none | 30×32 | HUG | FIXED | horizontal gap 15 pad 0/0/0/0 main MIN cross CENTER |  |  |

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

- 1 of 4 variants have no instances anywhere in WordPress Elements (unused, or used only from another file): `Device=Desktop, status=nonSub`.
- `Device=Desktop, status=none`: content overflows frame — 'Button Primary' (110×40 at 0,-4) exceeds frame 207×32.
- `Device=Desktop, status=none`: content overflows frame — 'Button Primary' (82×40 at 125,-4) exceeds frame 207×32.

## Rendering steps

1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `userstatus.json` → `variants[].variantProperties`).
2. Start from `userstatus.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.
3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.
4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).
5. Check against the preview PNG, then against the production references.
