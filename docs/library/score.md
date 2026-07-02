# score()

```python
siriscore.score(input_str: str, *, lookup: bool = False, rpc_url: str | None = None, rpc_user: str | None = None, rpc_password: str | None = None) -> Report
```

Accepts a PSBT (base64), raw transaction hex, or txid. Returns a [`Report`](models.md).

The input type is auto-detected:
- 64-character hex string → txid
- Non-64 hex string → raw transaction
- Everything else → PSBT (base64)

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_str` | `str` | required | PSBT (base64), raw tx hex, or txid |
| `lookup` | `bool` | `False` | Enable H3/H4 network lookups via mempool.space |
| `rpc_url` | `str` | `None` | Bitcoin Core RPC endpoint — routes all lookups through your node |
| `rpc_user` | `str` | `None` | Bitcoin Core RPC username |
| `rpc_password` | `str` | `None` | Bitcoin Core RPC password |

## Examples

```python
import siriscore

# Fully offline — H3 and H4 skipped
report = siriscore.score("cHNidP8BA...")

# With network checks (mempool.space / blockstream.info)
report = siriscore.score("cHNidP8BA...", lookup=True)

# Via your own Bitcoin Core node
report = siriscore.score(
    "a4f1c9d2e3b5...",
    rpc_url="http://127.0.0.1:8332",
    rpc_user="alice",
    rpc_password="hunter2",
)

# Score by txid
report = siriscore.score("a4f1c9d2e3b5...", lookup=True)

print(report.score)           # 72
print(report.input_count)     # 2
print(report.output_count)    # 2
```

## Return value

→ [`Report`](models.md#report)
