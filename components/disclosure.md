# Disclosure

**Status:** ✅ **Specced 2026-09-01.** The Figma source is **Button Linkstyle** in the main MNG Design System file (`jFHYqhZbJjvWQmDI4myCsd`, `***Buttons | 2026.02.27` page, component set `5428:3953`), with the label swapped between "Show Login Methods" / "Hide Login Methods". A pilot rebuild of this pattern was retired on 2026-09-25; use Button Linkstyle.
**Key correction, 2026-09-01 (Karl):** this was never a bespoke accordion/disclosure component at all. The toggle itself is a plain instance of the Button Linkstyle component. We spent real effort searching Reader Dashboard v2.0 and WordPress Elements (then "Website Page Templates") for a standalone "accordion" component before Karl pointed out where it actually lives — worth remembering for next time: check the main file's Buttons page for hyperlink-styled controls before assuming something is a bespoke pattern.
**Source:** `preprod.eastbaytimes.com/dashboard` (Reader Dashboard), Profile tab
**Note:** the previous session flagged this as documented-but-unbuilt from color references only; this is the first time it's been observed live, with real interaction.

⏸️ **Live-site follow-up paused:** the Reader Dashboard is its own separate React/Tailwind application, distinct from the main WordPress-based site, and appears to be mid-transition (see `modal.md` §4 — the Subscription tab already redirects to a different domain). Deeper audit of this live surface is on hold now that the Figma source covers the actual design-system deliverable.

⚠️ **Scope note:** the production Reader Dashboard (e.g. `chicagotribune.com/user-tools/dashboard`) has a *different*, chevron/icon-based accordion pattern (headings like "Subscriber Support," "Subscription Details," "Login Methods," each 28px/bold with an icon and a rotating chevron). Per instruction, that surface is being replaced and is **out of scope** — this spec documents only the preprod pattern below, which is a simpler text-link toggle, not the chevron accordion. If both patterns still exist after the replacement, they'll need to be reconciled or reduced to one.

---

## 1. Pattern

A plain-text toggle button that shows/hides a block of content inline, without an icon or chevron — just the link text itself flips between two states.

**Trigger example:** "Show Login Methods" ↔ "Hide Login Methods" (on the Profile page, next to Email Address)

- Element: `<button>`, not `<a>`
- Style: `font-size: 16px`, `font-weight: 400`, `color: rgb(0, 109, 163)` (`#006DA3`), `text-decoration: underline`
- The same toggle button text appears **twice** — once above the revealed content, once below it — so the user can collapse it again without scrolling back up

## 2. Revealed content

On toggle, reveals:
- A heading ("Connected Login Methods")
- A description line ("Manage how you sign in to your account")
- One row per connected method, each with a small icon + label + value (e.g. envelope icon + "Email & Password" + the email address)

No animation/transition was observed or tested — content simply appears/disappears. (Not confirmed either way; worth checking directly in Figma/dev handoff rather than assuming.)

## 3. Tokens

- Link/toggle color `#006DA3`. **Resolved 2026-08-27 — not a drift.** Previously written up as a mismatch against a live read of the shared theme's `--primary` variable. That read was taken on `document.documentElement`, which sits outside the scope of the WordPress Customizer's real override (scoped to `div#page`, not `:root`) — so it was only ever seeing an intermediate placeholder value, never the site's actual applied color. Read correctly (on `#page`), `--primary` is `#006DA3` on this site, an exact match. See `modal.md` for the full explanation — this is a measurement-methodology fix, not a production issue, and confirmed consistent across every other pilot site too.
- Typography otherwise uses plain system defaults (16px/400) — no distinct "disclosure label" text style found beyond the link color/underline.

## 4. Open items (live-site audit)

1. Only one instance of this pattern was found and tested (Login Methods on Profile). Other tabs (Subscription, Benefits, etc.) weren't checked for additional disclosure instances.
2. Expand/collapse transition behavior (animated vs. instant) not confirmed.
3. Relationship to the production-only chevron/accordion pattern is unresolved — see scope note above. If that pattern survives the Reader Dashboard replacement in any form, it needs its own spec.
4. This app's own responsive breakpoints not yet captured (see `modal.md` §5).

## 5. How to build it

Model the **expanded** state as: a Button Linkstyle toggle ("Hide Login Methods") → revealed panel (heading "Connected Login Methods" Bold 16px, description "Manage how you sign in to your account" Regular 14px `color/gray/200`, one method row — envelope icon + "Email & Password" label + email value, both Regular 16px) → a second identical Button Linkstyle toggle below, matching the confirmed live-site behavior of repeating the toggle text above and below the content.

The collapsed state is the same toggle alone, labeled "Show Login Methods", with the panel hidden. Use the real envelope icon from the main file's Icons set.

## 6. Button Linkstyle (the real underlying component)

Main file, `***Buttons | 2026.02.27` page, **Button Linkstyle** component set (`5428:3953`), `style=1row, state=Default` variant: hug-contents frame, padding 8, itemSpacing 8, optional icon slots on both sides (hidden by default — the source itself hides them for plain-text links like this one), label Noto Sans Regular 16px underlined, color bound to `color/brand/primary`. Other variants: `style=stacked`; `state=hoverPressed`/`InFocus` — per the Buttons page's own design notes, hover should go `primary-dark` + underline + hand cursor, and InFocus should add a contrasting border. The Modal's two text-link CTAs use this same component.
