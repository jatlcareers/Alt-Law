import Image from "next/image";
import Link from "next/link";
import { ArrowRight, BookOpen, Megaphone, HeartHandshake, Briefcase } from "lucide-react";
import { getSiteConfig } from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { Markdown } from "@/components/ui/Markdown";
import { withBasePath } from "@/lib/asset";

export const metadata = buildMetadata({
  title: "About JATL",
  description:
    "JATL (UQ Justice and the Law Society) promotes and critically examines the intersection between law and social justice. Learn what we do and how to join.",
  path: "/about/",
});

const OBJECTIVES = [
  {
    title: "Education",
    icon: BookOpen,
    body: "Build practical knowledge of how law and social justice intersect through panels, workshops, and publications like Alt+Law.",
  },
  {
    title: "Advocacy",
    icon: Megaphone,
    body: "Critically examine the legal system and amplify student voices on access to justice, law reform, and equity.",
  },
  {
    title: "Community",
    icon: HeartHandshake,
    body: "Connect students with practitioners, mentors, and peers across community legal centres, government, and the bar.",
  },
  {
    title: "Opportunity",
    icon: Briefcase,
    body: "Surface the breadth of legal practice beyond commercial clerkships - and the resources to step into it.",
  },
];

export default function AboutPage() {
  const site = getSiteConfig();
  return (
    <div className="mx-auto max-w-[1280px] px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header className="max-w-3xl">
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          About JATL
        </h1>
        <div className="prose-body mt-6 text-text">
          <Markdown>{site.welcomeIntro}</Markdown>
        </div>
      </header>

      <section className="mt-12">
        <h2 className="text-xl font-semibold tracking-tight text-text">
          Our objectives
        </h2>
        <ul className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {OBJECTIVES.map((o) => (
            <li
              key={o.title}
              className="rounded-2xl border border-border bg-surface p-5 shadow-sm"
            >
              <div className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-accent/10 text-accent">
                <o.icon size={20} />
              </div>
              <h3 className="mt-3 text-base font-semibold tracking-tight text-text">
                {o.title}
              </h3>
              <p className="mt-1 text-sm leading-6 text-text-muted">{o.body}</p>
            </li>
          ))}
        </ul>
      </section>

      <section className="mt-16 grid gap-8 rounded-2xl border border-border bg-bg-muted p-6 sm:grid-cols-2 sm:p-10">
        <div>
          <h2 className="text-xl font-semibold tracking-tight text-text">
            Become a member
          </h2>
          <p className="mt-3 text-text-muted">
            Membership keeps Alt+Law growing. Join JATL to access events,
            mentoring, and the wider UQ legal community.
          </p>
          <div className="mt-5 flex flex-wrap gap-3">
            <a
              href="https://www.uqu.com.au/"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 rounded-md bg-accent px-4 py-2 text-sm font-medium text-accent-fg transition-colors hover:bg-accent-hover"
            >
              Join via UQU <ArrowRight size={14} />
            </a>
            <Link
              href="/contact/"
              className="inline-flex items-center gap-1.5 rounded-md border border-border bg-surface px-4 py-2 text-sm font-medium text-text transition-colors hover:bg-bg-muted"
            >
              Contact JATL
            </Link>
          </div>
        </div>
        <div className="flex items-center justify-center rounded-xl border border-dashed border-border bg-surface p-8 text-center">
          <div>
            <Image
              src={withBasePath("/membership-qr.gif")}
              alt="Scan to join JATL"
              width={192}
              height={192}
              unoptimized
              className="mx-auto h-48 w-48 rounded-lg bg-white p-2"
            />
            <p className="mt-3 text-xs text-text-subtle">
              Scan to join JATL.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
