import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "Alt+Law - JATL's Student Careers Guide",
    template: "%s · Alt+Law",
  },
  description:
    "A counter-guide to commercial-clerkship-focused careers guides, showcasing the full spectrum of legal practice - from community legal centres and family law to associateships and the bar. Published by JATL (UQ Justice and the Law Society).",
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? "https://jatlcareers.github.io/Alt-Law/"),
  openGraph: {
    type: "website",
    siteName: "Alt+Law",
    locale: "en_AU",
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`${inter.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col bg-bg text-text">
        {children}
      </body>
    </html>
  );
}
