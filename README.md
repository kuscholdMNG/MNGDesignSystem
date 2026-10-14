# MNG Web Design System — Project Folder

> Folder map and filing rules. **Every session working on this project reads this first and follows it.**
> Set up 2026-09-30, when duplicate copies made by different sessions were removed. **Updated 2026-10-01:** the project moved from Google Drive to GitHub (`kuscholdMNG/MNGWebDesignSystem`). See "Working in GitHub" below. **Updated 2026-10-02:** added `scripts/`; the homepage template audit was deleted from `_archive/`. **Updated 2026-10-08:** added `tokens/icons/`, `logos/` and `scripts/logos-export/`. **Updated 2026-10-09:** added `figma-exports/mng-ads-export/` and `scripts/ads-export/`. **Updated 2026-10-13:** added `EXPORT-STANDARD.md`; `figma-exports/` is now legacy (frozen). **Updated 2026-10-14:** renamed from "MNG Design System" to **MNG Web Design System** (see "Names" below); local copy moved to `~/Github/`.

## Names

The design system was renamed on 2026-10-14 (Karl). Use these forms everywhere:

| Where | Form |
|---|---|
| Prose, docs, Figma file name and labels | **MNG Web Design System** |
| GitHub repo, local folder, Claude project, anything without spaces | **MNGWebDesignSystem** |
| Code identifiers, the `dist/` package name, snake_case contexts | **mng_web_design_system** |
| Status file | `MNG-Web-Design-System-Status.md` |

Not renamed on purpose: the frozen legacy exports in `figma-exports/` (including the folder `mng-design-system-export/` and its `mng-design-system/...@1` schema names), because other projects may point at them; dated historical labels such as "per MNG Design System 2025.07.16" in Figma; the CSS variable prefix `--mng-` and the DTCG extension namespace `com.mng`, which name the company, not the system.

## Folder map

```
MNGWebDesignSystem/
├── README.md                               ← this file
├── .gitignore                              ← keeps .DS_Store, zips and credentials out of the repo
├── MNG-Web-Design-System-Status.md         ← project status (the entry point)
├── EXPORT-STANDARD.md                      ← format rules for every token and component export (DTCG)
├── production-vs-design-differences.md     ← production gaps for Engineering
├── Reader-Dashboard-Library-Impact-Map.md
├── components/                             ← one .md per component, or a component audit
├── tokens/
│   ├── colors/                             ← mng-colors.tokens.json (source), .css, sites .csv,
│   │                                         decision log, README (color fixes: production-vs-design entry 21)
│   ├── typography/                         ← typography tokens + decision log
│   └── icons/                              ← production icon font (icomoon .ttf/.woff/.woff2), glyph map,
│                                             CSS and preview
├── logos/                                  ← newspaper logos: transparent SVGs (publications/, placeholder/),
│                                             logos.json manifest, preview.html, README
├── figma-exports/                          ← LEGACY, frozen 2026-10-13: older Figma → spec exports.
│                                             Kept, not updated; new exports follow EXPORT-STANDARD.md
│   ├── mng-design-system-export/           ← homepage, menus-and-parts, form-fields
│   ├── mng-buttons-export/                 ← all 8 Buttons-page families (primary, secondary, tertiary,
│   │                                         action, linkstyle, modal close, in-line close, hyperlink)
│   └── mng-ads-export/                     ← WordPress Elements Ad Blocks set (ad slots, 37 variants;
│                                             RevContent excluded)
├── scripts/                                ← generators that rebuild exports, one folder per export
│   ├── ads-export/                         ← extract.js (Figma plugin code) + build-ads-export.py
│   ├── buttons-export/                     ← extract.js (Figma plugin code) + build-buttons-export.py
│   ├── design-system-export/               ← extract.js + build-design-system-export.py + curated.json
│                                             (hand-checked notes) + save-previews.py
│   └── logos-export/                       ← build-logos.py + sources.json (publication → .ai file) +
│                                             extract-placeholders.js + figma-placeholders.json
└── _archive/                               ← retired files, kept for history only (empty right now;
                                              git shows the folder again when a file is moved in)
```

## Where new files go

| What you made | Where it goes |
|---|---|
| Project status update | Edit `MNG-Web-Design-System-Status.md` in place |
| A new production-vs-design gap | Add an entry to `production-vs-design-differences.md` |
| Component spec, audit or checklist | `components/<component-name>.md` |
| Color token export, CSS, CSV, decisions | `tokens/colors/` (replace the files there). Color fixes for Engineering go in `production-vs-design-differences.md` entry 21. |
| Typography tokens or decisions | `tokens/typography/` |
| Icon font, glyph map, icon previews | `tokens/icons/` |
| Newspaper logo SVGs, manifest, preview | `logos/` (rebuilt by `scripts/logos-export/build-logos.py`; don't hand-edit the SVGs) |
| A token or component export | Follow `EXPORT-STANDARD.md` (DTCG `.tokens.json`, layers, `dist/`). Never add to `figma-exports/` (legacy). |
| A script that rebuilds an export | `scripts/<export-name>/` (inputs and outputs explained at the top of the script) |
| Anything no longer current | `_archive/` |

## Rules

1. **One file per topic.** Before writing, check if a file for that topic already exists. If so, **update it in place**. Never save a second copy next to it or in another folder.
2. **No copy suffixes.** Never create names like `file (1).md`, `file (2).md`, `file-v2.md`, `file-final.md` or `file-copy.md`. If a download or sync adds a suffix, rename the file back and remove the older one.
3. **No catch-all output folders.** Don't create `Claude outputs/`, `outputs/`, `exports/` or dated folders. Files go where the map says.
4. **No zips.** Save exports unzipped in `figma-exports/`. Zips duplicate the folder and go stale.
5. **Date changes inside the file**, not in the file name (for example "**Updated 2026-09-30** for …" near the top).
6. **File names:** lowercase-with-hyphens for new files (`card-teaser.md`). Keep existing names as they are so links in other docs still work.
7. **Retiring a file:** move it to `_archive/`, then update any docs that mention its path.
8. **Exports follow `EXPORT-STANDARD.md`.** Token JSON is DTCG 2025.10 only; no Figma-import-shaped JSON, layer trees or custom `schema` formats. Generated files in `dist/` are never edited by hand.
9. **Paths in docs** are written from this folder's top level (for example `tokens/colors/mng-colors-sites.csv`).

## Working in GitHub

- **Repo:** https://github.com/kuscholdMNG/MNGWebDesignSystem (branch `main`).
- **Local copy:** `~/Github/MNGWebDesignSystem` on Karl's Mac (moved 2026-10-14; `~/Github` also holds the `for_you_tab_mvp` repo). Work only there. The old Google Drive folder is retired; don't save anything to it.
- **Commit every change** with a short message that says what changed and why (for example "Add card-teaser hover states"). Git history replaces the dates in file names, so rule 5 still applies: put the date inside the file.
- **Value changes that need Karl's review** (token values, decisions in the decision logs) go on a branch, such as `review/primary-blue-fix`, with a pull request. Everything else can go straight to `main`.
- **Push after committing.** Pushing uses a GitHub token saved in `.git/claude-credentials`, which is never committed. If a push fails with a sign-in error, the token has expired: Karl makes a new one and runs `git push` once in Terminal.
- **Never commit** credentials, `.DS_Store` files, `__pycache__` / `.pyc` files or zips. `.gitignore` blocks them.
