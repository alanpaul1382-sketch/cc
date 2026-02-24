# Hedging Strategies for Symmetrical Triangle Breakouts — Video Summary

## Overview

This video explains **hedging** — a technique that allows traders to profit from a breakout regardless of its direction. The presenter uses a symmetrical triangle pattern as the primary example and walks through three distinct hedging methods, followed by a practical demonstration on Binance Futures.

> **Prerequisite:** The strategies discussed are advanced. A solid understanding of technical analysis (support/resistance, chart patterns, order types) is assumed.

---

## What Is Hedging?

Hedging means **protecting your profits against an adverse move** by holding both a long and a short position on the same asset at the same time. When a symmetrical triangle forms — where the breakout direction is uncertain but the move is expected to be strong — hedging lets you capture that move either way.

---

## Three Hedging Methods

### Method 1 — Buy Stop & Sell Stop (Pending Orders)

1. Identify support and resistance lines at the edges of the triangle.
2. Place a **buy stop** (long entry) just above resistance.
3. Place a **sell stop** (short entry) just below support.
4. Set the stop-loss for the long at support, and for the short at resistance.
5. When price breaks one direction, the corresponding order triggers; you then **cancel** the untriggered order.

| Pros | Cons |
|------|------|
| You only enter the trade that wins the breakout. | A whipsaw (false breakout) can trigger one order, stop you out, trigger the other, and stop you out again — losing on both sides. |

### Method 2 — Simultaneous Long & Short with Small Stops

1. Near the triangle's apex, open **both** a long and a short at the same price.
2. Use a **small stop-loss** on each (e.g., 1 unit risk).
3. Set a larger take-profit on each (e.g., 5 units reward).
4. One side will be stopped out (small loss); the other should hit its target (large gain), yielding a **net profit** (e.g., 5 − 1 = 4).

| Pros | Cons |
|------|------|
| Guaranteed entry in the winning direction. | Requires at least a 3 : 1 reward-to-risk ratio on both sides to be worthwhile. Not always achievable. |

### Method 3 — Biased Entry with a Hedge Recovery

1. Choose a **directional bias** (e.g., long, because the prior trend was up).
2. Enter that trade with a normal stop-loss.
3. Simultaneously set a **sell stop** further below as a hedge: if the bias is wrong and the stop is hit, the sell stop opens a short to **recover** the loss on the ride down.
4. The same logic can be applied to **supply/demand zones** or order blocks.

| Pros | Cons |
|------|------|
| You trade your bias first and only hedge if wrong. | Requires precise entry and level selection — recommended for advanced traders only. |

---

## Binance Futures Setup

1. Go to **USDT-M Futures** → three-dot menu → **Position Mode** → select **Hedge Mode** and confirm (no open positions required).
2. This enables **Open / Close** tabs, allowing simultaneous long and short positions on the same pair.
3. **Market or Limit orders** — use the "Open" tab to enter both directions; tick the TP/SL box to set take-profit and stop-loss in one step.
4. **Stop Market orders** — use "Stop Market" to place buy stops above price and sell stops below price; TP/SL must be added separately afterward.

---

## Key Takeaways

- A symmetrical triangle signals a strong upcoming breakout but does **not** indicate direction.
- Hedging lets you capture the breakout **either way** by holding opposing positions.
- All three methods carry risk; the worst-case scenario is being stopped out on both sides.
- Proper hedging requires **advanced** knowledge of entries, stop placement, and risk management.
- Always confirm your position mode, margin type (cross/isolated), and leverage before placing orders.
