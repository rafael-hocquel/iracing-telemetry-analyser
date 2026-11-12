import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const playfair = localFont({
  src: [
    {
      path: "./fonts/PlayfairDisplay-Regular.woff2",
      style: "normal",
    },
    {
      path: "./fonts/PlayfairDisplay-Italic.woff2",
      style: "italic",
    },
  ],
});

export const metadata: Metadata = {
  title: "Iracing Telemetry Analyser",
  description:
    "Sim racing telemetry analysis: braking points, brake traces and lap-by-lap KPIs against a reference lap.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={`${playfair.className} h-full antialiased`}>
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
