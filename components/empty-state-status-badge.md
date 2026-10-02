# Empty State Card & Status Badge

> **Updated 2026-10-01** (last change recorded in this doc). Current project status is in `MNG-Design-System-Status.md`.

**Status:** Spec measured 2026-09-01 directly from Figma, not a live-site scrape. The Figma source for the Empty State is the **InLineMessage** component set in the main MNG Design System file (`jFHYqhZbJjvWQmDI4myCsd`, node `2776:2`, 114 variants), which Reader Dashboard v2.0 uses as a library component. A pilot rebuild of both patterns was retired on 2026-09-25. Status Badge still has no real component anywhere (see §2).
**Source:** "Reader Dashboard v2.0" Figma file (fileKey `PhXogWaQcnNSnQqxyRu4b2`) — Karl confirmed this file already has these patterns designed accurately, so this component doc is built from it directly rather than re-visiting the live Reader Dashboard. Empty State pulled from "Saved Articles | 2025.10.21" (node `3051:56937`); Status Badge pulled from "Benefits Panel | 2026.02.24".

---

## 1. Empty State Card

**Not a bespoke component in the source file — it's one variant of a single, large "InLineMessage" component set** (`8107:94110` is its library ID as seen inside Reader Dashboard v2.0; 114 variants) that MNG's UX team already built and reuses for header alerts, panel notices, and empty-state banners throughout the whole Reader Dashboard. This is a more powerful and more consistent pattern than a one-off "Empty State Card" would have been, and it should be modeled as such rather than as a separate, narrower component.

**Variant properties:** `Device` (Desktop/Mobile/TabletH/TabletV/FOLD/Menus) × `Priority` (High/Medium/low/Confirmation/none) × `Location` (page/context-specific, e.g. `DashSavedEmpty`, `DashGiftEmpty`, `Header`, `AcctMenu`, `DashSubsCancelError`, `CustomCheckout`, etc.) × `PanelType` (`HeaderAlert` / `Panel` / `Alert`).

**Empty State = `PanelType=Alert`, `Priority=none`, `Location=Dash<X>Empty`** (confirmed instance: `Device=Desktop, Priority=none, Location=DashSavedEmpty, PanelType=Alert`, id `8107:94165`). The same variant family also covers `DashGiftEmpty` (Gifted Articles) — Newsletters' empty state was found live in an earlier live-site pass but wasn't individually re-verified against this component set this session; low risk, same visual pattern.

**Measured specs (Desktop):**

| Property | Value |
|---|---|
| Container fill | `#F1EFEB` → `color/gray/600` |
| Container corner radius | `5` → `radius/utility` |
| Container padding | `24px` all sides |
| Vertical gap (title row → content row) | `16px` |
| Close button | `40×40`, fully circular (radius `40`) — dismissible |
| Title text | Noto Sans **Bold**, `16px`, color `#141414` — e.g. "Save your first article" |
| Content-row icon | `32×32` icon slot |
| Content-row gap (icon → text) | `8px` |
| Description text | Noto Sans Regular, `16px`, color `#141414` — e.g. "Simply click the Save icon on any article." |

---

## 2. Status Badge (access-tier badge)

Small pill shown under a benefit's title on the Benefits panel, indicating which subscription tier unlocks it (e.g. "🔒 PREMIUM DIGITAL" under "Ad-Free Reading," "Full Network Access," "Account Sharing"). Found identically styled on every gated benefit tile checked.

**Not currently a real Figma component** — unlike the Empty State pattern above, this is a manually-styled frame (`Left Item Variable`) that's copy-pasted inline wherever it's needed, not an instance of a shared component. Building it as a real reusable component in the main MNG Design System file would be an improvement over the source file.

**Measured specs:**

| Property | Value |
|---|---|
| Fill | `#F1EFEB` → `color/gray/600` (same token as the Empty State Card container) |
| Corner radius | `5` → `radius/utility` |
| Padding | `4px` all sides |
| Gap (icon → text) | `4px` |
| Sizing | Hug contents on both axes (auto-width, auto-height) — not a fixed-size pill |
| Icon | `16×16`, uses the existing "padlock" icon component (`Name=padlock`, id `8107:84068`) |
| Label text | Noto Sans Regular, `14px`, color `#141414`, **`textCase: UPPER`** (renders as "PREMIUM DIGITAL," but the underlying string is stored title-case — "Premium Digital" — with Figma's uppercase text-transform applied, not literally typed in caps) |

---

## 3. Token reuse — no new primitives needed

Both patterns reuse existing values:

- **Corner radius `5`** = `radius/utility` (5px), a Figma variable since 2026-10-01. It is for containers only; buttons use `radius/sm` (4px).
- **Fill `#F1EFEB`** exists twice: `color/neutral/menu-hover` (menu-hover-specific) and `color/gray/600` (the "Universal Grays" scale). **Karl's decision, 2026-09-01: use `color/gray/600` for both components.** `color/neutral/menu-hover` stays reserved for menu hover states.

---

## 4. Open items

1. Newsletters' empty state (and any other `Location=Dash*Empty` variant beyond `DashSavedEmpty`/`DashGiftEmpty`) wasn't individually re-verified against this component set — same container styling is expected per the variant naming, but icon/copy weren't re-checked one by one.
2. Status Badge's copy-pasted (non-componentized) state in the source file means there's no single "canonical" instance to diff against once we build our own — if the source file's badge frames drift from each other over time, our built component may need to reconcile against whichever is most current.
3. When Status Badge is built, use the real `padlock` icon from the main file's Icons set rather than a placeholder.

---

## 5. Methodology

- Measured directly from the "Reader Dashboard v2.0" Figma file via the Figma Desktop Bridge plugin (`figma_execute`, walking the node tree and reading `fills`/`cornerRadius`/`padding`/`itemSpacing`/text properties directly from the Figma API) — not a live-site DOM scrape. Per Karl's explicit direction (2026-09-01): this file is the accurate, already-designed source of truth for the Reader Dashboard, so live-site re-verification (originally planned against `canoncitydailyrecord.com/dashboard`) was skipped for these two components.
