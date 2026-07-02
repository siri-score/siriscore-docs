# H6 — Dust input present

**Severity:** Warning · **Weight:** 10 · **Network:** No

## What it detects

One or more inputs have a value below the dust threshold (typically 546 satoshis for P2PKH, 294 sat for P2WPKH).

## Why it matters

Dust inputs are often the result of a dust attack — an adversary sends a tiny amount to an address to link it to other UTXOs when the recipient spends the dust. Spending dust confirms to the attacker that you control the address.

## What to do

- Do not spend dust UTXOs unless you are prepared to link your wallet cluster
- Most wallets allow you to freeze or ignore dust inputs via coin control
- Consider labelling dust UTXOs and excluding them from future transactions
