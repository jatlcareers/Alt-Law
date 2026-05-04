# Alt+Law

JATL's Alt+Law student careers guide - a public-facing counter-guide to commercial-clerkship-focused legal careers content. Published by the Justice and the Law Society at the University of Queensland.

Live: https://jatlcareers.github.io/Alt-Law/

## Tech

Next.js 16 (App Router) · React 19 · Tailwind v4 · TypeScript · static export to GitHub Pages.

## Local development

Requires Node 20+ and pnpm 10+.

```bash
pnpm install
pnpm dev      # http://localhost:3000
pnpm build    # static export to out/
```

If `pnpm` errors with `Cannot find matching keyid` on this machine, prefix commands with `COREPACK_INTEGRITY_KEYS=0`.

## Content

All page content lives in `content/`:

- `content/site.json` - site-wide text (Acknowledgement of Country, welcome intro, full disclaimer, sponsors)
- `content/forewords.json` - foreword bodies (College of Law verbatim; JATL placeholders pending bodies)
- `content/testimonials.json` - testimonial entries; bodies are supplied externally
- `content/pathways/*.json` - one file per career pathway
- `content/resources/*.json` - one file per resource sub-page

To add a new pathway or resource page, create a new JSON file matching the existing schema (see `src/lib/types.ts`). The route handlers automatically pick it up via `generateStaticParams`.

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the static export and publishes to GitHub Pages.

The build uses two env vars:

- `NEXT_PUBLIC_BASE_PATH=/Alt-Law` - required because the site is hosted under the `/Alt-Law/` subpath of `jatlcareers.github.io`.
- `NEXT_PUBLIC_SITE_URL=https://jatlcareers.github.io/Alt-Law` - used for canonical URLs, OpenGraph, sitemap, and robots.

## What's still pending

- Foreword bodies for Tamika, Felix, Lubna, Leah
- Testimonial bodies (most entries are header-only placeholders)
- Org logos for community legal centres and others (currently rendered as initial-tile placeholders)
- A handful of "URL pending" stubs (tracked in `content/site.json` `pendingUrls`)
- B3.5 JATL Recommends page - skeleton only

See `_handoff/` for the original build brief and content sources.
