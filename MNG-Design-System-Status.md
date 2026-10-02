# MNG Design System — Project Status

> **Updated 2026-10-02** for the Buttons page work (fixes, renames, layer cleanup, re-export) and the repository cleanup. Rewritten 2026-09-24; earlier changes are in git history.

> - Color values: `tokens/colors/` (export \+ decision log). Color fixes for engineering: `production-vs-design-differences.md` entry 21\.  
> - Typography values: `tokens/typography/` (tokens \+ decision log).  
> - Production gaps for engineering: `production-vs-design-differences.md`.  
> - Figma component exports: `figma-exports/` (`mng-design-system-export/`, `mng-buttons-export/`).  
> - Folder map, filing rules and how to work in GitHub: `README.md` at the top of the repo.  
> - Repo: https://github.com/kuscholdMNG/MNGDesignSystem. The old Google Drive folder is retired.

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
- Colors resolve as **theme → sub-theme → site override**. A sub-theme is a publication or group ramp on top of the theme (e.g. Denver Post, Morning Call, 21C Michigan, NEPA-PMP). Every publication's theme and sub-theme is listed in `tokens/colors/mng-colors-sites.csv`.  
- **Morning Call** (mcall.com) is a site, not a theme. It runs Modern Earthy.  
- **Denver Post** runs Bold Coastal with its own colors. It isn't bespoke.  
- **Hartford Courant** runs Measured Vibrant (`measuredvibrant.css` \+ `site-tribune` stylesheet) with its own colors via the Customizer (verified live 2026-09-25).  
- **NEPA-PMP** (24 sites: the 19 Prairie Mountain Publishing sites, including Greeley Tribune and Cañon City Daily Record, plus the 5 NEPA sites) runs Modern Earthy plus a color override: PMP's shared `site-pmp` stylesheet, or each NEPA site's own plugin, with identical values (verified live 2026-10-01). It gets Modern Earthy typography and its own color sub-theme, whose should-be values are the Measured Vibrant values (2026-09-25). Greeley Tribune has no color theme of its own; its `div#page` override (primary, light, dark) is a documented exception, noted under the PMP style guide.  
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

- **Color:** the 20-mode Colors collection in the main file, plus a portable export of all 97 publications (`tokens/colors/mng-colors.tokens.json`). Since 2026-09-25 the Greeley Tribune mode is the **NEPA-PMP** mode (named Prairie Mountain Publishing until 2026-10-01). The Baltimore Sun and Capital Gazette don't fit in Figma's 20-mode limit and live only in the export. Design-vs-production color fixes for every theme and publication are in `production-vs-design-differences.md` entry 21 (the separate engineering-fixes file was retired 2026-09-30).  
- **Typography:** 4 collections in the main file (Type Primitives, Typeography Tokens, Typography Theme, Dashboard Typography). The editorial card, headline-list and body styles were added 2026-09-24. See `tokens/typography/typography-tokens.md`.  
- **Spacing and radius:** the "Spacing & Radius" collection in the main file (created 2026-10-01). Spacing stays on the 4/8 grid; the 10px and 14px values found in production are drift, not tokens (production-vs-design entry 22).

| Token | Value |
| :---- | :---- |
| `spacing/050` / `100` / `150` | 4 / 8 / 12 |
| `spacing/200` / `250` / `300` | 16 / 20 / 24 |
| `radius/sm` / `radius/utility` / `radius/lg` | 4 / 5 / 8 |

&nbsp;

## 5\. Where the components live

| Component | File | Node |
| :---- | :---- | :---- |
| Button Primary / Secondary / Tertiary | Main file, Buttons \| 2026.09.30 page | `5328:15928` / `5333:16013` / `5333:16089` |
| Button Linkstyle (text-link buttons, used for disclosures) | Main file, Buttons \| 2026.09.30 page | `5428:3953` |
| Action Button (`Button Action`) / Pop-Up Modal Close (`Button Modal Close`) / In-Line Close (`Button In-Line Close`) / Non-Button Hyperlink (`Hyperlink`) | Main file, Buttons \| 2026.09.30 page | `7075:6357` / `5335:16196` / `5335:16200` / `6282:5568` |
| InLineMessage (alerts, panels, empty states) | Main file, In-Line Content Containers page | `2776:2` |
| ModalsCenter / ModalsOffset | Main file, Modal Panels page (library copy also in Reader Dashboard v2.0) | `3040:2262` / `6497:6263` |
| Icons | Main file, Icons page | `4693:5` |
| Masthead | WordPress Elements, Menus and Parts | `456:2572` |
| AccountMenu (account dropdown) | WordPress Elements, Menus and Parts | `910:16425` |
| Section Title / Eyebrow | WordPress Elements, Homepage | `3333:42278` |

&nbsp;

All 8 button and link families are exported to `figma-exports/mng-buttons-export/` (re-exported 2026-10-02).

The component specs in `components/` (modal, disclosure, empty-state-status-badge, card-teaser, navigation) describe these patterns; the Figma sources are the components above.

## 6\. Open items

1. Build the Bootstrap-style Dropdown. The Account Dropdown Menu source is in WordPress Elements (node `910:15610`).
2. Apply the type tokens to real text layers. So far they're a reference catalog.
3. Do the DTCG renaming pass on WordPress Elements and Reader Dashboard v2.0.
4. Plan the Reader Dashboard v2.0 → v2.1 upgrade. See `Reader-Dashboard-Library-Impact-Map.md` for affected files.
5. Main file, **Style Guide | Radio Buttons**: it holds a Switch component set (20 variants: Selected × State × Icon) that likely belongs on the Toggle Switches page. Move or remove it when the Radio Buttons page is built out.
6. Main file, **Style Guide | Loading Animation**: needs real animation documentation (timing, easing, states). None exists yet.
7. Main file, **Style Guide | Themes**: still placeholder text. Fill it from the theming findings in §3.
8. **InLineMessage rebuild** (main file, node `2776:2`, still 114 variants as of 2026-09-25). Proposal: cut to about 25 variants (Priority × Placement) and move per-screen copy, icons and CTAs into component properties. See `components/reader-dashboard-inline-message-component-audit.md` (the proposal and open questions) and `components/inlinemessage-instance-migration-checklist.md` (1,173 live instances to re-check afterward). Not started; waiting on Karl's answers.
9. **Article trust tooltip:** build the "Based on facts…" trust/sourcing popover seen over article headlines, as a Figma component. See `components/Article-Page-To-Do.md`.
10. **Fonts, follow-up:** publish the WordPress Elements and main-file libraries, then accept the updates in Reader Dashboard v2.0 so its ~620 Masthead / ReaderDash Tempates instance texts pick up Noto. Reader Dashboard's Junk Yard page was not changed.
11. **Re-export `figma-exports/mng-design-system-export/`** (homepage, menus and parts, form fields). It dates from 2026-09-24, before the Form Field fix and the button renames.
12. **Ad follow-ups (WordPress Elements homepage templates):** (a) ~~extra template ads~~ removed 2026-10-02 (`Frame 45` at 1024 / 1100 / 1280 and the post-Footer `Ad` at 340 / 360 / 768). (b) `Mid-Article Banner` has no matching article slot: live OC Register articles carry `outstream_video` (480x360 desktop/tablet, 300x250 mobile) and `cube_article` (300x250) inside the article body, and no in-article 728x90. To-do for the article-page pass (Karl): decide whether Mid-Article Banner becomes Outstream Video / Cube Article or is retired. It isn't on any homepage template; its only 4 uses are in the Section Front templates. (The CitySpark ad inside Upcoming Events is unique to that widget and keeps using `Sidebar Rectangle 300x250`; no separate variant needed — Karl, 2026-10-02.) (c) Article-page ads (outstream_video, cube_article, SendtoNews) not yet checked.
13. **Upcoming Events components** (WordPress Elements, Homepage): the moved frame "Upcoming Events Widget (NEW — third-party events carousel…)" holds the building blocks (Upcoming Events Widget, Event Card, Event Card 768, Date Picker Day, Date Picker Calendar Icon) used by the `Upcoming Events Block` set — keep them. Delete only the three loose draft frames ("Upcoming Events + Ad (1024…)", "(1280…)", "Event Card Row (768…)"), and reconnect the Block's Mobile / 1100 / Desktop variants to the widget component instead of detached copies.

### Recently done

Kept here for a few weeks so the history is easy to find; git log has the rest.

- **No Display fonts; font-style tokens; excerpt tokens** (2026-10-02). (1) *Excerpt, pinned down on all 6 sites:* production excerpts are always 15px / 400 and never change with screen or container width. Line height is set by the card's CSS class: 21px (`.archive-view .excerpt`, ×1.4) by default, used by the Photos lead and the regular section cards, and 19px (×1.26667) on `.feature-primary .feature-large` (Top Zone lead), `.feature-section .feature-large` and the 3/4-up `.section-highlight` lead cards. The family is `font/theme/body-family`, except the section-highlight lead cards, which use `font/theme/small-headline-family`. Only `.more-news` excerpts change with width (16/22 below 1040px, 18/28 above); they're not on the homepage. New main-file tokens: `Editorial/Body/Excerpt` (15/400/21/0) and `Editorial/Body/ExcerptCompact` (15/400/19/0). Bound in WordPress Elements: Excerpt → 1Col Media Lead, Horizontal Feature Card, Feature + List / Narrow; ExcerptCompact → Zone 1 Lead Article Card (3); ExcerptCompact with small-headline-family → 1Col Standard. The 1Col Standard headline is now bound to `Editorial/Titles/CardQuaternary` (Noto Sans 600 19/24 −0.665, as in production; was Noto Serif Bold 19 / auto). Those excerpts were detached from the local `Zone 1 Excerpt` text style, which is left unchanged because Section Front uses it. (2) *Display fonts removed (Karl: never use Display fonts):* binding a numeric weight token in Figma makes it pick Noto Sans / Serif **Display** styles (about 5% narrower than what production renders). New tokens: `font/style/regular | medium | semibold | bold` (Type Primitives), a `…/Style` token in every typography group that has a Weight (30 groups), and `font/theme/eyebrow-style`. In Figma, bind Style (font style) instead of Weight; code and exports keep using Weight. The 14 weight-bound Homepage component layers in WordPress Elements (Eyebrow, thumbnail headlines, 1Col, Zone 1, Horizontal Feature Card, Feature + List) now bind Style. About 300 unbound Display layers were moved to the standard style across the main file and WordPress Elements. Not touched: the main file's Fonts specimens, Reader Dashboard things page and old Button sets (Frame 13001); 3 Display layers placed directly on WordPress Elements' Article Search Results page (Karl: leave Section Front / Search Results / Author pages for later). Reader Dashboard v2.0 not scanned yet (file wasn't open). *Figma note:* after each library publish, the Desktop Bridge plugin has to be closed and relaunched before library variables import; import them one at a time.
- **Detached homepage components reattached, matched to production at 360 / 768 / 1024** (2026-10-02, WordPress Elements): `1Col Article Card` is now a set with a **Style** property — `Standard` (the original 4:3 card, 19px headline; its 231 instances are unchanged; matches production feature-medium) and new `Media Lead` (16:9 image, FILL width, aspect locked; headline bound to the existing **Editorial/Titles/TitleMedia** tokens, Noto Serif 700 29/33 −1.16). Media Lead matches the OC Register Photos lead at 360 and 1280: the image is cropped to a 16:9 frame at every width (340x191 at 360, 580x326 at 1280), and the headline is 29/33 at both. No new tokens were needed. Every Photos lead now uses Media Lead: the Photos Block Mobile / Tablet / Desktop components and the 340, 360, 1024, 1100 and 1280 homepage templates (the 5 template leads were detached copies; text and visibility kept). The 768 template uses a Photos Block instance, so it updates automatically. Excerpt left as is: production uses Noto Sans 15px with a 19px or 21px line height depending on the card, so there's no single value to tokenize yet. The 6 detached thumbnails in Photos Block / Tablet are `Horizontal Thumbnail Card` Device=Mobile instances. Upcoming Events Block / Device=Mobile now uses an `Upcoming Events Widget` instance (2 cards, 5 days, as on OC Register at 360). `Horizontal Thumbnail Card` headline (all 3 variants) is bound to the Editorial/Titles/HeadlineList Family / Size / Weight / LineHeight / LetterSpacing tokens → Noto Sans Display SemiBold 15/19, −0.15 (production: Noto Sans 600 15/19); was unbound Noto Serif Bold 15–16. Still detached: 23 layers inside the homepage templates (thumbnails, TOP ZONE / Blueconic / Photos content at 1024 / 1100 / 1280) and the Upcoming Events Block 1100 / Desktop widgets (item 13).
- **Footer variants fixed in the homepage templates** (2026-10-02): 768 now uses `MD-TabletV` (was SM-Mobile) and 1024 uses `LG-TabletH` (was XL-Desktop). The 1024 / 1100 Top Zone's Device=Mobile Zone 1 Lead Article Card is intentional (layer names: matches production's vertical stack at 800–1279px), so it stays.
- **Ad Blocks matched to the Ad Team's WordPress Ad Map; homepage templates corrected** (2026-10-02, WordPress Elements). Ad Blocks (`517:4304`): renamed Footer Banner → **Bottom Leaderboard**, Floating Anchor → **Mobile Adhesion**; added 12 variants (Top Leaderboard / Sponsorship 2 / Bottom Leaderboard / Mobile Adhesion 300x50, Bottom Leaderboard 970x250 / 970x90 / 320x50, Cube 1 / 2 / 3 300x250, Outstream Video 480x360 / 300x250); un-stacked three overlapping variants. Slot sizes per width were read live from OC Register's GPT setup at 360, 768, 1024 and 1280. Templates: TOP ZONE Block Mobile/Tablet now use Cube 1 RRail ATF 300x250; 340 / 360 / 768 got cube2 (was PLACE HOLDER), new sponsorship_3, sponsorship_4 and cube3, and a Bottom Leaderboard; 1024 / 1100 / 1280 bottom_leaderboard now uses Bottom Leaderboard 970x250; the 1024 floating anchor was removed (mobile_adhesion has no size at 1024). Status item 10 (sponsorship_3 / _4 labels) closed: reusing Sponsorship 2 blocks was Karl's 2026-09-14 decision.
- **Hard-coded colors bound to tokens before the homepage re-export** (2026-10-02): in the WordPress Elements Homepage and Menus and Parts components, every exact match is bound (`gray/min`, `gray/max`, `gray/black` with opacity kept, `gray/500`, `gray/100`); `#111111` placeholder borders → `gray/min` and the Photos / thumbnail / Top Zone card borders (`#D7D6D2`) → `gray/500`. The Obituaries Masthead "Submit an Obituary" buttons use `color/theme/primary` with the Colors mode set to Endless Tributes, like their sibling buttons. Main-file Form Fields are fully bound. Left unbound on purpose: image / ad / marketing-slot / video-tile placeholders and the purple component-set borders. Skipped (Karl): near-matches in Upcoming Events and the Videos carousel. Breaking News Banner bound to `color/theme/secondary` (background) and `color/theme/near-black` (text), matching 5 of the 6 review sites; Denver Post's red override is production-vs-design entry 24. UserImage monogram `#FF702C` stays unbound (Karl's own pick). Sponsored badge (Article Status Badge `Type=Sponsored`) stays `#7D161E` with white text, unbound on purpose (Karl); production needs fixing (production-vs-design entry 25).
- **Section Title / Eyebrow bound to the per-theme eyebrow tokens** (2026-10-02, WordPress Elements `3333:42278`): both Style variants now take `font/theme/eyebrow-family`, `eyebrow-size` and `eyebrow-weight` from Typography Theme (Bold Coastal 20/400 Noto Sans, Modern Earthy 21/400 Noto Serif, Measured Vibrant 17/700 Noto Sans). The Style variant now only controls the underline. Karl bound them by hand because the plugin's library-variable import hangs.
- **Font cleanup, WordPress Elements and Reader Dashboard v2.0** (2026-10-02): WordPress Elements is all Noto now (about 2,750 text runs: Droid Sans/Serif, Helvetica, Roboto, Open Sans, Arial, Inter, Source Sans Pro). **New York** (Apple's system serif, used in the `ARTICLE IMAGE` placeholder label, Ad Blocks labels and the Upcoming Events cards) is now Noto Serif. The one exception is the **Weather Bug** temperature ("87°F", Helvetica Bold), kept for Karl's review. Reader Dashboard v2.0: 143 local text runs switched; library instances update when the libraries are published.
- **Main-file font cleanup** (2026-10-02): about 1,600 text layers moved to Noto Sans / Noto Serif (Droid Sans, Inter, Google Sans Flex, Open Sans, PT Serif and others), including the labels in all 8 button documentation frames, and 118 notes that said "Droid Sans" now say "Noto Sans". Exceptions kept on purpose: the Fonts page (fallback specimens), the Apple Pay / Safari / Chrome share-sheet mock-ups (they imitate OS UI), and the older `Button` sets on the Buttons page (`Frame 13001`, restored to their original fonts). On Style Guide | Themes, Elements to be detailed still and OLD Color Pallets only Droid Sans was switched; their other old fonts (Droid Serif, Poppins, Source Serif Pro, Lato and so on) were left for now.
- Create the spacing and radius tokens in the main file — **Done 2026-10-01:** "Spacing & Radius" collection with `spacing/050`–`300` (4, 8, 12, 16, 20, 24) and `radius/sm`, `radius/utility`, `radius/lg` (4, 5, 8). Buttons are 4px across the board (`radius/sm`, Karl 2026-10-01): Action Button, Button Action and Button ActionMenu moved from 5px to 4px, all button shapes are bound to `radius/sm`, `radius/utility` (5px) is for containers only (Karl, 2026-10-01): InLineMessage, ModalsCenter parts, Form Fields, check boxes, the status badge and the account dropdown keep 5px, bound to `radius/utility` in Figma. Production radius drift is entry 23. Karl: spacing is 4/8 only; production's 10px and 14px are logged as drift to fix (production-vs-design entry 22).
- Live-check the sites whose sheet data disagrees with Figma — **Done 2026-10-01.** The 5 NEPA sites match PMP exactly and joined it as the NEPA-PMP sub-theme. Morning Call, GrowthSpotter, Daily Press and NY Daily News match their Figma themes. Morning Call's `secondary` and `tertiary` stay flagged as missing (Karl, 2026-10-01): they inherit the right values but must be set explicitly. Hartford Courant was verified 2026-09-25 (Measured Vibrant \+ `site-tribune`). The Baltimore Sun uses its documented Figma styles as is.
- **Homepage template audit retired** (2026-10-02): the archived copy (`_archive/homepage-template-audit.md`) was deleted. The WordPress Elements files are the source for homepage templates.
- **Form Field set error** — **Fixed 2026-10-01:** the first variant was renamed `Size=Desktop, State=Blank`; the set has no errors now (State = Blank/Filled/Focus/Error/Disabled). (MNG Design System, Form Fields page, set `6963:6863`): two variants are both named `Size=Desktop, State=Filled`, which puts the set in an error state. The first one shows placeholder text, so it's really the missing Desktop/Blank state. Renaming it to `Size=Desktop, State=Blank` should clear the error. Found in the 2026-09-24 component export.
- **Buttons page findings** — **Done 2026-10-02** (Karl's review of the 2026-10-01 export):
    - Modal Close InFocus design was correct; the spec text was fixed (InFocus keeps the Default fill and border).
    - Primary, Secondary and Tertiary are 40px tall in every state (8px top/bottom padding, 40px min-height so a wrapped label can grow). Action Button (32px) and Linkstyle (38px) stay compact (Karl, 2026-10-02).
    - Icons: 16px on Primary, Secondary, Tertiary and Action Button; 12px on Modal Close and In-Line Close.
    - Every focus ring is bound to `color/gray/black` and drawn outside the element (absolute `Focus Ring` frame, 1px offset), so it never changes size or pushes neighbours. The In-Line Close ring has 4px corners to match its Hover/Pressed box.
    - Renamed: `Button Modal Close`, `Button In-Line Close`, `Hyperlink`; all variant properties and values capitalized (`State`, `Style`, `Icon`, `Breakpoint`; `Default`, `Left`, `Right`, `Stacked`, `1 Row`). The documented set `7075:6357` is now `Button Action`; the older library set `5417:3876` (formerly `Button Action`) is now `Action Button`.
    - Focus rings: verified that no InFocus variant changes size or shifts its text or icons; the ring draws outside the button (a 40px button reads as 46px with the ring).
    - Hyperlink's 16.5px text, teal focus ring and dashed underline inside the InFocus box match production and are intentional, not errors (Karl, 2026-10-02). The Figma spec text says so.
    - **Layer names (2026-10-02):** every variant in a set now has the same layer tree, so text and icon overrides carry across variant swaps. CTAs: `Button` › `Content` › `Icon Left` / `Label` / `Icon Right`. Button Action: `Button` › `Content` › `Icon Left` / `Label` / `Icon Right`. Linkstyle: `Label`. Modal Close: `Icon`. In-Line Close: `Button` › `Box` › `Icon` (the Box has no fill or border in Default and InFocus). Hyperlink: `Label` (InFocus: `Underline` › `Label`, kept to match production). InFocus adds only a `Focus Ring` frame. The extra InFocus wrapper frames were removed without changing any visual or instance override. The 8 documentation frames have no generic `Frame ####` names left (`Content Row`, `Sub-header`, `Grid Row`, `Section: Desktop`, `Section Header`, `Demo Row`, `Diagram`, `State: Default`, `Sample`, `Divider`, `Padding Marker` and so on).
- **Re-export the Buttons page** — **Done 2026-10-02:** `figma-exports/mng-buttons-export/` was regenerated from the current Figma state (8 sets, 96 variants, new previews, layer names, sizes and tokens incl. `radius/sm`, `spacing/100`, `spacing/200`).

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
- Never edit or audit the main file's **"*** Style Guide | Reader Dashboard things"** page (Karl, 2026-10-02). It's covered by Reader Dashboard v2.0.  
- On the Buttons page, keep the older `Button` sets in `Frame 13001` as they are (Karl, 2026-10-02).  
- The **Fonts** page documents fallbacks and font changes, so it keeps its non-Noto specimens. Everywhere else, text is Noto Sans or Noto Serif.  
- Color tokens always carry design (should-be) values. When production differs, mark the production row in Figma with the red-dashed outline and log the fix; never change the token to match production.  
- The project lives in GitHub (`kuscholdMNG/MNGDesignSystem`), not Google Drive. Work in the local copy, commit every change and push. Value changes that need Karl's review go on a branch with a pull request. See "Working in GitHub" in `README.md`.  
- Never commit credentials, `.DS_Store` files or zips.
