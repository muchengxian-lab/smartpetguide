/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        // Forest + Honey editorial palette
        cream:    { DEFAULT: "#FDF9F3", light: "#FFFDF9", dark: "#F5EFE6" },
        forest:   { DEFAULT: "#1A3C34", light: "#2A5C4F", dark: "#0F2620" },
        honey:    { DEFAULT: "#D4914B", light: "#E8B87A", dark: "#B8722E" },
        sage:     { DEFAULT: "#E9EFE8", light: "#F4F7F3", dark: "#C5D3C2" },
        bark:     { DEFAULT: "#2D2418", light: "#5C4E3A", muted: "#8B7E74" },
        rose:     { DEFAULT: "#E8D5D0", light: "#F5EBE8", dark: "#D4B8B0" },
      },
      fontFamily: {
        display:  ['"Fraunces"', "Georgia", "serif"],
        body:     ['"Atkinson Hyperlegible"', "system-ui", "sans-serif"],
        accent:   ['"Fraunces"', "Georgia", "serif"],
      },
    },
  },
  plugins: [],
};
