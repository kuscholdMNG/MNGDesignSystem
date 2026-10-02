# Article Page — To-Do

Running list of Article-page-specific gaps found during component audits, kept separate from the general Masthead/breakpoint audit so Article-page work doesn't get buried in it.

---

## 1. Trust/Source tooltip component — needs to be built in Figma

**Found:** 2026-09-15, during the masthead breakpoint audit (`breakpoint-audit.md`), 375px pass, Article page, default load.

**What production shows:** A small tooltip/popover appears over the headline area on article pages, anchored to a trust/sourcing-standard indicator near the "NEWS · [Section]" label. It's a white box with a speech-bubble pointer and its own close (X) button, containing this copy:

> "Based on facts, either witnessed and verified directly by the reporter, or reported and confirmed from knowledgeable sources."

Screenshot reference: captured live on ocregister.com at 375px width (see masthead audit for the full screenshot).

**Gap:** No equivalent component exists yet in Figma (checked WordPress Elements → Menus and Parts, and the Masthead component set — not present there or elsewhere as far as this audit covered).

**Action needed:** Build this as a proper Figma component — tooltip/popover with pointer, close (X) affordance, and the trust-standard copy above as editable text. Confirm with Karl whether this should live near the Masthead/article-header components or as its own standalone "Trust Indicator" component, and whether the copy is static or varies by content type.

**Status:** Open.
