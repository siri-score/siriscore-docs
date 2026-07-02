# H13 — nLockTime anti-fee-sniping

**Severity:** Info · **Weight:** 5 · **Network:** No

## What it detects

The transaction's `nLockTime` field is set to `0`. Most well-behaved wallets (Bitcoin Core, Sparrow, etc.) set `nLockTime` to the current block height as an anti-fee-sniping measure.

## Why it matters

`nLockTime = 0` is a wallet fingerprint. It reveals that the transaction was constructed by software that does not implement anti-fee-sniping — narrowing down which wallet or library was used. Blending in with the majority of transactions (which do set `nLockTime`) improves privacy.

Anti-fee-sniping protects against miners reorganising the chain to steal fees from recent blocks. Setting `nLockTime` to the current tip height makes the transaction invalid in any earlier block, removing the incentive to reorg.

## What to do

Use a wallet that sets `nLockTime` to the current block height. Bitcoin Core, Sparrow Wallet, and most modern wallets do this by default.

## Implementation

Fires when `tx.locktime == 0`. Low-weight (5) informational finding — reduces the score slightly but is rarely the dominant issue.
