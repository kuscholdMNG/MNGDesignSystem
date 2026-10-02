# InLineMessage — Instance Migration Checklist

**Companion to:** `reader-dashboard-inline-message-component-audit.md`
**Component:** `InLineMessage` (COMPONENT_SET, node `2776:2`, in the **main MNG Design System file** (formerly "UI Style Guide") → "In-Line Content Containers | 2026.01.02")
**Generated:** 2026-09-09, via live scan of the files open in the Desktop Bridge (file names updated 2026-09-25)
**Purpose:** Enumerate every live instance of `InLineMessage` across every file/page so your team can verify, after the component is rebuilt, that each one remapped correctly.
**Scope note:** Email Options for Non-Registered Users is excluded from this migration entirely per Karl's request — see §5.

---

## 1. Is remapping actually possible? (short answer)

Yes, with a condition: **as long as I rebuild the component additively — keeping every existing variant node in place under its current name/property values — every instance listed below will continue pointing at its variant automatically, with no manual relink required.** Figma instances bind to a specific variant node inside a component set, not to the component set's structure; if that node still exists after I add new properties (Text/Instance-swap/Boolean) or reorganize non-destructive metadata, instances don't even notice the change.

What is **not** automatically safe: deleting or renaming a variant node (e.g. collapsing `Location` values into a new axis) breaks every instance currently pointing at it — Figma detaches those instances to a "missing component" state rather than silently remapping them. Any consolidation from the audit's recommended axis rework (dropping `Device` as a variant, folding `Location`'s content into properties) has to happen through a **migration**, not a rename: build the new variant node, then programmatically repoint each existing instance's `.setProperties()` / `mainComponent` reference before removing the old node — not before.

So my plan (as I told you earlier) is: add new properties additively first, leave all current variant nodes untouched and in place, and only retire old nodes once I've confirmed — using this same instance list — that nothing is still pointing at them. That's what makes this checklist necessary before any destructive step.

**Update:** the `Location` value `StandAloneEmailPrefs` that turned up 64 times only lives in **Email Options for Non-Registered Users**, which you've since confirmed is excluded from this migration entirely (see §5) — including being fine if its instances break. So that Location doesn't need to be reconciled into the new axis after all; it can be left as-is or retired later without affecting anything in scope here.

---

## 2. How to use this checklist

Each file below lists every page that contains at least one `InLineMessage` instance, grouped by which variant (`Location`) each instance is using, with a live count as of this scan. After I rebuild the component:

1. Open the file.
2. Spot-check a few instances per row — right-click → "Go to main component" should land on the *new* component set, not report "missing component."
3. Check the box once a page's instances look correct.
4. If anything shows a missing-component warning, stop and flag it — don't re-link manually until we talk, in case it reveals a variant I retired too early.

I can also re-run the exact same scan script after the rebuild and diff the results against this file automatically, if that's faster for your team than manual spot-checks — just say the word.

---

## 3. Files with live instances (6 in scope)

### ☐ WordPress Elements (formerly Website Page Templates)
`b1iZxkFwtAYq9rElmnCAzd` · 14 pages scanned · **20 matched instances** across 2 pages

| Page | Instances | Variants in use |
|---|---|---|
| ☐ Menus and Parts | 14 | `Location=AcctMenu, Priority=High, PanelType=HeaderAlert` (Device=Menus) |
| ☐ Stand Alone Pages | 6 | `PrintSubError1` (Medium, Alert) ×2 · `DashSubsCCError` (High, Alert) ×4 |

*(Other 12 pages: no instances — nothing to check.)*

### ☐ MNG Design System (main file, formerly UI Style Guide)
`jFHYqhZbJjvWQmDI4myCsd` · 27 pages scanned · **60 matched instances** across 6 pages

| Page | Instances | Variants in use |
|---|---|---|
| ☐ In-Line Content Containers \| 2026.01.02 | 25 | The component's own documentation page — every variant is demoed here. Expect to see the *most* variety; also the page I'll be actively editing during the rebuild. |
| ☐ Alerts and Icons | 13 | Broad mix — Header, ModalError, and several Dash* alerts |
| ☐ Modal Panels \| 2025.12.29 | 12 | All `ModalError` (High, Alert) |
| ☐ Breakpoints and Page Templates \| 2026.05.19 | 6 | All `Header` (High, HeaderAlert) |
| ☐ Buttons \| 2026.09.30 | 3 | Mixed |
| ☐ Fonts (then "Fonts \| 2026.02.06") | 1 | `ModalError` (High, Alert) |

### ☐ Reader Dashboard v2.0
`PhXogWaQcnNSnQqxyRu4b2` · 17 real pages scanned (full coverage, including two pages that initially timed out and were retried) · **973 matched instances** — by far the heaviest file, as expected since this is where the pattern ships from

| Page | Instances | Notable variants |
|---|---|---|
| ☐ Update Payment Information \| 2025.10.22 | 120 | Header, DashSubsAcctShareALL, DashSubscriptionCCinfo, DashSubsCCupdate |
| ☐ Components \| 2026.02.25 | 137 | Very broad — this page holds working copies of most Location values, including DashProfileDisplayName, DashGiftEmpty/NoneLeft/CTAnonSub, DashSavedEmpty/Full/nonSub, DashSubsAcctShareALL, DashSubsNonSub, DashSubsCCexp/CCError/CCupdate, DashSMSEdit, NewspapersLINA/StndSub, DashSubsUpgradeError, DashSubsCancelError |
| ☐ Notification Prefferences \| DSUB-2242 \| 2025.11.24 | 111 | Header, DashSMSEdit, DashSMSSetUpMVP, DashSMSSetUpv2 |
| ☐ Newspapers Panel \| 2026.02.20 | 100 | Header, NewspapersLINA, NewspapersStndSub |
| ☐ Profile Panel \| 2025.08.05 | 105 | Header, DashProfileDisplayName, ModalError |
| ☐ Gifted Articles \| 2025.10.21 | 80 | Header, DashGiftEmpty, DashGiftNoneLeft, DashGiftCTAnonSub, ModalError |
| ☐ Saved Articles \| 2025.10.21 | 65 | Header, DashSavedEmpty, DashSavedFull, DashSavednonSub |
| ☐ Newsletters \| 2025.08.04 | 49 | Mostly Header, plus ModalError |
| ☐ Basic Page Structure / Nav Menu / LOWA \| 2025.06.13 | 47 | Header, DashSubsAcctShareALL |
| ☐ Upgrade Subscription \| 2025.08.21 | 48 | Header, DashSubsAcctShareALL, ModalError, DashSubsUpgradeError |
| ☐ Subscription Panel \| 2025.12.24 | 41 | Header, DashSubsAcctShareALL, DashSubsNonSub, DashSubsCCexp/CCError, DashSubscriptionCCinfo, DashSubsCCupdate |
| ☐ Cancel Subscription \| 2025.06.24 | 35 | Header, DashSubsAcctShareALL, DashSubsCancelError |
| ☐ Support Panel \| 2026.01.28 | 10 | All Header |
| ☐ Benefits Panel \| 2026.02.24 | 10 | All Header |
| ☐ SubText and Coms \| DSUB-2241 | 10 | DashSMSSetUpMVP, StandAlone |
| ☐ Mobile Apps Panel \| 2025.06.23 | 5 | All Header |
| — Account Dropdown Menus \| *DESIGNS MOVED* | 0 | No instances — nothing to check |

### ☐ Article Personalization Features | 2026
`5sqJvt72nk9Qunw1lw8bBO` · 4 pages scanned · **3 matched instances** across 2 pages

| Page | Instances | Variants in use |
|---|---|---|
| ☐ Next Step Revisions \| started 2026.06.23 | 1 | `Header` (High, HeaderAlert, Device=FOLD) |
| ☐ "Please subscribe to continue…" page | 2 | `DashGiftCTAnonSub` (Medium, Alert) · `DashSavednonSub` (Medium, Alert) |

### ☐ Log In Methods
`E3Aaluxvggdy4PdhHkUuVZ` · 4 pages scanned · **103 matched instances** across 2 pages

| Page | Instances | Variants in use |
|---|---|---|
| ☐ Embedded Login | 102 | Heavy repetition of `Registration` and `Login` (both High, Alert, Device=Menus) |
| ☐ Apple One Tap (AOT) | 1 | `DashProfileDisplayName` (none, Panel) |

### ☐ Custom Checkout Page
`2ATKWXpviAmbYUhREEq2Mc` · 7 pages scanned (full coverage) · **14 matched instances** across 2 pages

| Page | Instances | Variants in use |
|---|---|---|
| ☐ Custom Checkout on Engage Paywall v1 \| 2026.06.22 | 10 | `CustomCheckout` (Medium, Panel) + `ModalError` (High, Alert) |
| ☐ Updated (Karl) v3 \| 2026.05.31 | 4 | Same pattern |
| — Audit — Issues & Cleanup Notes | 0 | No instances |
| — Updated (Kristen) v2 | 0 | No instances |
| — LoFi Wires v1 | 0 | No instances |
| — New Flow Suggestions and updates. | 0 | No instances |
| — Tribune - Old Checkout Flow | 0 | No instances |

---

## 4. Files confirmed clean — no action needed

Listed so it's clear it was scanned, not skipped:

- **CRUX Style Library** (`uwKNDnGRH0otKDrgYiWmUw`) — all 25 pages scanned, 0 instances.

---

## 5. Excluded from this migration entirely

### 🚫 Email Options for Non-Registered Users
`CvIMbKFlZ68vEGaBRzQ3g6` · **103 instances found, not tracked or verified as part of this effort**

You confirmed this file is being handled separately and it's fine if its `InLineMessage` instances break/detach as a side effect of consolidating variants elsewhere. So it's dropped from the checklist and the grand total below, and I won't spot-check or verify it after the rebuild. For the record, what was found here (in case it's useful for whatever separate process handles this file):

| Page | Instances | Variants in use |
|---|---|---|
| Updated Enhanced Unsubscribe Page \| 2026.03.04 | 64 | `StandAloneEmailPrefs` (none, Panel) — only appears in this file — plus some ModalError |
| Email Opt-Out Page \| 2026.06.04 | 20 | Mostly `ModalError` + `Header` |
| Updated Enhanced Unsubscribe Page \| 2026.04.28 | 14 | `OptOutUnsub`/`OptOutReSub` (Confirmation, Panel), Header, ModalError |
| Updated Enhanced Unsubscribe Page \| 2026.03.23 | 5 | Header, `NewspapersStndSub` |
| Enhanced Unsubscribe Page \| 2026.02.23 | 0 | No instances |
| Generic Unsubscribe Page \| 2026.02.21 | 0 | No instances |
| Industry Research | 0 | Not scanned — 0 total instances of anything on this page |

Because `StandAloneEmailPrefs` only shows up here, retiring or leaving that Location value is now a non-issue for the rebuild — nothing in scope depends on it.

---

## 6. Grand total

**1,173 live `InLineMessage` instances** across 6 in-scope files / 22 pages, as of this scan (excludes Email Options for Non-Registered Users per §5).

Note this number is specific to `InLineMessage` alone — it's not directly comparable to the Impact Map's per-file "matched instances" figures (e.g. 2,709 for Email Options for Non-Registered Users), which counted usage of *all 21 component sets* in the Reader Dashboard v2.0 library, not just this one component. `InLineMessage` is one of several library components contributing to those totals.

---

## 7. Verification script (for re-running post-rebuild)

This is the scan I ran to produce the table above — one page at a time, run inside the Desktop Bridge console against each fileKey:

```js
const page = figma.root.children.find(p => p.name === '<PAGE NAME>');
await page.loadAsync();
const instances = page.findAllWithCriteria({ types: ['INSTANCE'] });
const matches = [];
for (let i = 0; i < instances.length; i += 500) {
  const batch = instances.slice(i, i + 500);
  const mains = await Promise.all(batch.map(inst => inst.getMainComponentAsync().catch(() => null)));
  for (let j = 0; j < batch.length; j++) {
    const mc = mains[j];
    if (mc && mc.name && mc.name.includes('PanelType=')) matches.push({ instanceId: batch[j].id, variant: mc.name });
  }
}
return { page: page.name, totalInstances: instances.length, matchCount: matches.length, matches };
```

Re-running this after the rebuild and comparing `matchCount` per page against this document is the fastest way to confirm nothing silently detached. A dropped count, or a `getMainComponentAsync()` result of `null` where there was a match before, means an instance lost its link and needs manual attention before we retire the old variant nodes.

---

## 8. What happens next

I have not made any changes to the `InLineMessage` component yet. Once you give the go-ahead, I'll rebuild additively (new properties added, no existing variant nodes removed), then re-run the verification script above across the 6 in-scope files to confirm this checklist still holds before we talk about retiring any old variants. Email Options for Non-Registered Users stays out of that verification pass per §5.
