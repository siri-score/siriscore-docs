# GET /score/{txid}

**Status:** Coming soon

Score a transaction by txid via a GET request. Convenience endpoint for browser and webhook use.

```
GET /score/a4f1c9d2e3b5a6f7890abc1234567890abcdef1234567890abcdef1234567890ab
```

Equivalent to `POST /score` with `input_type="txid"` and `lookup=true`.
