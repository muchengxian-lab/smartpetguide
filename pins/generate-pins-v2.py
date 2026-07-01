"""Pin template v2 — larger product, no brand bar, card shadow, bolder title"""
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
SHADOW = (200, 195, 190)  # subtle shadow for card

FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
FONT_REG = "C:/Windows/Fonts/arial.ttf"

def get_font(size, bold=True):
    try: return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except: return ImageFont.load_default()

PINS = [
    # --- R6 (6/13-15) ---
    {
        "id": "pin59", "img": "petkit-eversweet.jpg",
        "title": "Best Quiet Pet Fountains\nfor Apartments",
        "badge": "Silent Picks for 2026",
        "tags": ["Under 35dB Only", "Studio & 1-Bedroom", "Wireless Options", "Steel vs Plastic"],
        "cta": "See the Quiet Picks",
    },
    {
        "id": "pin60", "img": "petlibro-granary.jpg",
        "title": "Automatic Feeder\nMaintenance Checklist",
        "badge": "Daily, Weekly, Monthly",
        "tags": ["5-Min Weekly Routine", "Prevent Motor Failure", "Hopper Deep Clean", "Battery Backup Test"],
        "cta": "Get the Checklist",
    },
    # --- R7 (6/18) ---
    {
        "id": "pin61", "img": "amazon-basics-litter-box.jpg",
        "title": "LR5 vs Amazon Basics\n3-Year Cost Breakdown",
        "badge": "$799 vs $209 — Full Cost Comparison",
        "tags": ["Litter-Robot 5 vs Amazon", "Filters & Litter & Spray", "$1,049 vs $437 Over 3 Years", "WasteID Health Tracking"],
        "cta": "See the Full Cost Math",
    },
    {
        "id": "pin62", "img": "petkit-eversweet.jpg",
        "title": "Best Quiet Pet Fountains\nfor Apartments (2026)",
        "badge": "Under 35dB Only",
        "tags": ["PETKIT Eversweet 30dB", "YEAPAW Pumpless 0dB", "Pioneer Pet Classic", "Homerunpet Wireless"],
        "cta": "Find Your Quiet Fountain",
    },
    # --- R7 (6/19) ---
    {
        "id": "pin63", "img": "litter-robot-4.jpg",
        "title": "How to Deep Clean\nYour Self-Cleaning Litter Box",
        "badge": "Step-by-Step 2026 Guide",
        "tags": ["Rotating Globe & Crystal", "Monthly Deep Clean", "Waste Drawer Biofilm", "No Bleach or Ammonia"],
        "cta": "Get the Cleaning Guide",
    },
    {
        "id": "pin64", "img": "wopet-feeder.jpg",
        "title": "Are Automatic Feeders\nWorth It for One Cat?",
        "badge": "Honest 2026 Guide",
        "tags": ["Single-Cat Home Analysis", "WOPET $89 vs Petlibro $139", "Travel Without a Sitter", "Portion Control for Weight"],
        "cta": "See If It's Worth It",
    },
    {
        "id": "pin65", "img": "petlibro-granary.jpg",
        "title": "Automatic Feeder\nMaintenance Checklist",
        "badge": "Daily, Weekly, Monthly",
        "tags": ["5-Min Weekly Routine", "Prevent Motor Failure", "Hopper Deep Clean", "Battery Backup Test"],
        "cta": "Get the Checklist",
    },
    # --- R8 Week 7 (6/23-6/27) ---
    {
        "id": "pin66", "img": "xpai-4k-camera.jpg",
        "title": "5 Best No-Subscription\nPet Cameras (2026)",
        "badge": "Zero Monthly Fees",
        "tags": ["eufy 2K Auto-Tracking", "xpai 4K $43", "WOPET Treat Cam", "No Cloud Storage Needed"],
        "cta": "See the Subscription-Free Picks",
    },
    {
        "id": "pin67", "img": "petlibro-granary.jpg",
        "title": "Smart Home for Pets:\nAlexa & Google Home Guide",
        "badge": "Voice-Controlled Pet Tech",
        "tags": ["Alexa-Compatible Feeders", "Google Home Fountains", "Smart Plugs & Cameras", "Hands-Free Pet Care"],
        "cta": "Set Up Your Smart Pet Home",
    },
    {
        "id": "pin68", "img": "petkit-eversweet.jpg",
        "title": "PETKIT Eversweet vs Catit PIXI\nWhich Smart Fountain Wins?",
        "badge": "Head-to-Head Comparison",
        "tags": ["PETKIT $59 30dB Silent", "Catit PIXI $79 Intake Track", "App vs App Feature Battle", "Filter Cost 3-Year Math"],
        "cta": "See the Full Comparison",
    },
    {
        "id": "pin69", "img": "yeapaw-steel-fountain.jpg",
        "title": "Best Stainless Steel Cat\nWater Fountains (2026)",
        "badge": "Hygienic & Durable Picks",
        "tags": ["YEAPAW Pumpless $93", "Pioneer Pet Classic $39", "KittySpout Dishwasher-Safe", "No Plastic Contact"],
        "cta": "Find Your Steel Fountain",
    },
    {
        "id": "pin70", "img": "litter-robot-4.jpg",
        "title": "Best Automatic Litter Box\nfor Large Cats — Maine Coon Guide",
        "badge": "Big Breed Approved",
        "tags": ["LR4 Extra-Large Globe", "CATLINK 22-inch Interior", "Meowant 30lb Capacity", "Ragdoll & Maine Coon Safe"],
        "cta": "See Big Cat Options",
    },
    {
        "id": "pin71", "img": "tractive-gps.jpg",
        "title": "Traveling with Pets?\nSmart Tech You Actually Need",
        "badge": "Road Trip & Flight Essentials",
        "tags": ["GPS Trackers for Travel", "Portable Pet Cameras", "Car Safety Devices", "Emergency Power Backup"],
        "cta": "Pack Your Pet Travel Kit",
    },
    {
        "id": "pin72", "img": "litter-robot-4.jpg",
        "title": "Best Automatic Litter Box\nfor Multiple Cats (2026)",
        "badge": "Multi-Cat Household Guide",
        "tags": ["LR4 vs CS106 vs CATLINK", "Per-Cat Weight Tracking", "13L+ Waste Drawers", "3-4 Cat Capacity"],
        "cta": "Compare Multi-Cat Boxes",
    },
    # --- R9 出站实验 Pin (6/23-) ---
    {
        "id": "pin77_exp5", "img": "wopet-feeder.jpg",
        "title": "$89 vs $139 vs $249 —\nWhat You Get at Each Tier",
        "badge": "Budget to Premium: Real Value Analysis",
        "tags": ["WOPET $89 Basics-Only", "Petlibro $139 1080p Cam", "PetSafe $249 Smart Feed", "Sweet Spot: $139"],
        "cta": "See the Price Breakdown",
    },
    {
        "id": "pin78_exp6", "img": "elspet-pro.jpg",
        "title": "Single Cat? Small Apartment?\nYour Litter Box Is Too Big",
        "badge": "Space-Optimized vs Overkill — Size Comparison",
        "tags": ["CATLINK 22\" Needs 3ft²", "Elspet Compact 17\"", "1 Cat ≠ Biggest Box", "Measure Before You Buy"],
        "cta": "Find Your Right Size",
    },
    # --- R9 出站实验 Pin (6/23-) ---
    {
        "id": "pin73_exp1", "img": "eufy-pet-cam.jpg",
        "title": "5 Pet Cameras With\nZero Monthly Fees (2026)",
        "badge": "No Subscription Required — One-Time Purchase",
        "tags": ["eufy Security #1 Pick", "xpai 4K Budget Champ", "Honeytour Robot Cam", "Save $100+/Year vs Furbo"],
        "cta": "See All No-Fee Cameras",
    },
    {
        "id": "pin74_exp2", "img": "furbo-360.jpg",
        "title": "The Hidden $500 Cost of\nYour Pet Camera (2026)",
        "badge": "Subscription Fees Add Up — See the Math",
        "tags": ["Furbo $7.99/mo = $288/3yr", "vs eufy $0/mo Forever", "3-Year TCO Comparison", "$0 Sub Picks Inside"],
        "cta": "See the True 3-Year Cost",
    },
    {
        "id": "pin75_exp3", "img": "pioneer-pet-raindrop.jpg",
        "title": "Is Your Cat's Fountain\nMaking Them Sick?",
        "badge": "Plastic vs Stainless Steel — The Hidden Risk",
        "tags": ["Plastic Biofilm Warning", "18,500+ Owners Switched", "Dishwasher-Safe Picks", "From $39 — Health Upgrade"],
        "cta": "See Steel Fountain Picks",
    },
    {
        "id": "pin76_exp4", "img": "litter-robot-4.jpg",
        "title": "3 Cats, 1 Litter Box?\nYour Setup Might Be Too Small",
        "badge": "Multi-Cat Homes Need Bigger Solutions",
        "tags": ["LR5 Fits 5 Cats", "CATLINK 13L Drawer", "$349 Budget Pick", "Drawer Size Comparison"],
        "cta": "Compare Multi-Cat Boxes",
    },
    # --- R10 出站实验 Pin (6/30-) ---
    {
        "id": "pin79_exp7", "img": "petlibro-granary.jpg",
        "title": "WiFi Keeps Dropping?\n6 Fixes That Actually Work",
        "badge": "Reliability Guide — Fix It Yourself",
        "tags": ["2.4GHz Only — Check WiFi", "Router Channel Switching", "Don't Return It Yet", "Petlibro, WOPET, PETKIT"],
        "cta": "See the 6 Fixes",
    },
    {
        "id": "pin80_exp8", "img": "litter-robot-4.jpg",
        "title": "Cat Litter Everywhere?\n5 Robot Vacuums That Handle It",
        "badge": "Litter-Tested by Real Cat Owners",
        "tags": ["Roomba j7+ vs Roborock Q5", "Clay & Crystal Litter Test", "Auto-Empty Dock Picks", "From $179 to $499"],
        "cta": "See the Litter-Ready Vacuums",
    },
]

for pin in PINS:
    canvas = Image.new("RGBA", (W, H), CREAM + (255,))
    draw = ImageDraw.Draw(canvas)

    # === Header bar (dynamic height based on title lines) ===
    title_lines = pin["title"].split("\n")
    font_title = get_font(52, True)
    line_h = 56  # line spacing
    title_y = 14
    for line in title_lines:
        draw.text((40, title_y), line, fill=WHITE, font=font_title)
        title_y += line_h

    # Badge below title
    badge_text = pin["badge"]
    font_badge = get_font(20, True)
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bbox[2] - bbox[0] + 28, bbox[3] - bbox[1] + 12
    bx = 40
    by = title_y + 6
    draw.rounded_rectangle([(bx, by), (bx + bw, by + bh)], radius=14, fill=HONEY + (255,))
    draw.text((bx + 14, by + 6), badge_text, fill=WHITE, font=font_badge)

    # Header covers: title + badge + 16px bottom padding
    header_h = by + bh + 16
    draw.rectangle([(0, 0), (W, header_h)], fill=FOREST + (255,))
    # Redraw title + badge on top (since they were drawn before the bg)
    title_y = 14
    for line in title_lines:
        draw.text((40, title_y), line, fill=WHITE, font=font_title)
        title_y += line_h
    draw.rounded_rectangle([(bx, by), (bx + bw, by + bh)], radius=14, fill=HONEY + (255,))
    draw.text((bx + 14, by + 6), badge_text, fill=WHITE, font=font_badge)

    # === Product image card (shadow + white card) ===
    card_margin = 30
    card_top = header_h + 30
    card_bottom = 1130
    card_w = W - 2 * card_margin
    card_h = card_bottom - card_top

    # Shadow card (offset 6px down-right)
    shadow = Image.new("RGBA", (card_w, card_h), SHADOW + (255,))
    canvas.paste(shadow, (card_margin + 6, card_top + 6), shadow)

    # White card
    card = Image.new("RGBA", (card_w, card_h), WHITE + (255,))
    canvas.paste(card, (card_margin, card_top), card)

    # Product image — bigger, less padding (20px vs old 40px)
    img_pad = 20
    img_path = os.path.join(IMG_DIR, pin["img"])
    if os.path.exists(img_path):
        photo = Image.open(img_path).convert("RGBA")
        avail_w = card_w - 2 * img_pad
        avail_h = card_h - 2 * img_pad
        ratio = min(avail_w / photo.width, avail_h / photo.height)
        new_w, new_h = int(photo.width * ratio), int(photo.height * ratio)
        photo = photo.resize((new_w, new_h), Image.LANCZOS)
        px = card_margin + (card_w - new_w) // 2
        py = card_top + (card_h - new_h) // 2
        canvas.paste(photo, (px, py), photo)

    # === Tags ===
    tag_y = card_bottom + 18
    font_tag = get_font(20, True)
    x_pos = card_margin
    for tag in pin["tags"]:
        tbbox = draw.textbbox((0, 0), tag, font=font_tag)
        tw, th = tbbox[2] - tbbox[0] + 24, tbbox[3] - tbbox[1] + 10
        if x_pos + tw > W - card_margin:
            break
        draw.rounded_rectangle(
            [(x_pos, tag_y), (x_pos + tw, tag_y + th)],
            radius=12, fill=WHITE + (255,), outline=FOREST + (255,), width=2
        )
        draw.text((x_pos + 12, tag_y + 5), tag, fill=FOREST + (255,), font=font_tag)
        x_pos += tw + 10

    # === CTA button ===
    cta_text = pin["cta"] + " >"
    font_cta = get_font(26, True)
    cbbox = draw.textbbox((0, 0), cta_text, font=font_cta)
    cw, ch = cbbox[2] - cbbox[0] + 80, cbbox[3] - cbbox[1] + 28
    cx = (W - cw) // 2
    cy = 1380
    draw.rounded_rectangle([(cx, cy), (cx + cw, cy + ch)], radius=22, fill=FOREST + (255,))
    draw.text((cx + 40, cy + 14), cta_text, fill=WHITE, font=font_cta)

    # === Bottom accent bar ===
    draw.rectangle([(0, H - 8), (W, H)], fill=HONEY + (255,))

    out_path = os.path.join(OUT_DIR, f"{pin['id']}.jpg")
    canvas.convert("RGB").save(out_path, "JPEG", quality=95)
    print(f"  OK {pin['id']}.jpg")

print(f"\nDone! {len(PINS)} pins saved to pins/pins_with_text/")
