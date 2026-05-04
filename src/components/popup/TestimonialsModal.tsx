"use client";

import { useState } from "react";
import { ChevronLeft } from "lucide-react";
import { Modal } from "./Modal";
import { Markdown } from "@/components/ui/Markdown";
import type { Testimonial } from "@/lib/types";

type Props = {
  open: boolean;
  onClose: () => void;
  scope?: string;
  testimonials: Testimonial[];
};

export function TestimonialsModal({ open, onClose, scope, testimonials }: Props) {
  const [activeSlug, setActiveSlug] = useState<string | null>(null);
  const active = testimonials.find((t) => t.slug === activeSlug) ?? null;
  const title = active
    ? `${active.name} - ${active.organisation}`
    : `Testimonials${scope ? ` - ${scope}` : ""}`;

  const handleClose = () => {
    setActiveSlug(null);
    onClose();
  };

  return (
    <Modal open={open} onClose={handleClose} title={title} size="lg">
      {active ? (
        <div>
          <button
            type="button"
            onClick={() => setActiveSlug(null)}
            className="mb-4 inline-flex items-center gap-1 text-sm font-medium text-accent hover:text-accent-hover"
          >
            <ChevronLeft size={16} /> Back to list
          </button>
          <div className="mb-4">
            <p className="text-sm font-semibold text-text">{active.name}</p>
            <p className="text-sm text-text-muted">
              {[active.role, active.organisation, active.year]
                .filter(Boolean)
                .join(" - ")}
            </p>
          </div>
          {active.body ? (
            <Markdown>{active.body}</Markdown>
          ) : (
            <p className="rounded-md border border-dashed border-border bg-bg-muted p-4 text-sm text-text-muted">
              Body coming soon - this testimonial is awaiting transcription.
            </p>
          )}
        </div>
      ) : testimonials.length === 0 ? (
        <p className="text-sm text-text-muted">
          No testimonials yet for this section. Check back soon.
        </p>
      ) : (
        <ul className="divide-y divide-border">
          {testimonials.map((t) => (
            <li key={t.slug}>
              <button
                type="button"
                onClick={() => setActiveSlug(t.slug)}
                className="flex w-full flex-col items-start gap-0.5 py-3 text-left transition-colors hover:bg-bg-muted/60"
              >
                <span className="font-medium text-text">{t.name}</span>
                <span className="text-sm text-text-muted">
                  {[t.role, t.organisation, t.year].filter(Boolean).join(" - ")}
                </span>
              </button>
            </li>
          ))}
        </ul>
      )}
    </Modal>
  );
}
