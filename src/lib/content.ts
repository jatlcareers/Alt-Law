import "server-only";

import fs from "node:fs";
import path from "node:path";
import type {
  Foreword,
  Org,
  Pathway,
  ResourcePage,
  SiteConfig,
  Testimonial,
} from "./types";

const CONTENT_ROOT = path.join(process.cwd(), "content");
const PATHWAYS_DIR = path.join(CONTENT_ROOT, "pathways");
const RESOURCES_DIR = path.join(CONTENT_ROOT, "resources");

const MDX_TOKEN = /^__mdx:([\w.-]+)__$/;

function readJsonFile<T>(filePath: string): T {
  const raw = fs.readFileSync(filePath, "utf8");
  return JSON.parse(raw) as T;
}

function readMdxSibling(jsonFilePath: string, fieldName: string): string {
  const dir = path.dirname(jsonFilePath);
  const base = path.basename(jsonFilePath, ".json");
  const candidates = [
    path.join(dir, `${base}.${fieldName}.mdx`),
    path.join(dir, `${base}.${fieldName}.md`),
    path.join(dir, `${base}.mdx`),
    path.join(dir, `${base}.md`),
  ];
  for (const c of candidates) {
    if (fs.existsSync(c)) return fs.readFileSync(c, "utf8");
  }
  console.warn(
    `[content] No sibling MDX file found for ${jsonFilePath} field "${fieldName}". Tried: ${candidates.join(", ")}`,
  );
  return "";
}

function resolveMdxTokensInValue(value: unknown, jsonFilePath: string): unknown {
  if (typeof value === "string") {
    const match = value.match(MDX_TOKEN);
    if (match) {
      return readMdxSibling(jsonFilePath, match[1]);
    }
    return value;
  }
  if (Array.isArray(value)) {
    return value.map((v) => resolveMdxTokensInValue(v, jsonFilePath));
  }
  if (value && typeof value === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(value as Record<string, unknown>)) {
      out[k] = resolveMdxTokensInValue(v, jsonFilePath);
    }
    return out;
  }
  return value;
}

function readContentFile<T>(filePath: string): T {
  const data = readJsonFile<T>(filePath);
  return resolveMdxTokensInValue(data, filePath) as T;
}

// ============================================================================
// Site config
// ============================================================================

export function getSiteConfig(): SiteConfig {
  return readContentFile<SiteConfig>(path.join(CONTENT_ROOT, "site.json"));
}

// ============================================================================
// Pathways
// ============================================================================

export function getAllPathways(): Pathway[] {
  if (!fs.existsSync(PATHWAYS_DIR)) return [];
  const files = fs
    .readdirSync(PATHWAYS_DIR)
    .filter((f) => f.endsWith(".json"));
  return files
    .map((f) => readContentFile<Pathway>(path.join(PATHWAYS_DIR, f)))
    .sort((a, b) => a.slug.localeCompare(b.slug));
}

export function getPathway(slug: string): Pathway | null {
  const filePath = path.join(PATHWAYS_DIR, `${slug}.json`);
  if (!fs.existsSync(filePath)) return null;
  return readContentFile<Pathway>(filePath);
}

export function getOrg(pathwaySlug: string, orgSlug: string): Org | null {
  const pathway = getPathway(pathwaySlug);
  if (!pathway) return null;
  for (const section of pathway.sections) {
    const found = section.orgs.find((o) => o.slug === orgSlug);
    if (found) return found;
  }
  return null;
}

// ============================================================================
// Resources
// ============================================================================

export function getAllResources(): ResourcePage[] {
  if (!fs.existsSync(RESOURCES_DIR)) return [];
  const files = fs
    .readdirSync(RESOURCES_DIR)
    .filter((f) => f.endsWith(".json"));
  return files
    .map((f) => readContentFile<ResourcePage>(path.join(RESOURCES_DIR, f)))
    .sort((a, b) => a.slug.localeCompare(b.slug));
}

export function getResource(slug: string): ResourcePage | null {
  const filePath = path.join(RESOURCES_DIR, `${slug}.json`);
  if (!fs.existsSync(filePath)) return null;
  return readContentFile<ResourcePage>(filePath);
}

// ============================================================================
// Testimonials
// ============================================================================

type TestimonialFilter = {
  pathwaySlug?: string;
  orgSlug?: string;
};

export function getTestimonials(
  filter: TestimonialFilter = {},
): Testimonial[] {
  const filePath = path.join(CONTENT_ROOT, "testimonials.json");
  if (!fs.existsSync(filePath)) return [];
  const raw = readJsonFile<unknown[]>(filePath);

  const entries = raw.filter(
    (entry): entry is Testimonial =>
      !!entry &&
      typeof entry === "object" &&
      "slug" in (entry as Record<string, unknown>) &&
      typeof (entry as Record<string, unknown>).slug === "string",
  );

  return entries.filter((t) => {
    if (filter.pathwaySlug && !t.pathways.includes(filter.pathwaySlug)) {
      return false;
    }
    if (filter.orgSlug && !(t.orgSlugs ?? []).includes(filter.orgSlug)) {
      return false;
    }
    return true;
  });
}

// ============================================================================
// Forewords
// ============================================================================

export function getForewords(): Foreword[] {
  const filePath = path.join(CONTENT_ROOT, "forewords.json");
  if (!fs.existsSync(filePath)) return [];
  return readContentFile<Foreword[]>(filePath);
}
