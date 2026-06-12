"""
R5 Pin 图生成器 — 8 张新 Pin（5 新内容 + 3 变体）
设计规范：Forest #1A3C34 + Honey #D4914B + Cream #F5F0EB
"""
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
DARK = (30, 30, 30)

FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
FONT_REG = "C:/Windows/Fonts/arial.ttf"
FONT_LIGHT = "C:/Windows/Fonts/calibri.ttf"

def get_font(size, bold=True):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except:
        return ImageFont.load_default()

# ── 8 Pin 定义 ──
PINS = [
    # ── 新内容 Pin ──
    {
        "id": "pin46", "img": "pioneer-pet-raindrop.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Fountain Filter\nReplacement Guide",
        "badge": "Save $40/Year",
        "tags": ["Charcoal vs Ion-Exchange", "When to Replace", "Generic vs Branded", "3-Year Cost"],
        "cta": "Read the Guide",
    },
    {
        "id": "pin47", "img": "litter-robot-4.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Introduce Your Cat to\na Self-Cleaning Box",
        "badge": "Step-by-Step Guide",
        "tags": ["First-Time Setup", "Transition Method", "Troubleshooting Tips", "Best Box for Beginners"],
        "cta": "Read the Guide",
    },
    {
        "id": "pin48", "img": "litter-robot-4.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "How We Research\n& Evaluate",
        "badge": "Our Methodology",
        "tags": ["7-Point Evaluation", "500+ Reviews Analyzed", "No Sponsored Picks", "Updated Quarterly"],
        "cta": "See Our Process",
    },
    {
        "id": "pin49", "img": "pioneer-pet-raindrop.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Products We\nDon't Recommend",
        "badge": "And Why",
        "tags": ["Discontinued Models", "Poor Performers", "Better Alternatives", "Honest Reasons"],
        "cta": "See the List",
    },
    {
        "id": "pin50", "img": "wopet-feeder.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Feeder Portion\nSize Guide",
        "badge": "Feed with Confidence",
        "tags": ["Grams by Weight", "Kibble Calculator", "Weight Loss Portions", "Accuracy Test"],
        "cta": "Read the Guide",
    },
    # ── 变体 Pin ──
    {
        "id": "pin51", "img": "nofee-gps-tracker.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "3 GPS Trackers\nWith Zero Monthly Fees",
        "badge": "Save $100+/Year",
        "tags": ["No Subscription Ever", "3.5-Mile Range", "One-Time Purchase", "Verified Owner Picks"],
        "cta": "Compare Trackers",
    },
    {
        "id": "pin52", "img": "pioneer-pet-raindrop.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Your Cat's Plastic\nFountain Could Be\nMaking Them Sick",
        "badge": "Switch to Steel",
        "tags": ["No Biofilm Buildup", "Dishwasher-Safe", "No Chin Acne", "Lasts 5+ Years"],
        "cta": "See Steel Picks",
    },
    {
        "id": "pin53", "img": "xpai-4k-camera.jpg",
        "brand": "SMARTPETGUIDE",
        "title": "Stop Paying $10/Month\nJust to Watch\nYour Dog Sleep",
        "badge": "No Fees, No Catch",
        "tags": ["4K for $43", "Built-in 64GB Storage", "360° Pan & Tilt", "Zero Cloud Costs"],
        "cta": "See No-Fee Picks",
    },
]

def draw_rounded_rect(draw, xy, radius, fill):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)

def create_pin(pin):
    canvas = Image.new("RGBA", (W, H), CREAM + (255,))
    draw = ImageDraw.Draw(canvas)

    # ── Header bar ──
    draw.rectangle([(0, 0), (W, 170)], fill=FOREST + (255,))

    font_brand = get_font(22, bold=False)
    draw.text((40, 32), pin["brand"], fill=WHITE + (200,), font=font_brand)

    # Title (2-3 lines)
    title_lines = pin["title"].split("\n")
    font_title = get_font(42, bold=True)
    y = 64
    for line in title_lines:
        draw.text((40, y), line, fill=WHITE, font=font_title)
        y += 48

    # Badge
    badge_text = pin["badge"]
    font_badge = get_font(20, bold=True)
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bbox[2] - bbox[0] + 32, bbox[3] - bbox[1] + 12
    draw.rounded_rectangle([(40, y + 6), (40 + bw, y + 6 + bh)], radius=16, fill=HONEY + (255,))
    draw.text((40 + 16, y + 12), badge_text, fill=WHITE, font=font_badge)

    # ── Image area ──
    img_margin = 30
    img_top = 200
    img_bottom = 1150
    img_w = W - 2 * img_margin
    img_h = img_bottom - img_top

    if pin.get("img") and pin.get("icon") is None:
        img_path = os.path.join(IMG_DIR, pin["img"])
        if os.path.exists(img_path):
            photo = Image.open(img_path).convert("RGBA")
            # Scale to fit
            ratio = min(img_w / photo.width, img_h / photo.height)
            new_w, new_h = int(photo.width * ratio), int(photo.height * ratio)
            photo = photo.resize((new_w, new_h), Image.LANCZOS)
            # Center in image area
            px = img_margin + (img_w - new_w) // 2
            py = img_top + (img_h - new_h) // 2
            canvas.paste(photo, (px, py), photo)

    # White card background for image area
    card = Image.new("RGBA", (img_w, img_h), WHITE + (255,))
    card_draw = ImageDraw.Draw(card)
    canvas.paste(card, (img_margin, img_top), card)

    if pin.get("img") and pin.get("icon") is None:
        img_path = os.path.join(IMG_DIR, pin["img"])
        if os.path.exists(img_path):
            photo = Image.open(img_path).convert("RGBA")
            ratio = min((img_w - 40) / photo.width, (img_h - 40) / photo.height)
            new_w, new_h = int(photo.width * ratio), int(photo.height * ratio)
            photo = photo.resize((new_w, new_h), Image.LANCZOS)
            px = img_margin + (img_w - new_w) // 2
            py = img_top + (img_h - new_h) // 2
            canvas.paste(photo, (px, py), photo)
    elif pin.get("icon"):
        # Icon-based design
        font_icon = get_font(100, bold=True)
        font_label = get_font(36, bold=True)
        icon_text = pin["icon"]
        icon_bbox = draw.textbbox((0, 0), icon_text, font=font_icon)
        iw = icon_bbox[2] - icon_bbox[0]
        draw.text((W//2 - iw//2, img_top + img_h//2 - 80), icon_text, fill=FOREST + (255,), font=font_icon)

        label = "How We Research" if "Research" in pin["title"] else "Products We Skip"
        if "Don't" in pin["title"]:
            label = "Products We Skip"
        label_bbox = draw.textbbox((0, 0), label, font=font_label)
        lw = label_bbox[2] - label_bbox[0]
        draw.text((W//2 - lw//2, img_top + img_h//2 + 20), label, fill=FOREST + (180,), font=font_label)

    # ── Tags ──
    tags = pin["tags"]
    tag_y = img_bottom + 20
    font_tag = get_font(20, bold=True)
    tag_positions = []
    x_pos = img_margin
    for tag in tags:
        bbox = draw.textbbox((0, 0), tag, font=font_tag)
        tw, th = bbox[2] - bbox[0] + 24, bbox[3] - bbox[1] + 10
        if x_pos + tw > W - img_margin:
            break
        draw.rounded_rectangle([(x_pos, tag_y), (x_pos + tw, tag_y + th)], radius=14, fill=WHITE + (255,), outline=FOREST + (255,), width=2)
        draw.text((x_pos + 12, tag_y + 5), tag, fill=FOREST + (255,), font=font_tag)
        x_pos += tw + 10

    # ── CTA button ──
    cta = pin["cta"] + " >"
    font_cta = get_font(26, bold=True)
    bbox = draw.textbbox((0, 0), cta, font=font_cta)
    cw, ch = bbox[2] - bbox[0] + 80, bbox[3] - bbox[1] + 28
    cx = (W - cw) // 2
    cy = 1380
    draw.rounded_rectangle([(cx, cy), (cx + cw, cy + ch)], radius=22, fill=FOREST + (255,))
    draw.text((cx + 40, cy + 14), cta, fill=WHITE, font=font_cta)

    # ── Bottom bar ──
    draw.rectangle([(0, H - 8), (W, H)], fill=HONEY + (255,))

    # Save
    out_path = os.path.join(OUT_DIR, f"{pin['id']}.jpg")
    canvas.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"  OK {pin['id']}.jpg")

# ── Run ──
print("Generating R5 pins...")
for pin in PINS:
    create_pin(pin)
print(f"\nDone! {len(PINS)} pins saved to pins/pins_with_text/")
