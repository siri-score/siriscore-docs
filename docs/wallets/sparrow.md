# Sparrow Wallet — PSBT export flow

Sparrow Wallet can export PSBTs and BIP329 labels that work directly with SiriScore.

## Analyse a transaction before signing

1. In Sparrow, go to **Send** and construct your transaction
2. Click **Create Transaction** then **Export PSBT**
3. Save the `.psbt` file or copy the base64 string
4. Paste into SiriScore — either at [siriscore.xyz](https://siriscore.xyz) or via CLI:

```bash
btc-privacy-check --psbt "$(cat transaction.psbt | base64 -w0)"
```

The report will show you which privacy issues exist **before you sign**.

## Export coin labels

Sparrow's label export (BIP329 JSONL) lets SiriScore detect tainted inputs (H8) and coinjoin outputs (H9).

1. In Sparrow, go to **File → Export Wallet**
2. Select **Labels** and export as `.jsonl`
3. Import into SiriScore:

```bash
# CLI
btc-privacy-check --psbt <b64> --import-sparrow sparrow-labels.jsonl

# Library
import siriscore
siriscore.import_labels("sparrow-labels.jsonl")

# Web UI — click "Import labels from Sparrow Wallet"
```

## Label format

Sparrow exports one JSON object per line:

```jsonl
{"type":"tx","ref":"<txid>","label":"Exchange withdrawal","tag":"tainted"}
{"type":"addr","ref":"bc1q...","label":"KYC address","tag":"tainted"}
{"type":"output","ref":"<txid>:0","label":"Coinjoin output","tag":"coinjoin"}
```

→ [Label system reference](../labels/format.md)

## Supported Sparrow versions

Sparrow v1.8+ using the BIP329 JSONL export format. The older simple `{"txid:vout": "label"}` JSON shape is also supported for backward compatibility.
