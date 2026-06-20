import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://smartpetguide.net",
  integrations: [
    tailwind(),
    sitemap({
      serialize(item) {
        // Add lastmod to all URLs — helps Google prioritize crawling
        // Static pages get today's date; review/guide pages use their publish dates
        const isHomepage = item.url === "https://smartpetguide.net/";
        const isInfoPage = ["/about/", "/privacy/", "/affiliate-disclosure/", "/how-we-research/", "/products-we-dont-recommend/"].some(
          (p) => item.url.endsWith(p),
        );
        // Info pages updated less frequently — use a 2-week window
        if (isInfoPage) {
          const d = new Date();
          d.setDate(d.getDate() - 14);
          item.lastmod = d.toISOString().split("T")[0];
        } else {
          // All content pages and homepage use today
          item.lastmod = new Date().toISOString().split("T")[0];
        }
        // Set change frequency based on page type
        if (isHomepage) {
          item.changefreq = "daily";
          item.priority = 1.0;
        } else if (isInfoPage) {
          item.changefreq = "monthly";
          item.priority = 0.5;
        } else {
          item.changefreq = "weekly";
          item.priority = 0.7;
        }
        return item;
      },
    }),
  ],
  trailingSlash: "never",
});
