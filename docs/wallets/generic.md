# Generic wallet integration

## Library (Python)

Any wallet with a Python layer can integrate SiriScore directly:

```python
import siriscore

def pre_broadcast_check(psbt_base64: str) -> dict:
    report = siriscore.score(psbt_base64)
    return {
        "score": report.score,
        "findings": [
            {"id": f.heuristic_id, "title": f.title, "suggestion": f.suggestion}
            for f in report.findings if not f.positive
        ],
    }
```

## REST API

Any wallet with HTTP support can POST to the `/score` endpoint:

```
POST https://your-siriscore-instance.example.com/score
Content-Type: application/json

{"input": "<psbt-or-txid>", "input_type": "psbt", "lookup": false}
```

For maximum user privacy, run a local SiriScore instance and point the wallet at `http://127.0.0.1:8000`.

## CLI (shell wallets / scripts)

```bash
RESULT=$(btc-privacy-check --psbt "$PSBT" --json)
SCORE=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin)['score'])")
if [ "$SCORE" -lt 60 ]; then
  echo "Low privacy score: $SCORE"
fi
```
