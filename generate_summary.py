#!/usr/bin/env python3
"""
generate_summary.py

Generates a .docx summary document for the YouTube video
"How to Day Trade Crypto" (https://www.youtube.com/watch?v=z4vYaD6xLT8).

The script creates illustrative charts and diagrams, then assembles them
into a formatted Word document (.docx) that can be opened in Google Docs.

Usage:
    pip install -r requirements.txt
    python generate_summary.py

Output:
    How_to_Day_Trade_Crypto_Summary.docx
"""

import os
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ---------------------------------------------------------------------------
# Image generation helpers
# ---------------------------------------------------------------------------

def _img_path(name: str, img_dir: str) -> str:
    return os.path.join(img_dir, name)


def create_candlestick_chart(img_dir: str) -> str:
    """Create a sample Bitcoin candlestick chart with a moving average."""
    path = _img_path("candlestick_chart.png", img_dir)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    np.random.seed(42)
    n = 30
    dates = np.arange(n)
    price = 45000.0
    opens, closes, highs, lows = [], [], [], []
    for _ in range(n):
        change = np.random.normal(0, 800)
        o = price
        c = price + change
        h = max(o, c) + abs(np.random.normal(0, 400))
        l = min(o, c) - abs(np.random.normal(0, 400))
        opens.append(o)
        closes.append(c)
        highs.append(h)
        lows.append(l)
        price = c

    for i in range(n):
        color = "#00ff88" if closes[i] >= opens[i] else "#ff4444"
        ax.plot([dates[i], dates[i]], [lows[i], highs[i]], color=color, linewidth=1)
        ax.bar(
            dates[i],
            closes[i] - opens[i],
            bottom=min(opens[i], closes[i]),
            color=color,
            width=0.6,
            alpha=0.9,
        )

    ma = np.convolve(closes, np.ones(7) / 7, mode="valid")
    ax.plot(dates[6:], ma, color="#ffd700", linewidth=2, label="7-Period MA", alpha=0.8)

    ax.set_title(
        "Bitcoin (BTC/USD) - Candlestick Chart Example",
        color="white", fontsize=14, fontweight="bold", pad=15,
    )
    ax.set_xlabel("Trading Period", color="white", fontsize=11)
    ax.set_ylabel("Price (USD)", color="white", fontsize=11)
    ax.tick_params(colors="white")
    ax.legend(facecolor="#16213e", edgecolor="white", labelcolor="white")
    ax.grid(True, alpha=0.2, color="white")
    for spine in ax.spines.values():
        spine.set_color("#333")

    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    return path


def create_trading_strategies_diagram(img_dir: str) -> str:
    """Create a visual diagram of core day-trading strategies."""
    path = _img_path("trading_strategies.png", img_dir)
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(5, 9.5, "Core Day Trading Strategies", fontsize=18, fontweight="bold",
            ha="center", color="#1a1a2e")

    top = [
        ("Scalping", "Quick trades for small\nprofits (seconds to minutes)", "#00b894", 1.5),
        ("Momentum\nTrading", "Ride strong trends with\nhigh volume confirmation", "#0984e3", 5.0),
        ("Range\nTrading", "Buy at support, sell at\nresistance in sideways markets", "#6c5ce7", 8.5),
    ]
    for name, desc, color, x in top:
        rect = mpatches.FancyBboxPatch(
            (x - 1.3, 5.8), 2.6, 2.8, boxstyle="round,pad=0.15",
            facecolor=color, edgecolor="white", alpha=0.9,
        )
        ax.add_patch(rect)
        ax.text(x, 8.0, name, fontsize=12, fontweight="bold", ha="center", va="center", color="white")
        ax.text(x, 6.7, desc, fontsize=9, ha="center", va="center", color="white")

    bottom = [
        ("Breakout Trading", "Enter when price breaks\nthrough support/resistance levels", "#e17055", 2.5),
        ("News-Based Trading", "React to major crypto news,\nregulations, and announcements", "#fdcb6e", 7.5),
    ]
    for name, desc, color, x in bottom:
        rect = mpatches.FancyBboxPatch(
            (x - 1.8, 2.5), 3.6, 2.5, boxstyle="round,pad=0.15",
            facecolor=color, edgecolor="white", alpha=0.9,
        )
        ax.add_patch(rect)
        tc = "white" if color != "#fdcb6e" else "#1a1a2e"
        ax.text(x, 4.3, name, fontsize=12, fontweight="bold", ha="center", va="center", color=tc)
        ax.text(x, 3.2, desc, fontsize=9, ha="center", va="center", color=tc)

    for x in [1.5, 5.0, 8.5]:
        ax.annotate("", xy=(x, 5.8), xytext=(5, 5.4),
                    arrowprops=dict(arrowstyle="->", color="#636e72", lw=1.5))

    ax.text(5, 1.2, "Key: All strategies require strict risk management & stop-loss orders",
            fontsize=10, ha="center", style="italic", color="#636e72")

    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()
    return path


def create_risk_management_infographic(img_dir: str) -> str:
    """Create a risk-management infographic."""
    path = _img_path("risk_management.png", img_dir)
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(5, 6.5, "Risk Management Essentials", fontsize=18, fontweight="bold",
            ha="center", color="#2d3436")

    items = [
        ("1. Stop-Loss Orders", "Set automatic exit points to limit potential losses", "#e74c3c"),
        ("2. Position Sizing", "Never risk more than 1-2% of your portfolio per trade", "#3498db"),
        ("3. Take-Profit Levels", "Lock in gains by setting predetermined exit targets", "#2ecc71"),
        ("4. Emotional Control", "Stick to your plan, avoid revenge trading after losses", "#9b59b6"),
    ]
    for i, (title, desc, color) in enumerate(items):
        y = 5.0 - i * 1.3
        rect = mpatches.FancyBboxPatch(
            (0.5, y - 0.4), 9, 1.0, boxstyle="round,pad=0.1",
            facecolor=color, edgecolor="white", alpha=0.15,
        )
        ax.add_patch(rect)
        bar = mpatches.FancyBboxPatch(
            (0.5, y - 0.4), 0.15, 1.0, boxstyle="round,pad=0",
            facecolor=color, edgecolor="none",
        )
        ax.add_patch(bar)
        ax.text(1.2, y + 0.2, title, fontsize=13, fontweight="bold", va="center", color=color)
        ax.text(1.2, y - 0.15, desc, fontsize=10, va="center", color="#636e72")

    ax.text(5, 0.3,
            '"The goal is to protect your capital so you can trade another day."',
            fontsize=10, ha="center", style="italic", color="#636e72")

    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="#f8f9fa")
    plt.close()
    return path


def create_technical_indicators_chart(img_dir: str) -> str:
    """Create a multi-panel chart showing Bollinger Bands, RSI and Volume."""
    path = _img_path("technical_indicators.png", img_dir)
    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=(10, 8), gridspec_kw={"height_ratios": [3, 1, 1]},
    )
    fig.patch.set_facecolor("#1a1a2e")

    np.random.seed(42)
    n = 100
    t = np.arange(n)
    price = 45000 + np.cumsum(np.random.normal(0, 300, n)) + 2000 * np.sin(t / 15)

    # Bollinger Bands
    ax1.set_facecolor("#16213e")
    ma20 = np.convolve(price, np.ones(20) / 20, mode="same")
    std20 = np.array([np.std(price[max(0, i - 20): i + 1]) for i in range(n)])
    upper = ma20 + 2 * std20
    lower = ma20 - 2 * std20

    ax1.fill_between(t, lower, upper, alpha=0.15, color="#74b9ff")
    ax1.plot(t, price, color="#00ff88", linewidth=1.5, label="BTC Price")
    ax1.plot(t, ma20, color="#ffd700", linewidth=1.2, label="20-Period MA", linestyle="--")
    ax1.plot(t, upper, color="#74b9ff", linewidth=0.8, alpha=0.7, label="Bollinger Bands")
    ax1.plot(t, lower, color="#74b9ff", linewidth=0.8, alpha=0.7)
    ax1.set_title("Technical Analysis Indicators - BTC/USD", color="white", fontsize=13, fontweight="bold")
    ax1.set_ylabel("Price (USD)", color="white", fontsize=10)
    ax1.legend(facecolor="#16213e", edgecolor="white", labelcolor="white", fontsize=8)
    ax1.tick_params(colors="white")
    ax1.grid(True, alpha=0.15, color="white")
    for s in ax1.spines.values():
        s.set_color("#333")

    # RSI
    ax2.set_facecolor("#16213e")
    delta = np.diff(price)
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = np.convolve(gain, np.ones(14) / 14, mode="same")
    avg_loss = np.convolve(loss, np.ones(14) / 14, mode="same")
    rs = avg_gain / (avg_loss + 1e-10)
    rsi = 100 - (100 / (1 + rs))

    ax2.plot(t[1:], rsi, color="#a29bfe", linewidth=1.2)
    ax2.axhline(y=70, color="#ff4444", linestyle="--", alpha=0.7, linewidth=0.8)
    ax2.axhline(y=30, color="#00ff88", linestyle="--", alpha=0.7, linewidth=0.8)
    ax2.fill_between(t[1:], rsi, 70, where=rsi > 70, alpha=0.3, color="#ff4444")
    ax2.fill_between(t[1:], rsi, 30, where=rsi < 30, alpha=0.3, color="#00ff88")
    ax2.set_ylabel("RSI", color="white", fontsize=10)
    ax2.set_ylim(0, 100)
    ax2.tick_params(colors="white")
    ax2.grid(True, alpha=0.15, color="white")
    for s in ax2.spines.values():
        s.set_color("#333")

    # Volume
    ax3.set_facecolor("#16213e")
    volume = np.abs(np.random.normal(1000, 300, n))
    colors_v = ["#00ff88" if price[i] >= price[max(0, i - 1)] else "#ff4444" for i in range(n)]
    ax3.bar(t, volume, color=colors_v, alpha=0.7, width=0.8)
    ax3.set_ylabel("Volume", color="white", fontsize=10)
    ax3.set_xlabel("Trading Period", color="white", fontsize=10)
    ax3.tick_params(colors="white")
    ax3.grid(True, alpha=0.15, color="white")
    for s in ax3.spines.values():
        s.set_color("#333")

    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()
    return path


# ---------------------------------------------------------------------------
# Document builder
# ---------------------------------------------------------------------------

def build_document(img_dir: str, output_path: str) -> None:
    """Assemble the summary document with text and images."""
    doc = Document()

    # Page setup
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    # Helper to add a centered image with a caption
    def _add_image(image_path: str, caption_text: str, width: float = 5.5):
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture(image_path, width=Inches(width))
        cap = doc.add_paragraph(caption_text)
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in cap.runs:
            r.font.size = Pt(9)
            r.font.italic = True
            r.font.color.rgb = RGBColor(0x63, 0x6E, 0x72)
        doc.add_paragraph()

    # ----- Title -----
    title = doc.add_heading("How to Day Trade Crypto", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in title.runs:
        r.font.size = Pt(26)
        r.font.color.rgb = RGBColor(0x1A, 0x1A, 0x2E)

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = sub.add_run("Video Summary & Key Takeaways")
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0x63, 0x6E, 0x72)
    r.font.italic = True

    src = doc.add_paragraph()
    src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = src.add_run("Source: ")
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x63, 0x6E, 0x72)
    r = src.add_run("https://www.youtube.com/watch?v=z4vYaD6xLT8")
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x09, 0x84, 0xE3)
    r.font.underline = True
    doc.add_paragraph()

    # ----- Overview -----
    doc.add_heading("Overview", level=1)
    doc.add_paragraph(
        'This document summarizes the YouTube video "How to Day Trade Crypto," which '
        "provides a comprehensive beginner's guide to day trading in the cryptocurrency "
        "market. The video covers essential concepts including what crypto day trading is, "
        "how to choose the right platform, core trading strategies, technical analysis "
        "tools, and critical risk management practices."
    )

    # ----- 1. What Is Crypto Day Trading? -----
    doc.add_heading("1. What Is Crypto Day Trading?", level=1)
    doc.add_paragraph(
        "Day trading involves buying and selling cryptocurrencies within the same day "
        "(or even within minutes or hours) to profit from short-term price movements. "
        "Unlike traditional stock markets that operate during fixed hours, crypto markets "
        "are open 24 hours a day, 7 days a week."
    )
    for b in [
        "Positions are opened and closed within the same trading day",
        "Profits come from short-term price volatility, not long-term holding",
        "The 24/7 nature of crypto markets means opportunities are always available",
        "High volatility creates both significant opportunity and risk",
        "Requires active monitoring and quick decision-making",
    ]:
        doc.add_paragraph(b, style="List Bullet")

    # ----- 2. Choosing a Platform -----
    doc.add_heading("2. Choosing a Reliable Trading Platform", level=1)
    doc.add_paragraph(
        "Selecting the right exchange is one of the most important first steps. "
        "A good platform can make the difference between a smooth trading experience "
        "and costly mistakes."
    )
    for t_text, desc in [
        ("High Liquidity", "Ensures quick entry/exit without significant price slippage."),
        ("Low Trading Fees", "Frequent trading means fees add up — look for volume discounts."),
        ("Strong Security", "2FA, cold storage, and regulatory compliance are essential."),
        ("Advanced Charting Tools", "Built-in indicators and real-time charts are crucial."),
        ("User-Friendly Interface", "Reduces costly errors during fast-moving markets."),
    ]:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(t_text + ": ")
        r.bold = True
        p.add_run(desc)

    # ----- 3. Trading Plan -----
    doc.add_heading("3. The Importance of a Trading Plan", level=1)
    doc.add_paragraph(
        "Successful day trading starts with a well-defined trading plan. "
        "Trading without a plan is essentially gambling."
    )
    for t_text, desc in [
        ("Entry Criteria", "Specific conditions before opening a trade."),
        ("Exit Criteria", "Predetermined conditions for closing — profits and losses."),
        ("Risk Parameters", "Max loss per trade (typically 1-2% of portfolio) and per day."),
        ("Position Sizing Rules", "Capital allocation based on confidence and risk tolerance."),
        ("Trading Schedule", "Defined hours and rules for stepping away."),
        ("Record Keeping", "A journal logging every trade, rationale, and outcome."),
    ]:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(t_text + ": ")
        r.bold = True
        p.add_run(desc)

    # ----- 4. Technical Analysis -----
    doc.add_heading("4. Mastering Technical Analysis", level=1)
    doc.add_paragraph(
        "Technical analysis is the backbone of crypto day trading — studying historical "
        "price data, chart patterns, and statistical indicators to forecast future price "
        "movements."
    )
    _add_image(
        os.path.join(img_dir, "candlestick_chart.png"),
        "Figure 1: Example Bitcoin candlestick chart with 7-period moving average",
    )

    doc.add_paragraph(
        "Candlestick charts display Open, Close, High, and Low prices. "
        "Green candles are bullish (price up); red candles are bearish (price down)."
    )

    _add_image(
        os.path.join(img_dir, "technical_indicators.png"),
        "Figure 2: Technical indicators — Bollinger Bands, RSI, and Volume",
    )

    for t_text, desc in [
        ("Moving Averages (MA)", "Smooth price data to show trend direction."),
        ("RSI", "Momentum oscillator (0-100); >70 overbought, <30 oversold."),
        ("MACD", "Tracks relationship between two MAs to signal trend changes."),
        ("Bollinger Bands", "Show volatility; squeezes often precede big moves."),
        ("Volume Analysis", "High volume confirms the strength of a price move."),
    ]:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(t_text + ": ")
        r.bold = True
        p.add_run(desc)

    # ----- 5. Strategies -----
    doc.add_heading("5. Core Day Trading Strategies", level=1)
    doc.add_paragraph(
        "Several proven strategies are outlined; successful traders often combine "
        "multiple approaches depending on market conditions."
    )
    _add_image(
        os.path.join(img_dir, "trading_strategies.png"),
        "Figure 3: Overview of core crypto day trading strategies",
    )
    for t_text, desc in [
        ("Scalping", "Rapid trades lasting seconds to minutes for small, repeated gains."),
        ("Momentum Trading", "Ride strong trends confirmed by volume surges or news."),
        ("Range Trading", "Buy at support, sell at resistance in sideways markets."),
        ("Breakout Trading", "Enter when price moves decisively past support/resistance."),
        ("News-Based Trading", "React to major announcements — regulations, listings, etc."),
    ]:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(t_text + ": ")
        r.bold = True
        p.add_run(desc)

    # ----- 6. Risk Management -----
    doc.add_heading("6. Risk Management", level=1)
    doc.add_paragraph(
        "Protecting your capital is more important than making profits. "
        "Many beginners fail not from bad strategies but from poor risk management."
    )
    _add_image(
        os.path.join(img_dir, "risk_management.png"),
        "Figure 4: The four pillars of risk management for crypto day trading",
    )
    for t_text, desc in [
        ("Stop-Loss Orders", "Automatically close positions that move against you."),
        ("Position Sizing", "Never risk more than 1-2% of capital on one trade."),
        ("Take-Profit Levels", "Lock in gains with predetermined exit targets."),
        ("Daily Loss Limits", "Stop trading for the day if you hit your max loss."),
        ("Leverage Caution", "Beginners should avoid high leverage (start at 2-3x max)."),
    ]:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(t_text + ": ")
        r.bold = True
        p.add_run(desc)

    # ----- 7. Emotional Discipline -----
    doc.add_heading("7. Emotional Discipline & Psychology", level=1)
    doc.add_paragraph(
        "Day trading is as much a psychological challenge as a technical one."
    )
    for t_text, desc in [
        ("FOMO", "Jumping in impulsively without analysis."),
        ("Revenge Trading", "Taking bigger risks to recover losses — usually backfires."),
        ("Overconfidence", "Abandoning the plan after a winning streak."),
        ("Analysis Paralysis", "Over-analyzing to the point of inaction."),
    ]:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(t_text + ": ")
        r.bold = True
        p.add_run(desc)

    # ----- 8. Getting Started -----
    doc.add_heading("8. Getting Started — Practical Steps", level=1)
    for step in [
        "Educate yourself before risking real money.",
        "Practice with a demo / paper trading account.",
        "Choose a reputable exchange with low fees and strong security.",
        "Start with a small amount you can afford to lose.",
        "Focus on one or two trading pairs (e.g., BTC/USDT).",
        "Follow a written trading plan with clear rules.",
        "Keep a detailed trading journal.",
        "Start with simple strategies before advancing.",
        "Continuously review and refine your approach.",
        "Never stop learning — crypto markets evolve rapidly.",
    ]:
        doc.add_paragraph(step, style="List Number")

    # ----- Conclusion -----
    doc.add_heading("Conclusion", level=1)
    doc.add_paragraph(
        "Success in crypto day trading requires education, discipline, a solid plan, "
        "mastery of technical analysis, and rigorous risk management. Start small, "
        "practice with paper trading, and never risk more than you can afford to lose."
    )

    # ----- References -----
    doc.add_heading("References", level=1)
    for ref in [
        '"How to Day Trade Crypto" — https://www.youtube.com/watch?v=z4vYaD6xLT8',
        'Mitrade — "How to Day Trade Crypto? Simplest Day Trading Strategy Ever"',
        'Margex — "Best Crypto Day Trading Strategies: A Trader\'s Guide"',
        'Finder — "How to Day Trade Crypto | Day Trading Strategies"',
        'BeInCrypto — "How To Trade Cryptocurrency: A Step-by-Step Beginners Guide"',
        'Coin Bureau — "The Ultimate Beginner\'s Guide to Successful Crypto Day Trading"',
    ]:
        doc.add_paragraph(ref, style="List Bullet")

    doc.save(output_path)
    print(f"Document saved to {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = tempfile.mkdtemp(prefix="crypto_imgs_")

    print("Generating images …")
    create_candlestick_chart(img_dir)
    create_trading_strategies_diagram(img_dir)
    create_risk_management_infographic(img_dir)
    create_technical_indicators_chart(img_dir)

    output = os.path.join(script_dir, "How_to_Day_Trade_Crypto_Summary.docx")
    print("Building document …")
    build_document(img_dir, output)
    print("Done!")


if __name__ == "__main__":
    main()
