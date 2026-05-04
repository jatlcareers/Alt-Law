import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { OrgGrid } from "./OrgGrid";
import { OrgButtonRow } from "./OrgButtonRow";
import { OrgTable } from "./OrgTable";
import { Markdown } from "@/components/ui/Markdown";
import type { Pathway, Testimonial } from "@/lib/types";

type Props = {
  pathway: Pathway;
  testimonials: Testimonial[];
  allPathwayLookup?: Record<string, { name: string; slug: string }>;
};

export function PathwayRenderer({
  pathway,
  testimonials,
  allPathwayLookup = {},
}: Props) {
  const hasOrgPages = pathway.slug === "community-legal-centres";

  return (
    <article className="mx-auto max-w-[1280px] px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header className="mb-10">
        <Link
          href="/pathways/"
          className="mb-4 inline-flex items-center gap-1 text-sm font-medium text-text-muted hover:text-accent"
        >
          <ArrowRight size={14} className="rotate-180" /> All pathways
        </Link>
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          {pathway.name}
        </h1>
        {pathway.status === "coming-soon" && (
          <span className="mt-3 inline-block rounded-full bg-bg-muted px-3 py-1 text-xs font-medium text-text-muted">
            Coming soon
          </span>
        )}
      </header>

      {pathway.topLevelLinks && pathway.topLevelLinks.length > 0 && (
        <div className="mb-8">
          <OrgButtonRow
            pathwaySlug={pathway.slug}
            links={pathway.topLevelLinks}
            testimonials={testimonials}
          />
        </div>
      )}

      {pathway.introAbove && (
        <div className="prose-body mb-10 max-w-3xl text-text">
          <Markdown>{pathway.introAbove}</Markdown>
        </div>
      )}

      {pathway.sections.map((section, i) => {
        const scopedTestimonials = section.testimonialsScope
          ? testimonials
          : testimonials;
        return (
          <section key={i} className={i > 0 ? "mt-12" : ""}>
            {section.heading && (
              <h2 className="mb-3 text-xl font-semibold tracking-tight text-text sm:text-2xl">
                {section.heading}
              </h2>
            )}
            {section.intro && (
              <div className="prose-body mb-6 max-w-3xl text-text">
                <Markdown>{section.intro}</Markdown>
              </div>
            )}

            {section.displayMode === "cards" && section.orgs.length > 0 && (
              <OrgGrid
                pathwaySlug={pathway.slug}
                orgs={section.orgs}
                testimonials={scopedTestimonials}
                hasOrgPages={hasOrgPages}
              />
            )}

            {section.displayMode === "buttonRow" && (
              <OrgButtonRow
                pathwaySlug={pathway.slug}
                links={section.orgs.flatMap((o) => o.links)}
                testimonials={scopedTestimonials}
                showTestimonialsButton={section.showTestimonialsButton ?? true}
                testimonialsScope={section.testimonialsScope ?? section.heading}
              />
            )}

            {section.displayMode === "table" && section.orgs.length > 0 && (
              <OrgTable orgs={section.orgs} />
            )}
          </section>
        );
      })}

      {pathway.introBelow && (
        <div className="prose-body mt-10 max-w-3xl text-text">
          <Markdown>{pathway.introBelow}</Markdown>
        </div>
      )}

      {pathway.bodyContent && (
        <div className="prose-body mt-10 max-w-3xl text-text">
          <Markdown>{pathway.bodyContent}</Markdown>
        </div>
      )}

      {pathway.relatedPathways && pathway.relatedPathways.length > 0 && (
        <footer className="mt-16 border-t border-border pt-8">
          <h2 className="text-sm font-semibold uppercase tracking-[0.12em] text-text-subtle">
            See also
          </h2>
          <ul className="mt-3 flex flex-wrap gap-3">
            {pathway.relatedPathways.map((slug) => {
              const p = allPathwayLookup[slug];
              if (!p) return null;
              return (
                <li key={slug}>
                  <Link
                    href={`/pathways/${slug}/`}
                    className="inline-flex items-center gap-1 rounded-md border border-border bg-surface px-3 py-1.5 text-sm font-medium text-text transition-colors hover:bg-bg-muted"
                  >
                    {p.name} <ArrowRight size={14} />
                  </Link>
                </li>
              );
            })}
          </ul>
        </footer>
      )}
    </article>
  );
}
