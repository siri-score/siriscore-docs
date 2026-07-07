# Why use SiriScore

Every Bitcoin transaction is public forever. Before you broadcast one, SiriScore tells you what it reveals about you — so you can fix leaks while they can still be fixed.

## Why check before broadcasting

Once a transaction is on-chain it cannot be edited or recalled. Chain-analysis firms and curious observers apply well-known heuristics to cluster addresses, identify change outputs, and link transactions back to a single wallet. Most privacy leaks are cheap to avoid *before signing* — reorder outputs, avoid a round amount, skip a reused address — and impossible to undo afterwards.

SiriScore automates that pre-broadcast check: it runs the same style of heuristics an adversary would, and reports them to you first.

## What a transaction can leak

A few examples of what observers infer from a single transaction:

- **Which output is your change.** If one output uses the same script type as the inputs and the other doesn't, or one amount is suspiciously round, the change output — and therefore your remaining balance — is exposed.
- **That your addresses belong to one wallet.** Spending many inputs together, or paying to an address that has been used before, lets observers merge address clusters.
- **Which software built the transaction.** Input/output ordering, locktime behaviour, and dust handling fingerprint specific wallets.

Each leak SiriScore detects maps to a documented heuristic with a weight and a suggested fix.

:material-chevron-double-right: [Full heuristics reference](../heuristics/index.md)

## Who is it for

- **Bitcoin users** who want to understand whether a transaction they are about to broadcast leaks information about their wallet
- **Wallet developers** who want to surface privacy warnings before the user signs
- **BTCPay Server operators** who want to score transactions as part of a payment flow
- **Privacy researchers** who want a programmatic interface to Bitcoin transaction analysis

## What it does not do

- It does not broadcast transactions
- It does not store or transmit your transactions to any third party by default
- It does not replace a full chain-analysis tool; it focuses on pre-broadcast, single-transaction analysis

## Next steps

- [Use the web app](web-app.md): try it with no install
- [Install the library](install.md): Python API and CLI
- [Run locally](run-locally.md): keep everything on your machine
