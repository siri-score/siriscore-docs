# import_labels()

```python
siriscore.import_labels(path: str, *, source: str = "sparrow") -> int
```

Imports coin labels from a file into the local SQLite label store (`~/.utxo-privacy-scorer/labels.db`). Returns the number of labels imported.

Labels are used by [H8](../heuristics/h8-tainted-label.md) — if a tainted UTXO is found among the transaction's inputs, H8 fires and the score is capped at 40.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `path` | `str` | required | Path to the labels file |
| `source` | `str` | `"sparrow"` | Import format — currently only `"sparrow"` is supported |

## Supported format

Sparrow Wallet BIP329 JSONL export — one JSON object per line:

```jsonl
{"type":"tx","ref":"93c98c2a...","label":"Exchange withdrawal","tag":"tainted"}
{"type":"addr","ref":"bc1qalum...","label":"KYC address","tag":"tainted"}
{"type":"output","ref":"35cebb...:1","label":"Labelled coin","tag":"coinjoin"}
```

Field `tag` drives scoring: `tainted` triggers H8; `coinjoin` triggers H9 (suppresses H5).

→ [Tag types reference](../labels/tag-types.md)

## Example

```python
import siriscore

n = siriscore.import_labels("sparrow-labels.jsonl")
print(f"Imported {n} labels")

# Labels are now used automatically when scoring
report = siriscore.score("cHNidP8BA...")
```
