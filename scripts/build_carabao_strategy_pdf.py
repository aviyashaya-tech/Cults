from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfgen import canvas


OUTPUT = Path("/workspace/decks/avi-yashaya-carabao-strategy.pdf")
LDF_OUTPUT = Path("/workspace/decks/avi-yashaya-carabao-strategy.ldf")
MD_PATH = Path("/workspace/decks/avi-yashaya-carabao-strategy.md")
ASSET_DIR = Path("/workspace/assets/carabao-project/normalized")

CARABAO_LOGO = ASSET_DIR / "carabao_logo.png"
SINGHA_LOGO = ASSET_DIR / "singha_logo.png"
TAWANDANG_LOGO = ASSET_DIR / "tawandang_logo.png"
CARABAO_LAGER = ASSET_DIR / "carabao_lager.png"
CHANG_CLASSIC = ASSET_DIR / "chang_classic.png"
LEO_BEER = ASSET_DIR / "leo_beer.png"
CHAO_SUNGTHONG = ASSET_DIR / "chao_sungthong.png"
MAHANAKHON_WHITE_ALE = ASSET_DIR / "mahanakhon_white_ale.png"
LEO_SUPREME = ASSET_DIR / "leo_supreme.png"
SINGHA_RESERVE = ASSET_DIR / "singha_reserve.png"

PAGE_WIDTH = 960
PAGE_HEIGHT = 540

BG = HexColor("#0C1220")
CARD = HexColor("#172135")
CARD_ALT = HexColor("#222C42")
WHITE = HexColor("#F5F8FF")
MUTED = HexColor("#ABB9D5")
ACCENT_GOLD = HexColor("#F5B041")


def blank_slide(c, bg=BG):
    c.setFillColor(bg)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)


def top_meta(c, label):
    c.setFillColor(HexColor("#121B2E"))
    c.rect(0, PAGE_HEIGHT - 32, PAGE_WIDTH, 32, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, PAGE_HEIGHT - 20, label)


def title(c, head, sub=None):
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(52, PAGE_HEIGHT - 78, head)
    if sub:
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 12)
        y = PAGE_HEIGHT - 100
        for line in simpleSplit(sub, "Helvetica", 12, 840):
            c.drawString(52, y, line)
            y -= 15


def card(c, x, y, w, h, head, sub, fill=CARD, border=HexColor("#303D5A")):
    c.setFillColor(fill)
    c.setStrokeColor(border)
    c.roundRect(x, y, w, h, 12, fill=1, stroke=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x + 14, y + h - 24, head)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 10)
    yy = y + h - 40
    for line in simpleSplit(sub, "Helvetica", 10, w - 28):
        c.drawString(x + 14, yy, line)
        yy -= 13


def bullets(c, x, y, width, lines, size=12, color=MUTED, leading=1.38):
    c.setFillColor(color)
    c.setFont("Helvetica", size)
    cursor = y
    step = size * leading
    for item in lines:
        wrapped = simpleSplit(f"• {item}", "Helvetica", size, width)
        for row in wrapped:
            c.drawString(x, cursor, row)
            cursor -= step
        cursor -= 4


def draw_image(c, path, x, y, w, h):
    if path.exists():
        img = ImageReader(str(path))
        c.drawImage(img, x, y, width=w, height=h, preserveAspectRatio=True, anchor="c")
    else:
        c.setFillColor(CARD_ALT)
        c.setStrokeColor(HexColor("#404F73"))
        c.rect(x, y, w, h, fill=1, stroke=1)


def slide_cover(c):
    blank_slide(c)
    top_meta(c, "CARABAO BREWERY | LONG-TERM STRATEGY | AVI YASHAYA")
    c.setFillColor(ACCENT_GOLD)
    c.rect(0, 0, PAGE_WIDTH, 48, fill=1, stroke=0)
    title(
        c,
        "Get Brand Identity On Par With Operational Modernization",
        "A Carabao-targeted operating blueprint from Avi Yashaya",
    )
    bullets(
        c,
        56,
        355,
        480,
        [
            "10+ years building beverage systems across Thailand, Vietnam, and Laos.",
            "Proven $2M+ annual sell-through from hands-on development and market execution.",
            "Objective: modernize brand perception and accelerate profitable share growth.",
        ],
        size=13,
        color=WHITE,
    )
    draw_image(c, CARABAO_LOGO, 610, 355, 300, 135)
    draw_image(c, CARABAO_LAGER, 620, 185, 80, 126)
    draw_image(c, LEO_SUPREME, 720, 185, 80, 126)
    draw_image(c, SINGHA_RESERVE, 820, 185, 90, 126)
    c.setFillColor(BG)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(56, 16, "Avi Yashaya | aviyashaya@gmail.com")


def slide_dilemma(c):
    blank_slide(c)
    top_meta(c, "PROBLEM HOOK")
    title(c, "The Double-Edged Dilemma in Thai Beer")
    card(c, 52, 80, 410, 365, "SME ambition vs. industrial reality", "MOQs, logistics, and cash constraints block rapid iteration.")
    card(c, 498, 80, 410, 365, "Incumbent scale vs. cultural velocity", "Large systems optimize volume but miss fast urban preference shifts.", fill=CARD_ALT)
    bullets(
        c,
        72,
        362,
        370,
        [
            "Innovation dies before demand is validated.",
            "Volume pressure pushes discount-led behavior.",
            "Brand language remains traditional while lifestyle expectations evolve.",
        ],
    )
    bullets(
        c,
        518,
        362,
        370,
        [
            "Slow development cycles age consumer insights.",
            "Commercial execution outpaces identity strategy.",
            "SAM remains under-penetrated and SOM growth plateaus.",
        ],
    )


def slide_frames(c):
    blank_slide(c)
    top_meta(c, "FIVE BRANDING FRAMES")
    title(c, "Thai Beer Positioning Spans Five Distinct Frames")
    card(c, 52, 242, 165, 190, "1) Animal / Power", "Chang, Leo, Carabao")
    card(c, 232, 242, 165, 190, "2) Myth / Heritage", "Singha, Chao Sungthong")
    card(c, 412, 242, 165, 190, "3) Geographic", "Mahanakhon, Chiang Mai")
    card(c, 592, 242, 165, 190, "4) Subculture", "Outlaw craft niches")
    card(c, 772, 242, 136, 190, "5) Modern Aspirational", "The growth gap", fill=HexColor("#213A2E"))
    draw_image(c, CHANG_CLASSIC, 66, 302, 38, 58)
    draw_image(c, LEO_BEER, 109, 302, 38, 58)
    draw_image(c, CARABAO_LAGER, 152, 302, 38, 58)
    draw_image(c, SINGHA_LOGO, 246, 292, 58, 62)
    draw_image(c, CHAO_SUNGTHONG, 311, 298, 55, 63)
    draw_image(c, MAHANAKHON_WHITE_ALE, 438, 302, 65, 60)
    bullets(
        c,
        52,
        214,
        850,
        [
            "Growth is shifting from pure mass/traditional cues toward culturally fluent lifestyle codes.",
            "Frame 5 is where younger urban consumers reward stylish, accessible daily-luxury brands.",
        ],
        size=12,
    )


def slide_limits(c):
    blank_slide(c)
    top_meta(c, "CURRENT LIMITATIONS")
    title(c, "Where Current Framing Limits Growth")
    card(c, 52, 80, 285, 365, "Carabao", "Still perceived by many younger urbanites as heavy-worker or cheap-night-out coded.")
    card(c, 352, 80, 285, 365, "Tawandang", "High awareness, but can feel rigid or old-generation in casual modern spaces.")
    card(c, 652, 80, 256, 365, "Pattaya / Phuket / CNX labels", "Can get trapped in tourist-frame positioning and struggle to scale nationally.")
    draw_image(c, CARABAO_LOGO, 95, 184, 200, 95)
    draw_image(c, TAWANDANG_LOGO, 390, 184, 215, 95)
    draw_image(c, LEO_BEER, 708, 168, 146, 120)


def slide_sam(c):
    blank_slide(c)
    top_meta(c, "SAM TO SOM")
    title(c, "Presentation Is Not Optimized for SAM")
    card(c, 52, 96, 280, 338, "Current state", "Distribution strength, but weaker premium-adjacent lifestyle resonance.")
    card(c, 340, 96, 280, 338, "Unlock SAM", "Modern-retro identity upgrade without losing Thai mass resonance.", fill=HexColor("#1D372D"))
    card(c, 628, 96, 280, 338, "Increase SOM", "Targeted product development and channel sequencing raises conversion.", fill=HexColor("#332421"))
    bullets(c, 70, 346, 244, ["Price-led coding", "Limited aspiration cues", "Low social-signaling value"], size=11)
    bullets(c, 358, 346, 244, ["Lifestyle-led design", "Occasion-specific storytelling", "Urban outlet amplification"], size=11)
    bullets(c, 646, 346, 244, ["Premium mix lift", "Better repeat rate", "Share gain in high-value channels"], size=11)


def slide_proof(c):
    blank_slide(c)
    top_meta(c, "PROOF OF PRINCIPLE")
    title(c, "Boon Rawd Example: Premium Extension Works")
    card(c, 52, 80, 430, 365, "Leo Supreme + Singha Reserve", "Legacy equity + premiumized sub-lines = perception reset and margin upside.")
    card(c, 500, 80, 408, 365, "Implication for Carabao", "Build modern aspirational tier while protecting mass-scale engine.", fill=CARD_ALT)
    draw_image(c, LEO_SUPREME, 92, 174, 164, 164)
    draw_image(c, SINGHA_RESERVE, 286, 178, 176, 156)
    bullets(
        c,
        520,
        346,
        370,
        [
            "Use premium line architecture to re-code brand quality.",
            "Link identity refresh with execution cadence, not just campaign assets.",
            "Build faster product loops based on channel behavior.",
        ],
    )


def slide_mahanakhon(c):
    blank_slide(c)
    top_meta(c, "RELEVANT CREDIBILITY")
    title(c, "Mahanakhon Solved the Geographic-Frame Trap")
    draw_image(c, MAHANAKHON_WHITE_ALE, 70, 165, 210, 220)
    bullets(
        c,
        310,
        374,
        600,
        [
            "Local pride alone did not scale; aspirational framing had to be built.",
            "Collaboration + social awareness + commercial discipline shifted perception.",
            "Operating system linked sourcing, production, and route-to-market execution.",
            "Result: products delivering $2M+ annual sell-through.",
        ],
        size=13,
        color=WHITE,
    )


def slide_plan(c):
    blank_slide(c)
    top_meta(c, "ACTION FRAMEWORK")
    title(c, "Identity + Product + Commercial System Plan")
    card(c, 52, 96, 206, 338, "Phase 1 | Reframe", "Modern Thai confidence, not low-price signals.", border=ACCENT_GOLD)
    card(c, 274, 96, 206, 338, "Phase 2 | Product", "Upgrade liquid, pack, and occasion fit.", border=HexColor("#5EC988"))
    card(c, 496, 96, 206, 338, "Phase 3 | RTM", "Prioritize channels where perception and margin move fastest.", border=HexColor("#6395FF"))
    card(c, 718, 96, 190, 338, "Phase 4 | Scale", "Codify and expand once halo metrics are proven.", border=HexColor("#EB5757"))


def slide_product(c):
    blank_slide(c)
    top_meta(c, "PRODUCT DEVELOPMENT")
    title(c, "Priority Product Moves to Lift SOM")
    card(c, 52, 80, 285, 365, "Platform 1: Urban Core", "Cleaner profile, stronger pack architecture, better social fit.")
    card(c, 352, 80, 285, 365, "Platform 2: Premium Bridge", "Seasonal and limited sub-lines that cue quality and style.")
    card(c, 652, 80, 256, 365, "Platform 3: Channel Exclusives", "Modern trade and on-trade SKUs with clear role by account.")
    draw_image(c, CARABAO_LAGER, 144, 188, 95, 130)
    draw_image(c, LEO_SUPREME, 444, 188, 95, 130)
    draw_image(c, SINGHA_RESERVE, 718, 188, 124, 130)


def slide_contact(c):
    blank_slide(c, bg=HexColor("#0E1626"))
    top_meta(c, "EXECUTION PARTNERSHIP")
    title(c, "Avi Yashaya | Carabao Beer Transformation Partner")
    card(c, 52, 118, 430, 310, "Scope", "Brand architecture, product strategy, partner stack orchestration, and implementation governance.")
    card(c, 500, 118, 408, 310, "KPI focus", "Perception lift, premium mix growth, repeat rates, and urban channel share gains.", fill=CARD_ALT)
    bullets(c, 74, 340, 388, ["Diagnostic sprint", "90-day transformation blueprint", "Weekly implementation cadence", "SAM-to-SOM scorecard"], color=MUTED)
    bullets(c, 522, 340, 364, ["Contact: aviyashaya@gmail.com", "Built for practical execution, not presentation theater."], color=WHITE)


def slide_sources(c):
    blank_slide(c, bg=HexColor("#0D1423"))
    top_meta(c, "VISUAL SOURCES")
    title(c, "Web-Scraped Logos and Product References Included")
    bullets(
        c,
        58,
        390,
        840,
        [
            "Carabao logo: images.seeklogo.com",
            "Singha logo: Wikimedia Commons (Singha_Beer_Logo.png)",
            "Tawandang visual: tawandang.com",
            "Untappd references: Carabao Lager, Chang Classic, Leo, Singha, Chao Sungthong, Mahanakhon White Ale, Leo Supreme, Singha Reserve",
            "Wikimedia reference: Thailand-Leo-Beer.jpg",
        ],
        size=12,
        color=MUTED,
    )


def build_pdf():
    c = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    slides = [
        slide_cover,
        slide_dilemma,
        slide_frames,
        slide_limits,
        slide_sam,
        slide_proof,
        slide_mahanakhon,
        slide_plan,
        slide_product,
        slide_contact,
        slide_sources,
    ]
    for idx, render in enumerate(slides):
        if idx:
            c.showPage()
        render(c)
    c.save()


def build_ldf():
    if MD_PATH.exists():
        LDF_OUTPUT.write_text(MD_PATH.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    build_pdf()
    build_ldf()
