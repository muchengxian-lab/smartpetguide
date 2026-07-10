import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";
import { readFileSync } from "fs";

const dateData = JSON.parse(readFileSync(new URL("./src/data/content-dates.json", import.meta.url), "utf-8"));
const defaults = dateData.defaults || {};
const overrides = dateData.overrides || {};

function getLastmod(url) {
  // Extract type and slug from URL path: e.g. /guides/stop-automatic-feeder-from-jamming/ → type=guides, slug=stop-automatic-feeder-from-jamming
  const path = url.replace("https://smartpetguide.net/", "").replace(/\/$/, "");
  if (!path) return undefined; // homepage
  const parts = path.split("/");
  const type = parts[0];
  const slug = parts[parts.length - 1];
  const typeOverrides = overrides[type] || {};
  const typeDefaults = defaults[type] || {};
  if (typeOverrides[slug]) {
    return typeOverrides[slug].modifiedDate || typeDefaults.modifiedDate;
  }
  return typeDefaults.modifiedDate || undefined;
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
