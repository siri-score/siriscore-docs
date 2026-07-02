# Label format

SiriScore stores coin labels in a local SQLite database at `~/.utxo-privacy-scorer/labels.db`. No cloud sync, no telemetry.

## BIP329 JSONL (Sparrow export)

The primary import format is [BIP329](https://github.com/bitcoin/bips/blob/master/bip-0329.mediawiki) JSONL — one JSON object per line:

```jsonl
{"type":"tx","ref":"<txid>","label":"Exchange withdrawal","tag":"tainted"}
{"type":"addr","ref":"bc1q...","label":"KYC receive address","tag":"tainted"}
{"type":"output","ref":"<txid>:0","label":"Coinjoin output","tag":"coinjoin"}
{"type":"input","ref":"<txid>:0","label":"Spent coinjoin input","tag":"coinjoin"}
```

## Fields

| Field | Description |
|-------|-------------|
| `type` | `tx`, `addr`, `output`, or `input` |
| `ref` | The identifier — txid for `tx`, address for `addr`, `txid:vout` for `output`/`input` |
| `label` | Human-readable description |
| `tag` | Optional scoring tag (see below) |

## Tag types

→ [Tag types reference](tag-types.md)

## Legacy format

The older simple JSON shape `{"txid:vout": "label"}` is also accepted for backward compatibility:

```json
{
  "35cebb10:1": "tainted",
  "bc1qalum...": "KYC address"
}
```
