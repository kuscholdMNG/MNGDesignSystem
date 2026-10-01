# MNG Design System — Project Folder

> Folder map and filing rules. **Every session working on this project reads this first and follows it.**
> Set up 2026-09-30, when duplicate copies made by different sessions were removed.

## Folder map

```
MNGDesignSystem/
├── README.md                               ← this file
├── MNG-Design-System-Status.md             ← project status (the entry point)
├── production-vs-design-differences.md     ← production gaps for Engineering
├── Reader-Dashboard-Library-Impact-Map.md
├── components/                             ← one .md per component, or a component audit
├── tokens/
│   ├── colors/                             ← mng-colors.tokens.json (source), .css, sites .csv,
│   │                                         decision log, README (color fixes: production-vs-design entry 21)
│   └── typography/                         ← typography tokens + decision log
├── figma-exports/                          ← Figma → spec exports (MD + JSON + HTML + PNG previews)
│   ├── mng-design-system-export/           ← homepage, menus-and-parts, form-fields
│   └── mng-buttons-export/                 ← all 8 Buttons-page families (primary, secondary, tertiary,
│                                             action, linkstyle, modal close, in-line close, hyperlink)
└── _archive/                               ← retired files, kept for history only
```

## Where new files go

| What you made | Where it goes |
|---|---|
| Project status update | Edit `MNG-Design-System-Status.md` in place |
| A new production-vs-design gap | Add an entry to `production-vs-design-differences.md` |
| Component spec, audit or checklist | `components/<component-name>.md` |
| Color token export, CSS, CSV, decisions | `tokens/colors/` (replace the files there). Color fixes for Engineering go in `production-vs-design-differences.md` entry 21. |
| Typography tokens or decisions | `tokens/typography/` |
| A Figma component export | `figma-exports/<export-name>/` (unzipped, replacing the old one) |
| Anything no longer current | `_archive/` |

## Rules

1. **One file per topic.** Before writing, check if a file for that topic already exists. If so, **update it in place**. Never save a second copy next to it or in another folder.
2. **No copy suffixes.** Never create names like `file (1).md`, `file (2).md`, `file-v2.md`, `file-final.md` or `file-copy.md`. If Drive adds a suffix, rename the file back and remove the older one.
3. **No catch-all output folders.** Don't create `Claude outputs/`, `outputs/`, `exports/` or dated folders. Files go where the map says.
4. **No zips.** Save exports unzipped in `figma-exports/`. Zips duplicate the folder and go stale.
5. **Date changes inside the file**, not in the file name (for example "**Updated 2026-09-30** for …" near the top).
6. **File names:** lowercase-with-hyphens for new files (`card-teaser.md`). Keep existing names as they are so links in other docs still work.
7. **Retiring a file:** move it to `_archive/`, then update any docs that mention its path.
8. **Paths in docs** are written from this folder's top level (for example `tokens/colors/mng-colors-sites.csv`).
