"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, ExternalLink } from "lucide-react";
import { ResourceModal } from "@/components/popup/ResourceModal";
import { TestimonialsModal } from "@/components/popup/TestimonialsModal";
import type { Org, OrgLink, Testimonial } from "@/lib/types";
import { cn } from "@/lib/cn";

type ModalState =
  | { kind: "modal" | "resource"; title: string; body: string; byline?: string }
  | { kind: "testimonials"; scope?: string; orgSlug?: string }
  | null;

type Props = {
  pathwaySlug: string;
  orgs: Org[];
  testimonials: Testimonial[];
  hasOrgPages?: boolean;
};

export function OrgGrid({ pathwaySlug, orgs, testimonials, hasOrgPages = false }: Props) {
  const [modal, setModal] = useState<ModalState>(null);

  return (
    <>
      <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {orgs.map((org) => (
          <li key={org.slug}>
            <article className="group flex h-full flex-col rounded-2xl border border-border bg-surface p-5 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md">
              <OrgTilePlaceholder name={org.name} />
              <h3 className="mt-4 text-base font-semibold tracking-tight text-text">
                {org.name}
              </h3>
              {org.shortDescription && (
                <p className="mt-1 text-sm leading-6 text-text-muted">
                  {org.shortDescription}
                </p>
              )}
              <div className="mt-4 flex flex-wrap gap-2">
                {hasOrgPages && (org.body || org.shortDescription) && (
                  <Link
                    href={`/pathways/${pathwaySlug}/${org.slug}/`}
                    className="inline-flex items-center gap-1 rounded-md border border-border bg-bg-muted px-2.5 py-1 text-xs font-medium text-text transition-colors hover:bg-border"
                  >
                    See more <ArrowRight size={12} />
                  </Link>
                )}
                {(org.links || []).map((link, i) => (
                  <OrgLinkButton
                    key={i}
                    link={link}
                    onModal={(s) => setModal(s)}
                    pathwaySlug={pathwaySlug}
                    orgSlug={org.slug}
                  />
                ))}
              </div>
            </article>
          </li>
        ))}
      </ul>

      <ModalRenderer
        modal={modal}
        onClose={() => setModal(null)}
        testimonials={testimonials}
      />
    </>
  );
}

export function OrgTilePlaceholder({ name }: { name: string }) {
  const initials = name
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0])
    .join("")
    .toUpperCase();
  return (
    <div className="inline-flex h-12 w-12 items-center justify-center rounded-lg bg-accent/10 text-accent">
      <span className="text-sm font-semibold">{initials}</span>
    </div>
  );
}

export function OrgLinkButton({
  link,
  onModal,
  orgSlug,
  className,
}: {
  link: OrgLink;
  onModal: (s: ModalState) => void;
  pathwaySlug: string;
  orgSlug?: string;
  className?: string;
}) {
  const baseCls = cn(
    "inline-flex items-center gap-1 rounded-md px-2.5 py-1 text-xs font-medium transition-colors",
    "border border-border bg-surface text-text hover:bg-bg-muted",
    className,
  );

  if (link.type === "external" && link.href) {
    return (
      <a
        href={link.href}
        target="_blank"
        rel="noopener noreferrer"
        className={baseCls}
      >
        {link.label} <ExternalLink size={12} />
      </a>
    );
  }
  if (link.type === "page" && link.href) {
    return (
      <Link href={link.href} className={baseCls}>
        {link.label} <ArrowRight size={12} />
      </Link>
    );
  }
  if (link.type === "modal" || link.type === "resource-modal") {
    return (
      <button
        type="button"
        className={baseCls}
        onClick={() =>
          onModal({
            kind: link.type === "resource-modal" ? "resource" : "modal",
            title: link.label,
            body: link.modalContent ?? "",
            byline: link.byline,
          })
        }
      >
        {link.label}
      </button>
    );
  }
  if (link.type === "testimonials-modal") {
    return (
      <button
        type="button"
        className={baseCls}
        onClick={() => onModal({ kind: "testimonials", scope: link.label, orgSlug })}
      >
        {link.label}
      </button>
    );
  }
  return (
    <span className={cn(baseCls, "opacity-60")} aria-disabled="true">
      {link.label}
    </span>
  );
}

export function ModalRenderer({
  modal,
  onClose,
  testimonials,
}: {
  modal: ModalState;
  onClose: () => void;
  testimonials: Testimonial[];
}) {
  if (!modal) return null;
  if (modal.kind === "testimonials") {
    const filtered = modal.orgSlug
      ? testimonials.filter((t) => (t.orgSlugs ?? []).includes(modal.orgSlug!))
      : testimonials;
    return (
      <TestimonialsModal
        open={true}
        onClose={onClose}
        scope={modal.scope}
        testimonials={filtered}
      />
    );
  }
  return (
    <ResourceModal
      open={true}
      onClose={onClose}
      title={modal.title}
      body={modal.body}
      byline={modal.byline}
      size={modal.kind === "resource" ? "xl" : "lg"}
    />
  );
}
