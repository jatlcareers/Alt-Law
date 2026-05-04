import { Markdown } from "@/components/ui/Markdown";
import type { Org } from "@/lib/types";

type Props = {
  orgs: Org[];
};

export function OrgTable({ orgs }: Props) {
  return (
    <div className="overflow-hidden rounded-2xl border border-border bg-surface shadow-sm">
      <ul className="divide-y divide-border">
        {orgs.map((org) => (
          <li key={org.slug} className="grid gap-4 p-5 sm:grid-cols-[200px_1fr] sm:p-6">
            <div>
              <h3 className="text-base font-semibold tracking-tight text-text">
                {org.name}
              </h3>
            </div>
            <div className="text-sm leading-7 text-text">
              {org.body ? (
                <Markdown>{org.body}</Markdown>
              ) : org.shortDescription ? (
                <p className="text-text-muted">{org.shortDescription}</p>
              ) : (
                <p className="text-text-subtle">More information coming soon.</p>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
