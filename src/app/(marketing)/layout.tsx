import { SiteHeader } from "@/components/nav/SiteHeader";
import { SiteFooter } from "@/components/nav/SiteFooter";
import { AcknowledgementPopup } from "@/components/popup/AcknowledgementPopup";
import { getSiteConfig } from "@/lib/content";

export default function MarketingLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const site = getSiteConfig();

  return (
    <>
      <a href="#main" className="skip-to-content">
        Skip to content
      </a>
      <SiteHeader />
      <main id="main" className="flex-1 w-full">
        {children}
      </main>
      <SiteFooter sponsors={site.sponsors} />
      <AcknowledgementPopup acknowledgement={site.acknowledgementOfCountry} />
    </>
  );
}
