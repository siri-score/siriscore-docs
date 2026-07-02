# What is SiriScore

SiriScore is a Bitcoin transaction privacy analyser. It accepts a transaction in any of three forms — PSBT (partially signed Bitcoin transaction), raw transaction hex, or a txid — and returns a privacy score from 0 to 100 along with a list of findings explaining what privacy issues were detected and how to fix them.

## Who is it for

- **Bitcoin users** who want to understand whether a transaction they are about to broadcast leaks information about their wallet
- **Wallet developers** who want to surface privacy warnings before the user signs
- **BTCPay Server operators** who want to score transactions as part of a payment flow
- **Privacy researchers** who want a programmatic interface to Bitcoin transaction analysis

## What it checks

Eleven heuristics covering the most common on-chain privacy leaks:

| Category | Examples |
|----------|---------|
| Penalty | Script type mismatch, round payment amounts, address reuse, UTXO age clustering, high input consolidation, dust inputs, non-BIP69 ordering, tainted labels |
| Positive | Coinjoin inputs, coinjoin transaction structure, Payjoin opportunity |

→ [Full heuristics reference](../heuristics/index.md)

## What it does not do

- It does not broadcast transactions
- It does not store or transmit your transactions to any third party by default
- It does not replace a full chain-analysis tool — it focuses on pre-broadcast, single-transaction analysis
