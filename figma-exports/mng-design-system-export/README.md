# MNG Design System — component spec export

Exported 2026-09-24 from Figma. 49 items (27 components, 22 assemblies, 345 variants). Page templates are not included; the homepage templates are used only as "where it is used" and breakpoint evidence.

## Sources

- **Homepage components** — WordPress Elements ▸ Homepage ▸ Components (3334:42288)
- **Menus and Parts** — WordPress Elements ▸ Menus and Parts ▸ Push Nav Section Menu, Frame 12634 (Mastheads), Frame 12776 (User & Account Menus), Frame 12804 (Breaking News), Frame 12774 (Footer)
- **Form Fields** — MNG Design System ▸ Form Fields | 2026.09.24 (all components)

## How an agent should use this folder

1. Read `index.json` to find the item (by name, group or breakpoint). Items are numbered in build order: leaf components before the assemblies that contain them.
2. Open the item's `.md` for the human-readable spec, or its `.json` twin for exact values (`variants[].layerTree` holds the full Figma layer tree with sizes, auto-layout, fills, text styles and instance references).
3. Start rendering from the `.html` skeleton, which already maps auto-layout to flexbox and colors to `tokens.css`. Replace each dashed `data-component` placeholder with the skeleton of the referenced component.
4. Pick variants per breakpoint using the breakpoint table below.
5. Check `Known issues` before trusting a value; compare with the preview PNGs.

## Breakpoints

| Key | Viewport | Template | Bucket |
|---|---|---|---|
| 340 | ≤639px (XS-Fold, built 340) | 340 HomePage | XS-Fold |
| 360 | ≤639px (SM-Mobile, built 360) | Mobile HomePage | SM-Mobile |
| 768 | 640–799px (MD-TabletV) | 768 HomePage | MD-TabletV |
| 1024 | 800–1039px (LG-TabletH, built 1009) | 1024 HomePage | LG-TabletH |
| 1100 | ≥1040px (XL-Desktop, built 1085) | 1100 HomePage | XL-Desktop |
| 1280 | ≥1040px (XL-Desktop, built 1280) | Desktop HomePage | XL-Desktop |

Variant values map onto these keys as follows: `XS-Fold`/`FOLD` → 340, `SM-Mobile`/`Mobile` → 360 (and 340 when no Fold variant exists), `MD-TabletV`/`Tablet` → 768, `LG-TabletH`/`1024` → 1024, `XL-Desktop`/`Desktop` → 1100 and 1280. Form-field `Size=Mobile` → ≤639px and `Size=Desktop` → ≥640px.

## Homepage components (24)

| # | Item | Kind | Variants | Breakpoints | Built from (in export) | Issues |
|---|---|---|---|---|---|---|
| 1 | [Article Status Badge](homepage/components/01-article-status-badge/article-status-badge.md) | component | 3 | 340, 360, 768, 1024, 1100, 1280 |  | 4 |
| 2 | [Related Article List Item](homepage/components/02-related-article-list-item/related-article-list-item.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 |  | 1 |
| 3 | [Article Image Placeholder](homepage/components/03-article-image-placeholder/article-image-placeholder.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 |  | 2 |
| 4 | [Zone 1 Lead Article Card](homepage/components/04-zone-1-lead-article-card/zone-1-lead-article-card.md) | component | 3 | 340, 360, 768, 1024, 1100, 1280 | Article Status Badge, Article Image Placeholder, Related Article List Item | 2 |
| 5 | [TopZone Article Card](homepage/components/05-topzone-article-card/topzone-article-card.md) | component | 2 | 340, 360, 768, 1024, 1100, 1280 | Article Image Placeholder, Article Status Badge | 2 |
| 6 | [Section Title / Eyebrow](homepage/components/06-section-title-eyebrow/section-title-eyebrow.md) | component | 2 | 340, 360, 768, 1024, 1100, 1280 |  | 1 |
| 7 | [Latest Headlines List Item](homepage/components/07-latest-headlines-list-item/latest-headlines-list-item.md) | component | 3 | 340, 360, 768, 1024, 1100, 1280 | Article Status Badge | 1 |
| 8 | [Newsletter Signup](homepage/components/08-newsletter-signup/newsletter-signup.md) | component | 2 | 340, 360, 768, 1024, 1100, 1280 |  | 0 |
| 9 | [Latest Headlines](homepage/assemblies/09-latest-headlines/latest-headlines.md) | assembly | 3 | 340, 360, 768, 1024, 1100, 1280 | Section Title / Eyebrow, Latest Headlines List Item, Newsletter Signup | 0 |
| 10 | [Gallery Icon Badge](homepage/components/10-gallery-icon-badge/gallery-icon-badge.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 |  | 1 |
| 11 | [Horizontal Thumbnail Card](homepage/components/11-horizontal-thumbnail-card/horizontal-thumbnail-card.md) | component | 3 | 340, 360, 768, 1024, 1100, 1280 | Article Image Placeholder, Gallery Icon Badge | 1 |
| 12 | [TOP ZONE Block](homepage/assemblies/12-top-zone-block/top-zone-block.md) | assembly | 3 | 340, 360, 768, 1024, 1100, 1280 | Zone 1 Lead Article Card, Article Image Placeholder, TopZone Article Card, Latest Headlines, Article Status Badge, Horizontal Thumbnail Card | 2 |
| 13 | [Most Popular List Item](homepage/components/13-most-popular-list-item/most-popular-list-item.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 |  | 0 |
| 14 | [Blueconic Block (Most Popular)](homepage/assemblies/14-blueconic-block-most-popular/blueconic-block-most-popular.md) | assembly | 3 | 340, 360, 768, 1024, 1100, 1280 | Section Title / Eyebrow, Most Popular List Item | 2 |
| 15 | [Horizontal Feature Card](homepage/components/15-horizontal-feature-card/horizontal-feature-card.md) | component | 1 | 768, 1100, 1280 | Article Image Placeholder | 0 |
| 16 | [1Col Article Card](homepage/components/16-1col-article-card/1col-article-card.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 | Article Image Placeholder, Article Status Badge | 0 |
| 17 | [Feature + List Content Block](homepage/assemblies/17-feature-list-content-block/feature-list-content-block.md) | assembly | 2 | 768, 1024, 1100, 1280 | Horizontal Feature Card, 1Col Article Card, Article Image Placeholder | 0 |
| 18 | [Section Rail Card](homepage/assemblies/18-section-rail-card/section-rail-card.md) | assembly | 9 | 340, 360, 768, 1024, 1100, 1280 | Section Title / Eyebrow, 1Col Article Card, Feature + List Content Block | 0 |
| 19 | [Video Tile Image Placeholder](homepage/components/19-video-tile-image-placeholder/video-tile-image-placeholder.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 |  | 2 |
| 20 | [Videos from OCRegister Carousel](homepage/assemblies/20-videos-from-ocregister-carousel/videos-from-ocregister-carousel.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Video Tile Image Placeholder | 2 |
| 21 | [Show More Photos Affordance](homepage/components/21-show-more-photos-affordance/show-more-photos-affordance.md) | component | 1 | 340, 360, 768, 1024, 1100, 1280 |  | 1 |
| 22 | [Photos Block](homepage/assemblies/22-photos-block/photos-block.md) | assembly | 3 | 340, 360, 768, 1024, 1100, 1280 | Section Title / Eyebrow, Article Image Placeholder, Article Status Badge, Horizontal Thumbnail Card, Show More Photos Affordance, Gallery Icon Badge, 1Col Article Card | 5 |
| 23 | [Upcoming Events Widget (768, 3 cards, 7 days)](homepage/components/23-upcoming-events-widget-768-3-cards-7-days/upcoming-events-widget-768-3-cards-7-days.md) | component | 1 | 768 |  | 2 |
| 24 | [Upcoming Events Block](homepage/assemblies/24-upcoming-events-block/upcoming-events-block.md) | assembly | 5 | 340, 360, 768, 1024, 1100, 1280 | Upcoming Events Widget (768, 3 cards, 7 days) | 5 |

## Menus and Parts (12)

| # | Item | Kind | Variants | Breakpoints | Built from (in export) | Issues |
|---|---|---|---|---|---|---|
| 25 | [Weather Bug](menus-and-parts/components/25-weather-bug/weather-bug.md) | component | 2 | 1100, 1280 |  | 2 |
| 26 | [SectionMenuHeader](menus-and-parts/components/26-sectionmenuheader/sectionmenuheader.md) | component | 6 | 340, 360, 768, 1024, 1100, 1280 |  | 2 |
| 27 | [AlertLevel](menus-and-parts/components/27-alertlevel/alertlevel.md) | component | 8 | 340, 360, 768, 1024 |  | 1 |
| 28 | [UserImage](menus-and-parts/components/28-userimage/userimage.md) | component | 12 | 340, 360, 768, 1024 |  | 2 |
| 29 | [SearchBar](menus-and-parts/components/29-searchbar/searchbar.md) | component | 2 | 340, 360, 768, 1024, 1100, 1280 |  | 2 |
| 30 | [Breaking News Banner](menus-and-parts/components/30-breaking-news-banner/breaking-news-banner.md) | component | 3 | 340, 360, 768, 1024, 1100, 1280 |  | 1 |
| 31 | [Footer](menus-and-parts/components/31-footer/footer.md) | component | 5 | 340, 360, 768, 1024, 1100, 1280 |  | 3 |
| 32 | [SectionMenuItem](menus-and-parts/assemblies/32-sectionmenuitem/sectionmenuitem.md) | assembly | 9 |  | Weather Bug | 1 |
| 33 | [UserPic](menus-and-parts/assemblies/33-userpic/userpic.md) | assembly | 6 | 340, 360, 768, 1024 | UserImage, AlertLevel | 1 |
| 34 | [SectionMenu](menus-and-parts/assemblies/34-sectionmenu/sectionmenu.md) | assembly | 15 | 340, 360, 768, 1024, 1100, 1280 | SectionMenuHeader, SectionMenuItem | 3 |
| 35 | [UserStatus](menus-and-parts/assemblies/35-userstatus/userstatus.md) | assembly | 4 | 340, 360, 768, 1024, 1100, 1280 | UserPic | 3 |
| 36 | [Masthead](menus-and-parts/assemblies/36-masthead/masthead.md) | assembly | 75 | 340, 360, 768, 1024, 1100, 1280 | SectionMenu, Weather Bug | 9 |

## Form Fields (13)

| # | Item | Kind | Variants | Breakpoints | Built from (in export) | Issues |
|---|---|---|---|---|---|---|
| 37 | [Form Field](form-fields/components/37-form-field/form-field.md) | component | 10 | 340, 360, 768, 1024, 1100, 1280 |  | 5 |
| 38 | [Code Box](form-fields/components/38-code-box/code-box.md) | component | 10 | 340, 360, 768, 1024, 1100, 1280 |  | 2 |
| 39 | [Form Field Assembly / Checkbox + Terms](form-fields/assemblies/39-form-field-assembly-checkbox-terms/form-field-assembly-checkbox-terms.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 |  | 1 |
| 40 | [Search Field / Obituaries — Core](form-fields/components/40-search-field-obituaries-core/search-field-obituaries-core.md) | component | 1 |  |  | 0 |
| 41 | [Form Field (Dashboard Mockup Set)](form-fields/components/41-form-field-dashboard-mockup-set/form-field-dashboard-mockup-set.md) | component | 102 | 340, 360, 768, 1024, 1100, 1280 |  | 2 |
| 42 | [Form Field Assembly / Name pair](form-fields/assemblies/42-form-field-assembly-name-pair/form-field-assembly-name-pair.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Form Field | 1 |
| 43 | [Form Field Assembly / Zip + Street #](form-fields/assemblies/43-form-field-assembly-zip-street/form-field-assembly-zip-street.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Form Field | 1 |
| 44 | [Form Field Assembly / Zip + Phone](form-fields/assemblies/44-form-field-assembly-zip-phone/form-field-assembly-zip-phone.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Form Field | 1 |
| 45 | [Form Field Assembly / Address block](form-fields/assemblies/45-form-field-assembly-address-block/form-field-assembly-address-block.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Form Field | 1 |
| 46 | [Form Field Assembly / CC details](form-fields/assemblies/46-form-field-assembly-cc-details/form-field-assembly-cc-details.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Form Field | 0 |
| 47 | [Form Field Assembly / Password](form-fields/assemblies/47-form-field-assembly-password/form-field-assembly-password.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Form Field | 1 |
| 48 | [Form Field Assembly / Verification Code](form-fields/assemblies/48-form-field-assembly-verification-code/form-field-assembly-verification-code.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Code Box | 1 |
| 49 | [Search Field / Obituaries](form-fields/assemblies/49-search-field-obituaries/search-field-obituaries.md) | assembly | 2 | 340, 360, 768, 1024, 1100, 1280 | Search Field / Obituaries — Core | 1 |

## Dependency graph

```mermaid
flowchart LR
  subgraph homepage["Homepage components"]
    n0["Article Status Badge"]
    n1["Related Article List Item"]
    n2["Article Image Placeholder"]
    n3["Zone 1 Lead Article Card"]
    n4["TopZone Article Card"]
    n5["Section Title / Eyebrow"]
    n6["Latest Headlines List Item"]
    n7["Newsletter Signup"]
    n8[["Latest Headlines"]]
    n9["Gallery Icon Badge"]
    n10["Horizontal Thumbnail Card"]
    n11[["TOP ZONE Block"]]
    n12["Most Popular List Item"]
    n13[["Blueconic Block (Most Popular)"]]
    n14["Horizontal Feature Card"]
    n15["1Col Article Card"]
    n16[["Feature + List Content Block"]]
    n17[["Section Rail Card"]]
    n18["Video Tile Image Placeholder"]
    n19[["Videos from OCRegister Carousel"]]
    n20["Show More Photos Affordance"]
    n21[["Photos Block"]]
    n22["Upcoming Events Widget (768, 3 cards, 7 days)"]
    n23[["Upcoming Events Block"]]
  end
  subgraph menus_and_parts["Menus and Parts"]
    n24["Weather Bug"]
    n25["SectionMenuHeader"]
    n26["AlertLevel"]
    n27["UserImage"]
    n28["SearchBar"]
    n29["Breaking News Banner"]
    n30["Footer"]
    n31[["SectionMenuItem"]]
    n32[["UserPic"]]
    n33[["SectionMenu"]]
    n34[["UserStatus"]]
    n35[["Masthead"]]
  end
  subgraph form_fields["Form Fields"]
    n36["Form Field"]
    n37["Code Box"]
    n38[["Form Field Assembly / Checkbox + Terms"]]
    n39["Search Field / Obituaries — Core"]
    n40["Form Field (Dashboard Mockup Set)"]
    n41[["Form Field Assembly / Name pair"]]
    n42[["Form Field Assembly / Zip + Street #"]]
    n43[["Form Field Assembly / Zip + Phone"]]
    n44[["Form Field Assembly / Address block"]]
    n45[["Form Field Assembly / CC details"]]
    n46[["Form Field Assembly / Password"]]
    n47[["Form Field Assembly / Verification Code"]]
    n48[["Search Field / Obituaries"]]
  end
  n0 --> n3
  n2 --> n3
  n1 --> n3
  n2 --> n4
  n0 --> n4
  n0 --> n6
  n5 --> n8
  n6 --> n8
  n7 --> n8
  n2 --> n10
  n9 --> n10
  n3 --> n11
  n2 --> n11
  n4 --> n11
  n8 --> n11
  n0 --> n11
  n10 --> n11
  n5 --> n13
  n12 --> n13
  n2 --> n14
  n2 --> n15
  n0 --> n15
  n14 --> n16
  n15 --> n16
  n2 --> n16
  n5 --> n17
  n15 --> n17
  n16 --> n17
  n18 --> n19
  n5 --> n21
  n2 --> n21
  n0 --> n21
  n10 --> n21
  n20 --> n21
  n9 --> n21
  n15 --> n21
  n22 --> n23
  n24 --> n31
  n27 --> n32
  n26 --> n32
  n25 --> n33
  n31 --> n33
  n32 --> n34
  n33 --> n35
  n24 --> n35
  n40 --> n41
  n40 --> n42
  n40 --> n43
  n40 --> n44
  n40 --> n45
  n40 --> n46
  n37 --> n47
  n39 --> n48
```

Assemblies are drawn as `[[ ]]`. Arrows point from the building block to the item that contains it.

## Tokens

`tokens.css` defines 13 color variables bound in Figma; `tokens.json` also lists every hex value in use, placeholder colors, all font/size/line-height combinations and the breakpoints.

| Variable | CSS | Hex | Other modes |
|---|---|---|---|
| Colors/color/feedback/high-error | --mng-feedback-high-error | #CC2B27 |  |
| Colors/color/feedback/low-success | --mng-feedback-low-success | #2E8000 |  |
| Colors/color/feedback/medium | --mng-feedback-medium | #856A00 |  |
| Colors/color/gray/100 | --mng-gray-100 | #393938 |  |
| Colors/color/gray/200 | --mng-gray-200 | #5E5D5C |  |
| Colors/color/gray/300 | --mng-gray-300 | #838280 |  |
| Colors/color/gray/400 | --mng-gray-400 | #A7A6A3 |  |
| Colors/color/gray/500 | --mng-gray-500 | #CCCAC7 |  |
| Colors/color/gray/600 | --mng-gray-600 | #F1EFEB |  |
| Colors/color/gray/max | --mng-gray-max | #FFFFFF |  |
| Colors/color/gray/min | --mng-gray-min | #141414 |  |
| Colors/color/theme/primary | --mng-theme-primary | #007580 | #8D092D |
| Colors/color/theme/primary-dark | --mng-theme-primary-dark | #0A5962 |  |

## Folder layout

```
README.md  index.json  tokens.json  tokens.css
<group>/components/NN-slug/   slug.md  slug.json  slug.html  previews/*.png
<group>/assemblies/NN-slug/   …same…
```

Groups: `homepage/`, `menus-and-parts/`, `form-fields/`.

## Not included

- Components on Menus and Parts outside the requested frames (AccountMenu in Frame 12695, Footer_w_signup in Frame 12775, the draft Logo, Event Card). They appear only as external references where other items use them.
- Components from other pages (Icons, Ad Blocks, Button Primary/Linkstyle, CheckBox, NavMenu, etc.). These are listed as "not in this export" dependencies.
- Page templates (components only, as requested). Template names such as "Desktop HomePage" still appear in each spec under Where it is used.
- Content rules and accessibility notes (not in the selected scope).
