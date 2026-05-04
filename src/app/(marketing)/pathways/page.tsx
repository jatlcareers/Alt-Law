import Link from "next/link";
import * as Icons from "lucide-react";
import { ArrowRight } from "lucide-react";
import { getAllPathways } from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { PATHWAY_ORDER } from "@/lib/pathway-order";
import { cn } from "@/lib/cn";

export const metadata = buildMetadata({
  title: "Career Pathways",
  description:
    "Explore the breadth of legal practice - from community legal centres and family law to associateships and the bar. Curated by JATL law students.",
  path: "/pathways/",
});

function getIcon(name?: string) {
  if (!name) return Icons.Compass;
  const camel =
    name
      .split("-")
      .map((p) => p.charAt(0).toUpperCase() + p.slice(1))
      .join("") as keyof typeof Icons;
  const candidate = (Icons as Record<string, unknown>)[camel];
  return (typeof candidate === "function" ? candidate : Icons.Compass) as typeof Icons.Compass;
}

export default function PathwaysIndexPage() {
  const all = getAllPathways();
  const ordered = PATHWAY_ORDER.map((slug) => all.find((p) => p.slug === slug)).filter(
    (p): p is NonNullable<typeof p> => !!p,
  );
  const extras = all.filter((p) => !PATHWAY_ORDER.includes(p.slug));
  const list = [...ordered, ...extras];

  return (
    <div className="mx-auto max-w-[1280px] px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header className="mb-10 max-w-3xl">
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          Career Pathways
        </h1>
        <p className="mt-3 text-lg text-text-muted">
          Each pathway opens a different door in the legal profession. Browse the
          breadth of practice areas, organisations, and graduate routes captured
          here.
        </p>
      </header>

      <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {list.map((p) => {
          const Icon = getIcon(p.iconName);
          const isComingSoon = p.status === "coming-soon";
          return (
            <li key={p.slug}>
              <Link
                href={`/pathways/${p.slug}/`}
                className={cn(
                  "group flex h-full flex-col rounded-2xl border border-border bg-surface p-6 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md",
                  isComingSoon && "opacity-60",
                )}
              >
                <div className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-accent/10 text-accent">
                  <Icon size={20} />
                </div>
                <div className="mt-4 flex items-start gap-2">
                  <h2 className="text-lg font-semibold tracking-tight text-text">
                    {p.name}
                  </h2>
                  {isComingSoon && (
                    <span className="rounded-full bg-bg-muted px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-text-muted">
                      Soon
                    </span>
                  )}
                </div>
                {p.introAbove && (
                  <p className="mt-2 line-clamp-3 text-sm leading-6 text-text-muted">
                    {p.introAbove.replace(/[#*_>`]/g, "").split("\n")[0]}
                  </p>
                )}
                {!p.introAbove && p.introBelow && (
                  <p className="mt-2 line-clamp-3 text-sm leading-6 text-text-muted">
                    {p.introBelow.replace(/[#*_>`]/g, "").split("\n")[0]}
                  </p>
                )}
                <span className="mt-4 inline-flex items-center gap-1 text-sm font-medium text-accent">
                  Explore <ArrowRight size={14} className="transition-transform group-hover:translate-x-0.5" />
                </span>
              </Link>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
