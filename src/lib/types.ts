// ============================================================================
// PATHWAYS
// ============================================================================

export type DisplayMode = "cards" | "buttonRow" | "table" | "prose-only";

export type LinkType =
  | "page"
  | "modal"
  | "external"
  | "testimonials-modal"
  | "resource-modal";

export type OrgLink = {
  label: string;
  type: LinkType;
  href?: string;
  modalContent?: string;
  byline?: string;
};

export type OrgContact = {
  email?: string;
  phone?: string;
  website?: string;
  applicationWindows?: string;
};

export type Org = {
  slug: string;
  name: string;
  logoUrl?: string;
  shortDescription?: string;
  body?: string;
  pathways: string[];
  links: OrgLink[];
  contact?: OrgContact;
};

export type PathwaySection = {
  heading?: string;
  intro?: string;
  displayMode: DisplayMode;
  orgs: Org[];
  showTestimonialsButton?: boolean;
  testimonialsScope?: string;
};

export type Pathway = {
  slug: string;
  name: string;
  iconName?: string;
  status: "published" | "coming-soon";
  introAbove?: string;
  introBelow?: string;
  topLevelLinks?: OrgLink[];
  sections: PathwaySection[];
  bodyContent?: string;
  relatedPathways?: string[];
};

// ============================================================================
// TESTIMONIALS
// ============================================================================

export type Testimonial = {
  slug: string;
  name: string;
  role: string;
  organisation: string;
  year?: string;
  pathways: string[];
  orgSlugs?: string[];
  body: string;
};

// ============================================================================
// RESOURCES
// ============================================================================

export type ResourceLinkMeta = string;

export type ResourceLink = {
  label: string;
  href?: string;
  description?: string;
  expandable?: string;
  meta?: ResourceLinkMeta;
};

export type ResourceContactSocial = {
  platform: string;
  handle: string;
  href: string;
};

export type ResourceContactAddress = {
  label: string;
  mapHref?: string;
};

export type ResourceSection =
  | {
      type: "links";
      heading: string;
      subheading?: string;
      intro?: string;
      links: ResourceLink[];
    }
  | {
      type: "prose";
      heading: string;
      subheading?: string;
      body: string;
      links?: ResourceLink[];
      variant?: "default" | "callout-tip";
    }
  | {
      type: "contact";
      heading: string;
      intro?: string;
      email?: string;
      phone?: string;
      hours?: string;
      address?: ResourceContactAddress;
      social?: ResourceContactSocial[];
    }
  | {
      type: "comparison";
      heading: string;
      intro?: string;
      columns: [
        { label: string; items: string[] },
        { label: string; items: string[] },
      ];
    }
  | {
      type: "template";
      heading: string;
      intro?: string;
      subjectLine?: string;
      meta?: string;
      body: string;
      copyButton?: boolean;
    };

export type ResourcePage = {
  slug: string;
  category:
    | "resources-and-guides"
    | "networking-interviews-recruitment"
    | "jatl-career-tips";
  title: string;
  status: "published" | "coming-soon" | "partial";
  byJatl?: boolean;
  intro?: string;
  sections: ResourceSection[];
  buttons?: OrgLink[];
  relatedResources?: string[];
  relatedPathways?: string[];
};

// ============================================================================
// FOREWORDS
// ============================================================================

export type Foreword = {
  slug: string;
  name: string;
  role: string;
  body: string;
};

// ============================================================================
// SITE GLOBALS
// ============================================================================

export type SiteSponsor = {
  name: string;
  logoUrl?: string;
  href?: string;
};

export type SiteSocialLink = {
  platform: string;
  href: string;
};

export type SiteConfig = {
  acknowledgementOfCountry: string;
  welcomeIntro: string;
  legalDisclaimer: string;
  sponsors: SiteSponsor[];
  socialLinks?: SiteSocialLink[];
  pendingUrls?: { id: string; description: string }[];
};
