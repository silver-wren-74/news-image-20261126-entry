#!/usr/bin/env python3
"""Draw the front page for 26 November 2026 and save it as entry.png.

Build-time helper only: the submitted program (main.py) just ships the
finished image. Run:  python3 gen_image.py   (writes ./entry.png)
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (22, 22, 22)
MUTED = (88, 84, 76)
NAVY = (16, 35, 63)
RED = (185, 28, 28)
RULE = (16, 35, 63)
CARD = (255, 255, 255)
EDGE = (198, 192, 178)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


F_SERIF_B = font("DejaVuSerif-Bold.ttf", 62)
F_DATE = font("DejaVuSans-Bold.ttf", 21)
F_KICK = font("DejaVuSans-Bold.ttf", 14)
F_LEAD_H = font("DejaVuSans-Bold.ttf", 34)
F_LEAD_B = font("DejaVuSans.ttf", 16)
F_PANEL_H = font("DejaVuSans-Bold.ttf", 21)
F_PANEL_B = font("DejaVuSans.ttf", 14)
F_TICK = font("DejaVuSans.ttf", 15)
F_TICK_B = font("DejaVuSans-Bold.ttf", 15)
F_FOOT = font("DejaVuSans.ttf", 13)
F_STAT = font("DejaVuSans-Bold.ttf", 30)
F_STAT_S = font("DejaVuSans-Bold.ttf", 14)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=1.35):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def flame(draw, cx, cy, s, color):
    """Small flame pictogram from two triangles and a circle."""
    draw.polygon(
        [(cx, cy - s), (cx + s * 0.62, cy + s * 0.45),
         (cx - s * 0.62, cy + s * 0.45)], fill=color)
    draw.ellipse([cx - s * 0.34, cy - s * 0.05, cx + s * 0.34, cy + s * 0.62],
                 fill=(255, 214, 90))


def rocket(draw, cx, cy, s, color):
    draw.polygon([(cx, cy - s), (cx + s * 0.45, cy + s * 0.2),
                  (cx - s * 0.45, cy + s * 0.2)], fill=color)
    draw.rectangle([cx - s * 0.45, cy + s * 0.2, cx + s * 0.45, cy + s * 0.62],
                   fill=color)
    draw.polygon([(cx - s * 0.2, cy + s * 0.62), (cx, cy + s),
                  (cx + s * 0.2, cy + s * 0.62)], fill=(255, 170, 60))


def bars(draw, cx, cy, s, color):
    for i, h in enumerate((0.5, 0.85, 0.65, 1.0)):
        x0 = cx - s + i * s * 0.55
        draw.rectangle([x0, cy + s * 0.5 - h * s, x0 + s * 0.38,
                        cy + s * 0.5], fill=color)


def dove(draw, cx, cy, s, color):
    draw.ellipse([cx - s * 0.7, cy - s * 0.35, cx + s * 0.7, cy + s * 0.35],
                 fill=color)
    draw.polygon([(cx + s * 0.5, cy - s * 0.1), (cx + s * 1.05, cy - s * 0.45),
                  (cx + s * 0.95, cy + s * 0.15)], fill=color)
    draw.polygon([(cx - s * 0.2, cy - s * 0.3), (cx + s * 0.1, cy - s * 0.95),
                  (cx + s * 0.45, cy - s * 0.3)], fill=color)


def ball(draw, cx, cy, s, color):
    draw.ellipse([cx - s * 0.7, cy - s * 0.7, cx + s * 0.7, cy + s * 0.7],
                 fill=color)
    draw.arc([cx - s * 0.7, cy - s * 0.7, cx + s * 0.7, cy + s * 0.7],
             200, 340, fill=(255, 255, 255), width=3)


def tower(draw, cx, cy, s, color):
    draw.rectangle([cx - s * 0.28, cy - s, cx + s * 0.28, cy + s * 0.6],
                   fill=color)
    draw.rectangle([cx - s * 0.45, cy - s * 0.55, cx + s * 0.45, cy + s * 0.6],
                   fill=color)


def panel(draw, x, y, w, h, kicker, color, headline, body, icon):
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=EDGE, width=2)
    draw.rectangle([x, y, x + w, y + 8], fill=color)
    draw.text((x + 14, y + 18), kicker, font=F_KICK, fill=color)
    icon(draw, x + w - 28, y + 28, 11, color)
    hy = y + 44
    for line in wrap(draw, headline, F_PANEL_H, w - 28):
        draw.text((x + 14, hy), line, font=F_PANEL_H, fill=INK)
        hy += 26
    para(draw, x + 14, hy + 6, body, F_PANEL_B, w - 28, fill=MUTED, leading=1.32)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((32, 16), "THE WORLD TODAY", font=F_SERIF_B, fill=(255, 255, 255))
    d.text((32, 88), "THURSDAY, 26 NOVEMBER 2026",
           font=F_DATE, fill=(255, 214, 90))
    d.text((W - 32 - d.textlength("ONE DAY  •  ONE PICTURE", font=F_DATE),
            88), "ONE DAY  •  ONE PICTURE", font=F_DATE,
           fill=(255, 255, 255))
    d.rectangle([0, 118, W, 124], fill=RED)

    # ---- lead story ----
    ly = 140
    d.text((32, ly), "LEAD  —  THE GULF, ENERGY & WAR",
           font=F_KICK, fill=RED)
    hy = ly + 26
    for line in wrap(d, "HOUTHIS CLAIM HIT ON SAUDI'S BIGGEST REFINERY",
                     F_LEAD_H, 660):
        d.text((32, hy), line, font=F_LEAD_H, fill=INK)
        hy += 42
    body = ("Yemen's Houthis say they struck Ras Tanura, Saudi Arabia's "
            "largest refinery at 550,000 barrels a day. Riyadh says its "
            "defences downed four drones — but satellite images show thick "
            "smoke over the complex.")
    hy = para(d, 32, hy + 6, body, F_LEAD_B, 660, fill=MUTED, leading=1.35)
    body2 = ("Two oil tankers hit naval mines in the Strait of Hormuz, and "
             "Iran's navy says the strait \"will never be reopened\".")
    para(d, 32, hy + 4, body2, F_LEAD_B, 660, fill=MUTED, leading=1.35)

    # stat box, right of the lead
    bx, by, bw, bh = 716, 168, 276, 158
    d.rectangle([bx, by, bx + bw, by + bh], fill=NAVY)
    d.text((bx + 18, by + 14), "BRENT CRUDE", font=F_STAT_S,
           fill=(255, 214, 90))
    d.text((bx + 18, by + 40), "+2.4%", font=F_STAT, fill=(255, 255, 255))
    d.text((bx + 18, by + 82), "$93.60 a barrel", font=F_LEAD_B,
           fill=(255, 255, 255))
    d.text((bx + 18, by + 116), "Oil jumps as Gulf attacks widen",
           font=F_FOOT, fill=(200, 205, 215))

    # ---- six panels, two rows of three ----
    px, py = 32, 374
    pw, ph, gap = 304, 236, 16
    panels = [
        ("UKRAINE", (29, 78, 216),
         "KYIV HITS TWO RUSSIAN REFINERIES",
         "Drones set the Syzran and Kuibyshev plants ablaze in Samara, "
         "about 800 km inside Russia. Putin vows retaliation is "
         "\"inevitable\"; 29 of 33 refineries have been hit.",
         flame),
        ("GAZA", (124, 45, 18),
         "ISRAEL KILLS HAMAS SECURITY CHIEF",
         "An air strike kills the head of Hamas's internal security "
         "service and his family — the second senior Hamas security "
         "official killed in 24 hours. The ceasefire is under strain.",
         tower),
        ("SPACE", (76, 29, 149),
         "PAKISTAN'S FIRST ASTRONAUT FLIES",
         "China's Shenzhou-24 lifts off carrying Muhammad Zeeshan Ali — "
         "the first foreign astronaut to visit the Tiangong space "
         "station.",
         rocket),
        ("UNITED STATES", (6, 95, 70),
         "US CONFIDENCE NEARS TWO-YEAR HIGH",
         "American consumers turn more upbeat despite stubborn "
         "inflation. Washington floats tariffs of up to 35% on 14 "
         "economies, including China and the EU.",
         bars),
        ("COLOMBIA", (146, 64, 14),
         "TEN YEARS AFTER THE PEACE DEAL",
         "Colombia marks a decade since its historic peace agreement. "
         "The UN chief praises the progress — and warns commitments "
         "remain unfinished.",
         dove),
        ("SPORT", (15, 118, 110),
         "15-YEAR-OLD SMASHES 204 OFF 53 BALLS",
         "Vaibhav Sooryavanshi hits a world-record fastest List A "
         "double century against the UAE. In Geneva, Gukesh defends his "
         "world chess crown against Sindarov.",
         ball),
    ]
    for i, (kick, color, head, body, icon) in enumerate(panels):
        x = px + (i % 3) * (pw + gap)
        y = py + (i // 3) * (ph + gap)
        panel(d, x, y, pw, ph, kick, color, head, body, icon)

    # ---- also-today ticker ----
    ty = py + 2 * ph + gap + 14
    d.rectangle([32, ty, W - 32, ty + 96], fill=(255, 255, 255),
                outline=EDGE, width=2)
    d.text((48, ty + 12), "ALSO TODAY", font=F_KICK, fill=RED)
    tick = ("Mumbai marks 18 years since the 26/11 attacks  •  Petrobras "
            "unveils a $122bn investment plan  •  Venezuela reveals $237.5bn "
            "of public debt  •  BepiColombo reaches Mercury after an "
            "eight-year journey  •  Cairo truck fire kills at least 30")
    para(d, 48, ty + 36, tick, F_TICK, W - 96, fill=INK, leading=1.35)

    # ---- footer ----
    fy = H - 30
    d.text((32, fy), "THE WORLD TODAY  —  26 NOVEMBER 2026",
           font=F_FOOT, fill=MUTED)
    d.text((W - 32 - d.textlength("All stories as reported on the day",
                                  font=F_FOOT), fy),
           "All stories as reported on the day", font=F_FOOT, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
