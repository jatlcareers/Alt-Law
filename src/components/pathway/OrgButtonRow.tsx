"use client";

import { useState } from "react";
import { ModalRenderer, OrgLinkButton } from "./OrgGrid";
import type { OrgLink, Testimonial } from "@/lib/types";

type ModalState =
  | { kind: "modal" | "resource"; title: string; body: string; byline?: string }
  | { kind: "testimonials"; scope?: string; orgSlug?: string }
  | null;

type Props = {
  pathwaySlug: string;
  links: OrgLink[];
  testimonials: Testimonial[];
  showTestimonialsButton?: boolean;
  testimonialsScope?: string;
};

export function OrgButtonRow({
  pathwaySlug,
  links,
  testimonials,
  showTestimonialsButton,
  testimonialsScope,
}: Props) {
  const [modal, setModal] = useState<ModalState>(null);

  const allLinks: OrgLink[] = [...links];
  if (showTestimonialsButton) {
    allLinks.push({
      label: "Testimonials",
      type: "testimonials-modal",
    });
  }

  return (
    <>
      <div className="flex flex-wrap gap-2">
        {allLinks.map((link, i) => (
          <OrgLinkButton
            key={i}
            link={link}
            onModal={(s) => {
              if (s?.kind === "testimonials" && testimonialsScope) {
                setModal({ ...s, scope: testimonialsScope });
              } else {
                setModal(s);
              }
            }}
            pathwaySlug={pathwaySlug}
            className="px-3 py-2 text-sm"
          />
        ))}
      </div>

      <ModalRenderer
        modal={modal}
        onClose={() => setModal(null)}
        testimonials={testimonials}
      />
    </>
  );
}
