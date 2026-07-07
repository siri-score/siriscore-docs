# POST /score

Score a transaction via the REST API.

## Request

```
POST /score
Content-Type: application/json
```

```json
{
  "input": "cHNidP8BA...",
  "input_type": "psbt",
  "lookup": false
}
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `input` | string | required | PSBT (base64), raw tx hex, or txid |
| `input_type` | string | `"psbt"` | `"psbt"`, `"rawtx"`, or `"txid"` |
| `lookup` | boolean | `false` | Enable H3/H4 network checks |

## Response

```json
{
  "score": 72,
  "input_count": 2,
  "output_count": 2,
  "psbt_version": 0,
  "findings": [
    {
      "id": "H2",
      "severity": "warning",
      "title": "Round payment amount",
      "detail": "Output 0 has a round value of 10000000 sats (0.1 BTC).",
      "suggestion": "Consider using PayJoin to obscure the payment amount.",
      "weight": 15,
      "positive": false
    }
  ],
  "checks": [
    {"id": "H1", "status": "pass", "reason": "Script types are consistent."},
    {"id": "H2", "status": "fail", "reason": "Round output amount detected."},
    ...
  ],
  "labels": []
}
```

## Example

```bash
curl -s -X POST http://localhost:8000/score \
  -H "Content-Type: application/json" \
  -d '{"input": "cHNidP8BA...", "input_type": "psbt", "lookup": false}' \
  | python3 -m json.tool
```

## Error response

```json
{"detail": "Could not parse input as PSBT, raw tx, or txid."}
```

HTTP 422 for parse errors.
