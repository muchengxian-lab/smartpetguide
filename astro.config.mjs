import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://smartpetguide.net",
  integrations: [
    tailwind(),
    sitemap({
      // lastmod auto-detected from file modification time; changefreq/priority by page type
      serialize(item) {
        const isHomepage = item.url === "https://smartpetguide.net/";
        const isInfoPage = ["/about/", "/privacy/", "/affiliate-disclosure/", "/how-we-research/", "/products-we-dont-recommend/"].some(
          (p) => item.url.endsWith(p),
        );
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
  trailingSlash: "always",
});
