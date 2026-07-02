# Heuristics overview

SiriScore runs 12 privacy checks. Penalty heuristics deduct from the score; positive heuristics add to it or suppress false positives.

## Penalty heuristics

| ID | Name | Severity | Weight | Requires network |
|----|------|----------|--------|-----------------|
| [H1](h1-script-mismatch.md) | Script type mismatch | Critical | 25 | No |
| [H2](h2-round-amount.md) | Round payment amount | Warning | 15 | No |
| [H3](h3-address-reuse.md) | Address reuse on input | Critical | 20 | **Yes** |
| [H4](h4-utxo-age.md) | UTXO age clustering | Warning | 10 | **Yes** |
| [H5](h5-cioh.md) | High input count (CIOH) | Warning | 10 | No |
| [H6](h6-dust.md) | Dust input present | Warning | 10 | No |
| [H7](h7-bip69.md) | Non-BIP69 ordering | Info | 5 | No |
| [H8](h8-tainted-label.md) | Tainted labelled UTXO | Critical | 25 + score cap at 40 | No |
| [H13](h13-nlocktime.md) | nLockTime anti-fee-sniping | Info | 5 | No |

## Positive heuristics

| ID | Name | Severity | Effect | What triggers it |
|----|------|----------|--------|-----------------|
| [H9](h9-coinjoin-input.md) | Input is a coinjoin output | Info | Suppresses H5 | Whirlpool denomination or `coinjoin` label |
| [H10](h10-coinjoin-tx.md) | Transaction is a coinjoin | Info | +10 score bonus, suppresses H5 | Whirlpool / Wasabi / JoinMarket structure |
| [H11](h11-payjoin.md) | Payjoin opportunity | Info / Warning | No penalty | BIP-21 URI with `pj=` parameter |

## Silent payments (BIP-352)

[Silent payments](h12-silent-payments.md) awareness is built into H3. When H3 detects address reuse, it checks whether the recipient already supports BIP-352 silent payments and adjusts its suggestion accordingly.

## Scoring formula

```
score = min(100, max(0, 100 − sum(penalty weights) + sum(bonus weights)))
```

- Weights are additive — multiple heuristics can fire on the same transaction
- H10 uses `weight = −10` (negative penalty = bonus)
- H8 additionally caps the score at 40 regardless of other heuristics
- H9 or H10 firing strips H5 from the findings (coinjoin breaks the CIOH assumption)
