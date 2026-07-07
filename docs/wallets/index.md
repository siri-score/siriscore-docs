# Wallet Integration Guide

There are two alternative implementations in this section: use SiriScore alongside a wallet you already run, or build it into a wallet you're developing.

## Use SiriScore with your wallet

| Wallet | Status | What you get |
|--------|--------|--------------|
| [Sparrow Wallet](sparrow.md) | **Live** | Score PSBTs before signing; export BIP329 labels so H8/H9 can match your coins |
| [BTCPay Server](btcpay.md) | Planned | Score payments with Payjoin detection (H11) in the invoice flow |
| [Cake Wallet](cake.md) | Planned | In-wallet scoring via the library / a Dart FFI binding |

## Build SiriScore into your wallet

Any wallet can add pre-broadcast privacy scoring. The pieces:

**1. Pick an integration surface.** The [Python library](../library/index.md) gives you the richest interface (`Report` objects, label store access); the [REST API](../api/index.md) works from any language; the CLI suits shell-based flows. All three patterns, with code, are in the [generic integration guide](generic.md).

**2. Apply the core pattern.** Score the transaction after construction but before signing, show the findings and their suggestions to the user, and warn or block below a score threshold. The [BTCPay guide](btcpay.md) shows a working example of threshold gating.

**3. Make it a complete integration.** The difference between a basic and a thorough integration is three touchpoints:

- **Pass the payment URI.** Supply the BIP-21 URI as `psbt_meta={"payment_uri": ...}` via [`score_as()`](../library/score-as.md) so Payjoin opportunities (H11) are detected
- **Import the wallet's labels.** Feed BIP329 labels to [`import_labels()`](../library/import-labels.md) so tainted-coin (H8) and coinjoin (H9) detection have data to match
- **Respect the privacy defaults.** Keep `lookup=False` unless the user opts in, and let them point network checks at their own node. See the [privacy guarantee](../library/privacy-guarantee.md)

Building an integration for a wallet not listed here? We'd like to hear about it.



:material-source-pull: [Contributing](../contributing.md)
