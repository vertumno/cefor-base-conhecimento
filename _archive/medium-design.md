---
name: Medium
colors:
  primary: "#1a8917"        # from .em{background:#1A8917} declaration — Medium signature green CTA
  secondary: "#191919"      # from .ct{background:rgba(25,25,25,1)} declaration — secondary near-black CTA
  tertiary: "#156d12"       # from .ep:hover{background:#156D12} declaration — primary green hover state
  neutral: "#6b6b6b"        # from .fb{color:#6B6B6B} declaration — muted text / disabled state
  surface: "#ffffff"        # from .c{background-color:rgba(255,255,255,1)} declaration — page background
  text: "#242424"           # from .co{color:#242424} declaration — primary text color
  text-muted: "#6b6b6b"     # from .by:disabled{color:#6B6B6B} and .fb declaration — muted/disabled text
  border: "#242424"         # from .av{border-bottom:solid 1px #242424} and .ev{border-top:1px solid #242424} declarations
  error: "#c41a16"          # inferred from tokens-detected hex list — closest red present in stylesheet
  success: "#1a8917"        # inferred from primary green — Medium reuses the signature green for affirmative states
  cream: "#f7f4ed"          # from .ao{background-color:#F7F4ED} and .at{background:#F7F4ED} declarations — extended brand-warm reading surface
  near-black: "#191919"     # from rgba(25,25,25,1) — extended named token for secondary CTAs and dark surfaces
  hover-black: "#000000"    # from .cv:hover{background:#000000} declaration — hover destination of secondary CTA
typography:
  h1:
    fontFamily: "gt-super, Georgia, Cambria, Times New Roman, Times, serif"  # from .dw declaration + @font-face family 'gt-super'
    fontSize: 70px           # from .dx{font-size:70px} declaration
    fontWeight: 400          # from .b{font-weight:400} declaration applied at h1 scope (gt-super 400 only weight loaded)
    lineHeight: 74px         # from .dy{line-height:74px} declaration
    letterSpacing: -0.05em   # from .dz{letter-spacing:-0.05em} declaration
  h2:
    fontFamily: "sohne, Helvetica Neue, Helvetica, Arial, sans-serif"  # from .cl declaration + @font-face family 'sohne'
    fontSize: 22px           # from .ed{font-size:22px} declaration
    fontWeight: 400          # from .b declaration — Medium runs h2 at regular weight
    lineHeight: 28px         # from .ee{line-height:28px} declaration
    letterSpacing: 0em       # inferred from absence of letter-spacing rule on h2 selectors (browser default 'normal' converted to 0em)
  h3:
    fontFamily: "sohne, Helvetica Neue, Helvetica, Arial, sans-serif"  # from .cl declaration
    fontSize: 16px           # from .eh{font-size:16px} declaration
    fontWeight: 500          # inferred from sohne weights loaded (400/500/700) — h3 sits between body and h2 weight
    lineHeight: 24px         # from .ei{line-height:24px} declaration
    letterSpacing: 0em       # inferred — no letter-spacing declaration at h3 scope
  body-lg:
    fontFamily: "charter, Georgia, Cambria, Times New Roman, Times, serif"  # from @font-face family 'charter' (Medium's article reading face)
    fontSize: 22px           # inferred from .ed declaration — Medium reading body-large pairs charter with 22/28
    fontWeight: 400          # from @font-face charter-400-normal declaration
    lineHeight: 28px         # from .ee{line-height:28px} declaration
    letterSpacing: 0em       # inferred — no letter-spacing declaration at body scope
  body-md:
    fontFamily: "sohne, Helvetica Neue, Helvetica, Arial, sans-serif"  # from .cl declaration + @font-face family 'sohne'
    fontSize: 14px           # from .cm{font-size:14px} declaration — nav + UI body
    fontWeight: 400          # from .b{font-weight:400} declaration
    lineHeight: 20px         # from .cn{line-height:20px} declaration
    letterSpacing: 0em       # inferred — no letter-spacing declaration at sohne body scope
  body-sm:
    fontFamily: "sohne, Helvetica Neue, Helvetica, Arial, sans-serif"  # from .cl declaration
    fontSize: 13px           # from .fa{font-size:13px} declaration — footer scale
    fontWeight: 400          # from .b declaration
    lineHeight: 20px         # inferred from .cn{line-height:20px} reuse — Medium pairs 13/20 in footer
    letterSpacing: 0em       # inferred — no letter-spacing declaration
  label:
    fontFamily: "sohne, Helvetica Neue, Helvetica, Arial, sans-serif"  # from .cl declaration
    fontSize: 14px           # from .cm declaration — CTA label sizing
    fontWeight: 500          # inferred from sohne 500 weight loaded via @font-face — used for button labels
    lineHeight: 20px         # from .cn declaration
    letterSpacing: 0em       # inferred — no letter-spacing declaration
  mono:
    fontFamily: "source-code-pro, Menlo, Monaco, Consolas, Courier New, monospace"  # from @font-face family 'source-code-pro'
    fontSize: 14px           # inferred from prevailing UI body scale (14px) — Medium inline code matches body-md
    fontWeight: 400          # from @font-face source-code-pro-400-normal declaration
    lineHeight: 20px         # inferred from body-md pairing — Medium aligns mono leading to body grid
    letterSpacing: 0em       # inferred — no letter-spacing declaration
rounded:
  none: 0px                  # inferred — no border-radius declaration on buttons/inputs/cards yields 0
  sm: 0px                    # inferred — no small radius extracted from the stylesheet
  md: 0px                    # inferred — no medium radius extracted; flat-edge default
  lg: 0px                    # inferred — no large radius extracted; flat-edge default
  full: 9999px               # from .dc{border-radius:99em} declaration (99em pill, converted to 9999px functional equivalent)
spacing:
  xs: 8px                    # from .cr{padding:8px 16px} and .ek{padding:8px 20px} declarations — vertical button padding
  sm: 16px                   # from .cr{padding:8px 16px} declaration — secondary CTA horizontal padding
  md: 24px                   # from .ff{margin:0 24px} and .fj{padding:24px 0} declarations — section gutter
  lg: 48px                   # from .ec{margin-bottom:48px} declaration — heading-to-subhead block spacing
  xl: 64px                   # from "0 64px" spacing token — outermost container gutter
preview_tokens:
  button_primary_bg: "#1a8917"        # from .em{background:#1A8917} — primary green CTA fill
  button_primary_text: "#ffffff"      # from .ej{color:#FFFFFF} — primary CTA label
  button_primary_border: "#1a8917"    # from .eo{border-color:#1A8917} — primary CTA outline
  button_secondary_bg: "#191919"      # from .ct{background:rgba(25,25,25,1)} — secondary near-black CTA fill
  button_secondary_text: "#ffffff"    # from .cq{color:rgba(255,255,255,1)} — secondary CTA label
  button_secondary_border: "#191919"  # from .cu{border-color:rgba(25,25,25,1)} — secondary CTA outline
  button_tertiary_text: "#1a8917"     # inferred from primary green — tertiary text-only CTA reuses brand accent
  surface_bg: "#ffffff"               # from .c{background-color:rgba(255,255,255,1)} — page background
  card_bg: "#f7f4ed"                  # from .ao{background-color:#F7F4ED} — cream reading-surface card
  text: "#242424"                     # from .co{color:#242424} — primary text
  text_muted: "#6b6b6b"               # from .fb{color:#6B6B6B} — muted text
  border: "#242424"                   # from .av{border-bottom:solid 1px #242424} — hairline color
  accent: "#1a8917"                   # from .em background — brand accent equals primary green
  button_radius: "9999px"             # from .dc{border-radius:99em} — pill-shaped CTAs
  card_radius: "0px"                  # inferred — no border-radius declared on cream surface (.ao/.at), default flat
  input_radius: "0px"                 # inferred — no border-radius declared on input scope; default flat
---

## Overview

Medium is a reading-and-writing platform whose design system reads like a quietly-confident editorial product: warm cream paper, near-black ink, and one assertive green accent that lights up every call to action. The visual voice is optimistic and community-polished — generous typographic scale paired with pill-shaped buttons, an unmistakable invitation to lean in and read.

## Colors

The palette is a four-note chord. **Primary green `#1a8917`** is Medium's signature — it is the green of "Start reading" and "Get started," the only chromatic note in an otherwise monochrome page. **Secondary `#191919`** (the near-black `rgba(25,25,25,1)` from `.ct`) carries authority CTAs like "Sign in" and "Write" without competing with the green. **Tertiary `#156d12`** is the hover destination of the primary green — a half-shade darker, signalling "you are about to commit" without changing hue.

Neutrals are intentionally narrow. **Text `#242424`** is a single off-black used for body copy, hairline borders, and SVG fills (`fill:#242424`). **Text-muted `#6b6b6b`** carries footer copy and disabled states (`.by:disabled`, `.fb`). The reading surface is split between **white `#ffffff`** for chrome and the warm **cream `#f7f4ed`** that wraps the article hero — the latter is the cue that turns the page from "homepage" into "reading room."

Borders are explicit and one-pixel: `border-bottom:solid 1px #242424` for the topbar divider, `border-top:1px solid #242424` for the footer rule. There is no use of CSS custom properties for color tokens — Medium ships values literally inside atomic utility classes, which means the brand-mark green appears as `#1A8917` in the stylesheet rather than as `var(--brand-primary)`. **Error `#c41a16`** is the only red present in the regex token sweep and is inferred as the destructive role; **success** intentionally collapses onto the primary green, since Medium reuses the brand accent for affirmative confirmation.

`error` and `success` slots emit their inferred hex without alpha; the spec accepts only 6-digit hex, so any rgba/8-digit traces from the broader sweep are dropped before serialisation.

## Typography

Three typefaces, three jobs. **`gt-super`** (Georgia fallback, weight 400, serif) is the editorial display face — it carries the homepage's "Human stories & ideas" at 70px / 74px with a tight `-0.05em` letter-spacing. It only ships at one weight, by design: display headlines speak once and clearly. **`charter`** (Georgia fallback, weights 400 and 700, regular and italic) is the article-body face — the typeface readers actually live in for ten minutes at a time. **`sohne`** (Helvetica Neue fallback, weights 400/500/700) is the UI face — navigation, buttons, footer, captions, every interactive label.

Hierarchy reads top-down: H1 at 70/74 in gt-super for hero display; H2 at 22/28 in sohne for section headings; H3 at 16/24 for sub-sections; body-large at 22/28 in charter for article reading; body-md at 14/20 in sohne for UI; body-sm at 13/20 for footer fine print; labels at 14/20 weight 500 for buttons. **`source-code-pro`** ships as the monospace face for inline code blocks. The supporting `fell`, `noe`, and `opendyslexic` faces in the @font-face manifest are reading-room options Medium offers individual readers, not part of the chrome system. **`medium-content-sans-serif-font`** is the brand-named system stack used as the safe-fallback default body in `.a`.

## Layout

Spacing follows an 8-point rhythm with a generous outer scale. `xs 8px` is the vertical padding inside CTAs (`.cr` and `.ek` both lead with `8px`); `sm 16px` and `xl 20px` are the horizontal CTA paddings; `md 24px` is the section gutter (`margin:0 24px`, `padding:24px 0`); `lg 48px` is the heading-to-subhead block gap (`.ec{margin-bottom:48px}`); `xl 64px` is the outermost container padding pulled from the `0 64px` token. Page width caps at 1192px (`max-width:1192px`), and the topbar holds at 75px tall with a 25px vertical padding ring.

Radius philosophy is binary. Most surfaces — cards, inputs, the cream reading frame — are flat-edged at `0px`; the regex sweep returns only two non-zero radii (`50%` for circular avatars, `99em` for pill CTAs). The pill is the only soft shape on the page and is therefore disproportionately legible: any rounded element on Medium is, by definition, a button. The `99em` value normalises to `9999px` for spec compliance without functional change.

Grid patterns are flex-based. The topbar uses `display:flex; align-items:center; justify-content:center` with horizontal flow; the hero column-stacks via `flex-direction:column`; transitions are uniformly `300ms linear` on background-color and color (`.ba`, `.bb button`).

## Components

**Buttons** are the most opinionated atom. They come in two shapes that share a chassis (pill `border-radius:9999px`, `1px` border, `display:inline-block`, `cursor:pointer`, no text-decoration, `300ms` background/color transition, opacity-based disabled state, `box-sizing:border-box`):

- *Primary* — green `#1a8917` background, `#ffffff` label, `#1a8917` border, `8px 20px` padding. Hover transitions to `#156d12` background and border. Used for "Get started" and "Start reading."
- *Secondary* — near-black `#191919` background, `#ffffff` label, `#191919` border, `8px 16px` padding. Hover transitions to pure `#000000` background with `#242424` border. Used for "Sign in" and "Write."
- *Tertiary* — text-only, no background or border, green `#1a8917` label that underlines on hover (`.fc:hover{text-decoration:underline}`). Used for footer links and inline references.

Disabled state is uniform across button variants: `cursor:not-allowed`, `color:#6B6B6B`, `fill:#6B6B6B`, `opacity:0.1` for secondary or `opacity:0.3` for primary, and the disabled hover is locked to the resting background to suppress motion. The label face is `sohne` at `font-size:20px` for the hero CTA scale (`.am button{font-size:20px}`) and `14px` at the chrome scale.

**Cards** as a pattern materialise in the cream reading surface (`.ao` / `.at` use `background:#F7F4ED`) — there is no boxed card component with rounded corners or shadows; instead, Medium builds editorial regions as flat cream blocks separated by 1px hairlines (`border-bottom:solid 1px #242424`). The "card" is a *zone*, not a *box*. No box-shadow tokens were detected anywhere in the stylesheet (the shadows.json input is empty), confirming an elevation-free aesthetic.

**Inputs** ship transparent by default (the `a, button, input { color:transparent }` reset is present and intentional — Medium relies on overriding utilities to colour each input contextually) and inherit body sohne typography at 14/20. Borders, when applied, are `1px solid #242424` matching the section-rule colour.

**Navigation** is a fixed topbar (`position:fixed`, `top:0`, `left:0`, `right:0`, `z-index:10`) over `#F7F4ED` with a `border-bottom:solid 1px #242424`. Links inside it use sohne at `14px / 20px`, `color:#242424`, no text-decoration; the spacing rhythm is `margin-right:25px` between nav items. The brand mark is a 25px-height SVG with `fill:#242424`, sitting flush-left at 75px container height.

**Footer** drops to `font-size:13px` in `#6B6B6B`, with `padding:24px 0`, `margin-right:20px` between links, and a `1px` top hairline (`border-top:1px solid #242424`). Links inherit the muted gray and reveal an underline on hover — the same tertiary-button affordance reused as the footer-link contract.