import Link from "next/link";
import * as Icons from "lucide-react";
import { ArrowRight } from "lucide-react";
import { getAllResources } from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { RESOURCE_CATEGORY_ORDER } from "@/lib/pathway-order";

export const metadata = buildMetadata({
  title: "Resources",
  description:
    "Access essential tools and guidance to advance your legal career and professional development. Curated by JATL.",
  path: "/resources/",
});

function getIcon(name: string) {
  const candidate = (Icons as Record<string, unknown>)[name];
  return (typeof candidate === "function" ? candidate : Icons.FileText) as typeof Icons.FileText;
}

export default function ResourcesIndexPage() {
  const all = getAllResources();
  const map = new Map(all.map((r) => [r.slug, r]));

  return (
    <div className="mx-auto max-w-[1280px] px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header className="mb-10 max-w-3xl">
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          Resources
        </h1>
        <p className="mt-3 text-lg text-text-muted">
          Access essential tools and guidance to advance your legal career and
          professional development.
        </p>
      </header>

      <div className="grid gap-6 lg:grid-cols-3">
        {RESOURCE_CATEGORY_ORDER.map((cat) => {
          const Icon = getIcon(cat.iconName);
          return (
            <section
              key={cat.slug}
              className="rounded-2xl border border-border bg-surface p-6 shadow-sm"
            >
              <div className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-accent/10 text-accent">
                <Icon size={20} />
              </div>
              <h2 className="mt-4 text-lg font-semibold tracking-tight text-text">
                {cat.label}
              </h2>
              <ul className="mt-4 space-y-2">
                {cat.resources.map((slug) => {
                  const r = map.get(slug);
                  if (!r) return null;
                  return (
                    <li key={slug}>
                      <Link
                        href={`/resources/${slug}/`}
                        className="group inline-flex items-center gap-1.5 text-sm font-medium text-text transition-colors hover:text-accent"
                      >
                        {r.title}
                        {(r.status === "coming-soon" || r.status === "partial") && (
                          <span className="rounded-full bg-bg-muted px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wider text-text-muted">
                            {r.status === "coming-soon" ? "Soon" : "WIP"}
                          </span>
                        )}
                        <ArrowRight
                          size={12}
                          className="opacity-0 transition-all group-hover:translate-x-0.5 group-hover:opacity-100"
                        />
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </section>
          );
        })}
      </div>
    </div>
  );
}
