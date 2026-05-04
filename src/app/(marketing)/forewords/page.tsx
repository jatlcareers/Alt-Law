import { getForewords } from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { Markdown } from "@/components/ui/Markdown";

export const metadata = buildMetadata({
  title: "Forewords",
  description:
    "Forewords from JATL leadership and the College of Law for the Alt+Law student careers guide.",
  path: "/forewords/",
});

export default function ForewordsPage() {
  const forewords = getForewords();
  return (
    <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
      <header className="mb-10">
        <h1 className="text-3xl font-semibold tracking-tight text-text sm:text-4xl">
          Forewords
        </h1>
        <p className="mt-3 text-lg text-text-muted">
          Words from those who built Alt+Law and the partners that supported it.
        </p>
      </header>
      <ul className="space-y-6">
        {forewords.map((f) => (
          <li
            key={f.slug}
            className="rounded-2xl border border-border bg-surface p-6 shadow-sm sm:p-8"
          >
            <p className="text-xs font-semibold uppercase tracking-[0.14em] text-text-subtle">
              Foreword
            </p>
            <h2 className="mt-2 text-xl font-semibold tracking-tight text-text">
              {f.name}
            </h2>
            <p className="text-sm text-text-muted">{f.role}</p>
            {f.body ? (
              <div className="prose-body mt-4 text-text">
                <Markdown>{f.body}</Markdown>
              </div>
            ) : (
              <p className="mt-4 rounded-md border border-dashed border-border bg-bg-muted p-4 text-sm italic text-text-subtle">
                Body coming soon.
              </p>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
