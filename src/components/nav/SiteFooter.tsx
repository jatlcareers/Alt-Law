import Link from "next/link";
import { AltLawLogo } from "@/components/ui/AltLawLogo";
import type { SiteConfig } from "@/lib/types";

const FOOTER_SECTIONS: { heading: string; links: { label: string; href: string }[] }[] = [
  {
    heading: "Explore",
    links: [
      { label: "Career Pathways", href: "/pathways" },
      { label: "Resources", href: "/resources" },
      { label: "Forewords", href: "/forewords" },
    ],
  },
  {
    heading: "About",
    links: [
      { label: "About JATL", href: "/about" },
      { label: "Contact", href: "/contact" },
      { label: "Disclaimer", href: "/disclaimer" },
    ],
  },
];

type Props = {
  sponsors: SiteConfig["sponsors"];
};

export function SiteFooter({ sponsors }: Props) {
  return (
    <footer className="mt-20 border-t border-border bg-bg-muted">
      <div className="mx-auto max-w-[1280px] px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
          <div>
            <Link href="/" className="inline-flex items-center" aria-label="Alt+Law home">
              <AltLawLogo size="sm" />
            </Link>
            <p className="mt-3 max-w-xs text-sm text-text-muted">
              Published by JATL - UQ Justice and the Law Society. A student-led
              guide to the breadth of legal practice.
            </p>
          </div>

          {FOOTER_SECTIONS.map((section) => (
            <div key={section.heading}>
              <h3 className="text-sm font-semibold tracking-tight text-text">
                {section.heading}
              </h3>
              <ul className="mt-3 space-y-2">
                {section.links.map((link) => (
                  <li key={link.href}>
                    <Link
                      href={link.href}
                      className="text-sm text-text-muted transition-colors hover:text-accent"
                    >
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}

          <div>
            <h3 className="text-sm font-semibold tracking-tight text-text">
              Proudly supported by
            </h3>
            <ul className="mt-3 space-y-2">
              {sponsors.map((sponsor) =>
                sponsor.href ? (
                  <li key={sponsor.name}>
                    <a
                      href={sponsor.href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-sm text-text-muted transition-colors hover:text-accent"
                    >
                      {sponsor.name}
                    </a>
                  </li>
                ) : (
                  <li key={sponsor.name} className="text-sm text-text-muted">
                    {sponsor.name}
                  </li>
                ),
              )}
            </ul>
          </div>
        </div>

        <div className="mt-10 flex flex-col gap-3 border-t border-border pt-6 text-xs text-text-subtle sm:flex-row sm:items-center sm:justify-between">
          <p>
            © {new Date().getFullYear()} Justice and the Law Society (JATL),
            University of Queensland.
          </p>
          <p>
            Information is general and may change. See the{" "}
            <Link href="/disclaimer" className="underline hover:text-accent">
              full disclaimer
            </Link>
            .
          </p>
        </div>
      </div>
    </footer>
  );
}
