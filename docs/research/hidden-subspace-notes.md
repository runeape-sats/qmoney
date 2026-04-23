# Hidden-Subspace Public-Key Prototype Notes

This document describes the first **public-key quantum money prototype** added to QMoney under `pubkey_hidden_subspace/note_family.py`.

## Scope

This is a **small, research-only, state-vector toy model** inspired by the Aaronson-Christiano hidden-subspace direction.

What it does:
- represents a hidden subspace over `F_2^n` from explicit generators
- mints the uniform superposition over that subspace
- exposes a public verifier that checks two software-visible conditions:
  1. the note is uniform over the target subspace
  2. its Hadamard image is uniform over the dual subspace

What it does **not** do:
- implement cryptographic obfuscation or real oracle access control
- claim production-ready public-key security
- model noise tolerance
- scale beyond tiny `n`

Most importantly, the current Python prototype exposes the full accepting support through
`HiddenSubspacePublicKey.subspace_vectors` and `dual_vectors`. That means a caller can
reconstruct an accepting uniform superposition directly from the published software data.
This limitation is captured explicitly in `tests/test_pubkey_hidden_subspace.py` so the
prototype remains honest about what it does and does not prove.
So this module should be read as a **note-family/verifier sketch**, not as a secure
counterfeit-resistant public-key money implementation.

## Why this still matters

Even as a toy model, this prototype establishes the core architectural separation QMoney has been aiming for:
- the old baseline lives in `pkey_quorum/demo.py`
- the new public-key research track lives in `pubkey_hidden_subspace/`

That separation is important because hidden-subspace money is a **different note family** and a **different verifier model** from the BB84/quorum private-key baseline.

## Current API

- `HiddenSubspaceMint.from_generators(serial, generators)`
- `HiddenSubspaceMint.mint_note()`
- `HiddenSubspacePublicKey.verify(note)`
- `hadamard_transform(note)`
- `basis_state(dimension, basis, serial=...)`

## Verification intuition

For the minted note `|A>`:
- computational-basis support is exactly the subspace `A`
- amplitudes are uniform on `A`
- after applying the Walsh-Hadamard transform, support is exactly the dual subspace `A^⊥`
- amplitudes are uniform on `A^⊥`

A counterfeit basis state inside `A` fails because its Hadamard image spreads weight outside `A^⊥`.

## TLA+ model

The companion spec in `tla/hidden_subspace_money.tla` is intentionally abstract.
It still does **not** model amplitudes or the full hidden-subspace mathematics. Instead, it now models the verifier-facing lifecycle plus explicit **oracle publication/query invariants**:
- serial issuance
- authentic presentation
- counterfeit presentation
- subspace-oracle publication
- dual-oracle publication
- bounded oracle queries
- acceptance or rejection

The current oracle-focused invariants are:
- issued serials have both oracle tables published
- subspace and dual oracle publication stay coupled
- query records only reference issued serials
- logged query answers respect the abstract oracle rule for authentic vs counterfeit candidates
- subspace/dual query tags match the published oracle domain

This gives QMoney an initial state-machine artifact for reasoning about verifier outcomes and oracle-consistency safety properties while the mathematical simulator stays in Python.

## Canonical workflow

The implementation source of truth for AI agents is:
- [`docs/architecture/public-key-implementation-workflow.md`](../architecture/public-key-implementation-workflow.md)

That document defines the required cross-layer workflow for implementing public-key/oracle features in any language:
- runtime math layer
- TLA+ lifecycle layer
- Z3 transition-stability layer
- required verification and doc updates

## Z3 checker

QMoney now also includes a symbolic checker at `z3/check_oracle_invariants.py`.

Its job is different from TLC:
- TLC explores the bounded reachable state graph of the TLA+ model
- Z3 checks **one-step inductiveness** of selected oracle invariants across each supported transition

The current Z3 checker covers these invariants:
- `oracle_tables_match_issued`
- `oracle_tables_stay_coupled`
- `queries_only_reference_issued_serials`
- `query_answers_respect_oracle_rule`

The last item is currently modeled as an abstract bookkeeping obligation inside the
symbolic checker, not as a full symbolic oracle-answer derivation from amplitude-level
state. So the Z3 layer should be interpreted as checking **selected oracle-consistency
bookkeeping rules**, while TLC remains the stronger lifecycle/state-machine pass.

and checks them against these transitions:
- `mint`
- `present_authentic`
- `present_counterfeit`
- `query_subspace_oracle`
- `query_dual_oracle`
- `verify_authentic`
- `reject_counterfeit`
- `noop`

This means the repo now has both:
- finite-state validation of the abstract lifecycle in TLA+/TLC
- symbolic transition-stability checks for the oracle invariants in Z3
