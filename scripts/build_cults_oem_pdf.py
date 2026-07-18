from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas


OUTPUT = Path("/workspace/decks/cults-gummies-oem-hotel-proposal.pdf")
LDF_OUTPUT = Path("/workspace/decks/cults-gummies-oem-hotel-proposal.ldf")

PAGE_WIDTH = 960
PAGE_HEIGHT = 540

BG = HexColor("#08080C")
CARD = HexColor("#16161C")
WHITE_TXT = HexColor("#F5F5F5")
MUTED = HexColor("#A4A4AA")
PINK = HexColor("#F02D8C")
LIME = HexColor("#BADB44")
ORANGE = HexColor("#F48434")
PURPLE = HexColor("#A55DFF")


def draw_wrapped(c, text, x, y, width, font="Helvetica", size=12, color=WHITE_TXT, leading=1.3):
    c.setFont(font, size)
    c.setFillColor(color)
    lines = simpleSplit(text, font, size, width)
    step = size * leading
    cursor = y
    for line in lines:
        c.drawString(x, cursor, line)
        cursor -= step
    return cursor


def draw_meta(c):
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(26, 526, "@drinkcults")
    c.drawRightString(934, 526, "Business use  -  Highly confidential")


def draw_title(c, title):
    c.setFillColor(PINK)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(52, 468, title)


def draw_card(c, x, y, w, h, border):
    c.setFillColor(CARD)
    c.setStrokeColor(border)
    c.rect(x, y, w, h, fill=1, stroke=1)


def blank_slide(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_meta(c)


def cover(c):
    blank_slide(c)
    c.setFillColor(PINK)
    c.setFont("Helvetica-Bold", 64)
    c.drawString(54, 360, "CULTS")

    c.setFillColor(LIME)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(54, 318, "ADAPTOGEN GUMMIES")

    c.setFillColor(MUTED)
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(54, 292, "Recovery Ritual  -  OEM partnership proposal for boutique and luxury hotels")

    c.setFillColor(BG)
    c.setStrokeColor(ORANGE)
    c.rect(54, 238, 268, 34, fill=1, stroke=1)
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(188, 250, "RECOVER LIKE YOU MEAN IT")


def intro(c):
    blank_slide(c)
    draw_title(c, "Introduction")

    draw_wrapped(c, "Brief business overview", 56, 414, 420, "Helvetica-Bold", 13)
    draw_wrapped(
        c,
        "Cults makes functional gummies for modern travelers who want recovery and deeper sleep without clinical wellness theater.",
        56,
        394,
        430,
        "Helvetica",
        11,
        MUTED,
    )
    draw_wrapped(c, "Vision statement", 56, 346, 420, "Helvetica-Bold", 13)
    draw_wrapped(
        c,
        "Be the in-room recovery ritual guests trust when sleep quality and energy start to drop.",
        56,
        326,
        430,
        "Helvetica",
        11,
        MUTED,
    )
    draw_wrapped(c, "Mission statement", 56, 278, 420, "Helvetica-Bold", 13)
    draw_wrapped(
        c,
        "Place one honest, effective pouch in every room that needs a reset.",
        56,
        258,
        430,
        "Helvetica",
        11,
        MUTED,
    )

    draw_card(c, 505, 122, 405, 302, PINK)
    draw_wrapped(c, "What's in the pouch", 525, 398, 360, "Helvetica-Bold", 16, LIME)
    draw_wrapped(c, "Deep Sleep: reishi + ashwagandha + magnesium + passionflower + l-theanine", 525, 366, 360, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "Recovery: cordyceps + tart cherry + turmeric + mangosteen", 525, 300, 360, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "No powders. No capsules. Just one premium pouch.", 525, 232, 360, "Helvetica-Bold", 11, MUTED)


def who_we_are(c):
    blank_slide(c)
    draw_title(c, "Who we are")

    draw_wrapped(
        c,
        "Cults is a Thai functional gummy brand for guests who want recovery without friction. For hotels, that becomes a modern amenity guests use and remember.",
        56,
        412,
        430,
        "Helvetica",
        12,
        WHITE_TXT,
    )
    draw_wrapped(c, "Best-fit guest moments", 56, 328, 420, "Helvetica-Bold", 13)
    for idx, line in enumerate(["- First night post-flight", "- Post-gym or spa recovery", "- Wind-down after late dinner", "- Early call-time reset"]):
        draw_wrapped(c, line, 56, 304 - (idx * 24), 430, "Helvetica", 11, MUTED)

    cards = [
        (505, 286, 190, 130, PINK, "Boutique city hotel", "Amenity drawer, turn-down tray"),
        (716, 286, 194, 130, ORANGE, "Wellness resort", "Spa gift shop, retreat welcome kit"),
        (505, 132, 190, 130, LIME, "Business hotel", "Executive floor minibar"),
        (716, 132, 194, 130, PURPLE, "Private villa", "Welcome hamper, concierge upsell"),
    ]
    for x, y, w, h, border, head, sub in cards:
        draw_card(c, x, y, w, h, border)
        draw_wrapped(c, head, x + 14, y + h - 25, w - 24, "Helvetica-Bold", 13, WHITE_TXT)
        draw_wrapped(c, sub, x + 14, y + h - 52, w - 24, "Helvetica", 10, MUTED)


def market(c):
    blank_slide(c)
    draw_title(c, "Market opportunity")

    draw_wrapped(
        c,
        "Sleep tourism is now one of the strongest growth narratives in premium hospitality, and hotels need amenities that feel modern, useful, and easy to implement.",
        56,
        414,
        430,
        "Helvetica",
        12,
        WHITE_TXT,
    )
    draw_card(c, 56, 132, 430, 220, ORANGE)
    draw_wrapped(c, "Why Cults fits now", 74, 328, 390, "Helvetica-Bold", 15, ORANGE)
    draw_wrapped(c, "- Better than generic minibar clutter", 74, 298, 390, "Helvetica", 11, MUTED)
    draw_wrapped(c, "- Premium, photogenic, and guest-friendly", 74, 274, 390, "Helvetica", 11, MUTED)
    draw_wrapped(c, "- Crafted in Thailand with transparent ingredients", 74, 250, 390, "Helvetica", 11, MUTED)

    c.setFillColor(LIME)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(535, 396, "$369B")
    c.setFont("Helvetica", 12)
    c.setFillColor(MUTED)
    c.drawString(535, 374, "global luxury hotel market by 2032")
    c.setFillColor(LIME)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(535, 328, "9%")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 12)
    c.drawString(535, 306, "growth in wellness ritual demand")
    c.setFillColor(PINK)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(535, 260, "23%")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 12)
    c.drawString(535, 238, "guests value personalized amenities")
    draw_wrapped(c, "One SKU. One story. One premium touchpoint.", 535, 194, 360, "Helvetica-Bold", 12, WHITE_TXT)


def partners(c):
    blank_slide(c)
    draw_title(c, "Target hotel partners")
    c.setStrokeColor(LIME)
    c.setLineWidth(2)
    c.line(56, 412, 906, 412)

    draw_wrapped(c, "Primary", 56, 392, 390, "Helvetica-Bold", 14, ORANGE)
    draw_wrapped(c, "Boutique and lifestyle hotels in Bangkok, Phuket, Chiang Mai, Koh Samui", 56, 370, 390, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "Wellness resorts and spa retreats", 56, 328, 390, "Helvetica-Bold", 12, WHITE_TXT)
    draw_wrapped(c, "Independent luxury properties with fast procurement", 56, 306, 390, "Helvetica", 11, MUTED)

    draw_wrapped(c, "Secondary", 505, 392, 390, "Helvetica-Bold", 14, LIME)
    draw_wrapped(c, "International chain wellness floors", 505, 370, 390, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "Private villas and estate management", 505, 338, 390, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "Corporate retreat gifting and delegate kits", 505, 306, 390, "Helvetica", 11, WHITE_TXT)

    draw_card(c, 56, 132, 850, 126, PINK)
    draw_wrapped(c, "The guest they're serving", 74, 234, 790, "Helvetica-Bold", 13, PINK)
    draw_wrapped(
        c,
        "Long-haul arrivals, wellness-forward travelers, busy executives, and social travelers who need better sleep and recovery in a format that feels premium.",
        74,
        210,
        790,
        "Helvetica",
        11,
        MUTED,
    )


def value_market(c):
    blank_slide(c)
    draw_title(c, "Our value to the market")
    draw_wrapped(c, "The first true recovery amenity for modern Thailand hospitality.", 56, 424, 820, "Helvetica-Bold", 14, WHITE_TXT)

    circles = [
        (70, PINK, "Low-cost, high-value", "Premium feel, efficient unit economics."),
        (352, LIME, "Effortless ritual", "No prep. Tear, eat, sleep."),
        (634, ORANGE, "Real ingredients", "Transparent, credible formulation."),
    ]
    for x, border, head, body in circles:
        c.setFillColor(CARD)
        c.setStrokeColor(border)
        c.circle(x + 115, 248, 108, fill=1, stroke=1)
        draw_wrapped(c, head, x + 42, 262, 150, "Helvetica-Bold", 13, WHITE_TXT)
        draw_wrapped(c, body, x + 34, 234, 166, "Helvetica", 10, MUTED)


def value_you(c):
    blank_slide(c)
    draw_title(c, "Our value to you")
    cards = [
        (56, ORANGE, "1. Guest experience upgrade", "A recovery ritual that guests actually use."),
        (334, LIME, "2. Low cost, high perceived value", "Feels premium while staying operationally simple."),
        (612, PINK, "3. A story your team can tell", "Places your property inside sleep-tourism momentum."),
    ]
    for x, border, head, body in cards:
        draw_card(c, x, 286, 262, 146, border)
        draw_wrapped(c, head, x + 16, 408, 228, "Helvetica-Bold", 12, WHITE_TXT)
        draw_wrapped(c, body, x + 16, 382, 228, "Helvetica", 10, MUTED)

    draw_wrapped(c, "OEM program", 56, 244, 390, "Helvetica-Bold", 14, LIME)
    draw_wrapped(c, "Private label / co-brand options + low minimums + flexible fulfillment.", 56, 222, 820, "Helvetica", 11, WHITE_TXT)


def marketing(c):
    blank_slide(c)
    draw_title(c, "Marketing support")
    draw_wrapped(c, "Where to find Cults", 56, 408, 390, "Helvetica-Bold", 13, WHITE_TXT)
    draw_wrapped(c, "Partner-hotel discovery posts and booking-page referrals.", 56, 386, 390, "Helvetica", 11, MUTED)
    draw_wrapped(c, "In-room QR, post-stay flywheel", 56, 340, 390, "Helvetica-Bold", 13, WHITE_TXT)
    draw_wrapped(c, "QR links the guest to your story and reorder journey.", 56, 318, 390, "Helvetica", 11, MUTED)
    draw_wrapped(c, "Always-on content", 56, 272, 390, "Helvetica-Bold", 13, WHITE_TXT)
    draw_wrapped(c, "Founder-led social and creator content around real stays.", 56, 250, 390, "Helvetica", 11, MUTED)

    draw_card(c, 468, 136, 438, 296, LIME)
    draw_wrapped(c, "Marketing approach", 486, 408, 390, "Helvetica-Bold", 15, LIME)
    draw_wrapped(c, "Acquisition: social + hospitality media + hotel group intros", 486, 378, 390, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "Engagement: in-room QR and UGC touchpoints", 486, 346, 390, "Helvetica", 11, WHITE_TXT)
    draw_wrapped(c, "Repurchase: direct reorder path with referral logic", 486, 314, 390, "Helvetica", 11, WHITE_TXT)


def rollout(c):
    blank_slide(c)
    draw_title(c, "Pilot rollout and commercial model")
    stages = [
        (56, 272, PINK, "Phase 1", "30-day pilot\n2-3 room categories\n100-300 pouches"),
        (334, 272, LIME, "Phase 2", "90-day scale\nFull property rollout\nMonthly optimization"),
        (612, 272, ORANGE, "Commercial", "OEM or co-brand\nLow MOQ\nProtected margin"),
    ]
    for x, y, border, head, body in stages:
        draw_card(c, x, y, 262, 170, border)
        draw_wrapped(c, head, x + 16, y + 146, 230, "Helvetica-Bold", 14, border)
        draw_wrapped(c, body, x + 16, y + 120, 230, "Helvetica", 11, WHITE_TXT)

    draw_wrapped(
        c,
        "Target outcome: one Cults pouch in every room that needs better recovery and deeper sleep.",
        56,
        214,
        850,
        "Helvetica-Bold",
        12,
        WHITE_TXT,
    )


def closing(c):
    blank_slide(c)
    c.setFillColor(PINK)
    c.setFont("Helvetica-Bold", 42)
    c.drawCentredString(480, 292, "Be the first hotel to put deep sleep in every room.")

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 13)
    c.drawCentredString(480, 254, "Join the recovery movement with one honest pouch guests remember.")

    c.setFillColor(BG)
    c.setStrokeColor(LIME)
    c.rect(332, 205, 296, 34, fill=1, stroke=1)
    c.setFillColor(LIME)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(480, 217, "RECOVER LIKE YOU MEAN IT")


def build_pdf():
    c = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    slides = [cover, intro, who_we_are, market, partners, value_market, value_you, marketing, rollout, closing]
    for idx, fn in enumerate(slides):
        if idx:
            c.showPage()
        fn(c)
    c.save()


def build_ldf():
    md = Path("/workspace/decks/cults-gummies-oem-hotel-proposal.md")
    if md.exists():
        LDF_OUTPUT.write_text(md.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    build_pdf()
    build_ldf()
