"""Generate a .docx summary of 'How to Trade Using Binance Futures'.

Video: https://www.youtube.com/watch?v=SvXEAj7Mb48

This script creates illustrative diagrams and assembles them together with
a written summary into a Google-Docs-compatible .docx file.

Usage:
    pip install -r requirements.txt
    python generate_summary.py

Output:
    images/          – generated diagram PNGs
    Binance_Futures_Trading_Summary.docx
"""

import os
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images")
DOCX_PATH = os.path.join(BASE_DIR, "Binance_Futures_Trading_Summary.docx")

os.makedirs(IMG_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Image helpers
# ---------------------------------------------------------------------------

def _save(fig, name):
    path = os.path.join(IMG_DIR, name)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def create_account_setup_diagram():
    """Flow-chart style diagram showing the account setup steps."""
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")
    fig.patch.set_facecolor("#f9f9f9")

    steps = [
        ("Sign Up &\nVerify (KYC)", "#4CAF50"),
        ("Enable\nFutures", "#2196F3"),
        ("Deposit\nFunds (USDT)", "#FF9800"),
        ("Transfer to\nFutures Wallet", "#9C27B0"),
    ]

    box_w, box_h = 2.0, 1.6
    gap = 0.5
    x_start = 0.25
    y_center = 1.5

    for i, (label, color) in enumerate(steps):
        x = x_start + i * (box_w + gap)
        rect = mpatches.FancyBboxPatch(
            (x, y_center - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.15", facecolor=color, edgecolor="white",
            linewidth=2,
        )
        ax.add_patch(rect)
        ax.text(x + box_w / 2, y_center, label,
                ha="center", va="center", fontsize=10, color="white",
                fontweight="bold")
        if i < len(steps) - 1:
            ax.annotate(
                "", xy=(x + box_w + gap * 0.15, y_center),
                xytext=(x + box_w + 0.05, y_center),
                arrowprops=dict(arrowstyle="->", color="#333", lw=2),
            )

    ax.set_title("Account Setup Flow", fontsize=14, fontweight="bold", pad=12)
    return _save(fig, "account_setup.png")


def create_order_types_chart():
    """Bar-style comparison of the three main order types."""
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#f9f9f9")

    categories = ["Market Order", "Limit Order", "Stop-Limit Order"]
    speed = [10, 5, 3]
    control = [3, 9, 10]

    x = range(len(categories))
    width = 0.35

    bars1 = ax.bar([i - width / 2 for i in x], speed, width,
                   label="Execution Speed", color="#2196F3")
    bars2 = ax.bar([i + width / 2 for i in x], control, width,
                   label="Price Control", color="#FF9800")

    ax.set_ylabel("Rating (1-10)", fontsize=11)
    ax.set_title("Order Types – Speed vs Control", fontsize=13,
                 fontweight="bold")
    ax.set_xticks(list(x))
    ax.set_xticklabels(categories, fontsize=10)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 12)

    for bar_group in (bars1, bars2):
        for bar in bar_group:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                    str(int(bar.get_height())), ha="center", va="bottom",
                    fontsize=9, fontweight="bold")

    return _save(fig, "order_types.png")


def create_leverage_risk_chart():
    """Line chart illustrating how leverage amplifies gains and losses."""
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#f9f9f9")

    price_change = list(range(-10, 11))
    for lev, color, ls in [(1, "#4CAF50", "-"), (5, "#FF9800", "--"),
                           (10, "#F44336", "-"), (25, "#9C27B0", ":")]:
        pnl = [p * lev for p in price_change]
        ax.plot(price_change, pnl, color=color, ls=ls, lw=2,
                label=f"{lev}x Leverage")

    ax.axhline(0, color="grey", lw=0.8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.set_xlabel("Price Change (%)", fontsize=11)
    ax.set_ylabel("PnL (%)", fontsize=11)
    ax.set_title("Leverage Impact on Profit & Loss", fontsize=13,
                 fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    return _save(fig, "leverage_risk.png")


def create_margin_modes_diagram():
    """Side-by-side comparison of Cross vs Isolated margin."""
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    fig.patch.set_facecolor("#f9f9f9")

    for ax, (title, color, desc_lines) in zip(axes, [
        ("Cross Margin", "#2196F3", [
            "All positions share",
            "the same margin pool.",
            "",
            "• Lower liquidation risk",
            "  per position",
            "• Entire balance at stake",
        ]),
        ("Isolated Margin", "#FF9800", [
            "Each position has its",
            "own separate margin.",
            "",
            "• Risk limited to the",
            "  allocated margin",
            "• Position-level control",
        ]),
    ]):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")
        rect = mpatches.FancyBboxPatch(
            (0.5, 0.5), 9, 9,
            boxstyle="round,pad=0.3", facecolor=color, alpha=0.15,
            edgecolor=color, linewidth=2,
        )
        ax.add_patch(rect)
        ax.text(5, 8.5, title, ha="center", va="center", fontsize=13,
                fontweight="bold", color=color)
        ax.text(5, 4.5, "\n".join(desc_lines), ha="center", va="center",
                fontsize=10, color="#333", family="monospace")

    fig.suptitle("Margin Modes Comparison", fontsize=14, fontweight="bold",
                 y=1.02)
    fig.tight_layout()
    return _save(fig, "margin_modes.png")


def create_risk_management_diagram():
    """Checklist-style diagram of risk management best practices."""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    fig.patch.set_facecolor("#f9f9f9")
    ax.axis("off")

    items = [
        ("✓", "Start with small position sizes", "#4CAF50"),
        ("✓", "Always set a Stop-Loss order", "#4CAF50"),
        ("✓", "Use low leverage (2-5×) as a beginner", "#FF9800"),
        ("✓", "Monitor your liquidation price", "#FF9800"),
        ("✓", "Understand maker/taker fees", "#2196F3"),
        ("✓", "Practice on a demo/testnet first", "#2196F3"),
        ("✗", "Never risk more than you can afford to lose", "#F44336"),
    ]

    y = 0.92
    for check, text, color in items:
        ax.text(0.08, y, check, transform=ax.transAxes, fontsize=16,
                fontweight="bold", color=color, va="center")
        ax.text(0.15, y, text, transform=ax.transAxes, fontsize=12,
                va="center", color="#333")
        y -= 0.125

    ax.set_title("Risk Management Checklist", fontsize=14,
                 fontweight="bold", pad=16)
    return _save(fig, "risk_management.png")


# ---------------------------------------------------------------------------
# Document builder
# ---------------------------------------------------------------------------

def _heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)
    return h


def _para(doc, text, bold=False):
    p = doc.add_paragraph()
    run = p.add_run(textwrap.dedent(text).strip())
    run.font.size = Pt(11)
    if bold:
        run.bold = True
    return p


def build_document(images):
    """Assemble the .docx document with text and images."""
    doc = Document()

    # -- Title --
    title = doc.add_heading("How to Trade Using Binance Futures", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in title.runs:
        run.font.color.rgb = RGBColor(0xF0, 0xB9, 0x0B)

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run(
        "Video Summary & Guide\n"
        "Source: https://www.youtube.com/watch?v=SvXEAj7Mb48"
    )
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_paragraph()  # spacer

    # -- Introduction --
    _heading(doc, "Introduction")
    _para(doc, """
        This document summarises the key points from the YouTube video
        "How to Trade Using Binance Futures". Binance Futures is a
        cryptocurrency derivatives platform that allows traders to speculate
        on the future price of digital assets using leverage. The platform
        supports both long (buy) and short (sell) positions, enabling
        traders to profit in both rising and falling markets.
    """)

    # -- 1. Account Setup --
    _heading(doc, "1. Account Setup & Funding")
    doc.add_picture(images["account_setup"], width=Inches(5.5))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    _para(doc, """
        Step 1 – Sign Up & Verify: Create a Binance account at binance.com
        and complete identity verification (KYC) as required by your
        jurisdiction.

        Step 2 – Enable Futures Trading: Navigate to the "Derivatives" menu
        and activate your Binance Futures account. You may need to pass a
        short quiz about futures trading risks.

        Step 3 – Deposit Funds: Add funds (e.g., USDT, BUSD) to your Spot
        wallet via bank transfer, credit card, or peer-to-peer trading.

        Step 4 – Transfer to Futures Wallet: Use the in-platform "Transfer"
        button to move assets from your Spot wallet into your Futures wallet
        so they are available as margin for your trades.
    """)

    # -- 2. Understanding Futures Contracts --
    _heading(doc, "2. Understanding Futures Contracts")
    _para(doc, """
        Futures contracts let you speculate on an asset's future price
        without owning the underlying cryptocurrency. Binance offers two
        main types:

        • USDT-Margined (USDT-M): Settled in USDT. The most popular choice
          for beginners because profit and loss are denominated in a stable
          asset.

        • Coin-Margined (COIN-M): Settled in the cryptocurrency itself
          (e.g., BTC). Useful for holders who want to hedge or increase
          their crypto exposure.

        Each contract has an expiry date (quarterly) or can be "perpetual"
        (no expiry). Perpetual contracts use a funding-rate mechanism to
        keep prices close to the spot market.
    """)

    # -- 3. The Trading Interface --
    _heading(doc, "3. Using the Trading Interface")
    _heading(doc, "Order Types", level=2)
    doc.add_picture(images["order_types"], width=Inches(5.0))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    _para(doc, """
        Market Order – Executes immediately at the best available price.
        Ideal when speed matters more than the exact entry price.

        Limit Order – You set the price at which you want to buy or sell.
        The order only fills when the market reaches your specified price,
        giving you full control over entry/exit.

        Stop-Limit / Stop-Market Order – Combines a trigger price (stop)
        with a limit or market order. Commonly used for setting stop-losses
        or automated entries at key price levels.
    """)

    # -- 4. Leverage --
    _heading(doc, "4. Leverage")
    doc.add_picture(images["leverage_risk"], width=Inches(5.0))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    _para(doc, """
        Leverage allows you to control a larger position with a smaller
        amount of capital. Binance Futures offers leverage from 1× up to
        125× depending on the trading pair.

        Example: With 10× leverage and $100 margin, you control a $1,000
        position. A 5 % price move in your favour yields a 50 % gain,
        but the same move against you results in a 50 % loss.

        Key tip from the video: beginners should start with low leverage
        (2–5×) to limit risk while learning how the platform works.
    """)

    # -- 5. Margin Modes --
    _heading(doc, "5. Margin Modes: Cross vs Isolated")
    doc.add_picture(images["margin_modes"], width=Inches(5.5))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    _para(doc, """
        Cross Margin: Your entire Futures wallet balance serves as margin
        for all open positions. This lowers the chance of liquidation on
        any single position but puts your full balance at risk.

        Isolated Margin: Each position has its own dedicated margin. If
        the position is liquidated you only lose the margin allocated to
        that specific trade, protecting the rest of your balance.

        The video recommends Isolated Margin for beginners as it provides
        clearer risk boundaries.
    """)

    # -- 6. Opening & Managing Trades --
    _heading(doc, "6. Opening & Managing Trades")
    _para(doc, """
        1. Select a trading pair (e.g., BTCUSDT Perpetual).
        2. Choose your margin mode (Cross or Isolated) and leverage level.
        3. Decide on your direction:
           • Long (Buy) – you expect the price to rise.
           • Short (Sell) – you expect the price to fall.
        4. Enter the order size and choose an order type.
        5. Click "Buy/Long" or "Sell/Short" to open the position.

        Once the position is open, monitor it in the "Positions" tab at
        the bottom of the trading interface. Key metrics include:
        • Entry Price – the price at which you entered.
        • Mark Price – the current fair-value price used for PnL.
        • Liquidation Price – the price at which your margin is exhausted.
        • Unrealised PnL – your current floating profit or loss.
    """)

    # -- 7. Risk Management --
    _heading(doc, "7. Risk Management")
    doc.add_picture(images["risk_management"], width=Inches(5.0))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    _para(doc, """
        The video stresses that risk management is the most important
        aspect of futures trading:

        • Always use Stop-Loss orders to cap potential losses.
        • Set Take-Profit orders to lock in gains at target levels.
        • Start with very small position sizes until you are comfortable.
        • Use the Binance Futures testnet / demo account for practice
          before risking real funds.
        • Understand the fee structure: Binance uses a maker/taker model
          where limit orders (maker) typically pay lower fees than market
          orders (taker).
        • Never risk capital you cannot afford to lose – futures trading
          with leverage is inherently high-risk.
    """)

    # -- 8. Summary --
    _heading(doc, "8. Key Takeaways")
    _para(doc, """
        1. Binance Futures lets you trade crypto derivatives with leverage,
           profiting from both rising and falling markets.
        2. Set up your account, verify your identity, and transfer funds
           to your Futures wallet before trading.
        3. Understand the differences between Market, Limit, and Stop
           orders to pick the right tool for each situation.
        4. Start with low leverage and Isolated Margin mode to limit risk.
        5. Always set Stop-Loss and Take-Profit orders for every trade.
        6. Practice on the testnet before using real money.
        7. Continuously educate yourself – the crypto market moves fast.
    """)

    # -- Disclaimer --
    doc.add_paragraph()
    disc = doc.add_paragraph()
    disc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = disc.add_run(
        "Disclaimer: This document is for educational purposes only and does "
        "not constitute financial advice. Cryptocurrency futures trading "
        "involves substantial risk of loss. Always do your own research."
    )
    run.font.size = Pt(9)
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    doc.save(DOCX_PATH)
    print(f"Document saved to {DOCX_PATH}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Generating images …")
    images = {
        "account_setup": create_account_setup_diagram(),
        "order_types": create_order_types_chart(),
        "leverage_risk": create_leverage_risk_chart(),
        "margin_modes": create_margin_modes_diagram(),
        "risk_management": create_risk_management_diagram(),
    }

    for name, path in images.items():
        print(f"  ✓ {name}: {path}")

    print("\nBuilding .docx document …")
    build_document(images)
    print("Done!")


if __name__ == "__main__":
    main()
