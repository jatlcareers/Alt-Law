import type { MetadataRoute } from "next";
import { getAllPathways, getAllResources } from "@/lib/content";

export const dynamic = "force-static";

const SITE_URL =
  process.env.NEXT_PUBLIC_SITE_URL ?? "https://jatlcareers.github.io/Alt-Law";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = SITE_URL.replace(/\/$/, "");
  const staticRoutes = ["", "/about", "/forewords", "/pathways", "/resources", "/contact", "/disclaimer"];
  const pathwayRoutes = getAllPathways().map((p) => `/pathways/${p.slug}`);
  const resourceRoutes = getAllResources().map((r) => `/resources/${r.slug}`);
  const orgRoutes: string[] = [];
  for (const p of getAllPathways()) {
    if (p.slug !== "community-legal-centres") continue;
    for (const section of p.sections) {
      for (const org of section.orgs) {
        if (org.body || org.shortDescription) {
          orgRoutes.push(`/pathways/${p.slug}/${org.slug}`);
        }
      }
    }
  }
  const all = [...staticRoutes, ...pathwayRoutes, ...resourceRoutes, ...orgRoutes];
  const now = new Date();
  return all.map((path) => ({
    url: `${base}${path}/`,
    lastModified: now,
    changeFrequency: "monthly",
    priority: path === "" ? 1 : 0.7,
  }));
}
