# SiriScore - Bitcoin Privacy Scorer

<div class="ss-hero">
  <p class="ss-hero__tagline">Score your Bitcoin transaction's privacy <strong>before you broadcast it</strong>. Paste a PSBT, raw tx hex, or txid and get a scored report with actionable findings before you sign.</p>
  <div class="ss-hero__ctas">
    <a class="md-button md-button--primary" href="https://siriscore.xyz" target="_blank" rel="noopener noreferrer">Try the tool</a>
    <a class="md-button" href="getting-started/install/">Install the library</a>
  </div>
  <div class="ss-hero__card">
    <div class="ss-score">
      <div class="ss-score__number">82</div>
      <div class="ss-score__label">Privacy Score</div>
      <span class="ss-verdict ss-verdict--good">Good</span>
    </div>
    <div class="ss-gauge">
      <div class="ss-gauge__bar"><span class="ss-gauge__red"></span><span class="ss-gauge__amber"></span><span class="ss-gauge__green"></span></div>
      <div class="ss-gauge__dot" style="left: 82%"></div>
      <p class="ss-gauge__caption">Verdicts: <strong>Good</strong> ≥ 70 · <strong>Fair</strong> 40–69 · <strong>Poor</strong> &lt; 40</p>
    </div>
  </div>
</div>

<div class="grid cards" markdown>

- :material-web: **[Live tool](https://siriscore.xyz)**: analyse a transaction right now
- :material-package-variant: **[pip install siriscore](getting-started/install.md)**:use as a Python library
- :material-console: **[CLI](getting-started/install.md#cli)**: `btc-privacy-check --txid <txid>`
- :material-api: **[REST API](api/score.md)**: integrate into your wallet or service

</div>

## How it works

SiriScore runs up to 11 privacy heuristics against a transaction and produces a score from 0–100:

- **Penalty heuristics (H1–H8)** deduct from the score when a privacy issue is detected
- **Positive heuristics (H9–H11)** add to the score or suppress false positives when coinjoin or Payjoin patterns are detected

The score formula: `min(100, max(0, 100 − sum(penalty weights) + sum(bonus weights)))`

H8 (tainted UTXO) additionally caps the score at 40 regardless of other heuristics.

## Privacy by default

No transaction data leaves your machine unless you explicitly enable network checks (`lookup=True`). When network checks are on, only [mempool.space](https://mempool.space) is queried (with blockstream.info as fallback). You can point at your own Bitcoin node to avoid all third-party exposure entirely.

:material-chevron-double-right: [Privacy guarantee](library/privacy-guarantee.md)
