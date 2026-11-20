---
name: Binux
description: Reference-led bilingual software engineering website
colors:
  blue: "#3655ef"
  blue-deep: "#142184"
  ink: "#191c26"
  muted: "#535b6b"
  line: "#dfe2e8"
  pale-blue: "#ebf0ff"
  pale-yellow: "#fff4c4"
  pale-green: "#dcfce7"
  paper: "#fff"
  heading: "#050505"
  dark-section: "#030303"
  footer: "#030712"
  pill-blue: "#d6e1ff"
  contact-blue: "#0879f7"
  menu-lilac: "#faf5ff"
  panel-lilac: "#fae8ff"
  menu-blue: "#eff6ff"
  panel-blue: "#dbeafe"
  menu-mint: "#f0fdf4"
  menu-peach: "#fff7ed"
  technology-blue: "#c2d5ff"
  technology-tile: "#fafbfc"
  mobile-expansion: "#ecfccb"
typography:
  display:
    fontFamily: "Panamera, Arial, sans-serif"
    fontSize: "64px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Panamera, Arial, sans-serif"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Panamera, Arial, sans-serif"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: "18px"
    lineHeight: "28px"
  label:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 500
  persian:
    fontFamily: "Vazirmatn, Arial, sans-serif"
rounded:
  field: "6px"
  tile: "8px"
  button: "10px"
  card: "12px"
  overlay: "14px"
  principle: "16px"
  menu: "16px"
  technology: "7px"
  tag: "30px"
  pill: "40px"
spacing:
  field: "12px"
  card-inline: "24px"
  project-gap: "48px"
  section: "120px"
  section-mobile: "80px"
  menu-padding: "11px"
  menu-gap: "12px"
components:
  button-primary:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    rounded: "{rounded.button}"
    padding: "15px 24px"
  button-primary-hover:
    backgroundColor: "{colors.blue}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.button}"
    padding: "15px 24px"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "12px"
  service-card:
    rounded: "{rounded.card}"
    padding: "24px"
  tag:
    textColor: "{colors.muted}"
    rounded: "{rounded.tag}"
    padding: "3px 12px"
  preview-menu:
    backgroundColor: "{colors.menu-lilac}"
    rounded: "{rounded.menu}"
    padding: "11px"
    width: "1040px"
  preview-panel:
    backgroundColor: "{colors.panel-lilac}"
    rounded: "{rounded.tile}"
    padding: "16px"
  technology-tabs:
    backgroundColor: "{colors.technology-blue}"
    textColor: "{colors.ink}"
    padding: "48px"
  mobile-menu:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "16px"
  grouped-preview:
    backgroundColor: "{colors.panel-lilac}"
    padding: "16px"
  faq:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.tile}"
---

# Design System: Binux

## Overview

**Creative North Star: "User-pinned SolGuruz reference"**

Binux follows the user-pinned SolGuruz reference: a light canvas, blue actions, black outlines and offset shadows, Panamera headings, and pastel supporting surfaces. This records the implemented reference-matching system and its measured desktop geometry; it does not claim that every page or viewport is pixel-identical.

The desktop composition is spacious and centered. Navigation uses substantial tabbed preview panels; supporting content uses outlined project panels, a blue technology sidebar, boxed FAQs, and occasional dark bands. Persian preserves the hierarchy through Vazirmatn and RTL layout. Binux branding, approved project examples, and factual business copy remain authoritative.

**Key Characteristics:**

- White canvas with blue actions and black outlines.
- Firm offset shadows on buttons, floating navigation, and preview menus.
- Panamera English display type, Inter body type, and Vazirmatn Persian type.
- Pastel preview panels, real technology logos, and restrained state transitions.

## Colors

### Primary

Blue drives primary actions and focus outlines; blue-deep provides the primary action border and resting offset shadow. Primary hover retains blue. Contact-blue supplies the fixed contact affordance, whose hover fill is darker (#0067da).

### Secondary

Pale-yellow, pill-blue, and pale-green distinguish hero pills. Preview menus pair menu-lilac with panel-lilac, menu-blue with panel-blue, or menu-mint with pale-green. Company uses menu-peach. Open desktop category summaries match their category: Services stays lilac, AI uses menu-blue, industries/work use menu-mint, and company uses menu-peach. Mobile-expansion fills the backdrop when a mobile group is open. Technology-blue fills the tab sidebar; technology-tile fills individual tool tiles. Pale-blue remains available for inherited hover and supporting surfaces. Project illustrations retain their source gradients as content treatments.

### Neutral

Paper is the page and card canvas; heading supplies h1, ink supports text, muted supports secondary copy, and line provides quiet dividers. Dark-section and footer anchor the dark bands. Dark borders remain component-specific: navigation (#171717), buttons (#181818), and preview/technology/FAQ containers (ink).

**The Cascade Rule.** The base template loads `static/website/site.css` first and `static/website/reference.css` second. Reference overrides are canonical for the matched components. Respect selector specificity and the final append-only rules inside reference.css; the old Manrope/Geist stacks, earlier blue values, earlier hero/pill geometry, horizontal technology tabs, and divider-only FAQ treatment are superseded. Unmodified fields, inner-page layouts, and utility styles still inherit site.css.

## Typography

English display type is locally hosted Panamera with exact font-face weights (400, 500, 700, 900). English body and navigation use locally hosted variable Inter (100–900). Both ship with SIL Open Font License files beside the fonts. Persian body/display variables and explicit component overrides use locally hosted Vazirmatn (100–900). All faces use swap; the document preloads Panamera 700 for English or Vazirmatn for Persian. Legacy Manrope/Geist assets may remain on disk; the active base and reference stacks use Panamera and Inter, including the FAQ plus glyph.

The frontmatter gives desktop roles. Hero display is (64px/83.2px, weight 700, -1.28px tracking). Section headings use the headline role; project titles use (32px/40px). Service titles explicitly use Inter (24px/32px, weight 500). Body is (18px/28px), menu labels (16px/24px, weight 500), preview descriptions (12px/16.5px), and hero pills Panamera (18px/28px, weight 700) after the final override. Inner-page h1 retains its base size (58px).

At mobile (760px and below), hero h1 is (40px/52px), h2 is (32px/1.3), and hero pills are (16px/24px, weight 700). Persian hero resolves to (60px/84px) with a maximum width (980px) on desktop, then (38px/1.65) on mobile. Persian hero copy uses (18px/32px) on desktop and (17px/32px) on mobile. Persian headings retain zero letter spacing; project/service paragraphs retain the more generous inherited Persian leading. The final hero overrides take precedence over older compact/narrow hero sizes.

## Layout

The centered container caps at (1224px), subtracting (48px) from viewport width. Reference overrides keep this cap at wide viewports, superseding the base (1320px) wide-screen value. At an English desktop viewport (1440px wide), the floating navigation measures (x108, y58, width1224, height80). Its topbar is (58px) high. Header inline padding is (30px), with a compact desktop adjustment (24px) between (1200px–1370px).

The measured English home hero begins at (y244); its heading uses the display geometry, actions begin at (y658.4), and pills at (y800.4). These are copy- and font-dependent anchors for the current English desktop surface, not coordinates imposed on Persian or every viewport. Hero copy caps at (1034px); its first and second paragraphs reserve (112px) and (56px) respectively, separated by the implemented margins. Actions use a (28px) gap; pills use a centered (24px) gap, (80px) top margin, and English desktop minimum widths (322px, 456px, 359px).

Tabbed preview menus are fixed and centered, measuring (1040px) wide at (x200, y122) in the same desktop viewport. They use a (355px) sidebar, (12px) column gap, (11px) padding, and (1px) border. Sidebar and standard content have minimum height (496px). The CRM-specific grouped content raises its minimum height to (754px), with two labeled columns of nine rows each and a proof/CTA card with minimum height (140px). Column headings use (14px/20px, weight700), descriptions (12px/16px), and a minimum heading block height (52px). Their maximum width is viewport minus (56px), with viewport-bounded scrolling. Resource and company menus use narrower widths (800px) and (920px). Scrolled menus move to (y66).

General sections use the section spacing role; section headings leave (48px). The first content section removes top padding. Services retain a (35%/61%) split and sticky index; projects alternate (47%/53%) and (53%/47%). FAQ uses (35%/remaining) columns, a (24px) gap, and a sticky heading at (110px). Technology uses (40%/60%) columns with a minimum height (800px), (48px) pane padding, and a three-column logo grid. Dark/principle and process bands retain their component-specific spacing.

Desktop navigation switches to the mobile menu at (1199px and below); header search disappears, integrated menu search remains available, and the header language label becomes text. Technology pane padding becomes (30px), tool tiles become two columns, and FAQ heading becomes (40px). Base content-grid breakpoints at (1050px) still apply where reference.css does not override them. At (760px), the container subtracts (40px), the unscrolled header starts at (30px), hero starts at (151px), action buttons wrap in a row, pills stack, sections use (80px), technology becomes one column with a horizontally scrollable tab row, and FAQ becomes one column with a static heading. At (370px), the base container subtraction becomes (32px) and some inherited content grids become one column.

Use logical spacing and document language/direction. Persian mirrors the preview split through grid direction; technology names/logos stay in an LTR grid. Brand text, email, technical names, marquee, and designated product illustrations retain explicit LTR. Language switching preserves the current route.

## Elevation & Depth

Depth is structural: buttons cast a small downward shadow; floating navigation and preview menus cast firm diagonal shadows. Selected preview tabs and preview CTA strips use the same outlined, offset language. Content cards stay mostly flat; inherited soft shadows remain on the search dialog, contact drawer, project form, and framed project imagery. Exact values live in the sidecar.

Hover presses actions diagonally (2px, 2px) and removes their resting shadow. The inherited active state translates down (3px); primary active retains its more-specific compressed shadow. The header becomes a fixed full-width strip as soon as scrollY is greater than zero; the topbar disappears and its border, radius, and offset shadow drop away. It has no entrance animation.

Preview menus enter over (260ms) with cubic-bezier(0.34, 1.25, 0.64, 1), fading and moving horizontally from (16px) to the right of their centered position. Panels enter over (140ms ease-out) from translateY(4px). Menu close fades/moves back to the rightward (16px) offset over (100ms ease-in), following a (150ms) pointer-leave delay. The JavaScript close timeout is also (100ms). Preview tabs activate on mouse hover, click, or vertical keyboard navigation. Hero/reveal animations and project perspective transforms are disabled. The work marquee moves linearly at approximately (50px/second), pauses on hover/focus and when offscreen; subtle dark-band stars twinkle with staggered timing. Reduced motion disables animations/transitions through the inherited important reset, exposes a static scrollable marquee, removes duplicate marquee content, and keeps the stars static. Although reference.css contains a reduced-motion fade, the base important reset wins and panels open immediately.

**The Evidence Rule.** Match the captured component geometry and observed interaction. Do not add entrance choreography or 3D treatments absent from the reference overrides, and do not turn a decorative proof layout into unsupported business claims.

## Shapes

Use rounded rectangles and thin dark borders. Buttons use the button radius; project/service/form panels use card; fields use field. Desktop navigation keeps tight corners (4px), preview menus use menu, preview panes/tabs strips use tile, selected preview buttons use card, and technology frames use technology. FAQ boxes use tile. Hero pills and metadata tags remain fully rounded. Principles now use principle, superseding the earlier desktop (20px) corner. Reference-proof panels use (24px), their image frames (20px), and mobile outer frames (20px). Line icons use rounded caps/joins; technology tools use actual locally hosted logos where supplied.

## Components

### Buttons

Primary blue and white secondary actions share a minimum height (58px), padding from frontmatter, gap (14px), text (16px, weight500), and inherited line-height (1.6). Header actions use a minimum height (48px) and padding (11px 24px); preview CTA buttons use (46px) and (10px 23px). Hover/active behavior follows Elevation & Depth. Disabled controls retain opacity (0.55) and default cursor. Inherited blue text links underline on hover.

### Navigation

Native details/summary supplies open/closed semantics. Active summary has its category-colored outlined rounded backing, blue text, a pressed offset, and a plus rotating (45deg). Services, AI, industries, and work use tabbed previews; resource/company menus retain their own content layouts. The selected preview tab has a dark outline and downward shadow. Preview links reveal a white outlined hover surface; each panel ends with an outlined, offset CTA strip using factual Binux copy. Tab panels use ARIA selection, roving tabindex, and Home/End/arrow keys. Escape, click outside, and focus departure close menus. The mobile menu is an integrated fixed panel from (top30px) to the viewport bottom, inset (16px) on both sides, with a (2px) dark border, top corners (4px), (16px) padding, and offset shadow (4px 4px). This final override replaces the earlier below-header positions in both scrolled and unscrolled states. The underlying navigation shell hides and body scrolling locks while open. A brand/language/close row leads to the integrated search field, six expandable groups, quote link, quick email/contact actions, and a primary contact action. Only one group opens at a time; open summaries turn blue with a (2px) lower border and rotate the plus. Category content uses lilac, blue, mint, or peach backgrounds; the page-covering backdrop changes from white to mobile-expansion when any group opens. Search normalizes Persian letter variants and filters the shared local content index. Close and Escape restore toggle focus; resizing to desktop closes the panel.

### Cards / Containers

Service cards use thin dark borders, card corners, (24px) padding, and blue underlined titles. Project panels retain approved illustrations/screenshots paired with copy and colored feature tiles; screenshots have no perspective/hover transform. Principles are white outlined cards in a near-black star band. The reference-proof image/text split is an approved project demonstration, not a testimonial. Process steps sit in one outlined white grid on a pale-green section.

### Inputs / Fields

Project fields remain white with muted gray borders, field corners, (12px) padding, (16px) text, blue caret, and minimum input height (50px). Textareas resize vertically. Focus-visible uses a blue (3px) outline, usually offset (5px) or (2px) for fields. Native validity remains visible; no invented custom error system is defined. Contact prepares an email draft and must describe that state accurately.

### Chips / Tabs

Hero pills follow the final geometry and type overrides above. Metadata uses muted (13px) labels, line borders, tag corners, and compact padding. The technology frame has a blue vertical sidebar and white content pane; selected tabs are white and dark outlined, not blue underlined horizontal tabs. Tool tiles use local real logos (24px) with text and a neutral tile surface. Mobile changes the sidebar into a scrollable row. Keep ARIA selection and keyboard behavior from site.js.

### Accordions and Overlays

FAQs are individually outlined boxes with (28px) vertical gaps. Summary text is (18px/28px, weight600), padding (16px 24px), minimum height (60px), and stays ink when open; the plus rotates (45deg). Answers have padding (0 24px 20px). Only one FAQ opens at a time. On mobile, gap becomes (16px), summary becomes (16px/24px) with (16px) padding, and answers use (0 16px 16px).

Search retains its modal backdrop, bounded scrolling, and close/focus behavior. The fixed contact affordance uses the reference blue ribbon form with a folded corner, width (300px) capped by viewport minus (32px), and a drawer above it. Preserve its explicit Persian placement overrides and existing focus/close behavior.

## Do's and Don'ts

### Do:

- Do preserve the pinned SolGuruz visual reference and Binux identity.
- Do resolve visual values through site.css followed by reference.css, including late overrides and selector specificity.
- Do preserve RTL, route-preserving language switching, visible focus, keyboard controls, and reduced motion.
- Do use approved project imagery and the local technology logos with accurate labels.

### Don't:

- Don't invent another visual direction or import the reference company’s branding.
- Don't reintroduce hero blur/rise entrances, section reveals, or project perspective effects disabled by the reference overrides.
- Don't impose English negative letter spacing on Persian headings.
- Don't present illustrative work panels as testimonials, ratings, customer endorsements, or commercial metrics.
- Don't infer global pixel identity from the measured English desktop anchors.

Source of truth: the resolved cascade of `static/website/site.css` followed by `static/website/reference.css`; component markup in `templates/website/base.html`, `templates/website/page.html`, and `templates/website/partials/` (including `mobile-navigation.html` and the grouped preview in `mega.html`); interactions in `static/website/site.js`. Product constraints remain in `PRODUCT.md`; reference captures and parity evidence remain in `.impeccable/surfaces/website.md` and `.impeccable/review/`. This documentation records source parity and supplied measured anchors, not a new whole-site visual-validation claim.
