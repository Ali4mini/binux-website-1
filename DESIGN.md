---
name: Binux
description: Reference-led bilingual software engineering website
colors:
  blue: "#3555ed"
  blue-deep: "#1732a8"
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
  button-hover: "#2946d8"
  pill-blue: "#d6e1ff"
  contact-blue: "#0668dc"
typography:
  display:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: "64px"
    fontWeight: 750
    lineHeight: 1.3
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: "44px"
    fontWeight: 750
    lineHeight: 1.3
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Manrope, Arial, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: "18px"
    lineHeight: 1.6
  label:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 600
  persian:
    fontFamily: "Vazirmatn, Arial, sans-serif"
rounded:
  field: "6px"
  tile: "8px"
  button: "10px"
  card: "12px"
  overlay: "14px"
  principle: "20px"
  tag: "30px"
  pill: "40px"
spacing:
  field: "12px"
  card-inline: "24px"
  project-gap: "48px"
  section: "110px"
  section-mobile: "70px"
components:
  button-primary:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    rounded: "{rounded.button}"
    padding: "14px 24px"
  button-primary-hover:
    backgroundColor: "{colors.button-hover}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.button}"
    padding: "14px 24px"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "12px"
  service-card:
    rounded: "{rounded.card}"
    padding: "28px 24px"
  tag:
    textColor: "{colors.muted}"
    rounded: "{rounded.tag}"
    padding: "3px 12px"
---

# Design System: Binux

## Overview

**Creative North Star: "User-pinned SolGuruz reference"**

Binux follows the user-pinned current SolGuruz reference: a light canvas, blue actions, black outlines and offset shadows, large geometric headings, and pastel supporting surfaces. This records the implemented visual system, without introducing another creative direction.

The desktop composition is spacious and centered; supporting content uses bordered cards, alternating project panels, and occasional dark bands. Persian keeps the same visual hierarchy with Vazirmatn, logical spacing, and RTL direction.

**Key Characteristics:**

- White canvas with blue actions and black outlines.
- Offset shadows on buttons and floating navigation.
- Geometric English headings and matched Persian hierarchy.
- Pastel proof pills and project imagery; restrained entrance motion.

## Colors

### Primary

Blue drives primary actions, selected tabs, service icons, links, focus outlines, and process numerals. Blue-deep supplies the primary button border and offset shadow. Button-hover is the implemented darker hover fill. Contact-blue is the separate fixed contact affordance.

### Secondary

Pale-yellow, pill-blue, and pale-green distinguish the three hero pills. Pale-blue supports hover/selected surfaces and project framing. Project illustration panels also use the source's blue, purple, and peach gradients; those are content treatments rather than new action colors.

### Neutral

Paper is the page and card canvas. Heading provides the near-black h1, ink supports text, muted supports secondary copy, and line provides quieter dividers. Dark-section and footer anchor the dark bands. Cards and controls use near-black borders from their source component rules.

## Typography

English headings use locally hosted Manrope; body text uses locally hosted Geist. Persian substitutes locally hosted Vazirmatn for both roles. All font faces use swap. The frontmatter records base desktop roles; component-specific overrides remain intentional.

The hero uses the display role, while inner-page h1 is smaller (58px). Introductory hero text is larger than body (19px, line-height 1.5); inner-page introductions use 21px. Section headings use the headline role; project titles are 31px with line-height 1.35, and service titles use the body family at 24px and weight 500. Labels use the body family. Paragraphs commonly end with 24px of space. FAQ answers are limited to 75ch and CTA copy to 65ch.

At the compact desktop breakpoint, hero h1 becomes 58px. At mobile, hero and inner-page h1 become 40px, h2 becomes 32px, h3 becomes 24px, and body becomes 17px. At the narrow breakpoint, hero h1 becomes 36px. Persian headings remove letter spacing; desktop h1 line-height is 1.6, inner-page h1 is 1.65, and hero paragraphs are 1.9. Mobile Persian hero is 38px/1.65, inner h1 is 36px/1.7, and narrow hero is 34px. Preserve the source's more generous Persian paragraph leading.

## Layout

The centered container caps at 1224px with total horizontal subtraction of 48px. At 1600px and above it caps at 1320px. Sections use the section spacing role, with a 48px gap after centered section headings. The desktop hero starts 250px from the document top; the inner-page hero uses 235px top and 80px bottom padding. The hero heading caps at 1080px, and at 1150px on wide screens.

Project cards alternate 47/53 and 53/47 columns. Services use a 35/61 grid with a 4% gap and a sticky index at 110px. Principles use three columns, process four, technologies six, and the footer four unequal columns. Detail and contact layouts pair explanatory content with a supporting panel or form.

Responsive boundaries are explicit rather than fluid guesses: 1250px compacts navigation and headings; 1050px replaces desktop navigation with a menu toggle, changes process and footer to two columns, and technologies to three. At 760px the container subtracts 40px, topbar/search/header contact action disappear, navigation spans its shell width, hero actions stack, cards and detail/contact layouts become one column, services become a horizontally scrolling index, and technologies become two columns. Mobile hero starts at 151px; inner heroes use 175px/55px padding. Sections use the mobile spacing role. At 370px the container subtracts 32px and process, feature tiles, team, and footer become one column.

The root document sets language and direction. Use logical margins, padding, borders, and insets so Persian mirrors naturally. Brand, email addresses, marquee, technical names, and schematic product illustrations retain LTR where explicitly set. Directional arrows mirror in RTL. The route-preserving language switch is part of shared navigation.

## Elevation & Depth

The signature depth comes from firm offset shadows under buttons and the floating header. Most content cards remain flat and outlined. Soft shadows are reserved for expanded menus, dialogs, the contact drawer, framed project imagery, and the lightly lifted project form. Exact shadow values and motion timings live in the sidecar.

Primary and secondary buttons rise on hover and compress on active. The floating header becomes a full-width pinned strip after scrolling; its border radius and shadow disappear. Project screenshot perspective straightens on hover. Entrance motion uses the existing ease curve: hero content rises subtly, revealed sections translate upward, and menus clip/reveal vertically. The work marquee runs linearly, pauses on hover or keyboard focus, and exposes a static scrollable alternative under reduced motion. Reduced motion disables all animation/transitions, restores automatic scrolling, removes perspective, and hides the duplicate marquee content.

## Shapes

Use softly rounded rectangles with thin dark borders. Buttons use the button radius, fields the field radius, and project/service/form containers the card radius. The floating desktop header has distinctly tighter corners (4px); menus round their lower corners (12px), overlays use the overlay radius, and principles use the principle radius, reduced to 15px on mobile. Tags and hero pills are fully rounded. Keep line icons unfilled with rounded caps and joins; base icons are 22px with a 1.75 stroke.

## Components

### Buttons

Primary blue and white secondary actions share a 58px minimum height, 14px gap, label size 16px, weight 550, and line-height 1.6. Hover translates up 2px and deepens the offset shadow; active translates down 3px and compresses it. The header action uses a smaller 47px minimum height and 9px/20px padding. Full-width work actions use a 76px minimum height and 28px label, reduced on mobile. Disabled buttons show 0.55 opacity and default cursor. Text links use blue, weight 600, and underline on hover.

### Navigation

The desktop floating strip has an 80px minimum height, thin near-black border, and offset shadow. Native details/summary controls expose mega menus; the plus rotates when open and selected/hover navigation turns blue. Services use a sidebar and two-column link grid; compact menus collect work, resources, and company links. Mobile presents a bordered scrollable menu and a 44px toggle whose lines form a close icon when expanded. The fixed header state drops the topbar.

### Cards / Containers

Service cards use a thin dark border and card radius with 28px/24px padding, blue underlined titles, and large line icons. Project cards crop an illustration panel and a copy panel in one outlined container; feature tiles use four pastel fills and colored borders, and metadata uses small outlined tags. Principles are white cards inside a patterned near-black section. Form, fit, and project-detail panels retain their source-specific padding and border treatments.

### Inputs / Fields

Project fields are white with a muted gray border, field radius, 12px padding, 16px text, and blue caret; inputs have a 50px minimum height and fields have 24px bottom spacing. Textareas resize vertically with 1.7 leading. Search uses its own larger 17px field, 14px padding, and tile radius. All focus-visible controls receive a 3px blue outline, normally offset 5px and offset 2px for fields. Native required-field validity remains visible; no custom error visual system is defined.

### Chips / Tabs

Hero pills pair dark text and a line icon on three pastel fills. Metadata tags use muted 13px text, the line border, and compact padding. Technology tabs have a transparent resting background and bottom border; selected state uses blue text and border over pale-blue fill. Keep tab ARIA and keyboard semantics with the source interaction code.

### Accordions and Overlays

FAQs use horizontal dividers and native details/summary. Opening makes the summary blue and rotates its plus 45 degrees. The search dialog uses a dark translucent backdrop, overlay radius, bounded height, and scrolling results. The fixed contact bubble opens a small bordered drawer above it; both use logical inline-end positioning so Persian moves them to the other side. These retain close controls and focus behavior from the existing implementation.

## Do's and Don'ts

### Do:

- Do preserve the pinned SolGuruz visual reference and Binux identity.
- Do use logical inline/block spacing and the Persian font and line-height overrides.
- Do retain visible focus, keyboard controls, and the reduced-motion alternative.
- Do use outlined cards, offset button shadows, and the existing blue/pastel roles consistently.

### Don't:

- Don't invent another visual direction or import the reference company’s branding.
- Don't impose English negative letter spacing on Persian headings.
- Don't force moving marquees or perspective transforms when reduced motion is requested.
- Don't treat illustrative work panels as customer endorsements or commercial metrics.

Source of truth: `static/website/site.css`, `templates/website/base.html`, and `templates/website/page.html`; direction contract: `PRODUCT.md` and `.impeccable/surfaces/website.md`. Reference and implementation captures dated 2026-10-28 are recorded in the surface brief and `.impeccable/review/`. This is a scan of the implemented system.
