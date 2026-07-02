# H4 — UTXO age clustering

**Severity:** Warning · **Weight:** 10 · **Network:** Yes

## What it detects

Two or more inputs were confirmed within 6 blocks of each other. This suggests they were received in the same time window — a signal that they likely came from the same wallet or activity cluster.

## Why it matters

Block height is a proxy for time. Inputs confirmed close together are more likely to belong to the same wallet or to have been received in the same batch (e.g. an exchange withdrawal). This weakens the assumption that consolidating UTXOs from different sources hides their origin.

## Network requirement

H4 fetches the block height of each input's prevout transaction from mempool.space. It is skipped when `lookup=False`.

## What to do

- Avoid consolidating UTXOs received in the same time window
- Wait for more block confirmations between receive and spend
- Use a wallet with coin control to select inputs from different time periods
