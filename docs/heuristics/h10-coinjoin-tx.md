# H10 — Coinjoin structure detection

**Severity:** Info · **Weight:** −10 (bonus) · **Network:** No · **Positive:** Yes

## What it detects

The transaction being scored is itself a coinjoin, identified by one of three structural patterns:

### Whirlpool

3 or more outputs with equal values matching a Whirlpool denomination (100k / 1M / 5M / 50M sats) and at least 3 inputs.

### Wasabi / WabiSabi

5 or more equal-value outputs where the equal value is at least 10,000 sats (minimum viable coinjoin output).

### JoinMarket

Equal number of inputs and outputs (minimum 3 each) — JoinMarket uses a symmetric structure.

## Effect on scoring

H10 is a positive finding:

- **+10 score bonus** — the weight is −10, which subtracts from the penalty sum
- **H5 (CIOH) is suppressed** — coinjoin transactions are expected to have many inputs from different wallets
- Score is capped at 100

## Why it matters

A coinjoin transaction is a deliberate privacy action. Penalising it with CIOH or other heuristics would be incorrect. H10 rewards the user for participating in a coinjoin.
