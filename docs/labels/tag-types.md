# Tag types

The `tag` field on a label record controls how SiriScore uses it during scoring.

| Tag | Effect |
|-----|--------|
| `tainted` | Triggers H8 — score is penalised (weight 25) and capped at 40 |
| `coinjoin` | Triggers H9 — positive finding, suppresses H5 (CIOH) |
| `clean` | Informational only — no scoring effect |
| `unknown` | Informational only — no scoring effect |

## tainted

Use `tainted` for UTXOs you know are linked to a problematic source:

- Direct withdrawal from a KYC exchange
- Received from a flagged or identified address
- Explicitly marked as high-risk by your threat model

Spending a `tainted` UTXO will always result in H8 firing and a score cap of 40.

## coinjoin

Use `coinjoin` for UTXOs that came from a coinjoin transaction when the value alone does not match a Whirlpool denomination (e.g. a JoinMarket or Wasabi output at a non-standard amount).

When an input has the `coinjoin` tag, H9 fires as a positive finding and H5 (CIOH) is suppressed.

## clean / unknown

These are for your own bookkeeping. They do not affect the score but appear in the **Coin labels** section of the report.

## Setting tags in Sparrow

In Sparrow Wallet, the label export (`File → Export Wallet → Labels`) does not always include explicit tags. You can add them manually in the exported JSONL, or use SiriScore's REST API to add labels with tags directly:

```bash
curl -X POST http://localhost:8000/labels \
  -H "Content-Type: application/json" \
  -d '{"ref": "txid:vout", "type": "output", "label": "Exchange withdrawal", "tag": "tainted"}'
```
