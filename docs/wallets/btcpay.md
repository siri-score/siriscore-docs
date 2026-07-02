# BTCPay Server — Payjoin + scoring

BTCPay Server supports [BIP-77 async Payjoin](https://github.com/bitcoin/bips/blob/master/bip-0077.mediawiki) out of the box. When a customer pays a BTCPay invoice with a Payjoin-capable wallet, the transaction has a `pj=` parameter in the BIP-21 URI — which SiriScore detects as H11.

## Scoring a BTCPay payment

When a BTCPay invoice is paid, you can score the PSBT before broadcasting by passing the full BIP-21 URI:

```python
from siriscore import score_as

# BIP-21 URI from BTCPay invoice
payment_uri = "bitcoin:BC1QXXX...?amount=0.01&pj=https://btcpay.example.com/BTC/pj"

report = score_as(
    psbt_base64,
    input_type="psbt",
    psbt_meta={"payment_uri": payment_uri},
)

if report.score < 60:
    print("Warning: low privacy score before broadcast")
```

## H11 and Payjoin

When the `pj=` endpoint is present, H11 fires as a positive (green) finding:

- **Info** — Payjoin endpoint available, consider using it
- **Warning** — escalates when H5 (high input count / CIOH) also fires, because Payjoin directly mitigates that risk

## Webhook integration (coming)

A future version of SiriScore will support webhook callbacks so BTCPay can automatically score transactions and flag low-scoring payments for review.
