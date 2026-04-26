# QMoney pubkey_hidden_subspace

This package contains the **research-only** public-key hidden-subspace track,
kept intentionally separate from the BB84/quorum private-key baseline in
`pkey_quorum/`.

Current entrypoint:
- `note_family.py` — tiny state-vector hidden-subspace mint/verifier model
- `oracles.py` — explicit oracle publication/query registry with query logging
- `verifier.py` — oracle-backed verifier workflow that mirrors the abstract lifecycle model

Current scope:
- tiny `n` only
- exact state-vector dictionaries over `{0,1}^n`
- public verification using explicit subspace structure in software
- conceptual clarity over cryptographic realism

Important caveat:
- the current `HiddenSubspacePublicKey` publishes enough structure to reconstruct an accepting note in software, so this prototype is **intentionally not an unforgeability claim**

Non-goals for this prototype:
- production cryptographic claims
- realistic oracle obfuscation
- noise tolerance
- scalable qubit counts

Planned expansion points for this namespace:
- `noise_tolerant_hidden_subspace.py`
