# Run locally

Running SiriScore locally means no transaction data is sent to siriscore.xyz. Your PSBT or txid stays on your machine.

## Start the server

```bash
pip install siriscore
uvicorn api.main:app --reload
```

Open [http://localhost:8000](http://localhost:8000).

To bind to a different port:

```bash
uvicorn api.main:app --reload --port 8080
```

## Offline demo

Open `web/index.html` directly in a browser — no server, no install:

```bash
# macOS
open web/index.html

# Linux
xdg-open web/index.html

# Windows
start web/index.html
```

The page detects it is running as a local file and falls back to built-in mock data automatically. Useful for UI exploration or demos.

## Development mode (from source)

```bash
git clone https://github.com/siri-score/siriscore.git
cd siriscore
pip install -e ".[dev]"
uvicorn api.main:app --reload
```

Changes to `scorer/`, `api/`, or `web/` are reflected immediately.

## Privacy when running locally

When the server is running on your machine, the only external calls are H3/H4 network lookups if you have **Enable network checks** toggled on. To disable those completely, turn off the toggle in the UI or pass `lookup=False` in the API request.

To route lookups through your own Bitcoin Core node instead of mempool.space:

```bash
btc-privacy-check --txid <txid> \
  --rpc-url http://127.0.0.1:8332 \
  --rpc-user alice \
  --rpc-password hunter2
```
