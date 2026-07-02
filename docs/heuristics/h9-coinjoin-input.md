# H9 — Coinjoin input detection

**Severity:** Info · **Weight:** 0 · **Network:** No · **Positive:** Yes

## What it detects

One or more inputs appear to come from a previous coinjoin transaction, identified by:

- Input value matches a Whirlpool denomination: 100,000 / 1,000,000 / 5,000,000 / 50,000,000 satoshis
- Input UTXO is labelled `coinjoin` in the local label store

## Effect on scoring

H9 is a positive finding — it adds no penalty. When H9 fires:

- **H5 (CIOH) is suppressed** — a coinjoin-sourced input breaks the common-input-ownership assumption, so penalising for CIOH would be a false positive
- The finding appears green in the UI

## Why it matters

Spending a coinjoin output is a privacy-positive action — the UTXO's history is broken from its pre-coinjoin chain. Recognising this prevents the scorer from incorrectly penalising coinjoin users.

## Whirlpool denominations

| Denomination | Sats |
|-------------|------|
| 0.001 BTC | 100,000 |
| 0.01 BTC | 1,000,000 |
| 0.05 BTC | 5,000,000 |
| 0.5 BTC | 50,000,000 |
