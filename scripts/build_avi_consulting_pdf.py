from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas


OUTPUT = Path("/workspace/decks/avi-yashaya-consulting-deck.pdf")
LDF_OUTPUT = Path("/workspace/decks/avi-yashaya-consulting-deck.ldf")

PAGE_WIDTH = 960
PAGE_HEIGHT = 540
MARGIN_X = 56
TOP_Y = 500


NAVY = HexColor("#12233F")
GOLD = HexColor("#C79948")
SLATE = HexColor("#364559")
LIGHT = HexColor("#F7F9FC")


def draw_wrapped_text(c, text, x, y, max_width, font_name="Helvetica", font_size=16, color=SLATE, leading=1.35):
    c.setFont(font_name, font_size)
    c.setFillColor(color)
    lines = simpleSplit(text, font_name, font_size, max_width)
    line_height = font_size * leading
    current_y = y
    for line in lines:
        c.drawString(x, current_y, line)
        current_y -= line_height
    return current_y


def draw_cover(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    c.setFillColor(GOLD)
    c.rect(0, 0, PAGE_WIDTH, 52, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 44)
    c.drawString(MARGIN_X, 390, "Avi Yashaya")

    c.setFont("Helvetica", 22)
    c.drawString(MARGIN_X, 340, "Partner & CEO, Mahanakhon Beverages Co., Ltd")
    c.drawString(MARGIN_X, 310, "NPD Consultant for Beverage Growth Across Southeast Asia")

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN_X, 20, "aviyashaya@gmail.com")


def draw_slide(c, heading, title, bullets, footer=None):
    c.setFillColor(LIGHT)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    c.setFillColor(NAVY)
    c.rect(0, PAGE_HEIGHT - 38, PAGE_WIDTH, 38, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20, PAGE_HEIGHT - 25, heading)

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(MARGIN_X, PAGE_HEIGHT - 88, title)

    y = PAGE_HEIGHT - 132
    bullet_indent = MARGIN_X + 10
    text_indent = MARGIN_X + 26

    for bullet in bullets:
        c.setFillColor(GOLD)
        c.circle(bullet_indent, y + 4, 3, fill=1, stroke=0)
        y = draw_wrapped_text(
            c,
            bullet,
            text_indent,
            y,
            PAGE_WIDTH - text_indent - MARGIN_X,
            font_name="Helvetica",
            font_size=17,
            color=SLATE,
        )
        y -= 14

    if footer:
        c.setFillColor(GOLD)
        c.rect(MARGIN_X, 52, PAGE_WIDTH - (2 * MARGIN_X), 2, fill=1, stroke=0)
        draw_wrapped_text(
            c,
            footer,
            MARGIN_X,
            36,
            PAGE_WIDTH - (2 * MARGIN_X),
            font_name="Helvetica",
            font_size=12,
            color=SLATE,
            leading=1.2,
        )


def draw_two_column(c, heading, title, left_title, left_points, right_title, right_points):
    c.setFillColor(LIGHT)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    c.setFillColor(NAVY)
    c.rect(0, PAGE_HEIGHT - 38, PAGE_WIDTH, 38, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20, PAGE_HEIGHT - 25, heading)

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(MARGIN_X, PAGE_HEIGHT - 85, title)

    panel_y = 80
    panel_h = 345
    panel_w = 404
    left_x = 52
    right_x = 504

    border_color = Color(0.84, 0.88, 0.93)
    c.setFillColor(white)
    c.setStrokeColor(border_color)
    c.rect(left_x, panel_y, panel_w, panel_h, fill=1, stroke=1)
    c.rect(right_x, panel_y, panel_w, panel_h, fill=1, stroke=1)

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(left_x + 16, panel_y + panel_h - 28, left_title)
    c.drawString(right_x + 16, panel_y + panel_h - 28, right_title)

    def draw_points(start_x, points):
        y = panel_y + panel_h - 58
        for point in points:
            c.setFillColor(GOLD)
            c.circle(start_x + 3, y + 4, 2.5, fill=1, stroke=0)
            y = draw_wrapped_text(
                c,
                point,
                start_x + 14,
                y,
                panel_w - 30,
                font_name="Helvetica",
                font_size=13,
                color=SLATE,
            )
            y -= 10

    draw_points(left_x + 16, left_points)
    draw_points(right_x + 16, right_points)


def deck_data():
    return [
        ("cover",),
        (
            "Profile",
            "Built for Execution, Not Theory",
            [
                "10+ years building beverage brands, operations, and route-to-market systems across Thailand, Laos, and Vietnam.",
                "Led launches that now generate over $2M annual sell-through in retail and on-trade channels.",
                "Hands-on leadership across sourcing, production, packaging, pricing, and distribution.",
                "Trusted operator for companies that need profitable market entry and scale in Southeast Asia.",
            ],
            None,
        ),
        (
            "Value Proposition",
            "What Enterprise Beverage Teams Bring Me In To Solve",
            [
                "Build a resilient, multi-country beverage supply chain from raw materials to retail shelf.",
                "Design and validate product-market fit for Beer, Spirits, and RTD portfolios in Southeast Asia.",
                "Convert distributor conversations into measurable listings, volume, and margin expansion.",
                "De-risk new market entries with local manufacturing, regulatory, and channel execution plans.",
            ],
            None,
        ),
        (
            "Global Supply Chain",
            "Hyper-Specific Operating Model: Source Global, Produce Local, Sell Regional",
            [
                "Raw materials: hop procurement from the USA and New Zealand with quality/spec alignment and cost controls.",
                "Production backbone: partner plants in Vietnam and Thailand across Brewery, Distillery, and RTD categories.",
                "Packaging network: coordinated can, bottle, closure, and label suppliers to protect lead time and cash flow.",
                "Regional flow: finished goods exported to convenience store channels in Taiwan and Japan.",
                "Market expansion support: launch blueprints for clients opening new beverage markets in Laos.",
            ],
            "Result: diversified supply continuity with practical production optionality across countries and categories.",
        ),
        (
            "two_column",
            "Regional Commercialization",
            "Route-to-Market and Pricing Strategy by Market",
            "Thailand + Vietnam",
            [
                "Position portfolio by channel: modern trade, convenience, and on-trade activation.",
                "Set margin architecture for producers, importers/distributors, and retailers.",
                "Build launch calendars tied to local demand windows, events, and consumer behavior.",
                "Run SKU-by-SKU pricing ladders to protect both velocity and gross margin.",
            ],
            "Laos Market Entry",
            [
                "Define import or local production model based on tax and duty realities.",
                "Build first-wave assortment with clear opening price points and premium anchors.",
                "Train distributor teams on product story, outlet pitch, and sell-in mechanics.",
                "Stage rollout by city and outlet class to maximize conversion with controlled risk.",
            ],
        ),
        (
            "two_column",
            "Relationships",
            "A Working Network Built Over a Decade",
            "Supply + Production Partners",
            [
                "Hop and ingredient suppliers in the USA and New Zealand.",
                "Manufacturing partners in Thailand and Vietnam covering beer, spirits, and RTD.",
                "Packaging suppliers for cans, bottles, cartons, and labels with scalable capacity.",
                "Quality and operational alignment across partners to speed launch readiness.",
            ],
            "Commercial Partners",
            [
                "Distributors and route-to-market operators across Thailand, Laos, and Vietnam.",
                "Retail and convenience channel relationships in Taiwan and Japan export routes.",
                "On-trade account development through practical pricing and menu placement strategy.",
                "Cross-functional partner management to maintain execution standards and timelines.",
            ],
        ),
        (
            "Category Scope",
            "Cross-Category Execution Capabilities",
            [
                "Brewery: concept-to-commercialization support for craft and premium beer portfolios.",
                "Distillery: liquid positioning, production planning, and go-to-market design for spirits.",
                "RTD: speed-to-market product development and scalable production transition support.",
                "Integrated portfolio strategy to prevent channel conflict and maximize total account value.",
            ],
            None,
        ),
        (
            "Commercial Evidence",
            "Selected Outcomes Delivered",
            [
                "Built and operated systems behind Mahanakhon products now exceeding $2M annual retail + on-trade revenue.",
                "Structured practical supply chain pathways linking global ingredient sourcing to regional production execution.",
                "Developed export-ready operating flows for convenience store channels in Taiwan and Japan.",
                "Supported market-opening strategy for Laos with channel-specific launch sequencing and price architecture.",
            ],
            "All outcomes based on direct operating involvement in sourcing, production, and commercialization.",
        ),
        (
            "two_column",
            "Engagement Model",
            "How I Work With Beverage Companies",
            "Advisory + Operating Sprint",
            [
                "30-90 day focused engagements for market entry, product launch, or supply chain redesign.",
                "Workstreams: sourcing, plant partner selection, packaging readiness, pricing, and channel plan.",
                "Weekly decision cadence with leadership team and execution owners.",
                "Output: clear operating playbook with accountability and rollout checkpoints.",
            ],
            "Fractional NPD Leadership",
            [
                "Embedded support for teams that need senior NPD and commercialization leadership.",
                "Cross-functional bridge between procurement, operations, marketing, and sales.",
                "Focus on profitable scale, not just innovation theater.",
                "Output: repeatable launch process that compounds over multiple product cycles.",
            ],
        ),
        (
            "Ideal Clients",
            "Best Fit Engagements",
            [
                "Global or regional beverage companies entering Southeast Asia.",
                "Established players needing stronger execution in Thailand, Vietnam, or Laos.",
                "Teams expanding across beer, spirits, and RTD categories with shared infrastructure.",
                "Businesses seeking local operator credibility plus strategic clarity at executive level.",
            ],
            None,
        ),
        (
            "Contact",
            "Let's Build the Next Profitable Beverage Platform",
            [
                "Avi Yashaya",
                "Partner & CEO, Mahanakhon Beverages Co., Ltd",
                "NPD Consultant",
                "Email: aviyashaya@gmail.com",
            ],
            "Available for consulting mandates with larger beverage companies and growth-focused regional operators.",
        ),
    ]


def build_pdf():
    c = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    for idx, data in enumerate(deck_data()):
        if idx > 0:
            c.showPage()

        if data[0] == "cover":
            draw_cover(c)
        elif data[0] == "two_column":
            _, heading, title, left_title, left_points, right_title, right_points = data
            draw_two_column(c, heading, title, left_title, left_points, right_title, right_points)
        else:
            heading, title, bullets, footer = data
            draw_slide(c, heading, title, bullets, footer)

    c.save()


def build_ldf():
    # Create an LDF extension variant that contains the deck narrative
    # in plain text so it can be opened in any text editor.
    md_path = Path("/workspace/decks/avi-yashaya-consulting-deck.md")
    content = md_path.read_text(encoding="utf-8")
    LDF_OUTPUT.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    build_pdf()
    build_ldf()
