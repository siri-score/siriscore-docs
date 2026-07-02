# Use the web app

The fastest way to try SiriScore is the hosted tool at **[siriscore.xyz](https://siriscore.xyz)**. No install required.

## Walkthrough

1. **Choose an input type** using the tabs at the top of the form:
    - **Txid** — paste a 64-character transaction ID (most common)
    - **PSBT** — paste a base64-encoded partially signed Bitcoin transaction
    - **Raw Tx** — paste a raw transaction hex string

2. **Paste your transaction** into the text field.

3. **Network checks** — the toggle is on by default when the backend is running. This enables H3 (address reuse) and H4 (UTXO age clustering) by querying mempool.space. Turn it off if you do not want any data leaving your browser.

4. Click **Analyse Transaction**.

## Reading the results

| Section | What it shows |
|---------|--------------|
| Score gauge | 0–100 with a colour band: red (Critical/Poor), orange (Fair), green (Good/Excellent) |
| Findings | Heuristics that fired, with detail and a suggested fix |
| Checks | Every heuristic with its status: pass / fail / skipped / unavailable |
| Coin labels | UTXO labels relevant to this transaction's inputs |
| What to do next | Prioritised action list |

## Importing Sparrow labels

Click **Import labels from Sparrow Wallet** and select a `.jsonl` file exported from Sparrow Wallet (BIP329 format). Imported labels are stored locally in a SQLite database on the server and used to trigger H8 (tainted label detection).

→ [Label system reference](../labels/sparrow-import.md)

## Running your own instance

If you want full privacy — no data to siriscore.xyz — run the server locally:

```bash
pip install siriscore
uvicorn api.main:app --reload
# open http://localhost:8000
```

→ [Run locally](run-locally.md)
