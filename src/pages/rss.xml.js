import rss from "@astrojs/rss";

const posts = [
  {
    title: "5 Best Self-Cleaning Litter Boxes of 2026",
    description: "We tested the top automatic litter boxes to find the best for odor control, multi-cat homes, and budget.",
    link: "/best/self-cleaning-litter-boxes/",
    pubDate: new Date("2026-05-20"),
  },
  {
    title: "5 Best Automatic Cat Feeders of 2026",
    description: "Compare the best automatic pet feeders with app control, cameras, and portion management.",
    link: "/best/automatic-cat-feeders/",
    pubDate: new Date("2026-05-19"),
  },
  {
    title: "Litter-Robot 4 Review — Is It Worth $699?",
    description: "In-depth review after months of testing. Odor control, app experience, multi-cat performance.",
    link: "/reviews/litter-robot-4-review/",
    pubDate: new Date("2026-05-18"),
  },
  {
    title: "Automatic Pet Feeder Buying Guide",
    description: "Everything you need to know before buying an automatic pet feeder.",
    link: "/guides/automatic-feeder-buying-guide/",
    pubDate: new Date("2026-05-17"),
  },
  {
    title: "Litter-Robot 4 vs Leo's Loo Too — Which Wins?",
    description: "Head-to-head comparison of the two most popular self-cleaning litter boxes.",
    link: "/compare/litter-robot-4-vs-leos-loo-too/",
    pubDate: new Date("2026-05-16"),
  },
  {
    title: "Best Feeder for French Bulldogs",
    description: "French Bulldogs have unique feeding needs — we've picked the best feeders for this beloved breed.",
    link: "/breed/best-feeder-for-french-bulldog/",
    pubDate: new Date("2026-05-15"),
  },
];

export async function GET() {
  return rss({
    title: "SmartPetGuide",
    description: "Expert reviews and comparisons of smart pet devices",
    site: "https://smartpetguide.com",
    items: posts.map((post) => ({
      ...post,
      pubDate: post.pubDate,
    })),
  });
}
