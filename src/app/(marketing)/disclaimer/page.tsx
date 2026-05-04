import { getSiteConfig } from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { Markdown } from "@/components/ui/Markdown";

export const metadata = buildMetadata({
  title: "Disclaimer",
  description: "Legal disclaimer for the Alt+Law student careers guide.",
  path: "/disclaimer/",
});

export default function DisclaimerPage() {
  const site = getSiteConfig();
  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header className="mb-8">
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          Disclaimer
        </h1>
      </header>
      <div className="prose-body text-text">
        <Markdown>{site.legalDisclaimer}</Markdown>
      </div>
    </div>
  );
}
