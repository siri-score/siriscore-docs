# H8 — Tainted labelled UTXO

**Severity:** Critical · **Weight:** 25 · **Network:** No · **Score cap:** 40

## What it detects

One or more inputs match a UTXO, address, or transaction that has been imported into the local label store with a `tainted` tag.

## Why it matters

A tainted UTXO is one that is known to be linked to a problematic source — for example, a direct withdrawal from a KYC exchange, funds received from a flagged address, or a coin explicitly marked as high-risk. Spending a tainted UTXO directly links your transaction to that source.

## Score cap

When H8 fires, the final score is additionally capped at 40, regardless of how well the transaction performs on other heuristics. This reflects the severity of spending a known-tainted coin.

## Label matching

H8 checks three match types against the label store:

1. **UTXO match** — input's `txid:vout` matches a stored `output` or `input` label
2. **Address match** — input's address matches a stored `addr` label
3. **Transaction match** — input's prevout txid matches a stored `tx` label

## What to do

- Avoid spending tainted UTXOs directly into regular transactions
- Consider using a coinjoin to break the link before spending further
- Review your label store — a `tainted` tag on a transaction labels all its outputs, which may be broader than intended

→ [Label system](../labels/format.md)
→ [Importing from Sparrow](../labels/sparrow-import.md)
