# Importing from Sparrow

## Export from Sparrow Wallet

1. Open Sparrow Wallet
2. Go to **File → Export Wallet**
3. Select **Labels** — this exports a `.jsonl` file in BIP329 format

## Import into SiriScore

=== "Web UI"
    Click **Import labels from Sparrow Wallet** on the SiriScore home page and select your `.jsonl` file.

=== "CLI"
    ```bash
    btc-privacy-check --psbt <b64> --import-sparrow sparrow-labels.jsonl
    ```

=== "Library"
    ```python
    import siriscore
    n = siriscore.import_labels("sparrow-labels.jsonl")
    print(f"Imported {n} labels")
    ```

=== "REST API"
    ```bash
    curl -X POST http://localhost:8000/labels/import \
      -F "file=@sparrow-labels.jsonl"
    ```

## What gets imported

SiriScore processes three BIP329 record types:

| Type | ref format | Effect |
|------|-----------|--------|
| `tx` | txid | Labels all outputs of that transaction |
| `addr` | bitcoin address | Labels UTXOs received to that address |
| `output` | txid:vout | Labels a specific UTXO |

Labels with `tag: tainted` trigger H8 when a matching input is found. Labels with `tag: coinjoin` trigger H9.

## Testing

Create a test file `sparrow-labels.jsonl`:

```jsonl
{"type":"tx","ref":"93c98c2a742373460e74b7d3b39ba30283b14476df835916d0a3f60dfc988e0d","label":"Exchange withdrawal","tag":"tainted"}
{"type":"addr","ref":"bc1qalum72s7tmt39y32fv5r06qvu9nz5phdjfcw8h","label":"KYC receive address","tag":"tainted"}
{"type":"output","ref":"35cebb10f6d6129716effcd69eb43df40669f4b27533be0857299fec0c52a976:1","label":"Labelled coin","tag":"tainted"}
```

Then analyse txid `93c98c2a...` — H8 should fire because the transaction itself is tainted.
