"""
批量给产品图添加 Pinterest 文字叠加
输出: 1000x1500 Pin 图，带半透明黑底 + 白色文字
"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE = r"C:\Users\Administrator\smartpetguide\pins"
INPUT_DIR = os.path.join(BASE, "images")
OUTPUT_DIR = os.path.join(BASE, "pins_with_text")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 6 个 Pin 的文字配置
PINS = [
    {
        "file": "petkit-fresh-element.jpg",
        "line1": "Keeps Kibble Fresh",
        "line2": "3× Longer",
        "line3": "4.4★ · 6,100+ Reviews",
        "line4": "$129",
    },
    {
        "file": "petkit-eversweet.jpg",
        "line1": "30dB Whisper-Quiet",
        "line2": "Cat Fountain",
        "line3": "4.4★ · 7,200+ Reviews",
        "line4": "$59",
    },
    {
        "file": "petsafe-scoopfree.jpg",
        "line1": "Lowest Maintenance",
        "line2": "Auto Litter Box",
        "line3": "Just Swap Tray Every 2-4 Weeks",
        "line4": "$299",
    },
    {
        "file": "leos-loo-too.jpg",
        "line1": "UV Sterilization",
        "line2": "Kills Odor Bacteria",
        "line3": "4.3★ · $250 Less Than LR4",
        "line4": "$449",
    },
    {
        "file": "eufy-pet-cam.jpg",
        "line1": "NO Monthly Fee",
        "line2": "— Ever",
        "line3": "2K · 360° Auto-Tracking",
        "line4": "$129",
    },
    {
        "file": "catit-pixi.jpg",
        "line1": "Tracks How Much",
        "line2": "Your Cat Drinks",
        "line3": "3 Heights · App Connected",
        "line4": "$79",
    },
]

# 字体路径（Windows 系统自带字体）
FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"  # Arial Bold
FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"

CANVAS_SIZE = (1000, 1500)  # Pinterest 推荐 2:3

for pin in PINS:
    img_path = os.path.join(INPUT_DIR, pin["file"])
    if not os.path.exists(img_path):
        print(f"  SKIP: {img_path} not found")
        continue

    print(f"Processing: {pin['file']}")

    # 打开原图
    img = Image.open(img_path).convert("RGBA")

    # 缩放到画布宽度（保持比例）
    ratio = CANVAS_SIZE[0] / img.width
    new_h = int(img.height * ratio)
    img = img.resize((CANVAS_SIZE[0], new_h), Image.LANCZOS)

    # 创建 1000×1500 画布，居中放置图片
    canvas = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    y_offset = (CANVAS_SIZE[1] - new_h) // 2
    canvas.paste(img, (0, y_offset))

    draw = ImageDraw.Draw(canvas)

    # 文字位置（底部区域）
    text_area_top = 1100
    text_area_h = 340
    overlay_margin = 30

    # 半透明黑底
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rounded_rectangle(
        [(overlay_margin, text_area_top), (CANVAS_SIZE[0] - overlay_margin, text_area_top + text_area_h)],
        radius=20,
        fill=(0, 0, 0, 180),  # 半透明黑
    )
    canvas = Image.alpha_composite(canvas, overlay)
    draw = ImageDraw.Draw(canvas)

    # 文字排版
    center_x = CANVAS_SIZE[0] // 2
    line1_y = text_area_top + 30
    line2_y = line1_y + 85
    line3_y = line2_y + 85
    line4_y = line3_y + 60

    try:
        font_large = ImageFont.truetype(FONT_BOLD, 80)
        font_medium = ImageFont.truetype(FONT_BOLD, 64)
        font_small = ImageFont.truetype(FONT_REGULAR, 36)
        font_price = ImageFont.truetype(FONT_BOLD, 52)
    except OSError:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_price = ImageFont.load_default()

    # Line 1 & 2: 主标题（大字）
    bbox1 = draw.textbbox((0, 0), pin["line1"], font=font_large)
    tw1 = bbox1[2] - bbox1[0]
    draw.text((center_x - tw1 // 2, line1_y), pin["line1"], fill=(255, 255, 255), font=font_large)

    bbox2 = draw.textbbox((0, 0), pin["line2"], font=font_medium)
    tw2 = bbox2[2] - bbox2[0]
    # 如果有 line2，合并为一行；否则跳过
    draw.text((center_x - tw2 // 2, line2_y), pin["line2"], fill=(255, 255, 255), font=font_medium)

    # Line 3: 评分/次要信息
    bbox3 = draw.textbbox((0, 0), pin["line3"], font=font_small)
    tw3 = bbox3[2] - bbox3[0]
    draw.text((center_x - tw3 // 2, line3_y), pin["line3"], fill=(220, 220, 220), font=font_small)

    # Line 4: 价格（突出显示，金色）
    bbox4 = draw.textbbox((0, 0), pin["line4"], font=font_price)
    tw4 = bbox4[2] - bbox4[0]
    draw.text((center_x - tw4 // 2, line4_y), pin["line4"], fill=(255, 215, 0), font=font_price)

    # 保存
    out_name = pin["file"].replace(".jpg", "-pinterest.jpg")
    out_path = os.path.join(OUTPUT_DIR, out_name)
    canvas_rgb = canvas.convert("RGB")
    canvas_rgb.save(out_path, "JPEG", quality=95)
    print(f"  → {out_path}")

print("\nDone! All 6 Pin images with text overlay saved to pins/pins_with_text/")
