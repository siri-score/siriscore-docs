# Install the library

## From PyPI

```bash
pip install siriscore
```

Requires Python 3.11 or later.

## From source

```bash
git clone https://github.com/siri-score/siriscore.git
cd siriscore
pip install -e ".[dev]"
```

The `-e` flag installs in editable mode — changes to `scorer/`, `api/`, or `cli.py` take effect immediately without reinstalling.

## Verify the install

```python
import siriscore
print(siriscore.__version__)
```

## CLI

The `btc-privacy-check` command and the `siriscore` alias are both installed automatically:

```bash
btc-privacy-check --txid a4f1c9d2e3b5a6f7890abc1234567890abcdef1234567890abcdef1234567890ab
siriscore --psbt cHNidP8BA...
```

### Common flags

| Flag | Description |
|------|-------------|
| `--txid <txid>` | Score by transaction ID (fetches from mempool.space) |
| `--psbt <base64>` | Score a base64-encoded PSBT |
| `--rawtx <hex>` | Score a raw transaction hex |
| `--json` | Output machine-readable JSON |
| `--fail-below <N>` | Exit with code 1 if score is below N (CI use) |
| `--import-sparrow <file>` | Import Sparrow labels before scoring |
| `--lookup` | Enable network checks (H3, H4) |
| `--rpc-url <url>` | Bitcoin Core RPC endpoint |
| `--rpc-user <user>` | Bitcoin Core RPC username |
| `--rpc-password <pass>` | Bitcoin Core RPC password |

### Point at your own node

Avoid sending txids to any third party by routing all lookups through your own Bitcoin Core node:

```bash
btc-privacy-check --txid <txid> \
  --rpc-url http://127.0.0.1:8332 \
  --rpc-user alice \
  --rpc-password hunter2
```

Your node needs `txindex=1` in `bitcoin.conf`.

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Scored at or above threshold |
| 1 | Score below `--fail-below` threshold |
| 2 | Parse error or network failure |
