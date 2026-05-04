@AGENTS.md

# Alt+Law project notes

- Stack: Next.js 16 App Router, React 19, Tailwind v4, TypeScript, static export.
- All content lives in `content/*.json`; loaders are server-only sync (`src/lib/content.ts`).
- Body prose is rendered via `react-markdown` (see `src/components/ui/Markdown.tsx`).
- Tailwind v4 utility classes will be silently overridden by unlayered CSS — always wrap custom rules in `@layer base { ... }` or `@layer components { ... }` in `globals.css`.
- `pnpm` on the original author's machine needs `COREPACK_INTEGRITY_KEYS=0` prefix; CI does not.
- Never add em dashes to content or copy. House style is hyphens (`-`).
- Build uses `NEXT_PUBLIC_BASE_PATH=/Alt-Law` and `NEXT_PUBLIC_SITE_URL=https://jatlcareers.github.io/Alt-Law` for GitHub Pages deploy. Local dev uses no basePath.
- All internal `<Link>` hrefs include trailing slashes to satisfy `trailingSlash: true` in `next.config.ts`.
