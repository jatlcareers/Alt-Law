import type { Metadata } from "next";

const SITE_NAME = "Alt+Law";
const SITE_URL =
  process.env.NEXT_PUBLIC_SITE_URL ?? "https://jatlcareers.github.io/Alt-Law";

type OgInput = {
  title: string;
  description?: string;
  path?: string;
  type?: "website" | "article";
};

export function buildMetadata({
  title,
  description,
  path,
  type = "website",
}: OgInput): Metadata {
  const url = path ? `${SITE_URL}${path}` : SITE_URL;

  return {
    title,
    description,
    alternates: { canonical: url },
    openGraph: {
      type,
      url,
      title,
      description,
      siteName: SITE_NAME,
      locale: "en_AU",
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
    },
  };
}
