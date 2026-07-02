# score_as()

```python
siriscore.score_as(input_str: str, *, input_type: str, lookup: bool = False, psbt_meta: dict | None = None, **kwargs) -> Report
```

Like [`score()`](score.md) but with an explicit input type. Use this when you know the input format and want to skip auto-detection, or when you need to pass `psbt_meta` for H11 (Payjoin detection).

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_str` | `str` | required | PSBT, raw tx hex, or txid |
| `input_type` | `str` | required | `"psbt"`, `"rawtx"`, or `"txid"` |
| `lookup` | `bool` | `False` | Enable H3/H4 network lookups |
| `psbt_meta` | `dict` | `None` | Extra metadata — `payment_uri` or `bip21_uri` for H11 |

## Examples

```python
from siriscore import score_as

# Explicit PSBT
report = score_as("cHNidP8BA...", input_type="psbt")

# Raw tx
report = score_as("0200000001...", input_type="rawtx")

# Txid with network checks
report = score_as("a4f1c9d2...", input_type="txid", lookup=True)

# With Payjoin endpoint for H11
report = score_as(
    "cHNidP8BA...",
    input_type="psbt",
    psbt_meta={
        "payment_uri": "bitcoin:BC1Q...?amount=0.001&pj=https://btcpay.example.com/payjoin"
    },
)
```
