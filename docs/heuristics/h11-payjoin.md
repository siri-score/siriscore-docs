# H11 — Payjoin opportunity

**Severity:** Info (Warning if H5 also fires) · **Weight:** 0 · **Network:** No · **Positive:** Yes

## What it detects

The transaction's associated BIP-21 URI contains a `pj=` parameter, indicating the recipient supports BIP-77 async Payjoin.

## Effect on scoring

- No penalty — H11 is informational
- **Escalates to Warning** when H5 (high input count / CIOH) also fires, because Payjoin directly addresses that risk
- Appears green in the UI with a suggestion to use the Payjoin endpoint

## How to pass the BIP-21 URI

H11 reads `payment_uri` or `bip21_uri` from `psbt_meta`. Pass it via the library:

```python
from siriscore import score_as

report = score_as(
    "cHNidP8BA...",
    input_type="psbt",
    psbt_meta={
        "payment_uri": "bitcoin:BC1Q...?amount=0.001&pj=https://btcpay.example.com/payjoin"
    },
)
```

## Why it matters

Payjoin (BIP-77) allows the recipient to contribute an input to the transaction, breaking the CIOH assumption and obscuring the payment amount. When a recipient supports it, the sender should use it — it improves privacy for both parties.

## Payjoin endpoint format

The `pj=` parameter contains an HTTPS URL — the sender posts the original PSBT there and receives a modified PSBT with the recipient's input added.

→ [BTCPay Server integration](../wallets/btcpay.md)
