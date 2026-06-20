"""R6b — 2 pins for Week 6 Tuesday: Deep Clean + Feeder Worth It"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE = r"C:\Users\Administrator\smartpetguide\pins"
IMG_DIR = os.path.join(BASE, "images")
OUT_DIR = os.path.join(BASE, "pins_with_text")
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1000, 1500
FOREST = (26, 60, 52)
HONEY = (212, 145, 75)
CREAM = (245, 240, 235)
WHITE = (255, 255, 255)

FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
FONT_REG = "C:/Windows/Fonts/arial.ttf"

def get_font(size, bold=True):
    try: return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except: return ImageFont.load_default()

PINS = [
    {
        "id": "pin57", "img": "litter-robot-4.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Deep Clean Your\nSelf-Cleaning Litter Box",
        "badge": "Step-by-Step Guide",
        "tags": ["Every 2-3 Months", "Rotating Globe & Rake", "5 Common Mistakes", "No Bleach Needed"],
        "cta": "Read the Guide",
    },
    {
        "id": "pin58", "img": "wopet-feeder.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Are Automatic Feeders\nWorth It for One Cat?",
        "badge": "Honest 2026 Guide",
        "tags": ["Single Cat Math", "When It Pays Off", "When to Skip It", "Best $89 Pick"],
        "cta": "Read the Guide",
    },
]

for pin in PINS:
    canvas = Image.new("RGBA", (W, H), CREAM + (255,))
    draw = ImageDraw.Draw(canvas)

    # Header bar
    draw.rectangle([(0, 0), (W, 170)], fill=FOREST + (255,))
    draw.text((40, 32), pin["brand"], fill=WHITE + (200,), font=get_font(22, False))

    title_lines = pin["title"].split("\n")
    font_title = get_font(42, True)
    y = 64
    for line in title_lines:
        draw.text((40, y), line, fill=WHITE, font=font_title)
        y += 48

    badge_text = pin["badge"]
    font_badge = get_font(20, True)
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bbox[2] - bbox[0] + 32, bbox[3] - bbox[1] + 12
    draw.rounded_rectangle([(40, y + 6), (40 + bw, y + 6 + bh)], radius=16, fill=HONEY + (255,))
    draw.text((40 + 16, y + 12), badge_text, fill=WHITE, font=font_badge)

    # Image area
    img_margin = 30
    img_top = 200
    img_bottom = 1150
    img_w = W - 2 * img_margin
    img_h = img_bottom - img_top

    card = Image.new("RGBA", (img_w, img_h), WHITE + (255,))
    canvas.paste(card, (img_margin, img_top), card)

    img_path = os.path.join(IMG_DIR, pin["img"])
    if os.path.exists(img_path):
        photo = Image.open(img_path).convert("RGBA")
        ratio = min((img_w - 40) / photo.width, (img_h - 40) / photo.height)
        new_w, new_h = int(photo.width * ratio), int(photo.height * ratio)
        photo = photo.resize((new_w, new_h), Image.LANCZOS)
        px = img_margin + (img_w - new_w) // 2
        py = img_top + (img_h - new_h) // 2
        canvas.paste(photo, (px, py), photo)

    # Tags
    tag_y = img_bottom + 20
    font_tag = get_font(20, True)
    x_pos = img_margin
    for tag in pin["tags"]:
        bbox = draw.textbbox((0, 0), tag, font=font_tag)
        tw, th = bbox[2] - bbox[0] + 24, bbox[3] - bbox[1] + 10
        if x_pos + tw > W - img_margin:
            break
        draw.rounded_rectangle([(x_pos, tag_y), (x_pos + tw, tag_y + th)], radius=14, fill=WHITE + (255,), outline=FOREST + (255,), width=2)
        draw.text((x_pos + 12, tag_y + 5), tag, fill=FOREST + (255,), font=font_tag)
        x_pos += tw + 10

    # CTA
    cta = pin["cta"] + " >"
    font_cta = get_font(26, True)
    bbox = draw.textbbox((0, 0), cta, font=font_cta)
    cw, ch = bbox[2] - bbox[0] + 80, bbox[3] - bbox[1] + 28
    cx = (W - cw) // 2
    cy = 1380
    draw.rounded_rectangle([(cx, cy), (cx + cw, cy + ch)], radius=22, fill=FOREST + (255,))
    draw.text((cx + 40, cy + 14), cta, fill=WHITE, font=font_cta)

    # Bottom bar
    draw.rectangle([(0, H - 8), (W, H)], fill=HONEY + (255,))

    out_path = os.path.join(OUT_DIR, f"{pin['id']}.jpg")
    canvas.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"  OK {pin['id']}.jpg")

print(f"\nDone! {len(PINS)} pins saved to pins/pins_with_text/")
