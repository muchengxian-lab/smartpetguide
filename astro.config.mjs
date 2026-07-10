import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";
import { readFileSync } from "fs";

const dateData = JSON.parse(readFileSync(new URL("./src/data/content-dates.json", import.meta.url), "utf-8"));
const pages = dateData.pages || {};

function getLastmod(url) {
  const path = url.replace("https://smartpetguide.net/", "").replace(/\/$/, "");
  if (!path) return undefined;
  const parts = path.split("/");
  const type = parts[0];
  const slug = parts[parts.length - 1];
  const typePages = pages[type] || {};
  const entry = typePages[slug];
  if (entry) return entry.modifiedDate || entry.publishDate;
  return undefined;
}

export default defineConfig({
  site: "https://smartpetguide.net",
  integrations: [
    tailwind(),
    sitemap({
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
        // Set lastmod from content-dates registry
        const lm = getLastmod(item.url);
        if (lm) item.lastmod = lm;
        return item;
      },
    }),
  ],
  trailingSlash: "always",
});
