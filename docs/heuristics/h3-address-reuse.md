# H3 — Address reuse on input

**Severity:** Critical · **Weight:** 20 · **Network:** Yes

## What it detects

One or more input addresses have been used in previous transactions (i.e. they have a transaction history on-chain).

## Why it matters

Bitcoin addresses are not meant to be reused. Each time you reuse an address, you link all transactions involving that address together — effectively creating a permanent public record connecting all your activity through that address.

## Network requirement

H3 queries mempool.space (blockstream.info fallback) for the transaction history of each input address. It is skipped when `lookup=False` (the default).

## What to do

- Generate a fresh address for every transaction
- Most modern HD wallets do this automatically — check your wallet settings
- If you reused an address, consider consolidating those UTXOs in a coinjoin before spending further

## Privacy note

Running H3 sends each input address to an external block explorer. Use `--rpc-url` to route lookups through your own node, or disable it with `lookup=False` if you do not want address data leaving your machine.
