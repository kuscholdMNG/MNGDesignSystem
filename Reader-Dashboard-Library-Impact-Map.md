# Reader Dashboard v2.0 — Library Impact Map

*Compiled 2026-09-02, via the Figma Desktop Bridge plugin (local Plugin API against files open in Figma Desktop) — no REST API calls used. Karl's request: map which design-system files would be affected by publishing the Reader Dashboard v2.0 → v2.1 upgrade.*

> **File names (updated 2026-09-25):** "Website Page Templates" below is now **WordPress Elements** (`b1iZxkFwtAYq9rElmnCAzd`), and "UI Style Guide" is now the main **MNG Design System** file (`jFHYqhZbJjvWQmDI4myCsd`).

## Method

1. Opened Reader Dashboard v2.0 in Figma Desktop (Desktop Bridge plugin running) and enumerated every published component/variant on its **"Components | 2026.02.25"** page — 21 component sets, 467 individual variants, each with its library `key`.
2. Opened the other design-system files that also had the plugin running — **Website Page Templates** and **UI Style Guide** — and walked every page of each, checking every `INSTANCE` node's `mainComponent.key` against the Reader Dashboard key list.
3. Recorded, per file and per page, which Reader Dashboard components are actually instantiated there, and how many times.

**Caveat:** a full `loadAllPagesAsync()` sweep of Reader Dashboard v2.0 itself timed out — the file is large (8 audited dashboard sub-pages plus supporting pages). Only its "Components" page was used as the source of published keys, which matches the file's own convention (that's the page the design-system docs describe as holding the built library components). If any published component lives outside that page, it wouldn't be captured here.

## Source library

**Reader Dashboard v2.0** (`PhXogWaQcnNSnQqxyRu4b2`) — "Components | 2026.02.25" page: 21 component sets / 467 variants.

## Files affected

### Website Page Templates — 2 of 14 pages
- **Menus and Parts** (heaviest usage found): the site nav menu — `NavMenu` (Desktop/TabletV/Mobile/FOLD, Open/Closed states, 13–14 instances each), `NavItem` (130 instances), `IndicatorLeft`/`IndicatorRight` (117–130 instances), `NavItemLabel` Selected states. This is the header/off-canvas nav that links out to Reader Dashboard — a v2.1 change to any of these atoms ripples through the whole site nav.
- **Stand Alone Pages**: a broader mix — `NewsletterSublist` variants, `Tile Body Content` / `Item Tile` layout atoms, `Title-Bar Container` / `Title-SubLevel` (subscription-tier labels), `MobAp1`/`MobAp2` (mobile app items), `CCUpdateError` items, visible/info toggles. Reads like a reference/kitchen-sink page pulling in many Reader Dashboard pieces for use elsewhere on the site.

### UI Style Guide — 4 of 27 pages
- **\*\*\*Breakpoints and Page Templates | 2026.05.19** (heaviest here): the same `NavMenu`/`NavItem`/`Indicator` family as above (20 `NavItem` instances), tested across breakpoints — this page will need review alongside Website Page Templates' nav usage.
- **In-Line Content Containers | 2026.01.02**: 6× `Title-SubLevel`.
- **Alerts and Icons**: light touch — one each of `NewsletterSublist`, `Title-Bar Container`, `Title-SubLevel`, an `info` visibility toggle.
- **\*\*\*Buttons | 2026.02.27**: 2× a Desktop button state used inside `MarketsListsItems`.

## Component families with the most exposure

1. **Nav family** (`NavMenu`, `NavItem`, `IndicatorLeft`/`IndicatorRight`, `NavItemLabel`) — by far the largest footprint, concentrated in Website Page Templates → Menus and Parts and UI Style Guide → Breakpoints and Page Templates.
2. **Newsletter/subscription tile atoms** (`NewsletterSublist`, `Title-Bar Container`, `Title-SubLevel`) — spread across Stand Alone Pages, In-Line Content Containers, and Alerts and Icons.
3. **Tile/content layout atoms** (`Tile Body Content`, `Item Tile`, `1stSec Left/Right`) — Stand Alone Pages and Menus and Parts.

## Suggested review order before publishing v2.1

1. **Website Page Templates → Menus and Parts** and **UI Style Guide → \*\*\*Breakpoints and Page Templates** — the nav family instances live here and carry the largest instance counts.
2. **Website Page Templates → Stand Alone Pages** — widest variety of component families touched.

---

## Round 2 — 14 additional files opened and scanned

Same method, no REST API: each file was opened in Figma Desktop with the Desktop Bridge plugin running, then walked page-by-page for `INSTANCE` nodes matching the Reader Dashboard v2.0 key list.

### Confirmed heavy usage

**Account Selector Feat.** (`zksU85Vllo6urratUqHZny`) — 5 of 6 pages, and by far the heaviest consumer found in either round. Page names say it outright: *RDv2.0 | Account Sharing v3*, *RDv2.0 | Show Login Methods v3*, *RDv2.0 | Account Switching Flow v3*, *RD | Account Selector v2*, *RD | Account Selector*. Hundreds of instances per page of the `Item Tile` / `Tile Body Content` / `1stSec Left`/`Right` family (e.g. "RDv2.0 | Account Sharing v3" alone: 197× `Device=Desktop` Item Tile, 283× the `1stSec Left` name-style variant, 216× an old-style right-side text variant). This file is effectively built entirely out of Reader Dashboard v2.0 atoms — it should be treated as a first-class dependent, not a peripheral one.

**Single Use Landing Pages** (`5slzjnFAnyGRi0UXS8xbIW`) and **Email Options for Non-Registered Users** (`CvIMbKFlZ68vEGaBRzQ3g6`) were initially only sample-scanned — see Round 3 below for the complete, full-coverage results that supersede the partial figures originally reported here.

### Light or occasional usage

- **Custom Checkout Page** — 3 of 7 pages use a `MobAp1` (mobile-app-info) component in small numbers (2–10 instances): *Custom Checkout on Engage Paywall v1*, *Updated (Karl) v3*, *Updated (Kristen) v2*.
- **Search Tool reviews** — 1 of 9 pages (*Updated New Layout Suggestions*): a handful of closed-state `NavMenu` instances.
- **Obits | 2026 Projects** — 1 of 7 pages (*CI-14670 | CTA Testing Designs*): reuses the same nav + tile family seen in Account Selector Feat. (20 `NavItem`, dozens of tile/content atoms) — looks like this CTA test was built by copying from that file.
- **Obits | Event Panel | 2025.03.10** — 1 of 7 pages (*READY FOR PRODUCTION*): light, 2 instances each of a couple of tile/newsletter-empty atoms.

### No usage found

Article Personalization Features | 2026, Log In Methods, Auth0 Universal Login Page, Apple Pay, Obits | v2 Redesign, Obit | Guestbook | 2025, Special Article Template | 2026.01.16 — all fully scanned, zero Reader Dashboard instances.

## Updated exposure ranking (superseded by Round 3 for the two large files — see below)

1. **Account Selector Feat.** — heaviest by a wide margin, and structurally built on Reader Dashboard v2.0.
2. **Single Use Landing Pages** — confirmed affected, but scope not fully measured (too large for one pass).
3. **Website Page Templates** (Round 1) — nav family, site-wide.
4. **UI Style Guide** (Round 1) — same nav family, breakpoint testing.
5. **Email Options for Non-Registered Users** — status unknown, needs a dedicated follow-up scan.
6. Everything else in "light or occasional usage" above.

---

## Round 3 — complete (non-sampled) scan of the two oversized files

The two files above were flagged in Round 2 as too large to fully enumerate: sequential per-instance `getMainComponentAsync()` calls timed out on their biggest pages (19,000–23,000+ `INSTANCE` nodes each). Two workarounds were tried and ruled out first — checking `instance.mainComponent.key` synchronously (completes instantly but resolves 0% of instances; Figma won't populate that property without an async fetch) and a reduced-key subset scan (avoids the timeout but only samples). The fix that worked: batching `getMainComponentAsync()` calls with `Promise.all` (500 instances per concurrent batch) instead of awaiting them one at a time. That resolved all 23,164 instances on the largest page in ~3 seconds — versus timing out at 30+ seconds sequentially — and made a complete, full-467-key scan of every page in both files possible in a single pass each.

**Coverage: 100%.** Every instance on every page in both files was resolved (no timeouts, no truncation, no sampling).

### Single Use Landing Pages (`5slzjnFAnyGRi0UXS8xbIW`) — complete results

38,142 total instances scanned across 7 pages; 1,094 are Reader Dashboard v2.0 component instances (about 2.9% of the file).

| Page | Instances (page) | Reader Dashboard matches |
|---|---|---|
| Overview | 17,147 | 102 — nav family (`NavMenu`, `NavItem`, `IndicatorLeft`/`Right`) + Notifications tile atoms, Desktop and Mobile |
| Newsletter Opt-In/Out \| 2026.06.10 | 1,041 | 300 — heaviest concentration in this file: `NewsletterSublist` variants, newsletter list/intro tiles, Desktop/Mobile/FOLD toggle atoms |
| Activate Subscription v2 \| 2026.08.18 | 10,785 | 270 — `Item Tile` / tile-body layout atoms and `MobAp1` mobile-app-info component (Desktop + Mobile, ~45 each) |
| Update CreditCard \| 2026.06.08 | 3,421 | 254 — full nav family plus `CCupdateError`, `AcctSharingALL`, `PaymentPlan` items across Desktop/Mobile/FOLD/TabletV |
| Activate Subscription \| 2026.08.12 | 5,128 | 168 — same `Item Tile`/`MobAp1` pattern as the v2 page above, smaller scale |
| Maintainence Pages \| 2026.06.09 | 620 | 0 |
| -------- OLD STUFF BELOW HERE -------- | 0 | 0 |

This confirms and extends the Round 2 sample: the file is affected on the same 5 of 7 pages, with the newsletter opt-in page turning out to be the single heaviest page in the file (300 matches) rather than a proportionally light one — something the earlier partial scan under-counted.

### Email Options for Non-Registered Users (`CvIMbKFlZ68vEGaBRzQ3g6`) — complete results

76,013 total instances scanned across 7 pages; 2,709 are Reader Dashboard v2.0 component instances (about 3.6% of the file). This is the largest confirmed consumer file found in the whole exercise by matched-instance count.

| Page | Instances (page) | Reader Dashboard matches |
|---|---|---|
| Email Opt-Out Page \| 2026.06.04 | 22,578 | 102 — nav + Notifications tile family only |
| Updated Enhanced Unsubscribe Page \| 2026.04.28 | 23,164 | 102 — identical footprint to the page above |
| Updated Enhanced Unsubscribe Page \| 2026.03.23 | 19,397 | **747** — nav/Notifications base set *plus* a large Markets/Regions block (`MarketsListsItems` alone: 341 instances) and desktop/mobile/FOLD newsletter-list style variants |
| Updated Enhanced Unsubscribe Page \| 2026.03.04 | 8,846 | **1,426** — the single heaviest page found anywhere in this exercise: `NewsletterSublist`/title-bar/sublevel/visibility-toggle components each used 160–330 times, plus the nav/Notifications base set |
| Enhanced Unsubscribe Page \| 2026.02.23 | 1,911 | 316 — same newsletter-sublist family as above, lighter |
| Generic Unsubscribe Page \| 2026.02.21 | 117 | 16 — same newsletter-sublist family, lightest |
| Industry Research | 0 | 0 |

This resolves the "status unknown" flag from Round 2: the file is affected on 6 of 7 pages, and its two mid-sized unsubscribe-page revisions (03.23 and 03.04) carry far more Reader Dashboard exposure — both in raw count and in variety of component families touched — than either of the two largest pages (which turned out to be nav-only, light usage despite their size).

## Updated exposure ranking (final)

1. **Email Options for Non-Registered Users** — 2,709 matched instances across 6 of 7 pages; the widest and heaviest confirmed footprint of any file scanned, concentrated in the newsletter-sublist and markets/regions component families on the 03.23 and 03.04 unsubscribe-page revisions.
2. **Account Selector Feat.** — structurally built on Reader Dashboard v2.0 (hundreds of instances per page), still the most architecturally dependent single file.
3. **Single Use Landing Pages** — 1,094 matched instances across 5 of 7 pages, heaviest on the newsletter opt-in/out page.
4. **Website Page Templates** (Round 1) — nav family, site-wide.
5. **UI Style Guide** (Round 1) — same nav family, breakpoint testing.
6. Everything else in "light or occasional usage" above.

## Updated recommendation

Before publishing v2.1, review in this order: **Account Selector Feat.** (structural dependency — treat as a first-class consumer), then **Email Options for Non-Registered Users** (highest matched-instance count, concentrated in newsletter-sublist and markets/regions atoms on its 2026.03.04 and 2026.03.23 pages), then **Single Use Landing Pages** (heaviest on its Newsletter Opt-In/Out page). All three files, plus Website Page Templates and UI Style Guide from Round 1, share the nav-family atoms (`NavMenu`, `NavItem`, `IndicatorLeft`/`Right`) — any v2.1 change to those atoms has the widest blast radius of anything in the library. Coverage of every file scanned in this exercise is now complete (no sampling, no partial scans, no "status unknown" files remaining).
