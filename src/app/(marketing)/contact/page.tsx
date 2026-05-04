import { Mail, Camera, Briefcase } from "lucide-react";
import { buildMetadata } from "@/lib/og";

export const metadata = buildMetadata({
  title: "Contact",
  description: "Get in touch with JATL - UQ Justice and the Law Society.",
  path: "/contact/",
});

const CHANNELS = [
  {
    label: "Email JATL",
    icon: Mail,
    href: "mailto:hello@jatluq.com",
    detail: "hello@jatluq.com",
  },
  {
    label: "Instagram",
    icon: Camera,
    href: "https://www.instagram.com/justiceandthelawsociety/",
    detail: "@justiceandthelawsociety",
  },
  {
    label: "LinkedIn",
    icon: Briefcase,
    href: "https://www.linkedin.com/company/uq-justice-and-the-law-society/",
    detail: "UQ Justice and the Law Society",
  },
];

export default function ContactPage() {
  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header>
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          Contact
        </h1>
        <p className="mt-3 text-lg text-text-muted">
          We'd love to hear from you. Reach out for content corrections, partnership
          opportunities, or to share your own legal-careers story.
        </p>
      </header>

      <ul className="mt-10 space-y-3">
        {CHANNELS.map((c) => (
          <li key={c.label}>
            <a
              href={c.href}
              target={c.href.startsWith("http") ? "_blank" : undefined}
              rel={c.href.startsWith("http") ? "noopener noreferrer" : undefined}
              className="group flex items-center gap-4 rounded-2xl border border-border bg-surface p-5 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md"
            >
              <span className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-accent/10 text-accent">
                <c.icon size={18} />
              </span>
              <span className="flex-1">
                <span className="block font-medium text-text">{c.label}</span>
                <span className="block text-sm text-text-muted">{c.detail}</span>
              </span>
            </a>
          </li>
        ))}
      </ul>

      <p className="mt-10 text-sm text-text-subtle">
        Spotted an error or broken link? Email us with the page URL and the issue,
        and we'll fix it on the next update.
      </p>
    </div>
  );
}
