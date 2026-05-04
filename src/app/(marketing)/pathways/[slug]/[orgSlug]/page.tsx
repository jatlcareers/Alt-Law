import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowRight, Mail, Phone, Globe, Calendar } from "lucide-react";
import {
  getAllPathways,
  getOrg,
  getPathway,
  getTestimonials,
} from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { Markdown } from "@/components/ui/Markdown";
import { OrgTilePlaceholder } from "@/components/pathway/OrgGrid";

type Params = { slug: string; orgSlug: string };

export function generateStaticParams() {
  const out: Params[] = [];
  for (const p of getAllPathways()) {
    if (p.slug !== "community-legal-centres") continue;
    for (const section of p.sections) {
      for (const org of section.orgs) {
        if (org.body || org.shortDescription) {
          out.push({ slug: p.slug, orgSlug: org.slug });
        }
      }
    }
  }
  return out;
}

export async function generateMetadata({ params }: { params: Promise<Params> }) {
  const { slug, orgSlug } = await params;
  const org = getOrg(slug, orgSlug);
  if (!org) return {};
  return buildMetadata({
    title: org.name,
    description:
      org.shortDescription ??
      org.body?.slice(0, 160) ??
      `${org.name} - profile in the JATL Alt+Law community legal centres pathway.`,
    path: `/pathways/${slug}/${orgSlug}/`,
  });
}

export default async function OrgPage({ params }: { params: Promise<Params> }) {
  const { slug, orgSlug } = await params;
  const org = getOrg(slug, orgSlug);
  const pathway = getPathway(slug);
  if (!org || !pathway) notFound();

  const testimonials = getTestimonials({ pathwaySlug: slug, orgSlug });

  return (
    <article className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <Link
        href={`/pathways/${slug}/`}
        className="mb-4 inline-flex items-center gap-1 text-sm font-medium text-text-muted hover:text-accent"
      >
        <ArrowRight size={14} className="rotate-180" /> Back to {pathway.name}
      </Link>
      <header className="mb-8 flex items-start gap-4">
        <OrgTilePlaceholder name={org.name} />
        <div>
          <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
            {org.name}
          </h1>
          {org.shortDescription && (
            <p className="mt-2 text-base text-text-muted">
              {org.shortDescription}
            </p>
          )}
        </div>
      </header>

      {org.body && (
        <div className="prose-body text-text">
          <Markdown>{org.body}</Markdown>
        </div>
      )}

      {org.contact && (
        <section className="mt-10 rounded-2xl border border-border bg-bg-muted p-5 sm:p-6">
          <h2 className="text-base font-semibold tracking-tight text-text">
            Contact
          </h2>
          <ul className="mt-3 space-y-2 text-sm text-text">
            {org.contact.email && (
              <li className="flex items-center gap-2">
                <Mail size={16} className="text-text-muted" />
                <a
                  href={`mailto:${org.contact.email}`}
                  className="text-accent hover:text-accent-hover"
                >
                  {org.contact.email}
                </a>
              </li>
            )}
            {org.contact.phone && (
              <li className="flex items-center gap-2">
                <Phone size={16} className="text-text-muted" />
                <a
                  href={`tel:${org.contact.phone.replace(/\s/g, "")}`}
                  className="text-accent hover:text-accent-hover"
                >
                  {org.contact.phone}
                </a>
              </li>
            )}
            {org.contact.website && (
              <li className="flex items-center gap-2">
                <Globe size={16} className="text-text-muted" />
                <a
                  href={org.contact.website}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-accent hover:text-accent-hover"
                >
                  {org.contact.website}
                </a>
              </li>
            )}
            {org.contact.applicationWindows && (
              <li className="flex items-center gap-2">
                <Calendar size={16} className="text-text-muted" />
                <span>{org.contact.applicationWindows}</span>
              </li>
            )}
          </ul>
        </section>
      )}

      {testimonials.length > 0 && (
        <section className="mt-10">
          <h2 className="text-base font-semibold tracking-tight text-text">
            Testimonials
          </h2>
          <ul className="mt-3 space-y-3">
            {testimonials.map((t) => (
              <li
                key={t.slug}
                className="rounded-2xl border border-border bg-surface p-4 shadow-sm"
              >
                <p className="font-medium text-text">{t.name}</p>
                <p className="text-sm text-text-muted">
                  {[t.role, t.organisation, t.year].filter(Boolean).join(" - ")}
                </p>
                {t.body ? (
                  <div className="mt-2 text-sm text-text">
                    <Markdown>{t.body}</Markdown>
                  </div>
                ) : (
                  <p className="mt-2 text-sm italic text-text-subtle">
                    Body coming soon.
                  </p>
                )}
              </li>
            ))}
          </ul>
        </section>
      )}
    </article>
  );
}
