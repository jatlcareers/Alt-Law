# Alt+Law — Claude Code Build Prompt

You are building **Alt+Law**, a public-facing web guide for law students published by JATL (Justice and the Law Society, UQ student society). It's a counter-guide to traditional commercial-clerkship-focused careers guides, showcasing the full spectrum of legal practice with a social-justice lean.

This prompt is the single source of truth for the build. Read it end-to-end before you start. The accompanying file `CONTENT.md` contains all verbatim content; `content/` contains structured JSON/MDX files you should populate during the build.

---

## Part 1 — Project setup

### Tech stack (locked)
- **Framework:** Next.js 15+ with App Router, TypeScript
- **Styling:** Tailwind CSS v4
- **Content:** MDX for long-form prose, JSON for structured data (orgs, testimonials, pathways)
- **Hosting target:** Vercel
- **Package manager:** pnpm (fall back to npm if pnpm is unavailable)

### Initial commands
```bash
pnpm create next-app@latest alt-law --typescript --tailwind --app --src-dir --import-alias "@/*" --no-eslint
cd alt-law
pnpm add @next/mdx @mdx-js/loader @mdx-js/react gray-matter remark-gfm rehype-slug rehype-autolink-headings clsx tailwind-merge lucide-react
pnpm add -D @types/mdx
```

### Folder structure to create
```
src/
├── app/
│   ├── (marketing)/
│   │   ├── layout.tsx                    # site shell (nav + footer + AoC popup)
│   │   ├── page.tsx                      # home
│   │   ├── about/page.tsx
│   │   ├── forewords/page.tsx
│   │   ├── contact/page.tsx
│   │   ├── pathways/
│   │   │   ├── page.tsx                  # pathway index grid
│   │   │   └── [slug]/
│   │   │       ├── page.tsx              # generic pathway renderer
│   │   │       └── [orgSlug]/page.tsx    # per-org sub-page (only used by CLCs)
│   │   ├── resources/
│   │   │   ├── page.tsx                  # resource index (3 cards)
│   │   │   └── [slug]/page.tsx           # resource sub-pages
│   │   └── disclaimer/page.tsx
│   ├── layout.tsx                        # root layout
│   └── globals.css                       # Tailwind + design tokens
├── components/
│   ├── nav/SiteHeader.tsx
│   ├── nav/SiteFooter.tsx
│   ├── popup/AcknowledgementPopup.tsx
│   ├── popup/Modal.tsx                   # generic accessible modal primitive
│   ├── popup/TestimonialsModal.tsx
│   ├── popup/ResourceModal.tsx
│   ├── pathway/PathwayHeader.tsx
│   ├── pathway/OrgGrid.tsx               # 'cards' display mode
│   ├── pathway/OrgButtonRow.tsx          # 'buttonRow' display mode
│   ├── pathway/OrgTable.tsx              # 'table' display mode
│   ├── pathway/PathwayBody.tsx           # MDX renderer for body prose
│   ├── pathway/RelatedPathways.tsx
│   ├── resource/ResourcePageRenderer.tsx
│   ├── resource/LinkSection.tsx
│   ├── resource/ProseSection.tsx
│   ├── resource/ContactBlock.tsx
│   ├── resource/ComparisonTable.tsx
│   ├── resource/CopyTemplate.tsx         # the copy-to-clipboard template block
│   └── ui/                                # buttons, cards, etc.
├── content/
│   ├── pathways/                         # one MDX/JSON pair per pathway
│   ├── resources/                        # one MDX/JSON pair per resource sub-page
│   ├── forewords.json
│   ├── testimonials.json                 # ~85 entries
│   └── site.json                         # nav, footer, AoC text, disclaimer
└── lib/
    ├── content.ts                        # content loaders
    ├── types.ts                          # all TypeScript types (see Part 4)
    └── og.ts                             # OpenGraph helpers
```

---

## Part 2 — Brand & design

### Colour palette (CSS variables in `globals.css`)
```css
:root {
  --bg: #ffffff;
  --bg-muted: #f6f6f4;
  --surface: #ffffff;
  --border: #e5e5e2;
  --text: #1a1a1a;
  --text-muted: #5a5a5a;
  --text-subtle: #8a8a85;
  --accent: #2f7d4f;            /* JATL green — keyboard tile */
  --accent-hover: #266740;
  --accent-fg: #ffffff;
  --ink: #0d0d0d;               /* hero/dark panel background */
  --ink-fg: #ffffff;
  --warning: #b45309;
}
```
The "A+L" logo is a black square tile + green square tile rendered as keyboard keys. Build it as inline SVG or a small React component — don't depend on a logo file unless one is supplied.

### Typography
- Sans-serif system stack with Inter as preferred web font (load from `next/font/google`)
- Body 16px / 1.6 line height; headings tight tracking
- Long-form prose pages: max-width ~70ch
- Card grids: max-width ~1280px outer container

### Layout patterns
- Top nav: Home · About JATL ▾ · Career Pathways ▾ · Resources ▾ · Contact
- Hero (home only): dark `--ink` panel, white heading, two CTAs (`Join JATL →`, `Explore Career Pathways`)
- Footer: site links + sponsor acknowledgements (College of Law, QLS) + brief disclaimer with link to full disclaimer page
- Mobile: full hamburger nav, single-column stacks for grids
- Responsive breakpoints: `sm:640 md:768 lg:1024 xl:1280`

### Visual rules
- **Minimal formatting** — prefer whitespace over rules and dividers
- **One accent only** — green is for CTAs, active states, and accents. Don't multiply colours.
- **Cards have soft shadow + 1px border** — `shadow-sm border border-[--border] rounded-xl`
- **Hover states subtle** — small Y-shift on cards, accent colour on links
- **No gradient backgrounds**, no decorative patterns
- **Icons:** lucide-react throughout (16/20/24px sizes)

### Editorial voice signal
JATL-authored content (B3.x, forewords, intro copy) should feel editorially distinct from sourced content (BEL/UQ/QLS resources). Add a small "From JATL" tag/byline on JATL-authored Resources pages. Don't overdo it — a single inline label is enough.

---

## Part 3 — Information architecture

### Top-level pages
- `/` — Home
- `/about` — About JATL (objectives + mission + Join QR)
- `/forewords` — Stacked foreword cards
- `/pathways` — Career Pathways index (grid of icon cards)
- `/pathways/[slug]` — Individual pathway page
- `/pathways/community-legal-centres/[orgSlug]` — Per-CLC sub-page (only CLCs use this)
- `/resources` — Resources index (3 category cards)
- `/resources/[slug]` — Individual resource sub-page
- `/contact` — Contact
- `/disclaimer` — Full legal disclaimer

### Pathway list (canonical order)
1. Community Legal Centres (`community-legal-centres`) — `cards` mode, has per-org pages
2. Legal Aid Queensland (`legal-aid-queensland`) — single-org, no display mode
3. Associateships (`associateships`) — `buttonRow`, two sub-sections (QLD / Commonwealth)
4. Government & Public Service (`government-and-public-service`) — `buttonRow`, two sub-sections (Federal / Queensland)
5. First Nations' Law (`first-nations-law`) — `table`
6. International Law (`international-law`) — `table`
7. Family Law (`family-law`) — `buttonRow` with single Organisations popup
8. Criminal Law (`criminal-law`) — hybrid: top-level Testimonials + sub-section button row
9. Plaintiff Personal Injury (`plaintiff-personal-injury`) — `buttonRow` single popup
10. Boutique & Other Specialties (`boutique-and-other-specialties`) — `buttonRow` single popup
11. Academia (`academia`) — prose-only
12. In-House Law (`in-house-law`) — `buttonRow` with two `resource-modal` popups
13. The Bar (`the-bar`) — `buttonRow` single Opportunities popup
14. Legal Technology (`legal-technology`) — **status: coming-soon**
15. Pro Bono Within Commercial Firms (`pro-bono-commercial-firms`) — **status: coming-soon**

### Resources sub-page list (15 sub-pages across 3 categories)
**Category 1: Resources and Guides**
- `job-search`
- `career-support`
- `external-resources`
- `resumes`
- `cover-letters`

**Category 2: Networking, Interviews and Job Recruitment Help**
- `preparing-for-applications`
- `job-interviews`
- `understand-the-recruitment-process`
- `get-workplace-ready`
- `get-experience`

**Category 3: JATL's Career Tips**
- `personal-branding-and-networking-tips`
- `career-mentoring`
- `linkedin`
- `information-interview-guide`
- `jatl-recommends` — **status: partial** (skeleton only)

---

## Part 4 — Content model (TypeScript types)

Put all of this in `src/lib/types.ts`.

```typescript
// ============================================================================
// PATHWAYS
// ============================================================================

export type DisplayMode = 'cards' | 'buttonRow' | 'table' | 'prose-only';

export type LinkType =
  | 'page'              // resolves to a sub-page on this site
  | 'modal'             // opens an org-info popup
  | 'external'          // outbound link
  | 'testimonials-modal' // opens the testimonials list popup
  | 'resource-modal';   // long-form essay/resource popup

export type OrgLink = {
  label: string;
  type: LinkType;
  href?: string;        // required for 'external'; slug for 'page'
  modalContent?: string; // markdown body for 'modal' / 'resource-modal'
  byline?: string;      // for resource-modal — e.g. "By Mel Storey"
};

export type Org = {
  slug: string;
  name: string;
  logoUrl?: string;     // local /public path or external URL
  shortDescription?: string;  // ~1-2 lines for cards mode
  body?: string;        // markdown — for the See More page on cards mode, or the table cell on table mode
  pathways: string[];   // for cross-pathway tagging
  links: OrgLink[];
  contact?: {
    email?: string;
    phone?: string;
    website?: string;
    applicationWindows?: string;  // free-text, e.g. "Jan/Jul"
  };
};

export type PathwaySection = {
  heading?: string;            // optional; some pages have no sub-section heading
  intro?: string;              // markdown intro above the org list
  displayMode: DisplayMode;
  orgs: Org[];                 // empty if displayMode is 'prose-only'
  showTestimonialsButton?: boolean;  // default true; some sub-sections suppress
  testimonialsScope?: string;  // e.g. "QLD Jurisdiction" — labels the Level-1 popup
};

export type Pathway = {
  slug: string;
  name: string;
  iconName?: string;           // lucide-react icon name
  status: 'published' | 'coming-soon';
  introAbove?: string;         // markdown — intro above the button row (CLCs use this)
  introBelow?: string;         // markdown — intro below the button row (Associateships use this)
  topLevelLinks?: OrgLink[];   // page-wide buttons (e.g. just `Testimonials` on Criminal Law)
  sections: PathwaySection[];
  bodyContent?: string;        // long-form MDX prose that sits below the org list (e.g. Associateships "What is an Associate?")
  relatedPathways?: string[];  // slugs for "See also" footer
};

// ============================================================================
// TESTIMONIALS
// ============================================================================

export type Testimonial = {
  slug: string;
  name: string;
  role: string;
  organisation: string;
  year?: string;
  pathways: string[];          // slugs — testimonials can be tagged to multiple pathways
  orgSlugs?: string[];         // sub-tagging — for CLC-specific testimonial groups (e.g. ["atsils"])
  body: string;                // markdown — the long-form testimonial text
};

// ============================================================================
// RESOURCES
// ============================================================================

export type ResourceLinkMeta = string; // "PDF, 127.8 KB", "Login required", etc.

export type ResourceLink = {
  label: string;
  href?: string;               // optional — pages may have label-only "URL pending" stubs
  description?: string;        // inline italic blurb, always visible
  expandable?: string;         // hidden by default, expands on click
  meta?: ResourceLinkMeta;
};

export type ResourceSection =
  | { type: 'links'; heading: string; subheading?: string; intro?: string; links: ResourceLink[] }
  | { type: 'prose'; heading: string; subheading?: string; body: string; links?: ResourceLink[]; variant?: 'default' | 'callout-tip' }
  | { type: 'contact'; heading: string; email?: string; phone?: string; hours?: string; address?: { label: string; mapHref?: string }; social?: { platform: string; handle: string; href: string }[] }
  | { type: 'comparison'; heading: string; intro?: string; columns: [{ label: string; items: string[] }, { label: string; items: string[] }] }
  | { type: 'template'; heading: string; intro?: string; subjectLine?: string; meta?: string; body: string; copyButton?: boolean };

export type ResourcePage = {
  slug: string;
  category: 'resources-and-guides' | 'networking-interviews-recruitment' | 'jatl-career-tips';
  title: string;
  status: 'published' | 'coming-soon' | 'partial';
  byJatl?: boolean;            // adds "From JATL" byline
  intro?: string;
  sections: ResourceSection[];
  buttons?: OrgLink[];         // for button-row resource pages (B1.3 External Resources)
  relatedResources?: string[]; // slugs
  relatedPathways?: string[];
};

// ============================================================================
// FOREWORDS
// ============================================================================

export type Foreword = {
  slug: string;
  name: string;
  role: string;
  body: string;                // markdown
};

// ============================================================================
// SITE GLOBALS
// ============================================================================

export type SiteConfig = {
  acknowledgementOfCountry: string;     // shown as first-visit popup
  welcomeIntro: string;                  // home/about
  legalDisclaimer: string;               // /disclaimer page
  sponsors: { name: string; logoUrl?: string; href?: string }[];
  socialLinks?: { platform: string; href: string }[];
};
```

---

## Part 5 — Content sources

The accompanying file **`CONTENT.md`** contains every verbatim text block from the brief, organised by destination. **Use it as the source of truth for prose**; do not paraphrase or rewrite.

### What's in CONTENT.md
- §A — All 13 published pathway pages (intros, sub-section content, popup bodies)
- §B — All 15 Resources sub-pages (intros, sections, link lists, templates)
- §C — Forewords (College of Law full body; placeholders for Tamika/Felix/Lubna/Leah)
- §D — Site-wide content (Acknowledgement of Country, welcome intro, full legal disclaimer)
- §E — Cross-pathway tag map (orgs and testimonials that span multiple pathways)
- §F — Open items / known gaps

### Testimonials JSON
**`content/testimonials.json` is supplied separately.** The schema for each entry matches the `Testimonial` type above. The user is responsible for providing this file before the build is "done"; if it's not present at build time, render testimonial cards with `{name, role, organisation}` only and a "Body coming soon" placeholder where the body would go. **Do not invent testimonial bodies.**

### CLCs without full content
The A1 brief identified ~15 Brisbane CLCs and 15 regional QLD CLCs. Some have full `See More` content captured (marked ✅ in the brief); others have only a logo + name. For the missing ones:
1. Render the org card with name only (no See More button) by default.
2. **Optionally**, attempt to fetch a short description from the org's official website and store it in `content/pathways/community-legal-centres/orgs/[slug].mdx`. If you do this, use a simple `fetch` script during dev — not at runtime. Cite the source URL in a code comment.
3. If neither is available, fall back to name-only.

### Logos
- For each org, attempt to find a usable logo by visiting the org's official site and looking for a `<link rel="icon">` or hero logo image.
- Save as `/public/logos/[org-slug].png` (or `.svg` if SVG is provided).
- If no logo is findable, render the org card with the org's name in a styled placeholder (use the JATL green tile pattern).
- **Never embed copyrighted logos as inline base64.** Always reference from `/public/logos/`.

### Missing URLs
A handful of pages have label-only "URL pending" link stubs (B2.5, B3.1). For these:
- Render the link label as plain text with a small "Coming soon" badge.
- Don't attempt to guess URLs.
- List them in `content/site.json` under a `pendingUrls` key for tracking.

---

## Part 6 — Page-by-page build instructions

### 6.1 Home (`/`)

**Sections (top to bottom):**
1. Hero panel (dark `--ink` background, full-width). H1: "JATL's Alt+Law Student Careers Guide". Subheading: "Empowering the next generation of legal professionals through education, opportunity, and community." Two CTA buttons: `Join JATL →` (external link to JATL membership), `Explore Career Pathways` (internal link to `/pathways`).
2. Welcome intro (white background, centred max-width prose). Use the verbatim text from §D of CONTENT.md.
3. Three feature cards: For Students 🎓 / Career Guidance 💼 / Community 🤝. Each card: icon + title + ~2-line description + small CTA link.
4. Sponsor strip (subtle): "Proudly supported by" → College of Law and QLS logos.

**On first visit only:** show the Acknowledgement of Country popup (modal, centred, with "Acknowledge & continue" button). Use `localStorage` is **not allowed** in this app per the design — use a cookie instead with a 1-year expiry. Key: `altlaw-aoc-acknowledged=1`.

### 6.2 About JATL (`/about`)

- Page H1 + intro paragraph (use welcome intro from §D).
- 4-card "Objectives" grid (placeholder content: Education, Advocacy, Community, Opportunity — replace with JATL's actual objectives if supplied; otherwise stub).
- Dual-panel section: left column = mission text (use §D welcome intro continuation); right column = Join JATL QR code placeholder + "Become a member" CTA.

### 6.3 Forewords (`/forewords`)

- Page H1: "Forewords"
- Stacked card list, one per foreword. Each card: small label ("Foreword"), name, role, body markdown.
- Order: Tamika (President) → Felix (VP Careers) → Lubna (Careers Officer) → Leah (Careers Officer) → College of Law.
- For the four JATL forewords with body pending, render the card with name + role + "Body coming soon" placeholder.
- College of Law foreword body is verbatim in §C.

### 6.4 Career Pathways index (`/pathways`)

- Page H1: "Career Pathways"
- Subtitle: short intro paragraph about the breadth of pathways.
- 3-column responsive grid (1 col mobile, 2 col tablet, 3 col desktop).
- Each tile: icon (lucide), pathway name, ~2-line description, hover state, link.
- `coming-soon` pathways: muted opacity (0.6), small "Coming Soon" badge, clicking goes to a stub page rather than disabled.

### 6.5 Pathway page (`/pathways/[slug]`)

This is the hardest page. Single dynamic route handles all 15 pathways via the `Pathway` type.

**Render order:**
1. Page header: pathway name as H1, optional `iconName` icon.
2. **If `topLevelLinks` exists**, render a top-level button row above the intro (Criminal Law uses this — its single Testimonials button is page-wide).
3. **If `introAbove` exists**, render markdown intro above the sections.
4. For each section in `pathway.sections`:
   a. Optional `heading` as H2.
   b. Optional `intro` markdown.
   c. Render the org list using the section's `displayMode`:
      - `cards` → `<OrgGrid>` — 3-col responsive grid of `<OrgCard>` components. Each card: logo (or styled placeholder), name, optional shortDescription, action buttons rendered from `org.links`.
      - `buttonRow` → `<OrgButtonRow>` — horizontal pill buttons; clicking opens the appropriate modal/page.
      - `table` → `<OrgTable>` — 2-col table: `<th>` org name, `<td>` rendered markdown of `org.body`.
      - `prose-only` → render nothing here; the body comes from `bodyContent`.
   d. Section-level Testimonials button (if `showTestimonialsButton`, default true). Opens a `<TestimonialsModal>` filtered to this section's scope.
5. **If `introBelow` exists**, render below the sections (Associateships uses this).
6. **If `bodyContent` exists**, render long-form MDX prose (Associateships, Academia, In-House, The Bar all have this).
7. **If `relatedPathways` exists**, render a "See also" footer with links to other pathway pages.

### 6.6 Per-CLC org page (`/pathways/community-legal-centres/[orgSlug]`)

Only Community Legal Centres uses this route. Renders an individual org's full content:
- Org name as H1
- Logo
- Body MDX (intro + For Students + How to Apply + Contact)
- Contact card (email, phone, website, application windows)
- Org-specific testimonials list
- Back link to `/pathways/community-legal-centres`

### 6.7 Resources index (`/resources`)

- Page H1: "Resources"
- Subtitle: "Access essential tools and guidance to advance your legal career and professional development."
- 3-column card grid (matches the screenshot the user provided):
  1. **Resources and Guides** (icon: file-text)
     - Job Search · Career Support · External Resources · Resumes · Cover Letters
  2. **Networking, Interviews and Job Recruitment Help** (icon: users)
     - Preparing for Applications · Job Interviews · Understand the Recruitment Process · Get Workplace Ready · Get Experience
  3. **JATL's Career Tips** (icon: message-circle)
     - Personal Branding and Networking Tips · Career Mentoring · LinkedIn · Information Interview Guide · JATL Recommends
- Each bulleted item is a link to its sub-page.

### 6.8 Resource sub-page (`/resources/[slug]`)

Generic renderer driven by the `ResourcePage` type. Render order:
1. Page H1: `title`. Below H1: small breadcrumb showing the parent category. If `byJatl`, add a "From JATL" tag.
2. **If `intro` exists**, render markdown intro.
3. **If `buttons` exists** (B1.3 External Resources), render a button row that opens resource modals.
4. For each section in `sections`, render based on `type`:
   - `links` → heading + optional subheading + intro + a `<ul>` of links with optional descriptions/expandables/meta badges.
   - `prose` → heading + subheading + markdown body + optional inline links. If `variant === 'callout-tip'`, render with accent-tinted background and "Tip" label.
   - `contact` → heading + structured contact card.
   - `comparison` → heading + 2-column comparison table (responsive: stacks on mobile).
   - `template` → heading + intro + subject-line label (if email) + monospace-styled code-block-like template body with copy-to-clipboard button. Italic `[placeholders]` should render visually distinct (lighter colour, italic).
5. **If `relatedResources` or `relatedPathways` exists**, render "See also" footer.

### 6.9 Contact (`/contact`)

Simple page. Email JATL, social links, optional contact form (form is optional — if you build it, hook it to a serverless function). Don't build the form unless time permits.

### 6.10 Disclaimer (`/disclaimer`)

Plain prose page rendering the full legal disclaimer from §D.

---

## Part 7 — Modal components

Three modal types to build, all sharing a base `<Modal>` primitive:

### `<Modal>` (primitive)
- Accessible (focus trap, ESC to close, aria-modal, return focus on close)
- Backdrop with click-to-close
- Mobile: bottom sheet style (slides up from bottom)
- Desktop: centred dialog
- Sizes: `sm | md | lg | xl` (controls max-width)

### `<TestimonialsModal>`
**Two-level popup:**
- **Level 1:** Title "Testimonials – [scope]". Vertical list of testimonial cards. Each card: name (bold), organisation, year, role. Click to open level 2.
- **Level 2:** Same modal frame but content swaps to: name + role + organisation header, then full body markdown.
- Back button on Level 2 returns to Level 1.

### `<ResourceModal>`
For org-info popups (`type: 'modal'`) and resource modals (`type: 'resource-modal'`).
- Renders markdown body inside modal.
- For `resource-modal`, slightly wider (size `lg`) and includes a byline if supplied (Mel Storey essay uses this).
- All popup content is plain markdown — no special components needed inside.

---

## Part 8 — Content authoring workflow

For each pathway and resource page, create two files:
- `content/pathways/[slug].json` — the structured `Pathway` data
- `content/pathways/[slug].mdx` — the long-form `bodyContent` and any `introAbove`/`introBelow` if too long for inline JSON

Same pattern for resources:
- `content/resources/[slug].json` — `ResourcePage` data
- `content/resources/[slug].mdx` — long-form prose

The JSON references the MDX via a string token like `__mdx:bodyContent__` which the loader (`src/lib/content.ts`) resolves at build time. This keeps the JSON readable while letting prose live in MDX.

**Loaders:**
- `getPathway(slug)` → `Pathway`
- `getAllPathways()` → `Pathway[]`
- `getOrg(pathwaySlug, orgSlug)` → `Org` (only used for CLCs)
- `getResource(slug)` → `ResourcePage`
- `getAllResources()` → `ResourcePage[]`
- `getTestimonials({ pathwaySlug?, orgSlug? })` → `Testimonial[]` (filters by tags)
- `getForewords()` → `Foreword[]`
- `getSiteConfig()` → `SiteConfig`

All loaders are server-only and synchronous (read JSON/MDX from disk at build time). No client-side fetching of content.

---

## Part 9 — Accessibility & SEO

### Accessibility (non-negotiable)
- WCAG 2.2 AA target.
- Semantic HTML — use `<main>`, `<nav>`, `<article>`, `<section>` correctly.
- All interactive elements keyboard-reachable. Visible focus rings (Tailwind `focus-visible:` utilities, never `outline: none` without a replacement).
- Modals: focus trap, ESC closes, return focus to opener, `aria-modal="true"`, `aria-labelledby` pointing to the title.
- Skip-to-content link at the top of the layout.
- Colour contrast: body text ≥ 4.5:1, large text ≥ 3:1. Test the green `--accent` against white — if it fails on small text, only use it on large headings/buttons.
- All images have alt text. Decorative images use `alt=""`.
- No reliance on hover-only interactions — everything must work with keyboard and touch.
- Reduced motion: respect `prefers-reduced-motion`.

### SEO
- Per-page `<title>` and `<meta name="description">` via Next.js metadata API.
- OpenGraph tags on every page (use `og.ts` helper).
- `sitemap.xml` and `robots.txt` generated at build time using Next.js conventions.
- Structured data (JSON-LD) on pathway pages: `Article` or `WebPage` schema.

---

## Part 10 — Build, deploy, polish

### Local development
```bash
pnpm dev          # http://localhost:3000
pnpm build        # production build
pnpm start        # serve production build locally
```

### Pre-deploy checks
1. `pnpm build` succeeds with no warnings.
2. Run `pnpm next lint` (add eslint manually if not installed) — fix all errors.
3. Run a quick Lighthouse pass on /, /pathways, /pathways/community-legal-centres, /resources, /resources/information-interview-guide. Target: Performance ≥ 90, Accessibility ≥ 95, SEO ≥ 95, Best Practices ≥ 95.
4. Manual keyboard-only test: tab through home → pathway → modal → close modal → back to nav.
5. Test on mobile viewport (375px).

### Deploy to Vercel
```bash
pnpm dlx vercel --prod
```
Or connect the GitHub repo via the Vercel dashboard for auto-deploy on push.

### Domain
Default Vercel subdomain is fine for first deploy. If a custom domain is supplied later, configure in Vercel dashboard.

---

## Part 11 — Things you should NOT do

- **Don't paraphrase or rewrite the verbatim content** in CONTENT.md. The legal disclaimer, Acknowledgement of Country, and welcome text must appear exactly as supplied.
- **Don't invent testimonial bodies.** If `testimonials.json` doesn't have a body for a given testimonial, render a placeholder.
- **Don't fabricate URLs.** If a URL is missing, render the link label only.
- **Don't use third-party UI kits** (no shadcn/ui setup here unless you want to — Tailwind primitives + lucide-react are sufficient and keep the bundle small). If you do bring in shadcn, only pull what you need.
- **Don't add localStorage or sessionStorage** for the AoC popup — use cookies (Anthropic artifact rules don't apply here since this is Next.js, but the user prefers cookies for first-visit tracking).
- **Don't add analytics** without checking with the user first.
- **Don't add a CMS** (Sanity, Contentful, etc.). Content lives in MDX/JSON in the repo.
- **Don't deploy until** the user reviews a local preview and approves.

---

## Part 12 — Definition of done

The build is complete when:
1. All 13 published pathway pages render correctly with their captured content.
2. The 2 coming-soon pathway pages render their stub.
3. All 15 Resource sub-pages render correctly. Pages with full content show full content; `coming-soon` resource pages (the other 5 of B3 from the original screenshot, if any remain) show stubs.
4. Modals (Testimonials, ResourceModal, AoC) work with keyboard and touch.
5. Cross-pathway "See also" links work both directions.
6. Lighthouse scores meet the targets in §10.
7. The site builds and deploys to Vercel successfully.
8. A `README.md` at the repo root explains: how to run locally, where to add content, how to update testimonials.json, how to deploy.
9. A `CONTENT-AUDIT.md` at the repo root lists every known gap (missing URLs, missing testimonial bodies, missing forewords, CLCs without See More content) so the user can fill them in over time.

Good luck. Build with care — this site will be used by real students making real career decisions.
