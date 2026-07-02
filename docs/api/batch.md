# POST /score/batch

**Status:** Coming soon

Score multiple transactions in a single request.

```json
{
  "transactions": [
    {"input": "cHNidP8BA...", "input_type": "psbt"},
    {"input": "a4f1c9d2...", "input_type": "txid"}
  ],
  "lookup": false
}
```

Returns an array of `Report` objects in the same order.
