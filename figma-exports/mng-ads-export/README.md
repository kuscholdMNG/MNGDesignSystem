# MNG ad slots — component spec export

Exported 2026-10-09 from Figma: the **Ad Blocks** component set in WordPress Elements ▸ Ads and Sponsored (`517:4304`), 37 variants (23 placed in templates or components, 14 not used yet), with 37 variant previews plus an overview. **RevContent is excluded** (not built to production; Karl, 2026-10-08).

Rebuild: run the calls in `scripts/ads-export/extract.js` in Figma, then `python3 scripts/ads-export/build-ads-export.py <raw> figma-exports/mng-ads-export`.

## How an agent should use this folder

1. Open [`components/01-ad-blocks/ad-blocks.md`](components/01-ad-blocks/ad-blocks.md): the **Ad units** table lists every unit with its size, production slot name, breakpoints and where it's used; the **Homepage slot map** shows which unit fills which slot at each width.
2. For exact values use the `.json` twin (`adSlots[]` is the flat unit list; `variants[].layerTree` is the full Figma layer tree).
3. Start rendering from [`ad-blocks.html`](components/01-ad-blocks/ad-blocks.html) (one `<section>` per variant, colors from `tokens.css`).
4. In production the slot is an empty GPT container of that size; the green box is only a design placeholder.
5. Check **Known issues** before trusting a value.

## Breakpoints

| Key | Viewport | Homepage template |
|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | 340 HomePage |
| 360 | ≤639px (SM-Mobile, built 360) | Mobile HomePage |
| 768 | 640–799px (MD-TabletV) | 768 HomePage |
| 1024 | 800–1039px (LG-TabletH, built 1009) | 1024 HomePage |
| 1100 | ≥1040px (XL-Desktop, built 1085) | 1100 HomePage |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Desktop HomePage |

## Units at a glance

| Unit | Sizes |
|---|---|
| Sponsorship 1 | 320x50, 300x50 |
| Top Leaderboard | 970x250, 970x90, 728x90, 320x100, 320x50, 300x50 |
| Sponsorship 2 | 970x250, 970x90, 728x90, 320x50, 300x50 |
| Cube 1 RRail ATF | 300x1050, 300x600, 300x250, 160x600 |
| Cube 2 RRail Mid | 300x600, 300x250 |
| Cube 3 RRail Lower | 300x600, 300x250 |
| Cube Article | 300x250 |
| Sidebar Rectangle | 300x250 |
| Outstream Video | 480x360, 300x250 |
| Mid-Article Banner | 728x90, 300x250 |
| Bottom Leaderboard | 970x250, 970x90, 728x90, 320x100, 320x50, 300x50 |
| Mobile Adhesion | 728x90, 320x50, 300x50 |
| PLACE HOLDER | 300x250 |

## Folder layout

```
mng-ads-export/
├── README.md        this file
├── index.json       item list (paths, breakpoints, issue count)
├── tokens.json      color variables used (+ placeholder fill), type tokens, breakpoints
├── tokens.css       :root custom properties for the skeleton
└── components/01-ad-blocks/
    ├── ad-blocks.md       human-readable spec
    ├── ad-blocks.json     machine-readable spec with layer trees
    ├── ad-blocks.html     HTML/CSS skeleton, one section per variant
    └── previews/       one PNG per variant (1x) + ad-blocks--overview.png
```

## Not included

- RevContent component set (`506:3865`), the RevContent Image Template frame.
- The "Advertizment Template" frame (`496:7892`) is referenced but not exported; it's the drawing the Ad Blocks variants were built from, not a component.
- Page templates themselves (homepage templates are in `figma-exports/mng-design-system-export/` as usage evidence only).
