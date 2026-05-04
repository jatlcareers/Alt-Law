import { notFound } from "next/navigation";
import {
  getAllPathways,
  getAllResources,
  getResource,
} from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { ResourcePageRenderer } from "@/components/resource/ResourcePageRenderer";

type Params = { slug: string };

export function generateStaticParams() {
  return getAllResources().map((r) => ({ slug: r.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;
  const r = getResource(slug);
  if (!r) return {};
  return buildMetadata({
    title: r.title,
    description:
      r.intro?.slice(0, 160) ??
      `${r.title} - resource in the JATL Alt+Law guide.`,
    path: `/resources/${r.slug}/`,
  });
}

export default async function ResourcePage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;
  const resource = getResource(slug);
  if (!resource) notFound();

  const allResources = getAllResources();
  const allPathways = getAllPathways();
  const related = {
    resources:
      (resource.relatedResources ?? [])
        .map((s) => allResources.find((r) => r.slug === s))
        .filter((r): r is NonNullable<typeof r> => !!r)
        .map((r) => ({ name: r.title, slug: r.slug })),
    pathways:
      (resource.relatedPathways ?? [])
        .map((s) => allPathways.find((p) => p.slug === s))
        .filter((p): p is NonNullable<typeof p> => !!p)
        .map((p) => ({ name: p.name, slug: p.slug })),
  };

  return <ResourcePageRenderer resource={resource} related={related} />;
}
