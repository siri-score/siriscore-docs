# Library Reference

The `siriscore` Python library scores a transaction and returns a structured report you can render, log, or gate on. Install it with `pip install siriscore`.

See <a href="../getting-started/install.md" target="_blank" rel="noopener noreferrer">Install the library</a> for requirements and CLI setup.

## Quick example

```python
import siriscore

# Accepts a PSBT (base64), raw tx hex, or txid — type is auto-detected
report = siriscore.score("cHNidP8BA...")

print(report.score)  # 82

for finding in report.findings:
    print(f"{finding.heuristic_id}: {finding.title}")
    print(f"  → {finding.suggestion}")
```

## Choosing a function

| You want to | Use |
|-------------|-----|
| Score a transaction; let the input type be auto-detected | [`score()`](score.md) |
| Skip auto-detection, or pass `psbt_meta` for Payjoin detection (H11) | [`score_as()`](score-as.md) |
| Import wallet labels so label-based scoring (H8/H9) has data to match | [`import_labels()`](import-labels.md) |

## Understanding results

Every call returns a [`Report`](models.md), ie the score, the [`Finding`](models.md#finding) entries for heuristics that fired, and a `checks` list recording what every heuristic did, including the ones that passed or were skipped.

- [Report and Finding models](models.md) - every field, with the score formula
- [Check statuses](check-statuses.md) - `pass` / `fail` / `skipped` / `unavailable` and when each occurs

## Privacy

Scoring runs entirely offline unless you opt in to network lookups with `lookup=True`, and you can route those through your own node.

:material-chevron-double-right: [Privacy guarantee](privacy-guarantee.md)
