# Alt+Law — Build Handoff Bundle

This bundle contains everything Claude Code needs to build the Alt+Law website.

## Files in this bundle

| File | Purpose |
|---|---|
| `CLAUDE_CODE_PROMPT.md` | The build prompt. Paste this into Claude Code as the primary instruction. |
| `CONTENT.md` | Verbatim content for every page — pathways, resources, forewords, site-wide text. |
| `content/pathways/family-law.json` | Worked example of a pathway JSON file (button-row mode, single-popup). |
| `content/resources/information-interview-guide.json` | Worked example of a resource page JSON (uses every section type — comparison, template, prose, callout). |
| `content/testimonials.json` | Skeleton of the testimonials data file with the multi-pathway entries pre-tagged. |
| `README.md` | This file. |

## How to use

### Option A — single-shot
1. Open Claude Code in the directory where you want the site built.
2. Drop all the files in this bundle into a folder (e.g. `_handoff/`) at the repo root.
3. Tell Claude Code: *"Read `_handoff/CLAUDE_CODE_PROMPT.md` and follow it end-to-end. Use `_handoff/CONTENT.md` for verbatim content and `_handoff/content/` for example schema patterns. Build the site according to the prompt."*
4. Claude Code will scaffold the Next.js app, set up the content model, and build pages page-by-page.

### Option B — section by section
1. Same setup, but instead of asking for the whole build at once, work through it in phases:
   - Phase 1: project setup, design tokens, layout, nav, footer, AoC popup
   - Phase 2: content model + loaders + types
   - Phase 3: pathway index + 3 sample pathway pages (CLC + Associateships + Family Law) — one per display mode
   - Phase 4: remaining pathway pages
   - Phase 5: resources index + sample resource pages (one per section type)
   - Phase 6: remaining resource pages
   - Phase 7: forewords, contact, disclaimer, polish, deploy
2. Review each phase before moving on.

### Option B is recommended
The site has a lot of moving parts. Reviewing in phases catches design issues early and keeps the diff manageable.

## Things you'll still need to do

After the initial build:

1. **Fill in `content/testimonials.json`.** ~85 testimonial bodies need to be supplied. The file is the only place the build can't infer content from this bundle. Without it, testimonial cards will render with header info only. Format: see the schema and skeleton entries.
2. **Supply the four JATL forewords** (Tamika, Felix, Lubna, Leah). Replace the "Coming soon" placeholders in the forewords data file.
3. **Resolve URLs marked "URL pending"** — listed in `CONTENT-AUDIT.md` after the build (the prompt instructs Claude Code to generate this file).
4. **Provide org logos** to `/public/logos/[org-slug].png`. The build attempts to fetch these where possible but you'll likely need to source some manually from the JATL Canva or org websites.
5. **Fill in B3.5 JATL Recommends** — the page is currently a skeleton.
6. **Review and confirm** the EMPLOY101x voucher code is safe to publish before launch.
7. **Confirm** "Future Leaders" vs "Policy Futures" Graduate Program naming with the source.
8. **Connect a custom domain** in Vercel after first deploy (optional).

## Design references

- Existing Figma Make draft (locked behind auth — export needed before pixel-fidelity is possible)
- JATL Canva (locked behind auth — for brand assets)
- Mermaid sitemap (locked behind auth — for IA confirmation)
- Resources page screenshot (in original conversation — describes the 3-card layout)

The build prompt describes the design direction in enough detail that Claude Code can build directionally without these. Refining to match Figma exactly is a follow-up task once exports are available.

## What's NOT in this bundle

- Testimonial bodies (you'll supply)
- Org logos (build will try to fetch; some manual)
- Foreword bodies for the 4 JATL forewords (placeholders only)
- The Mel Storey essay full body — but it's verbatim in CONTENT.md §A12
- Anything from the OneNote source (already extracted into CONTENT.md)

## Questions during the build

If Claude Code hits an ambiguity not covered by the prompt, default behaviour:
- **Missing content** → render a placeholder, log to `CONTENT-AUDIT.md`
- **Missing URL** → render label-only with "Coming soon" badge
- **Missing logo** → render styled name placeholder using JATL green tile pattern
- **Cross-pathway ambiguity** → consult §E of CONTENT.md
- **Layout edge case not in §3 of the prompt** → fall back to the closest existing pattern, log a note in code comments

Good luck with the build.
