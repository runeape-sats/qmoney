# QMoney Z3 checks

This directory holds symbolic one-step invariant preservation checks.

Current checker:
- `check_oracle_invariants.py`

Use this layer for:
- transition-local invariant preservation
- fast UNSAT/counterexample checks against the TLA+-inspired lifecycle rules

Current scope is intentionally narrower than TLC: the checker focuses on the
core oracle publication/query consistency subset, while some broader lifecycle
invariants remain TLC-only until they are worth encoding symbolically.

This is complementary to `tla/`, not a replacement for finite-state model
checking.