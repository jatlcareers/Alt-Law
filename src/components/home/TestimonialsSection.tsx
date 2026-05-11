"use client";

import { useState } from "react";
import { ArrowRight, Quote } from "lucide-react";
import { TestimonialsModal } from "@/components/popup/TestimonialsModal";
import type { Testimonial } from "@/lib/types";

type Props = {
  testimonials: Testimonial[];
};

const FEATURED_COUNT = 3;

export function TestimonialsSection({ testimonials }: Props) {
  const [open, setOpen] = useState(false);

  if (testimonials.length === 0) return null;

  // Prefer testimonials that have a body. If none do, fall back to the first
  // few scaffolded entries so the section still surfaces the people.
  const withBody = testimonials.filter((t) => t.body && t.body.trim().length > 0);
  const featured = (withBody.length > 0 ? withBody : testimonials).slice(
    0,
    FEATURED_COUNT,
  );

  return (
    <section className="bg-bg-muted">
      <div className="mx-auto max-w-[1280px] px-4 py-16 sm:px-6 sm:py-20 lg:px-8">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-sm font-medium uppercase tracking-[0.18em] text-text-subtle">
              Voices
            </p>
            <h2 className="mt-2 text-2xl font-semibold tracking-tight text-text sm:text-3xl">
              Hear from the people doing this work
            </h2>
            <p className="mt-2 max-w-2xl text-text-muted">
              Students, graduates, and practitioners sharing what their roles
              are really like - across CLCs, government, the bar, and beyond.
            </p>
          </div>
          <button
            type="button"
            onClick={() => setOpen(true)}
            className="inline-flex items-center gap-1.5 self-start rounded-md bg-accent px-4 py-2 text-sm font-medium text-accent-fg transition-colors hover:bg-accent-hover sm:self-auto"
          >
            See all testimonials <ArrowRight size={14} />
          </button>
        </div>

        <ul className="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {featured.map((t) => {
            const hasBody = t.body && t.body.trim().length > 0;
            const excerpt = hasBody
              ? t.body.length > 220
                ? `${t.body.slice(0, 220).trimEnd()}...`
                : t.body
              : null;
            return (
              <li key={t.slug}>
                <button
                  type="button"
                  onClick={() => setOpen(true)}
                  className="group flex h-full w-full flex-col rounded-2xl border border-border bg-surface p-5 text-left shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md"
                >
                  <Quote
                    size={20}
                    className="text-accent/70"
                    aria-hidden="true"
                  />
                  {excerpt ? (
                    <p className="mt-3 text-sm leading-6 text-text">
                      {excerpt}
                    </p>
                  ) : (
                    <p className="mt-3 text-sm italic leading-6 text-text-muted">
                      Full testimonial coming soon.
                    </p>
                  )}
                  <div className="mt-4 border-t border-border pt-3">
                    <p className="text-sm font-semibold text-text">{t.name}</p>
                    <p className="text-xs text-text-muted">
                      {[t.role, t.organisation, t.year]
                        .filter(Boolean)
                        .join(" - ")}
                    </p>
                  </div>
                  <span className="mt-3 inline-flex items-center gap-1 text-xs font-medium text-accent transition-transform group-hover:translate-x-0.5">
                    Read more <ArrowRight size={12} />
                  </span>
                </button>
              </li>
            );
          })}
        </ul>
      </div>

      <TestimonialsModal
        open={open}
        onClose={() => setOpen(false)}
        scope="from Alt+Law"
        testimonials={testimonials}
      />
    </section>
  );
}
