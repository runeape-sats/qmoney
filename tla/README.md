# QMoney TLA+ specs

This directory holds the protocol/lifecycle state-machine specs for QMoney.

Current spec:
- `hidden_subspace_money.tla`
- `hidden_subspace_money.cfg`

Use this layer for:
- issuance/publication/query/decision ordering
- lifecycle invariants over reachable states
- TLC model checking

Do not use TLA+ here to model amplitude-level quantum math; that belongs in the
runtime note-family code under `pubkey_hidden_subspace/`.