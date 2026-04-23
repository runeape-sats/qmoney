# Software MPS Quorum Design for QMoney

This document preserves the original technical appendix-style design for the current QMoney simulator track.

It describes the simplest software-only path to a larger-qubit **quorum-verified private-key quantum cash** system using:
- BB84 product states
- verifier-held secret basis/bit data
- verify-and-remint semantics
- very low entanglement, so the bill remains MPS-friendly

This is a **private-key** design note for the current baseline, not a public-key quantum money construction.

---

## 1. Design goal

The baseline simulator targets a path to **512 or 1024 qubits** that:
- keeps the quantum note easy to simulate in software
- supports **public access to verification requests** via a verifier quorum
- avoids exotic public-key quantum money constructions
- uses a BB84 product-state note family with MPS bond dimension `D=1`

The key architectural move is:
- keep the quantum note family simple and private-key
- put distributed coordination in the classical settlement/quorum layer

---

## 2. Verification by a quorum, not by the bill holder

The simplest scalable design for the current repo is to make verification an **online quorum service**.

### Core model
- A verifier quorum collectively holds the bill’s hidden verification data.
- The bill holder does **not** learn the full verification secret.
- Verification consumes the presented note by measurement.
- If valid, the quorum re-mints a fresh note for the receiver.

This preserves the core anti-counterfeiting story:
- the note is hard to clone because the secret measurement rule remains hidden
- the system can still circulate value through verify-and-remint

This is “public” only in the limited sense that **anyone can request verification from the network**. It is **not** non-interactive public-key quantum money.

---

## 3. Data model

For a bill with `n ∈ {512, 1024}` qubits:

- `serial`: unique identifier, e.g. 128-bit random
- `owner_pk`: current owner public key in the classical ledger
- `C`: optional public commitment to hidden verification data, e.g. `C = H(serial || B || V || nonce)`

Hidden verifier-held data:
- `B ∈ {0,1}^n`
  - `B[i]=0` means measure qubit `i` in the Z basis
  - `B[i]=1` means measure qubit `i` in the X basis
- `V ∈ {0,1}^n`
  - expected outcome in that basis

In the current simulator, these are represented concretely by `BillSecret.basis` and `BillSecret.bits`.

---

## 4. Quantum state preparation

Each qubit `i` is prepared as a BB84 state:

- if `B[i]=0` and `V[i]=0`: `|0⟩`
- if `B[i]=0` and `V[i]=1`: `|1⟩`
- if `B[i]=1` and `V[i]=0`: `|+⟩`
- if `B[i]=1` and `V[i]=1`: `|−⟩`

The full bill is a tensor product of these single-qubit states.

### Why this matters
Because the bill is a product state:
- it has **very low entanglement**
- it is naturally representable as an MPS with bond dimension `D=1`
- software simulation scales linearly in `n` as long as no entangling gates are introduced

That is why this note family is a good software baseline.

---

## 5. Verify-and-remint protocol

A system-level transfer looks like this:

1. **Transfer intent**
   - sender creates a classical transfer intent naming `(old_serial, receiver_pk, ...)`
   - sender signs it with the classical ownership key

2. **Present bill**
   - sender submits the quantum note plus transfer intent to the verifier quorum

3. **Quorum verification**
   - the quorum measures the note in the secret bases `B`
   - it checks the resulting outcomes against `V`
   - all qubits are checked across the participating quorum members

4. **Ledger update**
   - if accepted: mark `old_serial` spent and attach the new note to `receiver_pk`
   - if rejected after measurement: mark `old_serial` spent/invalid, since the state was consumed
   - if a quorum cannot be assembled **before verification starts**: abort and leave the original note live

5. **Re-mint**
   - the quorum generates a fresh `(new_serial, B', V')`
   - the quorum prepares a fresh `n`-qubit note for the recipient

This gives one-time quantum spend semantics with repeated circulation achieved by re-minting.

---

## 6. Mapping to the current implementation

The current code implementing this baseline is in [`qmoney_mps_quorum_demo.py`](../../qmoney_mps_quorum_demo.py).

### Main objects
- `Bill`
  - current note: serial + qubit list
- `BillSecret`
  - hidden basis/bit verification rule
- `Ledger`
  - spent-state and owner tracking
- `QuorumNode`
  - secret-holding verifier node
- `QuorumService`
  - minting and `verify_and_remint`

### Current implementation behavior
The implementation currently guarantees:
- a bill is only verified if quorum participation is available
- if quorum is unavailable before verification starts, the bill remains live
- if verification starts, the bill is consumed by measurement
- all qubits are measured across the quorum, not just a threshold prefix
- accepted bills are re-minted with a fresh serial for the receiver
- double-spend attempts fail at the ledger layer

The test coverage in `tests/test_qmoney.py` currently checks:
- all qubits are measured even when threshold is less than node count
- a bill is not spent when quorum cannot be assembled before verification begins

---

## 7. MPS / simulation requirements

For this baseline note family, the simulator only needs:
- single-qubit state preparation
- Hadamard transforms for X-basis measurement
- projective measurement with collapse
- optional simple noise channels like per-qubit bit-flip

### Practical rule of thumb
- ordinary state-vector simulation is comfortable up to roughly `30–32` logical qubits
- beyond that, low-entanglement tensor-network / MPS methods become the natural route
- for this specific product-state note family, bond dimension stays `D=1` unless the design is changed to introduce entanglement

That is why the repo can legitimately target larger software-only qubit counts while keeping the current note family simple.

---

## 8. Acceptance rule and noise tolerance

A baseline acceptance rule is:
- measure all `n` qubits
- accept if `matches ≥ n - t`

Where:
- `matches` = number of outcomes matching the hidden secret bits
- `t` = allowed mismatch budget from noise or implementation tolerance

### Current implementation parameters
The demo exposes:
- `--tolerance`
- `--noise-bitflip`
- `--seed`

This allows the simulator to explore:
- exact-match acceptance (`t=0`)
- simple noisy channels
- forged-note failure under imperfect measurement conditions

---

## 9. Security intuition for the baseline

In the simplest intercept/resend model, a counterfeiter without `B` must guess a basis for each qubit.

Per qubit, success is:
- correct basis: success probability `1`
- wrong basis: success probability `1/2`

Averaging over hidden bases gives:
- per-qubit success probability `3/4`

So for exact matching on all qubits:
- `P_forge = (3/4)^n`

Security bits are approximately:
- `s = -log2(P_forge) = n * log2(4/3) ≈ 0.415 * n`

Examples:
- `n=512` → about `212.5` bits
- `n=1024` → about `425` bits

This is only the simple product-state intercept/resend threat model, but it is the right baseline story for the current simulator track.

---

## 10. Suggested software-only parameters

Good starting points for the baseline simulator:

- qubits per bill: `n=512` or `n=1024`
- threshold: `2f+1` approvals out of `3f+1` nodes
- tolerance: start with `0`, then introduce small mismatch budgets under noise
- secret storage:
  - start with full replication across quorum nodes in software
  - later explore threshold sharing or partial secret distribution

The current demo is intentionally conservative and simple. Its job is to make the architecture clear and executable, not to claim a production-ready quantum money system.

---

## 11. Why keep this design note separate from the README

The README should stay short and repo-facing.

This document exists to preserve the more technical appendix-style material:
- larger-qubit simulator target
- concrete note data model
- exact protocol flow
- acceptance/tolerance mechanics
- forge-rate intuition
- implementation mapping

That makes this the right place for the original appendix content to live going forward.

---

## 12. Status

This document matches the **current private-key baseline**.

It should evolve only when the implementation meaningfully changes, for example if QMoney adds:
- entangled note families
- more realistic noise models
- threshold-shared secrets in code
- richer quorum fault handling
- a separate public-key note-family namespace
