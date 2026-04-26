# QMoney pkey_quorum

This package is the current **private-key quorum** baseline for QMoney.

Current entrypoint:
- `demo.py` — BB84/product-state minting, quorum verification, verify-and-remint,
  simple intercept/resend counterfeit experiments, one-note-to-two-note counterfeit
  trials, and adaptive replacement probes for verifier-leakage testing

What belongs here:
- private-key note-family logic
- quorum-held verification secrets
- verify-and-remint transfer behavior
- classical owner/spent-state tracking tied to the private-key baseline

What does **not** belong here:
- hidden-subspace public-key note-family experiments
- oracle publication/query models better represented in `tla/` and `z3/`

This separation is intentional so agents can distinguish the current deployed
baseline from the future public-key research track at a glance.
