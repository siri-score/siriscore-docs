# H1 — Script type mismatch

**Severity:** Critical · **Weight:** 25 · **Network:** No

## What it detects

All inputs use one script type but one or more outputs use a different type. For example: all inputs are P2WPKH (native SegWit) but one output is P2PKH (legacy).

## Why it matters

A chain analyst can identify which output is the change by finding the one that matches the sender's script type. This reveals the payment direction and links the change output back to the sender's wallet.

## What to do

Use the same script type for change outputs as your inputs. Most modern wallets do this automatically, but it is worth checking when constructing transactions manually or using coin control.

## False positive note

If the recipient uses a different script type than you do, this finding may be unavoidable. In that case it is still worth noting — a privacy-conscious recipient would publish a same-type address.
