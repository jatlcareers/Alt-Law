import Link from "next/link";
import { ArrowRight, GraduationCap, Briefcase, HeartHandshake } from "lucide-react";
import { getSiteConfig } from "@/lib/content";
import { buildMetadata } from "@/lib/og";

export const metadata = buildMetadata({
  title: "JATL's Alt+Law Student Careers Guide",
  description:
    "Empowering the next generation of legal professionals through education, opportunity, and community. A counter-guide to commercial-clerkship-focused careers guides.",
  path: "/",
});

const FEATURES = [
  {
    title: "For Students",
    icon: GraduationCap,
    body: "Explore the breadth of legal practice - from community legal centres and family law to associateships and the bar.",
    cta: { label: "Browse pathways", href: "/pathways" },
  },
  {
    title: "Career Guidance",
    icon: Briefcase,
    body: "Curated resources covering job search, interviews, networking, applications, and JATL's own career tips.",
    cta: { label: "View resources", href: "/resources" },
  },
  {
    title: "Community",
    icon: HeartHandshake,
    body: "JATL connects students with practitioners, mentors, and peers grounded in social justice.",
    cta: { label: "About JATL", href: "/about" },
  },
] as const;

export default function HomePage() {
  const site = getSiteConfig();

  return (
    <>
      <section className="bg-ink text-ink-fg">
        <div className="mx-auto max-w-[1280px] px-4 py-20 sm:px-6 sm:py-24 lg:px-8 lg:py-28">
          <p className="text-sm font-medium uppercase tracking-[0.18em] text-ink-fg/60">
            Justice and the Law Society · UQ
          </p>
          <h1 className="mt-4 max-w-3xl text-balance text-4xl font-semibold leading-[1.05] tracking-tight sm:text-5xl lg:text-6xl">
            JATL&apos;s Alt+Law Student Careers Guide
          </h1>
          <p className="mt-6 max-w-2xl text-pretty text-lg text-ink-fg/85 sm:text-xl">
            Empowering the next generation of legal professionals through
            education, opportunity, and community.
          </p>
          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <Link
              href="/about"
              className="inline-flex items-center justify-center gap-2 rounded-md bg-accent px-5 py-3 text-sm font-medium text-accent-fg transition-colors hover:bg-accent-hover"
            >
              Join JATL <ArrowRight size={16} />
            </Link>
            <Link
              href="/pathways"
              className="inline-flex items-center justify-center gap-2 rounded-md border border-ink-fg/25 bg-transparent px-5 py-3 text-sm font-medium text-ink-fg transition-colors hover:bg-ink-fg/10"
            >
              Explore Career Pathways
            </Link>
          </div>
        </div>
      </section>

      <section className="bg-bg">
        <div className="mx-auto max-w-3xl px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="prose-body text-text">
            {site.welcomeIntro.split("\n\n").map((para, i) => (
              <p key={i}>{para}</p>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-bg-muted">
        <div className="mx-auto max-w-[1280px] px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {FEATURES.map(({ title, icon: Icon, body, cta }) => (
              <article
                key={title}
                className="group flex flex-col rounded-2xl border border-border bg-surface p-6 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md"
              >
                <div className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-accent/10 text-accent">
                  <Icon size={20} />
                </div>
                <h2 className="mt-4 text-lg font-semibold tracking-tight text-text">
                  {title}
                </h2>
                <p className="mt-2 text-sm leading-6 text-text-muted">{body}</p>
                <Link
                  href={cta.href}
                  className="mt-4 inline-flex items-center gap-1.5 text-sm font-medium text-accent transition-colors hover:text-accent-hover"
                >
                  {cta.label}
                  <ArrowRight size={14} className="transition-transform group-hover:translate-x-0.5" />
                </Link>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-bg border-t border-border">
        <div className="mx-auto max-w-[1280px] px-4 py-10 sm:px-6 lg:px-8">
          <p className="text-center text-xs font-semibold uppercase tracking-[0.18em] text-text-subtle">
            Proudly supported by
          </p>
          <ul className="mt-4 flex flex-wrap items-center justify-center gap-x-8 gap-y-3">
            {site.sponsors.map((sponsor) => (
              <li
                key={sponsor.name}
                className="text-sm font-medium text-text-muted"
              >
                {sponsor.href ? (
                  <a
                    href={sponsor.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-accent"
                  >
                    {sponsor.name}
                  </a>
                ) : (
                  sponsor.name
                )}
              </li>
            ))}
          </ul>
        </div>
      </section>
    </>
  );
}
