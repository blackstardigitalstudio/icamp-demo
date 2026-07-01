# -*- coding: utf-8 -*-
"""Genera logo.png y og-image.jpg para ICAMP con la identidad de marca."""
from PIL import Image, ImageDraw, ImageFont

NAVY = (15, 41, 66)
NAVY2 = (18, 51, 86)
TEAL = (14, 165, 168)
GOLD = (224, 164, 88)
WHITE = (255, 255, 255)
MUTED = (198, 215, 232)

def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

ARIAL_B = r"C:\Windows\Fonts\arialbd.ttf"
ARIAL = r"C:\Windows\Fonts\arial.ttf"

def vgradient(w, h, top, bottom):
    base = Image.new("RGB", (w, h), top)
    dr = ImageDraw.Draw(base)
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        dr.line([(0, y), (w, y)], fill=c)
    return base

def draw_mark(d, x, y, s, scale):
    """Dibuja el isotipo ICAMP (edificio teal + punto dorado) escalado."""
    def P(px, py):
        return (x + px / 48 * s, y + py / 48 * s)
    # cuadrado redondeado
    d.rounded_rectangle([x, y, x + s, y + s], radius=int(s * 0.25), fill=(28, 67, 112))
    # "edificio": polígono 14,34 -> 20 ... (misma forma que el favicon)
    pts = [(14,34),(14,20),(24,13),(34,20),(34,34),(28,34),(28,25),(20,25),(20,34)]
    d.polygon([P(px,py) for (px,py) in pts], fill=TEAL)
    # punto dorado
    cx, cy = P(24, 15.5)
    r = 2.4 / 48 * s
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)

# ---------- LOGO 512x512 ----------
logo = vgradient(512, 512, NAVY, NAVY2)
d = ImageDraw.Draw(logo)
draw_mark(d, 96, 60, 320, 1)
f1 = font(ARIAL_B, 128)
tw = d.textlength("ICAMP", font=f1)
d.text(((512 - tw) / 2, 400), "ICAMP", font=f1, fill=WHITE)
logo.save("logo.png")

# ---------- OG IMAGE 1200x630 ----------
og = vgradient(1200, 630, NAVY, NAVY2)
d = ImageDraw.Draw(og)
# acento teal (círculo suave arriba-derecha)
glow = Image.new("RGBA", (1200, 630), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([880, -220, 1400, 300], fill=(14, 165, 168, 60))
gd.ellipse([-200, 380, 260, 840], fill=(224, 164, 88, 45))
og = Image.alpha_composite(og.convert("RGBA"), glow).convert("RGB")
d = ImageDraw.Draw(og)
# isotipo + wordmark
draw_mark(d, 90, 70, 92, 1)
d.text((205, 78), "ICAMP", font=font(ARIAL_B, 62), fill=WHITE)
d.text((207, 146), "INSTITUTO CANARIO DE MARCAS Y PATENTES", font=font(ARIAL_B, 19), fill=(150, 176, 205))
# título
d.text((90, 268), "Registro de Marcas y Patentes", font=font(ARIAL_B, 68), fill=WHITE)
d.text((90, 346), "en Canarias", font=font(ARIAL_B, 68), fill=GOLD)
# subtítulo
d.text((90, 452), "Agentes de la Propiedad Industrial  ·  Las Palmas y Tenerife",
       font=font(ARIAL, 30), fill=MUTED)
# barra inferior
d.rectangle([0, 560, 1200, 630], fill=(11, 31, 51))
d.text((90, 578), "www.icamp.es", font=font(ARIAL_B, 30), fill=TEAL)
tel = "928 38 23 95"
tw = d.textlength(tel, font=font(ARIAL_B, 30))
d.text((1110 - tw, 578), tel, font=font(ARIAL_B, 30), fill=WHITE)
og.save("og-image.jpg", quality=90)

print("Generados: logo.png (512x512), og-image.jpg (1200x630)")
