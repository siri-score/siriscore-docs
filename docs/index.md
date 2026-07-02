# SiriScore

**Pre-broadcast Bitcoin transaction privacy analysis.**

Paste a PSBT, raw tx hex, or txid — get a scored privacy report with actionable findings before you sign.

<div class="grid cards" markdown>

- :material-web: **[Live tool](https://siriscore.xyz)** — analyse a transaction right now
- :material-package-variant: **[pip install siriscore](getting-started/install.md)** — use as a Python library
- :material-console: **[CLI](getting-started/install.md#cli)** — `btc-privacy-check --txid <txid>`
- :material-api: **[REST API](api/score.md)** — integrate into your wallet or service

</div>

## How it works

SiriScore runs up to 11 privacy heuristics against a transaction and produces a score from 0–100:

- **Penalty heuristics (H1–H8)** deduct from the score when a privacy issue is detected
- **Positive heuristics (H9–H11)** add to the score or suppress false positives when coinjoin or Payjoin patterns are detected

The score formula: `min(100, max(0, 100 − sum(penalty weights) + sum(bonus weights)))`

H8 (tainted UTXO) additionally caps the score at 40 regardless of other heuristics.

## Privacy by default

No transaction data leaves your machine unless you explicitly enable network checks (`lookup=True`). When network checks are on, only [mempool.space](https://mempool.space) is queried (with blockstream.info as fallback). You can point at your own Bitcoin node to avoid all third-party exposure entirely.

→ [Privacy guarantee](library/privacy-guarantee.md)
