# -*- coding: utf-8 -*-
"""Genera imágenes originales (hero, servicios, logos de clientes) para ICAMP."""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.makedirs("img", exist_ok=True)
NAVY=(15,41,66); NAVY2=(18,51,86); TEAL=(14,165,168); TEALD=(9,97,99)
GOLD=(224,164,88); WHITE=(255,255,255); INK=(22,32,43)

def F(b,s):
    p=r"C:\Windows\Fonts\%s"%("arialbd.ttf" if b else "arial.ttf")
    try:return ImageFont.truetype(p,s)
    except:return ImageFont.load_default()

def vgrad(w,h,a,b,diag=False):
    im=Image.new("RGB",(w,h),a); d=ImageDraw.Draw(im)
    for y in range(h):
        t=y/max(1,h-1)
        c=tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
        d.line([(0,y),(w,y)],fill=c)
    return im

def mark(d,x,y,s):
    d.rounded_rectangle([x,y,x+s,y+s],radius=int(s*.25),fill=(28,67,112))
    def P(px,py):return (x+px/48*s,y+py/48*s)
    pts=[(14,34),(14,20),(24,13),(34,20),(34,34),(28,34),(28,25),(20,25),(20,34)]
    d.polygon([P(a,b) for a,b in pts],fill=TEAL)
    cx,cy=P(24,15.5); r=2.4/48*s
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GOLD)

# ---------- HERO (1200x920) ----------
im=vgrad(1200,920,NAVY,NAVY2); d=ImageDraw.Draw(im,"RGBA")
# glows
g=Image.new("RGBA",(1200,920),(0,0,0,0)); gd=ImageDraw.Draw(g)
gd.ellipse([760,-260,1400,380],fill=(14,165,168,70))
gd.ellipse([-260,560,320,1140],fill=(224,164,88,55))
g=g.filter(ImageFilter.GaussianBlur(40))
im=Image.alpha_composite(im.convert("RGBA"),g).convert("RGB"); d=ImageDraw.Draw(im,"RGBA")
# escudo (shield) con check = protección
sx,sy,sw=470,250,360
shield=[(sx+sw//2,sy),(sx+sw,sy+sw*0.22),(sx+sw,sy+sw*0.55),(sx+sw//2,sy+sw*1.02),(sx,sy+sw*0.55),(sx,sy+sw*0.22)]
d.polygon(shield,fill=(255,255,255,18),outline=(14,165,168,255))
d.line([(sx+sw*0.30,sy+sw*0.52),(sx+sw*0.45,sy+sw*0.68),(sx+sw*0.72,sy+sw*0.34)],fill=GOLD,width=16,joint="curve")
# nodos técnicos (patente) alrededor
import itertools
for ang in range(0,360,45):
    r=250; cx=650+int(r*math.cos(math.radians(ang))); cy=430+int(r*math.sin(math.radians(ang)))
    d.line([(650,430),(cx,cy)],fill=(127,227,229,120),width=3)
    d.ellipse([cx-8,cy-8,cx+8,cy+8],fill=(127,227,229,220))
# wordmark ICAMP
mark(d,90,110,90)
d.text((205,120),"ICAMP",font=F(1,60),fill=WHITE)
d.text((207,188),"MARCAS · PATENTES · DISEÑO",font=F(1,20),fill=(150,176,205))
d.text((90,720),"Protegemos lo que",font=F(1,52),fill=WHITE)
d.text((90,778),"te hace único",font=F(1,52),fill=GOLD)
im.save("img/hero.jpg",quality=88)

# ---------- SERVICIOS (600x380) ----------
def servcard(name,base,icon):
    im=vgrad(600,380,base,tuple(min(255,c+22) for c in base)); d=ImageDraw.Draw(im,"RGBA")
    gg=Image.new("RGBA",(600,380),(0,0,0,0)); gd=ImageDraw.Draw(gg)
    gd.ellipse([360,-140,760,260],fill=(255,255,255,40)); gg=gg.filter(ImageFilter.GaussianBlur(30))
    im=Image.alpha_composite(im.convert("RGBA"),gg).convert("RGB"); d=ImageDraw.Draw(im,"RGBA")
    cx,cy=300,175
    if icon=="star":
        pts=[];
        for i in range(10):
            r=95 if i%2==0 else 42; a=math.radians(-90+i*36)
            pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
        d.polygon(pts,outline=WHITE,width=8)
    elif icon=="bulb":
        d.ellipse([cx-70,cy-90,cx+70,cy+50],outline=WHITE,width=8)
        d.rectangle([cx-32,cy+50,cx+32,cy+92],outline=WHITE,width=8)
        d.line([cx-20,cy+108,cx+20,cy+108],fill=WHITE,width=8)
    elif icon=="cube":
        d.polygon([(cx,cy-95),(cx+90,cy-45),(cx+90,cy+55),(cx,cy+105),(cx-90,cy+55),(cx-90,cy-45)],outline=WHITE,width=8)
        d.line([(cx,cy-95),(cx,cy+105)],fill=WHITE,width=6); d.line([(cx-90,cy-45),(cx+90,cy-45)],fill=WHITE,width=6)
    elif icon=="globe":
        d.ellipse([cx-90,cy-90,cx+90,cy+90],outline=WHITE,width=8)
        d.line([cx-90,cy,cx+90,cy],fill=WHITE,width=6); d.line([cx,cy-90,cx,cy+90],fill=WHITE,width=6)
        d.ellipse([cx-45,cy-90,cx+45,cy+90],outline=WHITE,width=6)
    d.text((40,300),name,font=F(1,34),fill=WHITE)
    im.save("img/%s.jpg"%name.lower().replace(" ","-").replace("ñ","n").replace("ó","o"),quality=86)
servcard("Marcas",TEALD,"star")
servcard("Patentes",(24,67,112),"bulb")
servcard("Diseno",(38,90,120),"cube")
servcard("Marca UE",(12,80,110),"globe")

# ---------- LOGOS CLIENTES (invented wordmark badges 340x120) ----------
def logo(fn,txt,sub,accent):
    im=Image.new("RGB",(340,120),(255,255,255)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([2,2,338,118],radius=18,outline=(226,232,238),width=2,fill=(255,255,255))
    d.ellipse([26,44,58,76],fill=accent)
    d.text((72,34),txt,font=F(1,30),fill=(15,41,66))
    d.text((73,72),sub,font=F(0,15),fill=(120,135,150))
    im.save("img/%s"%fn)
logo("cli-macaronesian.png","Macaronesian","GIN · Canarias",(30,120,120))
logo("cli-kn.png","KN Hoteles","Hospitality",(210,150,60))
logo("cli-mojo.png","Mojo Surf","Surf & Lifestyle",(20,150,180))
logo("cli-arenas.png","Arenas del Mar","Resort",(224,164,88))
print("Imágenes generadas en img/:", sorted(os.listdir("img")))
