# H2 — Round payment amount

**Severity:** Warning · **Weight:** 15 · **Network:** No

## What it detects

One or more outputs have a round value in a common denomination — for example, exactly 0.01 BTC, 0.1 BTC, or 1 BTC (or their satoshi equivalents: 1,000,000 sat, 10,000,000 sat, etc.).

## Why it matters

Round amounts are a strong signal that an output is a payment rather than change. Change outputs are almost never round — they represent whatever is left after paying the recipient and fees. An analyst can identify the payment direction from this alone.

## What to do

- Use PayJoin (H11) to obscure the payment amount
- Consider splitting the payment across multiple transactions
- If using a wallet with coin control, avoid creating round change amounts
