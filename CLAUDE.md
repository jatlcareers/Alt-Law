@AGENTS.md

# Alt+Law project notes

- Stack: Next.js 16 App Router, React 19, Tailwind v4, TypeScript, static export.
- All content lives in `content/*.json`; loaders are server-only sync (`src/lib/content.ts`).
- Body prose is rendered via `react-markdown` (see `src/components/ui/Markdown.tsx`).
- Tailwind v4 utility classes will be silently overridden by unlayered CSS — always wrap custom rules in `@layer base { ... }` or `@layer components { ... }` in `globals.css`.
- `pnpm` on the original author's machine needs `COREPACK_INTEGRITY_KEYS=0` prefix; CI does not.
- Never add em dashes to content or copy. House style is hyphens (`-`).
- Build uses `NEXT_PUBLIC_SITE_URL=https://altlawuqjatl.com` for GitHub Pages deploy. The site lives at the apex of `altlawuqjatl.com` with no basePath; `public/CNAME` carries the domain into the deploy artifact.
- All internal `<Link>` hrefs include trailing slashes to satisfy `trailingSlash: true` in `next.config.ts`.
