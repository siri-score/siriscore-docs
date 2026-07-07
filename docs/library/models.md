# Report and Finding models

## Report

```python
@dataclass
class Report:
    score: int               # 0–100
    findings: list[Finding]  # only heuristics that fired
    checks: list[Check]      # every heuristic, with its status
    labels: list[dict]       # UTXO labels relevant to this transaction's inputs
    input_count: int
    output_count: int
    psbt_version: int | None # None for raw tx / txid inputs
```

`score` is computed as `min(100, max(0, 100 − sum(weights)))`. Negative weights (H10: −10) add to the score. When H8 fires, the score is additionally capped at 40.

## Finding

```python
@dataclass
class Finding:
    heuristic_id: str    # "H1"–"H11"
    severity: Severity
    title: str
    detail: str          # what was observed in this transaction
    suggestion: str      # what to do about it
    weight: int          # penalty added to score calculation
    positive: bool       # True for H9/H10/H11 (rendered green in the UI)
```

## Check

```python
@dataclass
class Check:
    heuristic_id: str
    status: str          # "pass" | "fail" | "skipped" | "unavailable"
    reason: str          # human-readable explanation
```

:material-chevron-double-right: [Check statuses](check-statuses.md)

## Severity

```python
class Severity(str, Enum):
    CRITICAL = "critical"
    WARNING  = "warning"
    INFO     = "info"
```

## Example

```python
import siriscore

report = siriscore.score("cHNidP8BA...")

print(f"Score: {report.score}/100")
print(f"Inputs: {report.input_count}, Outputs: {report.output_count}")

for f in report.findings:
    flag = "✓" if f.positive else "✗"
    print(f"{flag} [{f.heuristic_id}] {f.severity.value.upper()}: {f.title}")
    print(f"   {f.detail}")
    print(f"   Fix: {f.suggestion}")

for c in report.checks:
    print(f"{c.heuristic_id}: {c.status}")
```
