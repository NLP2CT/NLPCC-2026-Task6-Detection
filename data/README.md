# Data

## Data Files

| File | Description |
|------|-------------|
| `train_data.json` | Training set, containing `ID`, `HWT` (original text), `LGT` (generated text), and `HLT` (refined text) fields |
| `testp1.json` | Test phase 1 data, containing `id`, `text`, and `label` (label is null) |
| `testp2.json` | Test phase 2 data, containing `id`, `text`, and `label` (label is null) |
| `testp1_testing_label.json` | Ground truth labels for test phase 1, containing `id` and `label` |
| `testp2_testing_label.json` | Ground truth labels for test phase 2, containing `id`, `text`, and `label` |

Label classes: `HWT(0)`, `LGT(1)`, `HLT(2)`

## Scoring Script Usage

```bash
python score.py <prediction.json> <reference.json>
```

- `prediction.json`: Model predictions, format: `[{"id": "xxx", "label": 0}, ...]`
- `reference.json`: Ground truth file (e.g., `testp1_testing_label.json`)

Outputs macro-averaged F1-Score, accuracy, and per-class F1. Results are also saved to `scores.json`.
