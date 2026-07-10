import { readFile, readdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const registry = JSON.parse(await readFile(path.join(root, "src/data/content-dates.json"), "utf8"));
const sitemap = await readFile(path.join(root, "dist/sitemap-0.xml"), "utf8");
const datePattern = /^\d{4}-\d{2}-\d{2}$/;
const today = new Intl.DateTimeFormat("en-CA", {
  timeZone: "Asia/Shanghai",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
}).format(new Date());
const issues = [];

const sitemapEntries = new Map(
  [...sitemap.matchAll(/<url><loc>([^<]+)<\/loc>(?:<lastmod>([^<]+)<\/lastmod>)?.*?<\/url>/g)].map(
    ([, url, lastmod]) => [url, lastmod],
  ),
);

const expectedRoutes = new Set();
let sameDateCount = 0;

for (const [type, pages] of Object.entries(registry.pages ?? {})) {
  const routeDir = path.join(root, "dist", type);
  const builtSlugs = new Set(
    (await readdir(routeDir, { withFileTypes: true })).filter((entry) => entry.isDirectory()).map((entry) => entry.name),
  );
  const registeredSlugs = new Set(Object.keys(pages));

  for (const slug of builtSlugs) {
    if (!registeredSlugs.has(slug)) issues.push(`Missing registry entry: ${type}/${slug}`);
  }
  for (const slug of registeredSlugs) {
    if (!builtSlugs.has(slug)) issues.push(`Registry entry has no built route: ${type}/${slug}`);
  }

  for (const [slug, dates] of Object.entries(pages)) {
    const { publishDate, modifiedDate } = dates;
    const route = `${type}/${slug}`;
    expectedRoutes.add(route);

    if (!datePattern.test(publishDate) || !datePattern.test(modifiedDate)) {
      issues.push(`Invalid date format: ${route}`);
      continue;
    }

    if (publishDate > modifiedDate) issues.push(`publishDate after modifiedDate: ${route}`);
    if (publishDate > today || modifiedDate > today) issues.push(`Future date: ${route}`);
    if (publishDate === modifiedDate) sameDateCount += 1;

    const html = await readFile(path.join(root, "dist", type, slug, "index.html"), "utf8");
    const visibleDateCount = (html.match(new RegExp(`<time datetime="${modifiedDate}"`, "g")) ?? []).length;
    const requiredVisibleDates = type === "reviews" ? 2 : 1;
    if (visibleDateCount < requiredVisibleDates) {
      issues.push(`Visible modified date mismatch: ${route}`);
    }
    if (!html.includes(`"datePublished":"${publishDate}"`)) {
      issues.push(`Schema publishDate mismatch: ${route}`);
    }
    if (!html.includes(`"dateModified":"${modifiedDate}"`)) {
      issues.push(`Schema modifiedDate mismatch: ${route}`);
    }

    const url = `https://smartpetguide.net/${type}/${slug}/`;
    const expectedLastmod = `${modifiedDate}T00:00:00.000Z`;
    if (sitemapEntries.get(url) !== expectedLastmod) {
      issues.push(`Sitemap lastmod mismatch: ${route}`);
    }
  }
}

const datedSitemapEntries = [...sitemapEntries.values()].filter(Boolean).length;
if (expectedRoutes.size !== 100) issues.push(`Expected 100 registered content routes, found ${expectedRoutes.size}`);
if (sitemapEntries.size !== 113) issues.push(`Expected 113 sitemap URLs, found ${sitemapEntries.size}`);
if (datedSitemapEntries !== expectedRoutes.size) {
  issues.push(`Expected ${expectedRoutes.size} dated sitemap URLs, found ${datedSitemapEntries}`);
}

if (issues.length) {
  console.error(issues.join("\n"));
  process.exit(1);
}

console.log(
  `Date validation passed: ${expectedRoutes.size} content pages, ${sameDateCount} conservative modified dates, ` +
    `${sitemapEntries.size} sitemap URLs (${datedSitemapEntries} with lastmod).`,
);
