# MNG icon font (production `icomoon`)

> **Extracted 2026-10-08** from ocregister.com. This is the icon font the live WordPress themes use for UI icons (search, arrows, close, social, share and so on).

## Files

| File | What it is |
|---|---|
| `icomoon.ttf` | The exact production font (32,944 bytes), taken from the `@font-face` in `boldcoastal.css` |
| `icomoon.woff`, `icomoon.woff2` | Web versions converted from the TTF with fontTools (same glyphs, smaller files) |
| `icomoon.css` | Ready-to-use `@font-face` plus all 172 `.icon-*` classes (`<i class="icon-search"></i>`) |
| `icons.json` | Glyph map: every class → codepoint, whether the glyph exists, notes on broken classes, and the 9 glyphs that have no class |
| `preview.html` | Open in a browser to see every icon with its class name |
| `preview.png` | Picture of all 174 glyphs with their codepoints |

## Where it comes from

- Source: `https://www.ocregister.com/wp-content/themes/assets/static/css/boldcoastal.css`. The font is embedded there as a base64 TrueType + WOFF data URI under `font-family: icomoon`. Each `.icon-X::before` uses `content: var(--icon-X)`, and the codepoints come from those variables.
- The TTF was saved from the live page in Chrome, because ocregister.com can't be fetched directly from Claude's sessions.
- Only Bold Coastal (OC Register) was extracted. Measured Vibrant and Modern Earthy load their own theme CSS, which may embed the same font; not checked yet.

## Production quirks (see `icons.json` notes and production-vs-design entry 30)

- `icon-grid2` shows the gift glyph (U+E930); the dot grid is U+E932, which has no class.
- `icon-windows8` shows warning2 (U+E986); the Windows logo is U+E987, which has no class.
- `icon-book3` points at the letter "e" (U+0065); the closed book U+E993 has no class.
- `icon-google-plus` points at U+EEEA, which isn't in the font.
- `icon-mng-podcast1` shows the Android logo (U+E902).
- `icon-google-color` is built from U+EA25 plus the pieces U+EA2C–EA2E, layered in different colors.

## Relation to Figma

The main file's **Icons** component set (`4693:5`, Icons | 2026.08.28 page) holds 95 SVG icons. About 67 of them have a production class with the same or a near-identical name (for example `arrow-right2` → `icon-arrow-right`, `printer3` → `icon-print`). The Figma set also has the payment marks (Visa, AmEx, Apple Pay…) and a few icons production doesn't have (`crown`, `giving-hand`, `yield-*`, `content_copy`). Figma stays the design source of truth; this folder documents what production ships.
