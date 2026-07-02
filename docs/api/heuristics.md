# GET /heuristics

**Status:** Coming soon

Returns metadata for all available heuristics — IDs, names, severity, weight, and whether a network connection is required.

```json
[
  {
    "id": "H1",
    "name": "Script type mismatch",
    "severity": "critical",
    "weight": 25,
    "requires_network": false,
    "positive": false
  },
  ...
]
```
