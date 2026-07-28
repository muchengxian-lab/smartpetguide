import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";

const reviewsDir = join(process.cwd(), "dist", "reviews");
const entries = await readdir(reviewsDir, { withFileTypes: true });
const reviewPages = entries.filter((entry) => entry.isDirectory());

if (reviewPages.length === 0) {
  throw new Error("No generated review pages found under dist/reviews. Run the build first.");
}

const forbiddenTypes = new Set(["Review", "Product", "Offer", "AggregateRating"]);
const failures = [];

function collectTypes(value, types = new Set()) {
  if (Array.isArray(value)) {
    for (const item of value) collectTypes(item, types);
    return types;
  }

  if (!value || typeof value !== "object") return types;

  const rawType = value["@type"];
  if (Array.isArray(rawType)) rawType.forEach((type) => types.add(type));
  else if (typeof rawType === "string") types.add(rawType);

  for (const child of Object.values(value)) collectTypes(child, types);
  return types;
}

for (const entry of reviewPages) {
  const html = await readFile(join(reviewsDir, entry.name, "index.html"), "utf8");
  const jsonLdBlocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
  const types = new Set();

  for (const [, rawJson] of jsonLdBlocks) {
    try {
      collectTypes(JSON.parse(rawJson), types);
    } catch (error) {
      failures.push(`${entry.name}: invalid JSON-LD (${error.message})`);
    }
  }

  const forbidden = [...types].filter((type) => forbiddenTypes.has(type));
  if (forbidden.length > 0) {
    failures.push(`${entry.name}: forbidden third-party rating/offer schema types: ${forbidden.join(", ")}`);
  }
  if (!types.has("Article")) failures.push(`${entry.name}: missing Article schema`);
  if (!types.has("BreadcrumbList")) failures.push(`${entry.name}: missing BreadcrumbList schema`);
  if (!html.includes("Amazon customer rating")) failures.push(`${entry.name}: missing visible Amazon rating attribution`);
}

if (failures.length > 0) {
  console.error("Review schema validation failed:\n" + failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log(
  `Review schema validation passed: ${reviewPages.length} pages retain Article/Breadcrumb markup, ` +
  "attribute visible ratings to Amazon, and emit no Review/Product/Offer/AggregateRating markup."
);
