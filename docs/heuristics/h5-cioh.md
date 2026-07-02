# H5 — High input count (CIOH)

**Severity:** Warning · **Weight:** 10 · **Network:** No

## What it detects

The transaction has 5 or more inputs. This triggers the Common Input Ownership Heuristic (CIOH): an analyst may assume all inputs are controlled by the same wallet.

## Why it matters

Consolidating many inputs in a single transaction is a common pattern that reveals wallet structure. It effectively announces "these UTXOs all belong to the same entity."

## H9/H10 suppression

When H9 or H10 fires (coinjoin input or coinjoin transaction detected), H5 is automatically suppressed. Coinjoin transactions intentionally have many inputs from different wallets — applying CIOH would be a false positive.

## What to do

- Limit consolidation to 2–4 inputs per transaction
- Consider using a coinjoin to merge UTXOs without revealing common ownership
- If you must consolidate many inputs, do it in a dedicated consolidation transaction when fees are low, rather than combining it with a payment
