# QMoney

QMoney is a research repo for **distributed private-key quantum cash** inspired by:

- **[Stephen Wiesner](https://scottaaronson.blog/?p=5730) / [Peter Shor](https://math.mit.edu/~shor/)'s quantum money ideas**: unclonable quantum states, hidden verification data, and the distinction between private-key and public-key quantum money
- **[Scott Aaronson / Paul Christiano](https://www.scottaaronson.com/papers/moneyfull.pdf) private-key quantum money ideas**: adaptive-query security, compact-secret tradeoffs, mini-scheme vs full-scheme thinking, and the importance of rigorous verifier models
- **[Satoshi Nakamoto](https://bitcoin.org/bitcoin.pdf) Bitcoin**: public ownership, signed transfer intent, distributed validation, and ledger finality

The core idea:

> use **no-cloning** for the quantum anti-counterfeiting layer, and use a **Bitcoin-like classical settlement layer** for ownership transfer, attestations, and spent-state tracking.

The current repo does **not** implement true public-key quantum money. It implements a **quorum-verified, private-key quantum cash** model with **verify-and-remint** semantics.

---

## What QMoney currently is

QMoney today is best described as:

- **private-key quantum cash** at the quantum layer
- **quorum-verified** rather than universally self-verifiable
- **verify-and-remint** rather than “verify the same note forever”
- **classical public-key settlement** at the ownership / ledger layer

In the current simulator family, a bill is a BB84-style product state with hidden per-qubit verification data. A verifier quorum holds the secret measurement information, checks the note, consumes it by measurement, and if valid re-mints a fresh note for the recipient.

That means:
- the note family is **Wiesner-like / private-key** in structure
- the system-level circulation model is **distributed and Bitcoin-inspired**
- the public-facing part is the **classical ledger/attestation layer**, not a public quantum verifier

---

## Why this framing matters

The research in this repo is organized around a distinction that Shor and Aaronson both make clear:

### Private-key quantum money / cash
- valid verification depends on hidden note information
- verifier interaction is a major attack surface
- repeated-query / adaptive attacks matter
- compact verifier secrets often introduce computational assumptions

### Public-key quantum money
- anyone can verify from public information
- verification must not reveal how to mint valid notes
- requires a different note family and a different security story

QMoney’s current baseline is in the **private-key** camp.

---

## Current architecture

QMoney has two layers.

### 1. Quantum note layer
- BB84-style note family
- hidden basis / outcome data
- consumptive verification
- no-cloning as the anti-counterfeiting primitive

### 2. Classical settlement layer
- owner public keys
- signed transfer intent
- quorum attestations
- spent-state tracking
- ledger finality

This split is intentional. Classical public-key cryptography helps handle ownership and settlement, but it does **not** turn the quantum note family into public-key quantum money.

---

## Verify-and-remint model

The current QMoney model is:

1. A sender presents a quantum note plus a classical transfer intent.
2. A verifier quorum measures the note using hidden verification data.
3. The note is consumed by measurement.
4. If valid, the quorum attests acceptance and prepares a fresh note for the recipient.
5. The classical ledger marks the old serial spent and records the new owner / note state.

This is closer to **distributed private-key quantum cash** than to a self-verifying public token.

---

## Bitcoin system architecture

Bitcoin matters to QMoney not because Bitcoin already solves quantum money, but because it contributes the **system architecture**:

- distributed validation
- signed transactions
- public ownership tracking
- ledger finality
- no reliance on a single monolithic bank server

QMoney tries to combine that system architecture with a quantum anti-counterfeiting primitive. The result is not “quantum Bitcoin,” but a hybrid design:

- **quantum** for unclonable notes
- **classical distributed systems** for circulation and settlement

---

## What this repo is for

This repo is a research and simulation workspace for:

- honest framing of private-key vs public-key quantum money
- quorum-based private-key quantum cash architectures
- verify-and-remint transfer flows
- software simulation of BB84-style note families
- future public-key quantum money research tracks kept separate from the current baseline

Near-term value here is primarily:
- conceptual clarity
- simulator design
- attack modeling
- note-family comparison
- architecture documentation

not near-term deployment of production quantum money.

---

## Key references in this repo

### Architecture
- [`docs/architecture/public-vs-private-key-qmoney.md`](docs/architecture/public-vs-private-key-qmoney.md) — canonical statement of the current repo architecture and why QMoney is private-key quantum cash rather than public-key quantum money.
- [`docs/architecture/software-mps-quorum-design.md`](docs/architecture/software-mps-quorum-design.md) — preserved technical appendix for the current software-only MPS/quorum baseline, including data model, protocol flow, simulation assumptions, and security intuition.
- [`docs/architecture/public-key-implementation-workflow.md`](docs/architecture/public-key-implementation-workflow.md) — implementation source of truth for AI agents and human implementers extending the public-key/oracle track in any language.

### Research notes
- [`docs/research/shor-arguments-and-qmoney-integration.md`](docs/research/shor-arguments-and-qmoney-integration.md) — how Peter Shor’s arguments should shape QMoney’s architecture split, terminology, and public-key research boundaries.
- [`docs/research/aaronson-private-key-quantum-money-and-qmoney.md`](docs/research/aaronson-private-key-quantum-money-and-qmoney.md) — transcript-backed note on Aaronson’s private-key quantum money ideas, adaptive-query security, compact-secret tradeoffs, and why QMoney fits the distributed private-key lineage.

---

## Current simulator / demo

Run the pure software simulator demo:

- `python pkey_quorum/demo.py --n 512`
- `python pkey_quorum/demo.py --n 1024`

The current simulator keeps the note family intentionally simple:
- BB84 product states
- quorum-held verification secrets
- very low entanglement
- MPS-friendly scaling for larger software-only experiments

This is a useful private-key baseline, not a claim of true public-key quantum money.

### Actual implementation sample

The implementation lives in [`pkey_quorum/demo.py`](pkey_quorum/demo.py). At a high level it exposes:
- `Ledger` for spent-state and owner tracking
- `QuorumNode` for secret-holding verifiers
- `QuorumService` for minting plus `verify_and_remint`
- `Bill` / `BillSecret` for the note and its hidden verification data

A minimal end-to-end example from the current implementation looks like this:

```python
from pkey_quorum import Ledger, QuorumNode, QuorumService

nodes = [QuorumNode(i) for i in range(4)]
quorum = QuorumService(nodes, threshold=3)
ledger = Ledger()

bill = quorum.mint_bill(32, owner="alice", ledger=ledger)

accepted, new_bill = quorum.verify_and_remint(
    bill,
    claimant="alice",
    receiver="bob",
    ledger=ledger,
    tolerance=0,
    noise_bitflip_p=0.0,
    seed=123,
)

print("accepted", accepted)
print("old spent", ledger.is_spent(bill.serial))
print("new owner", ledger.owner_of(new_bill.serial) if new_bill else None)
```

The built-in CLI demo then shows the intended system behavior:

```bash
python pkey_quorum/demo.py --n 32 --nodes 4 --threshold 3 --forge-trials 10000
```

Expected shape of output:

```text
transfer alice->bob accepted=True
double-spend accepted=False
new serial minted to bob: <hex-serial>
forge success rate: <x>/10000
```

That sample captures the current implementation thesis of the repo:
- mint a private-key BB84-style note
- let a quorum verify it using hidden basis/bit data
- consume the original note on verification
- re-mint a fresh note for the receiver
- reject double-spend attempts at the ledger layer

---

## Research direction

The repo should be read as having two tracks:

### Track A — current baseline
- distributed private-key quantum cash
- secret-holding verifier quorum
- verify-and-remint
- classical settlement layer

### Track B — future research
- true public-key note families
- hidden-subspace/oracle-backed prototypes
- stronger coherence-sensitive verification
- public-key constructions clearly separated from the current baseline

---

## Citations

- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://bitcoin.org/bitcoin.pdf
- Wiesner, S. (1983). *Conjugate coding*. SIGACT News, 15(1), 78–88. (Written in the late 1960s; foundational private-key quantum money idea.)
- Wootters, W. K., & Zurek, W. H. (1982). *A single quantum cannot be cloned*. Nature, 299(5886), 802–803.
- Aaronson, S., & Christiano, P. (2012). *Quantum Money from Hidden Subspaces*. https://www.scottaaronson.com/papers/moneyfull.pdf

## Additional references
- Peter Shor seminar transcript notes in this repo: [`docs/research/shor-arguments-and-qmoney-integration.md`](docs/research/shor-arguments-and-qmoney-integration.md)
- Scott Aaronson seminar transcript notes in this repo: [`docs/research/aaronson-private-key-quantum-money-and-qmoney.md`](docs/research/aaronson-private-key-quantum-money-and-qmoney.md)
