# Silent payments (BIP-352)

Silent payments detection is not a standalone heuristic — it is built into [H3 (address reuse)](h3-address-reuse.md).

## How it works

When H3 detects address reuse on an input, it also checks whether any output pays to a BIP-352 silent payment address (identified by the `sp1q` / `tsp1q` prefix).

- **Recipient already supports silent payments** — H3's suggestion reads: *"Recipient supports silent payments. Future payments to this recipient will not reuse addresses."*
- **Recipient does not support silent payments** — H3 suggests requesting a silent payment address to eliminate reuse permanently.

## What is a silent payment address

[BIP-352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki) silent payment addresses are static addresses that derive a unique one-time on-chain output per payment. The recipient scans the chain without publishing a fresh address per transaction.

Silent payment addresses start with `sp1q` (mainnet) or `tsp1q` (testnet/regtest).

## Scoring effect

Silent payment awareness does not change H3's weight (20) or severity (Critical). It adjusts the suggestion text only.
