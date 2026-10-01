# MNG Design System — Project Status

> **Rewritten 2026-09-24.** Replaces the Aug 13 status doc, which later sections had contradicted. It had said there were 4 shared themes, that Denver Post was "bespoke" and that the eyebrow was standardized at 20px. This version keeps only what's true now. **Updated 2026-09-25** for the Greeley Tribune → Prairie Mountain Publishing color change, **2026-09-30** for the Greeley exception, Hartford Courant, the folder reorganization and the browser-resize rule, and **2026-10-01** for the full Buttons-page export (8 button and link families).

> - Color values: `tokens/colors/` (export \+ decision log). Color fixes for engineering: `production-vs-design-differences.md` entry 21\.  
> - Typography values: `tokens/typography/` (tokens \+ decision log).  
> - Production gaps for engineering: `production-vs-design-differences.md`.  
> - Figma component exports: `figma-exports/` (`mng-design-system-export/`, `mng-buttons-export/`).  
> - Folder map and filing rules: `README.md` at the top of this folder.

## 1\. Goal

Build a Figma design system for MediaNews Group (90+ properties), based on what's actually live in production. Tokens follow the DTCG naming standard (e.g. `color/theme/primary`, `font/size/16`).

## 2\. Figma files

| File | Key | Role |
| :---- | :---- | :---- |
| **MNG Design System** (formerly "UI Style Guide") | `jFHYqhZbJjvWQmDI4myCsd` | Main library. Holds the color and typography tokens and the Color Pallets style guides. |
| WordPress Elements (older docs call it "Website Page Templates") | `b1iZxkFwtAYq9rElmnCAzd` | Page templates and the production Masthead component set (`456:2572`, 75 variants). |
| Reader Dashboard v2.0 | `PhXogWaQcnNSnQqxyRu4b2` | Source of truth for Reader Dashboard components (a v2.1 upgrade is planned). |
| CRUX Style Library | `uwKNDnGRH0otKDrgYiWmUw` | Read-only reference. **Never edited.** |

&nbsp;

**Library approach (decided 2026-08-28):** the libraries stay as separate files and are cleaned up in place. Components are never moved between files, because hundreds of existing instances depend on them. Renaming is safe (Figma links by ID), while value changes need review.

**Main file page cleanup (2026-08-27).** The file's 27 pages were reviewed one by one. Its own maturity labels (`IN PRODUCTION`, `READY FOR PRODUCTION`, `NEEDS REVIEW`, `JUNK YARD` dividers and `***` priority names) aren't reliable, so don't trust them.

- **Left alone on purpose:** Modal Panels' "DO NOT USE; NEEDS REVIEW" nodes (intentional), the Icons placeholders (no icon designs exist yet), "Elements to be detailed still", Junk Yard and the divider pages (never meant for import), and Style Guide | Reader Dashboard things (covered by Reader Dashboard v2.0).  
- **Generic "Frame 11523" frames** (31 across 9 pages) were each renamed to what they are (e.g. "Sample Basic Form Field", "Focus Field", "Primary CTA Button Sample", "State and Sample") or deleted. None remain.  
- The old Color Pallets page (2025.12.17) was superseded by the rebuilt 2026.09.10 page.

## 3\. How the sites are themed

- There are **3 shared WordPress themes**: Bold Coastal, Measured Vibrant and Modern Earthy. Each site loads one and can override colors through the WordPress Customizer (scoped to `#page`).  
- Colors resolve as **theme → sub-theme → site override**. A sub-theme is a publication or group ramp on top of the theme (e.g. Denver Post, Morning Call, 21C Michigan, Prairie Mountain Publishing). Every publication's theme and sub-theme is listed in `tokens/colors/mng-colors-sites.csv`.  
- **Morning Call** (mcall.com) is a site, not a theme. It runs Modern Earthy.  
- **Denver Post** runs Bold Coastal with its own colors. It isn't bespoke.  
- **Hartford Courant** runs Measured Vibrant (`measuredvibrant.css` \+ `site-tribune` stylesheet) with its own colors via the Customizer (verified live 2026-09-25).  
- **Prairie Mountain Publishing** (19 sites, including Greeley Tribune and Cañon City Daily Record) runs Modern Earthy plus a PMP color override. It gets Modern Earthy typography and its own color sub-theme, whose should-be values are the Measured Vibrant values (2026-09-25). Greeley Tribune has no color theme of its own; its `div#page` override (primary, light, dark) is a documented exception, noted under the PMP style guide.  
- **Obituaries** (Endless Tributes) look the same on every site, whatever the theme.  
- **Type:** sizes, weights and spacing are the same on every theme. Only the font families change per theme. Eyebrows are per theme.

**Standard review sites:**

| Site | Theme |
| :---- | :---- |
| ocregister.com | Bold Coastal |
| denverpost.com | Bold Coastal (own colors) |
| chicagotribune.com | Measured Vibrant |
| orlandosentinel.com | Measured Vibrant (own colors) |
| canoncitydailyrecord.com | Modern Earthy (PMP) |
| mcall.com | Modern Earthy (own colors) |

&nbsp;

The mercurynews.com and eastbaytimes.com sites were removed from the list on 2026-09-03. Greeley Tribune is used for extra PMP checks.

## 4\. Tokens

- **Color:** the 20-mode Colors collection in the main file, plus a portable export of all 97 publications (`tokens/colors/mng-colors.tokens.json`). Since 2026-09-25 the Greeley Tribune mode is the **Prairie Mountain Publishing** mode. The Baltimore Sun and Capital Gazette don't fit in Figma's 20-mode limit and live only in the export. Design-vs-production color fixes for every theme and publication are in `production-vs-design-differences.md` entry 21 (the separate engineering-fixes file was retired 2026-09-30).  
- **Typography:** 4 collections in the main file (Type Primitives, Typeography Tokens, Typography Theme, Dashboard Typography). The editorial card, headline-list and body styles were added 2026-09-24. See `tokens/typography/typography-tokens.md`.  
- **Spacing and radius** aren't Figma variables yet. These are the values measured so far, to use when they're created:

| Token | Value |
| :---- | :---- |
| `spacing/050` / `100` / `150` | 4 / 8 / 12 |
| `spacing/075` / `175` | 10 / 14 |
| `spacing/200` / `250` / `300` | 16 / 20 / 24 |
| `radius/sm` / `radius/utility` / `radius/lg` | 4 / 5 / 8 |

&nbsp;

## 5\. Where the components live

| Component | File | Node |
| :---- | :---- | :---- |
| Button Primary / Secondary / Tertiary | Main file, Buttons \| 2026.09.30 page | `5328:15928` / `5333:16013` / `5333:16089` |
| Button Linkstyle (text-link buttons, used for disclosures) | Main file, Buttons \| 2026.09.30 page | `5428:3953` |
| Action Button / Pop-Up Modal Close (`Button ModalClose`) / In-Line Close (`Button PanelClose`) / Non-Button Hyperlink (`nonButton Hyperlink`) | Main file, Buttons \| 2026.09.30 page | `7075:6357` / `5335:16196` / `5335:16200` / `6282:5568` |
| InLineMessage (alerts, panels, empty states) | Main file, In-Line Content Containers page | `2776:2` |
| ModalsCenter / ModalsOffset | Main file, Modal Panels page (library copy also in Reader Dashboard v2.0) | `3040:2262` / `6497:6263` |
| Icons | Main file, Icons page | `4693:5` |
| Masthead | WordPress Elements, Menus and Parts | `456:2572` |
| AccountMenu (account dropdown) | WordPress Elements, Menus and Parts | `910:16425` |
| Section Title / Eyebrow | WordPress Elements, Homepage | `3333:42278` |

&nbsp;

All 8 button and link families are exported to `figma-exports/mng-buttons-export/` (2026-10-01).

The component specs in `components/` (modal, disclosure, empty-state-status-badge, card-teaser, navigation) describe these patterns; the Figma sources are the components above.

## 6\. Open items

1. Update the Section Title / Eyebrow component (WordPress Elements, `3333:42278`) to the per-theme eyebrow tokens.  
2. Build the Bootstrap-style Dropdown. The Account Dropdown Menu source is in WordPress Elements (node `910:15610`).  
3. Create the spacing and radius tokens in the main file (values in §4).  
4. Apply the type tokens to real text layers. So far they're a reference catalog.  
5. Live-check the sites whose sheet data disagrees with Figma (NEPA, Morning Call, GrowthSpotter, Daily Press, NY Daily News). They're flagged in the `notes` column of `tokens/colors/mng-colors-sites.csv`. Hartford Courant was verified 2026-09-25 (Measured Vibrant \+ `site-tribune`). The Baltimore Sun uses its documented Figma styles as is.  
6. Do the DTCG renaming pass on WordPress Elements and Reader Dashboard v2.0.  
7. Plan the Reader Dashboard v2.0 → v2.1 upgrade. See `Reader-Dashboard-Library-Impact-Map.md` for affected files.  
8. Main file, **Style Guide | Radio Buttons**: it holds a Switch component set (20 variants: Selected × State × Icon) that likely belongs on the Toggle Switches page. Move or remove it when the Radio Buttons page is built out.  
9. Main file, **Style Guide | Loading Animation**: needs real animation documentation (timing, easing, states). None exists yet.  
10. Main file, **Style Guide | Themes**: still placeholder text. Fill it from the theming findings in §3.  
11. **InLineMessage rebuild** (main file, node `2776:2`, still 114 variants as of 2026-09-25). Proposal: cut to about 25 variants (Priority × Placement) and move per-screen copy, icons and CTAs into component properties. See `components/reader-dashboard-inline-message-component-audit.md` (the proposal and open questions) and `components/inlinemessage-instance-migration-checklist.md` (1,173 live instances to re-check afterward). Not started; waiting on Karl's answers.  
12. **Article trust tooltip:** build the "Based on facts…" trust/sourcing popover seen over article headlines, as a Figma component. See `components/Article-Page-To-Do.md`.  
13. **Retire the homepage template audit.** Moved to `_archive/homepage-template-audit.md` on 2026-09-30. It's an old working log that still mentions the deleted earlier "MNG Design System" file (those mentions are out of date). It will be deleted and replaced by the WordPress Elements files, which will become the source for homepage templates.  
14. **Form Field set error** (MNG Design System, Form Fields page, set `6963:6863`): two variants are both named `Size=Desktop, State=Filled`, which puts the set in an error state. The first one shows placeholder text, so it's really the missing Desktop/Blank state. Renaming it to `Size=Desktop, State=Blank` should clear the error. Found in the 2026-09-24 component export.  
15. **Sponsorship ad labels, 1024 and 1100 homepages** (WordPress Elements, Homepage): the sponsorship\_3 and sponsorship\_4 frames both use the "Sponsorship 2 970x250" Ad Blocks unit. Swap in the matching units or rename the frames. Found in the 2026-09-24 component export.  
16. **Wrong-width variants in homepage templates** (WordPress Elements, Homepage): the 768 homepage uses the Footer's `SM-Mobile` variant (should be `MD-TabletV`), and the 1024 homepage uses the Footer's `XL-Desktop` variant (should be `LG-TabletH`). The detached TOP ZONE blocks at 1024 and 1100 still contain a `Device=Mobile` Zone 1 Lead Article Card. Found in the 2026-09-24 component export.  
17. **Fonts outside Noto Sans / Noto Serif:** Droid Sans, Source Sans Pro, New York and Helvetica still appear in a few WordPress Elements components, mostly the Masthead variants and Sponsored items. Replace them with the production pair. Found in the 2026-09-24 component export.

18. **Buttons page findings** (2026-10-01 export, `figma-exports/mng-buttons-export/`), for Karl's review:
    - Pop-Up Modal Close InFocus keeps the gray fill and border, but its spec text says the fill is removed. Fix the text or the variant.
    - CTA inner button heights vary (40/41/42/46px) against the 40px min-height. Secondary and Tertiary icons are 14px on some variants (spec: 16px). The Mobile InFocus rings on Secondary/Tertiary (Icon=None, left) are unbound `#000000`.
    - Non-Button Hyperlink: 16.5px text, teal focus ring and a leftover dashed underline in InFocus (all already flagged in Figma).
    - In-Line Close InFocus ring is square, with no offset (spec: 1px offset).
    - Naming: Modal Close uses `state=default` in lower case. The set names `Button ModalClose`, `Button PanelClose` and `nonButton Hyperlink` don't match their page titles. Renaming is safe.

## 7\. Standing rules

> **Mirrored in the project instructions (2026-09-30).** The critical rules below are copied into the MNGDesignSystem project instructions so every session sees them. If you change a rule here, update the project instructions too, and the reverse.

- Never enter passwords or credentials on any site, even if provided. Karl logs in himself.  
- On Reader Dashboard Gifted Articles, never click "Remove".  
- Give sites at least 10 seconds to load before measuring.  
- Never resize browser windows. When a check needs a different viewport width, stop and ask Karl to resize the window himself, then continue once he confirms.  
- Read site colors on `#page`, not the page root (see the method note in production-vs-design).  
- Don't use `figma_arrange_component_set` or `autoArrange: true`. It once deleted the Button / Primary set. Position components by hand.  
- The Figma design-system audit tool reports 0/100 for "Token Architecture" on this plan. That's a tool limitation, not a real defect.  
- Never edit the CRUX Style Library.  
- Color tokens always carry design (should-be) values. When production differs, mark the production row in Figma with the red-dashed outline and log the fix; never change the token to match production.