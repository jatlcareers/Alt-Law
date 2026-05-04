export const PATHWAY_ORDER: string[] = [
  "community-legal-centres",
  "legal-aid-queensland",
  "associateships",
  "government-and-public-service",
  "first-nations-law",
  "international-law",
  "family-law",
  "criminal-law",
  "plaintiff-personal-injury",
  "boutique-and-other-specialties",
  "academia",
  "in-house-law",
  "the-bar",
  "legal-technology",
  "pro-bono-commercial-firms",
];

export const RESOURCE_CATEGORY_ORDER: {
  slug:
    | "resources-and-guides"
    | "networking-interviews-recruitment"
    | "jatl-career-tips";
  label: string;
  iconName: string;
  resources: string[];
}[] = [
  {
    slug: "resources-and-guides",
    label: "Resources and Guides",
    iconName: "FileText",
    resources: [
      "job-search",
      "career-support",
      "external-resources",
      "resumes",
      "cover-letters",
    ],
  },
  {
    slug: "networking-interviews-recruitment",
    label: "Networking, Interviews and Job Recruitment Help",
    iconName: "Users",
    resources: [
      "preparing-for-applications",
      "job-interviews",
      "understand-the-recruitment-process",
      "get-workplace-ready",
      "get-experience",
    ],
  },
  {
    slug: "jatl-career-tips",
    label: "JATL's Career Tips",
    iconName: "MessageCircle",
    resources: [
      "personal-branding-and-networking-tips",
      "career-mentoring",
      "linkedin",
      "information-interview-guide",
      "jatl-recommends",
    ],
  },
];
