"use client";

import { useState } from "react";
import Link from "next/link";
import {
  ArrowRight,
  Mail,
  Phone,
  Clock,
  MapPin,
  Copy,
  Check,
  ExternalLink,
} from "lucide-react";
import { Markdown } from "@/components/ui/Markdown";
import { ResourceModal } from "@/components/popup/ResourceModal";
import { cn } from "@/lib/cn";
import { RESOURCE_CATEGORY_ORDER } from "@/lib/pathway-order";
import type { OrgLink, ResourcePage, ResourceLink } from "@/lib/types";

type Props = {
  resource: ResourcePage;
  related: { resources: { name: string; slug: string }[]; pathways: { name: string; slug: string }[] };
};

export function ResourcePageRenderer({ resource, related }: Props) {
  const [modal, setModal] = useState<
    { title: string; body: string; byline?: string } | null
  >(null);

  const category = RESOURCE_CATEGORY_ORDER.find((c) => c.slug === resource.category);

  return (
    <article className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <Link
        href="/resources/"
        className="mb-3 inline-flex items-center gap-1 text-xs font-medium uppercase tracking-[0.12em] text-text-subtle hover:text-accent"
      >
        <ArrowRight size={12} className="rotate-180" />
        {category?.label ?? "Resources"}
      </Link>
      <header className="mb-8">
        <div className="flex flex-wrap items-center gap-3">
          <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
            {resource.title}
          </h1>
          {resource.byJatl && (
            <span className="rounded-full border border-accent/40 bg-accent/10 px-2.5 py-1 text-xs font-medium text-accent">
              From JATL
            </span>
          )}
          {resource.status === "coming-soon" && (
            <span className="rounded-full bg-bg-muted px-2.5 py-1 text-xs font-medium text-text-muted">
              Coming soon
            </span>
          )}
          {resource.status === "partial" && (
            <span className="rounded-full bg-bg-muted px-2.5 py-1 text-xs font-medium text-text-muted">
              In progress
            </span>
          )}
        </div>
        {resource.intro && (
          <div className="prose-body mt-4 text-text">
            <Markdown>{resource.intro}</Markdown>
          </div>
        )}
      </header>

      {resource.buttons && resource.buttons.length > 0 && (
        <div className="mb-10 flex flex-wrap gap-2">
          {resource.buttons.map((btn, i) => (
            <ResourceButton
              key={i}
              btn={btn}
              onModal={(s) => setModal(s)}
            />
          ))}
        </div>
      )}

      <div className="space-y-12">
        {resource.sections.map((section, i) => (
          <SectionBlock key={i} section={section} />
        ))}
      </div>

      {(related.resources.length > 0 || related.pathways.length > 0) && (
        <footer className="mt-16 border-t border-border pt-8">
          <h2 className="text-sm font-semibold uppercase tracking-[0.12em] text-text-subtle">
            See also
          </h2>
          <ul className="mt-3 flex flex-wrap gap-3">
            {related.resources.map((r) => (
              <li key={`r-${r.slug}`}>
                <Link
                  href={`/resources/${r.slug}/`}
                  className="inline-flex items-center gap-1 rounded-md border border-border bg-surface px-3 py-1.5 text-sm font-medium text-text transition-colors hover:bg-bg-muted"
                >
                  {r.name} <ArrowRight size={14} />
                </Link>
              </li>
            ))}
            {related.pathways.map((p) => (
              <li key={`p-${p.slug}`}>
                <Link
                  href={`/pathways/${p.slug}/`}
                  className="inline-flex items-center gap-1 rounded-md border border-border bg-surface px-3 py-1.5 text-sm font-medium text-text transition-colors hover:bg-bg-muted"
                >
                  {p.name} <ArrowRight size={14} />
                </Link>
              </li>
            ))}
          </ul>
        </footer>
      )}

      {modal && (
        <ResourceModal
          open={true}
          onClose={() => setModal(null)}
          title={modal.title}
          body={modal.body}
          byline={modal.byline}
          size="xl"
        />
      )}
    </article>
  );
}

function ResourceButton({
  btn,
  onModal,
}: {
  btn: OrgLink;
  onModal: (s: { title: string; body: string; byline?: string }) => void;
}) {
  const cls =
    "inline-flex items-center gap-1.5 rounded-md border border-border bg-surface px-4 py-2 text-sm font-medium text-text transition-colors hover:bg-bg-muted";
  if (btn.type === "external" && btn.href) {
    return (
      <a href={btn.href} target="_blank" rel="noopener noreferrer" className={cls}>
        {btn.label} <ExternalLink size={14} />
      </a>
    );
  }
  if (btn.type === "page" && btn.href) {
    return (
      <Link href={btn.href} className={cls}>
        {btn.label} <ArrowRight size={14} />
      </Link>
    );
  }
  return (
    <button
      type="button"
      className={cls}
      onClick={() => onModal({ title: btn.label, body: btn.modalContent ?? "", byline: btn.byline })}
    >
      {btn.label}
    </button>
  );
}

function SectionBlock({
  section,
}: {
  section: ResourcePage["sections"][number];
}) {
  if (section.type === "links") {
    return (
      <section>
        <SectionHeader heading={section.heading} subheading={section.subheading} />
        {section.intro && (
          <div className="prose-body mb-4 text-text">
            <Markdown>{section.intro}</Markdown>
          </div>
        )}
        <LinkList links={section.links} />
      </section>
    );
  }

  if (section.type === "prose") {
    const isCallout = section.variant === "callout-tip";
    return (
      <section
        className={cn(
          isCallout && "rounded-2xl border border-accent/30 bg-accent/5 p-5 sm:p-6",
        )}
      >
        {isCallout && (
          <p className="mb-3 inline-flex items-center gap-2 rounded-full bg-accent/15 px-3 py-1 text-xs font-medium uppercase tracking-[0.1em] text-accent">
            Tip
          </p>
        )}
        <SectionHeader
          heading={section.heading}
          subheading={section.subheading}
          calloutSafe={isCallout}
        />
        {section.body && (
          <div className="prose-body text-text">
            <Markdown>{section.body}</Markdown>
          </div>
        )}
        {section.links && section.links.length > 0 && (
          <div className="mt-5">
            <LinkList links={section.links} />
          </div>
        )}
      </section>
    );
  }

  if (section.type === "contact") {
    return (
      <section>
        <SectionHeader heading={section.heading} />
        {section.intro && (
          <div className="prose-body mb-4 text-text">
            <Markdown>{section.intro}</Markdown>
          </div>
        )}
        <div className="rounded-2xl border border-border bg-bg-muted p-5 sm:p-6">
          <ul className="space-y-2 text-sm text-text">
            {section.email && (
              <li className="flex items-center gap-2">
                <Mail size={16} className="text-text-muted" />
                <a
                  href={`mailto:${section.email}`}
                  className="text-accent hover:text-accent-hover"
                >
                  {section.email}
                </a>
              </li>
            )}
            {section.phone && (
              <li className="flex items-center gap-2">
                <Phone size={16} className="text-text-muted" />
                <a
                  href={`tel:${section.phone.replace(/\s/g, "")}`}
                  className="text-accent hover:text-accent-hover"
                >
                  {section.phone}
                </a>
              </li>
            )}
            {section.hours && (
              <li className="flex items-center gap-2">
                <Clock size={16} className="text-text-muted" />
                <span>{section.hours}</span>
              </li>
            )}
            {section.address && (
              <li className="flex items-center gap-2">
                <MapPin size={16} className="text-text-muted" />
                {section.address.mapHref ? (
                  <a
                    href={section.address.mapHref}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-accent hover:text-accent-hover"
                  >
                    {section.address.label}
                  </a>
                ) : (
                  <span>{section.address.label}</span>
                )}
              </li>
            )}
          </ul>
          {section.social && section.social.length > 0 && (
            <ul className="mt-3 flex flex-wrap gap-3 text-sm">
              {section.social.map((s, i) => (
                <li key={i}>
                  <a
                    href={s.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-accent hover:text-accent-hover"
                  >
                    {s.platform} {s.handle}
                  </a>
                </li>
              ))}
            </ul>
          )}
        </div>
      </section>
    );
  }

  if (section.type === "comparison") {
    return (
      <section>
        <SectionHeader heading={section.heading} />
        {section.intro && (
          <div className="prose-body mb-4 text-text">
            <Markdown>{section.intro}</Markdown>
          </div>
        )}
        <div className="grid gap-4 sm:grid-cols-2">
          {section.columns.map((col, i) => (
            <div
              key={i}
              className="rounded-2xl border border-border bg-surface p-5 shadow-sm"
            >
              <h3 className="text-sm font-semibold tracking-tight text-text">
                {col.label}
              </h3>
              <ul className="mt-3 space-y-2 text-sm text-text">
                {col.items.map((it, j) => (
                  <li key={j} className="flex gap-2">
                    <span className="mt-2 inline-block h-1.5 w-1.5 flex-shrink-0 rounded-full bg-accent" />
                    <span>{it}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>
    );
  }

  if (section.type === "template") {
    return <TemplateBlock section={section} />;
  }

  return null;
}

function SectionHeader({
  heading,
  subheading,
  calloutSafe,
}: {
  heading: string;
  subheading?: string;
  calloutSafe?: boolean;
}) {
  return (
    <header className={cn("mb-3", calloutSafe ? "mt-1" : "")}>
      <h2 className="text-xl font-semibold tracking-tight text-text sm:text-2xl">
        {heading}
      </h2>
      {subheading && (
        <p className="mt-1 text-sm font-medium text-text-muted">{subheading}</p>
      )}
    </header>
  );
}

function LinkList({ links }: { links: ResourceLink[] }) {
  return (
    <ul className="space-y-2">
      {links.map((link, i) => (
        <ResourceLinkItem key={i} link={link} />
      ))}
    </ul>
  );
}

function ResourceLinkItem({ link }: { link: ResourceLink }) {
  const [open, setOpen] = useState(false);
  const isExternal = !!link.href && /^https?:/i.test(link.href);
  return (
    <li className="rounded-xl border border-border bg-surface p-4 shadow-sm">
      <div className="flex flex-wrap items-baseline gap-2">
        {link.href ? (
          <a
            href={link.href}
            target={isExternal ? "_blank" : undefined}
            rel={isExternal ? "noopener noreferrer" : undefined}
            className="inline-flex items-center gap-1 text-sm font-medium text-accent hover:text-accent-hover"
          >
            {link.label}
            {isExternal && <ExternalLink size={12} />}
          </a>
        ) : (
          <span className="inline-flex items-center gap-2 text-sm font-medium text-text">
            {link.label}
            <span className="rounded-full bg-bg-muted px-2 py-0.5 text-[10px] font-medium uppercase tracking-wider text-text-muted">
              Coming soon
            </span>
          </span>
        )}
        {link.meta && (
          <span className="text-xs text-text-subtle">({link.meta})</span>
        )}
      </div>
      {link.description && (
        <p className="mt-1 text-sm italic text-text-muted">{link.description}</p>
      )}
      {link.expandable && (
        <div className="mt-2">
          <button
            type="button"
            onClick={() => setOpen((o) => !o)}
            className="text-xs font-medium text-accent hover:text-accent-hover"
          >
            {open ? "Hide details" : "Show details"}
          </button>
          {open && (
            <p className="mt-2 text-sm text-text">{link.expandable}</p>
          )}
        </div>
      )}
    </li>
  );
}

function TemplateBlock({
  section,
}: {
  section: Extract<ResourcePage["sections"][number], { type: "template" }>;
}) {
  const [copied, setCopied] = useState(false);
  const onCopy = async () => {
    try {
      await navigator.clipboard.writeText(section.body);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // ignore
    }
  };
  return (
    <section>
      <SectionHeader heading={section.heading} />
      {section.intro && (
        <p className="mb-3 text-sm italic text-text-muted">{section.intro}</p>
      )}
      <div className="overflow-hidden rounded-2xl border border-border bg-bg-muted">
        <div className="flex items-center justify-between gap-3 border-b border-border bg-surface px-4 py-2.5 text-xs">
          <div className="flex flex-wrap items-baseline gap-3">
            {section.subjectLine && (
              <span className="font-semibold text-text">
                Subject: <span className="font-normal">{section.subjectLine}</span>
              </span>
            )}
            {section.meta && (
              <span className="text-text-subtle">{section.meta}</span>
            )}
          </div>
          {section.copyButton !== false && (
            <button
              type="button"
              onClick={onCopy}
              className="inline-flex items-center gap-1 rounded-md border border-border bg-bg px-2 py-1 text-xs font-medium text-text transition-colors hover:bg-bg-muted"
            >
              {copied ? (
                <>
                  <Check size={12} /> Copied
                </>
              ) : (
                <>
                  <Copy size={12} /> Copy
                </>
              )}
            </button>
          )}
        </div>
        <pre className="whitespace-pre-wrap break-words p-5 font-sans text-sm leading-7 text-text">
          {renderTemplateBody(section.body)}
        </pre>
      </div>
    </section>
  );
}

function renderTemplateBody(body: string) {
  // Split on *[placeholder]* style markers and render those distinctly
  const parts = body.split(/(\*\[[^\]]+\]\*|\[[^\]]+\])/);
  return parts.map((p, i) => {
    if (/^\*\[.+\]\*$/.test(p) || /^\[[^\]]+\]$/.test(p)) {
      const inner = p.replace(/^\*\[/, "[").replace(/\]\*$/, "]");
      return (
        <span key={i} className="italic text-text-subtle">
          {inner}
        </span>
      );
    }
    return <span key={i}>{p}</span>;
  });
}
