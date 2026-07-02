# H7 — Non-BIP69 ordering

**Severity:** Info · **Weight:** 5 · **Network:** No

## What it detects

The inputs or outputs are not sorted according to [BIP69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki) (lexicographic ordering of inputs by txid/vout, outputs by value/script).

## Why it matters

Non-deterministic ordering leaks information about which output is change. The change output is often appended last by wallets that do not randomise output ordering. BIP69 standardises the order so that ordering alone reveals nothing.

## What to do

Use a wallet that implements BIP69 output ordering, or one that randomises output order. Most modern wallets do one or the other.

## Note

This is an informational finding with a low weight (5). It is unlikely to be the deciding factor in a score but is worth addressing alongside other findings.
