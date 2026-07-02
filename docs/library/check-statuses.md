# Check statuses

Every heuristic produces a `Check` entry in `report.checks`, even when it does not fire. This gives a complete audit trail of what ran, what passed, and what was skipped.

| Status | Meaning |
|--------|---------|
| `pass` | Heuristic ran and found no issue. Also used for suppressed H5 (when H9/H10 fires) and for positive findings (H9/H10/H11 when they fire). |
| `fail` | Heuristic fired as a penalty finding — appears in `report.findings`. |
| `skipped` | Network check deliberately not run (`lookup=False`). Applies to H3 and H4. |
| `unavailable` | Could not run — required input data was missing. Common when a PSBT does not include prevout values. |

## Example

```python
for check in report.checks:
    print(f"{check.heuristic_id:4} {check.status:12} {check.reason}")
```

Typical output for an offline score:

```
H1   pass         Script types are consistent across inputs and outputs
H2   pass         No round output amounts detected
H3   skipped      Network lookups disabled
H4   skipped      Network lookups disabled
H5   pass         Input count (2) is below the consolidation threshold
H6   pass         No dust inputs detected
H7   pass         Inputs and outputs follow BIP69 ordering
H8   pass         No tainted labels matched
H9   pass         No coinjoin inputs detected
H10  pass         Transaction does not match any coinjoin structure
H11  pass         No BIP-21 URI with pj= parameter found
```
