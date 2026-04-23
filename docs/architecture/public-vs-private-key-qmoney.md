# Public vs Private-Key QMoney

This note clarifies the architecture that exists in this repository today, the role of classical public-key cryptography inside it, and how a future true public-key quantum money track should be separated from the current system.

## TL;DR

QMoney, as currently implemented in this repo, is **not** public-key quantum money.

It is:
- **private-key quantum cash** at the quantum layer
- **public-key/classical cryptography** at the ownership and settlement layer
- **quorum-verified** rather than universally self-verifiable
- **verify-and-remint** rather than "verify the same note forever"

That distinction matters because publishing the secret quantum verification data for the current BB84-style note family would make counterfeiting easy.

---

## 1. Current architecture

The current QMoney design has two different security layers.

### 1.1 Quantum note layer
Each bill is represented by a quantum state together with a classical serial number.

In the current simulator family (`pkey_quorum/demo.py`), the note is a BB84-style product state determined by hidden per-qubit data:
- `B[i]` chooses the measurement basis (`Z` or `X`)
- `V[i]` chooses the expected outcome in that basis

The bill is secure against simple counterfeiting because an adversary does **not** know the hidden basis/outcome strings in advance.

This is the core reason the current system is **private-key** at the quantum layer.

### 1.2 Classical ledger / ownership layer
Separately, QMoney uses ordinary classical cryptographic ideas for:
- ownership identity
- transaction signing
- quorum attestations
- ledger finality and spent-state tracking

This layer can absolutely use **public/private keys** in the ordinary blockchain sense.

That does **not** make the quantum money scheme itself public-key quantum money. It only means the surrounding settlement layer is classical-public-key-based.

---

## 2. Why current QMoney is private-key quantum cash

A quantum money scheme is private-key when valid verification requires secret information that is not available to the public.

That is exactly the case here.

To verify a current QMoney bill, the verifier quorum needs access to the hidden verification material for that serial:
- the secret basis string `B`
- the secret target string `V`
- or equivalent secret material from which they can derive the verification rule

If that secret were published, then the current BB84 product-state bill could be recreated by an attacker. In other words:

- **private-key property:** verifier knows secret measurement data
- **current note family:** security depends on that secrecy
- **therefore:** current QMoney is private-key quantum cash, not public-key quantum money

---

## 3. What “public verification” means in the current repo

The README uses "public verification" in an access sense, not in the Aaronson/Zhandry cryptographic sense.

In the current architecture:
- anyone can request that the network verify a note
- a selected verifier quorum performs the actual quantum verification
- the quorum holds the secret note-verification material
- the rest of the network validates a **classical signed attestation** from the quorum

So the system is publicly *accessible* for verification requests, but the quantum verification itself is still performed by a party that holds secrets.

That is a decentralized **private-key verification service**, not a non-interactive public-key quantum money verifier.

---

## 4. Verify-and-remint semantics

Current QMoney is best understood as a **verify-and-remint** system:

1. The sender presents a quantum bill to a verifier quorum.
2. The quorum measures the bill using secret verification data.
3. Measurement consumes the presented state.
4. If the bill is valid, the system mints a fresh replacement note for the recipient.
5. The classical ledger marks the old serial spent and records the new ownership state.

This differs from a naive classical-cash mental model where the same token is repeatedly checked in place. In QMoney, verification is consumptive, so repeated circulation comes from re-minting fresh notes, not from preserving the original state after each verification.

---

## 5. Why the current BB84 note family cannot simply be made public-key

A tempting mistake is to ask whether QMoney can become public-key just by publishing commitments, openings, basis strings, or verifier metadata for the existing note family.

For the current design, the answer is no.

If the public learns enough information to derive the exact valid BB84 product state, then the public can prepare a fresh copy of that note family. That destroys the anti-counterfeiting property.

So the roadmap cannot be:
- "take the current BB84 quorum design and reveal more of its secrets"

The roadmap has to be:
- "keep the current BB84 quorum design as the private-key baseline"
- "add a separate note family for true public-key quantum money research"

---

## 6. Clean architecture split for the repo

The repo should treat current QMoney and future public-key QMoney as related but distinct tracks.

### 6.1 Track A: Current product / engineering baseline
This repo's current production-facing architecture should be described as:
- decentralized private-key quantum cash
- quorum-held verification secrets
- verify-and-remint transfer model
- classical ledger settlement with signatures and attestations

This track is where near-term engineering work belongs:
- simulator hardening
- noise models
- quorum fault handling
- remint atomicity
- documentation cleanup

### 6.2 Track B: Future research track for true public-key money
True public-key quantum money should live in a separate namespace and docs track.

That future track should target note families where:
- anyone can run verification using public information
- public verification does **not** reveal how to mint valid notes
- the security claim does not secretly depend on hidden per-note basis strings

The right first research direction is not "make BB84 public"; it is to implement a separate public-key construction, starting with oracle-backed hidden-subspace money at small scale.

---

## 7. Recommended repo boundaries

A clean split helps prevent overclaiming and confusion.

### Keep under current QMoney baseline
- `pkey_quorum/demo.py`
- current BB84/product-state note logic
- quorum verification and attestation logic
- classical ownership / settlement logic
- tests for counterfeit probability, quorum behavior, and remint semantics

### Add under a separate public-key namespace
- `pubkey_hidden_subspace/...`
- hidden-subspace / oracle-backed simulators
- future noise-tolerant public-key experiments
- literature-backed research notes

This avoids mixing two different cryptographic stories under one label.

---

## 8. What would count as true public-key quantum money here

A future QMoney-PK track would deserve the term **public-key quantum money** only if it provides all of the following:

- **public verification:** anyone can verify using public data
- **non-trivial unforgeability:** public verification does not let an attacker mint new valid notes
- **honest separation from the private-key baseline:** no hidden note-specific secret is doing the real security work behind the scenes
- **clear note-family distinction:** the construction is not merely the existing BB84 note with relabeled metadata

The most realistic first milestone is a small, research-only hidden-subspace simulator that demonstrates the different verification model clearly and honestly.

For clarity: a toy simulator that directly publishes the accepting support for software inspection is still useful as a verifier-model sketch, but it is **not yet** a genuine public-key unforgeability result.

---

## 9. Practical language for the project

For current docs and discussions, the safest accurate description is:

> QMoney currently implements a quorum-verified, private-key quantum cash design with verify-and-remint, plus a classical public-key ownership and settlement layer.

For future work, the accurate framing is:

> A separate research track may explore true public-key quantum money constructions, beginning with oracle-backed hidden-subspace prototypes and only later considering more speculative frontier constructions.

---

## 10. Bottom line

The current QMoney system already has an interesting and coherent architecture.

But its architecture is:
- **private-key** for quantum note verification
- **public-key** for classical ownership and settlement
- **decentralized** through quorum verification
- **not** yet a true public-key quantum money scheme

The honest roadmap is to preserve that baseline, document it clearly, and build any future public-key work as a separate note family and research track rather than trying to stretch the current BB84 quorum design into a claim it does not support.
