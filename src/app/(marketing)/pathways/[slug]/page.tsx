import { notFound } from "next/navigation";
import {
  getAllPathways,
  getPathway,
  getTestimonials,
} from "@/lib/content";
import { buildMetadata } from "@/lib/og";
import { PathwayRenderer } from "@/components/pathway/PathwayRenderer";

type Params = { slug: string };

export function generateStaticParams() {
  return getAllPathways().map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: { params: Promise<Params> }) {
  const { slug } = await params;
  const pathway = getPathway(slug);
  if (!pathway) return {};
  return buildMetadata({
    title: pathway.name,
    description:
      pathway.introAbove?.slice(0, 160) ??
      pathway.introBelow?.slice(0, 160) ??
      `${pathway.name} - career pathway in the JATL Alt+Law guide.`,
    path: `/pathways/${pathway.slug}/`,
  });
}

export default async function PathwayPage({
  params,
}: {
  params: Promise<Params>;
}) {
  const { slug } = await params;
  const pathway = getPathway(slug);
  if (!pathway) notFound();

  const testimonials = getTestimonials({ pathwaySlug: pathway.slug });
  const all = getAllPathways();
  const lookup: Record<string, { name: string; slug: string }> = {};
  for (const p of all) lookup[p.slug] = { name: p.name, slug: p.slug };

  return (
    <PathwayRenderer
      pathway={pathway}
      testimonials={testimonials}
      allPathwayLookup={lookup}
    />
  );
}
