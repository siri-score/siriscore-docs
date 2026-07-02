# Privacy guarantee

SiriScore is designed so that no transaction data leaves your machine by default.

## What makes network calls

| Heuristic | What is sent | Destination |
|-----------|-------------|-------------|
| H3 — Address reuse | Each input address | mempool.space (blockstream.info fallback) |
| H4 — UTXO age clustering | Each input's prevout txid | mempool.space (blockstream.info fallback) |

Network checks are **opt-out by default** — they only run when you explicitly pass `lookup=True` (library / CLI) or toggle on "Enable network checks" (web UI).

All other heuristics (H1, H2, H5, H6, H7, H8, H9, H10, H11) run entirely offline against the transaction data you provide.

## Point at your own node

To run H3 and H4 without sending anything to a third party, configure your own Bitcoin Core node:

```bash
# bitcoin.conf
txindex=1

# CLI
btc-privacy-check --txid <txid> \
  --rpc-url http://127.0.0.1:8332 \
  --rpc-user alice \
  --rpc-password hunter2
```

```python
# Library
report = siriscore.score(
    txid,
    rpc_url="http://127.0.0.1:8332",
    rpc_user="alice",
    rpc_password="hunter2",
)
```

When `rpc_url` is set, all network lookups go to your node. No data reaches mempool.space or blockstream.info.

!!! note
    H3 (address reuse) is automatically skipped when using RPC mode because Bitcoin Core's RPC does not expose a full address transaction history index by default. H4 (UTXO age) still runs via `gettxout` / block height lookups.

## Label store

Labels are stored in `~/.utxo-privacy-scorer/labels.db` — a local SQLite file. No cloud sync, no telemetry.

## The web app at siriscore.xyz

When you use the hosted tool at siriscore.xyz, your PSBT or txid is sent to the siriscore.xyz server over HTTPS. For maximum privacy, run the server locally instead.

→ [Run locally](../getting-started/run-locally.md)
