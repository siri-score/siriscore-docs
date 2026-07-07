# REST API

SiriScore ships a FastAPI backend that exposes the same scoring engine as the <strong><a href="https://pypi.org/project/siriscore/" target="_blank" rel="noopener noreferrer">Python library</a></strong> over HTTP. Use it from any language, or wire it into a wallet or payment flow.

## Run the server

```bash
pip install siriscore
uvicorn api.main:app
```

The API is now at `http://localhost:8000`. The hosted instance behind <strong><a href="https://siriscore.xyz" target="_blank" rel="noopener noreferrer">siriscore.xyz</a></strong> exposes the same endpoints.


## Quick example

```bash
curl -s http://localhost:8000/score \
  -H "Content-Type: application/json" \
  -d '{"input": "a4f1c9d2e3b5...", "input_type": "txid"}'
```

```json
{
  "score": 72,
  "findings": [
    {
      "id": "H2",
      "title": "Round payment amount",
      "suggestion": "Consider using PayJoin to obscure the payment amount."
    }
  ],
  "checks": ["..."]
}
```

## Endpoints

| Endpoint | Status | Description |
|----------|--------|-------------|
| [`POST /score`](score.md) | **Live** | Score a single transaction |
| `GET /labels` / `POST /labels` | **Live** | Read and write the local label store. See [Label System](../labels/index.md) |
| [`POST /labels/import`](../labels/sparrow-import.md) | **Live** | Import a Sparrow BIP329 label export |
| [`POST /score/batch`](batch.md) | Planned | Score multiple transactions in one request |
| [`GET /heuristics`](heuristics.md) | Planned | Metadata for every heuristic;IDs, weights, severity |
| [`GET /score/{txid}`](score-txid.md) | Planned | Score by txid via a plain GET |

## Privacy

Calling a hosted instance sends your transaction data to that server, run the server locally to keep it on your machine. Scoring itself is offline by default: H3/H4 network lookups only run when the request sets `"lookup": true`.

