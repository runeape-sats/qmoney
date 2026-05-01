# Private-Key Quorum Threat Model

> **Status:** first-pass architecture checklist for the current `pkey_quorum/` baseline. This document describes what the current simulator models, what it does not yet model, and which security questions should be answered before QMoney is described as anything more than research software.

## Purpose

QMoney's current implemented baseline is **distributed private-key quantum cash**:

- the note family is BB84/Wiesner-like and private-key;
- a verifier quorum holds hidden basis/bit verification material;
- verification consumes the presented note;
- a successful transfer remints a fresh note for the receiver;
- a classical ledger records ownership and spent serials.

That architecture is coherent, but it is not automatically trustless, public-key, or production-ready. This threat model keeps the near-term engineering path honest by naming the assumptions that still need to be implemented, measured, or formalized.

## Current simulator scope

The current `pkey_quorum/demo.py` simulator models:

- symbolic BB84 product-state preparation;
- hidden per-qubit basis/outcome secrets;
- in-memory note ownership and spent-state tracking;
- verifier availability through a `threshold` parameter;
- consumptive measurement during verification;
- verify-and-remint transfer semantics;
- simple counterfeiting and adaptive-probe helpers.

The current simulator does **not** yet model:

- signed transfer-intent objects;
- persistent, concurrent, or consensus-backed ledger state;
- threshold secret sharing for verifier secrets;
- Byzantine or colluding quorum members;
- verifier attestation signatures;
- atomic remint failure recovery;
- hardware noise, loss, storage, transport, or custody;
- a production public-key quantum verifier.

## Assets and security goals

### Assets

- **Quantum note state:** the physical or simulated BB84-style state associated with a serial.
- **Verifier secret:** hidden basis/outcome data needed to validate a serial.
- **Serial lifecycle:** unspent/spent state and remint lineage.
- **Ownership state:** the classical owner or claimant authorized to spend the note.
- **Verifier attestations:** future signed statements that a quorum accepted or rejected a presented note.
- **Remint randomness:** fresh basis/outcome data and serial generation for replacement notes.

### Intended security goals

1. A holder of one valid note should not be able to create two notes that both pass verification.
2. A spent serial should not be accepted again.
3. A valid transfer should either complete with a fresh replacement note or fail in a clearly recoverable state.
4. A verifier request should not leak enough information to let an attacker reconstruct the hidden basis/outcome recipe.
5. A minority of unavailable or faulty verifier nodes should not halt honest transfers if the configured quorum assumptions allow progress.
6. A compromised verifier set below the defined compromise threshold should not be able to mint, validate, or leak arbitrary notes.

The current code demonstrates only a subset of these goals. The rest are roadmap items.

## Adversary classes

### 1. Note-holder counterfeiter

The attacker owns or temporarily obtains a valid note and tries to produce multiple notes that pass verification.

Current coverage:

- `counterfeit_intercept_resend(...)`
- `one_note_to_two_counterfeit_trial(...)`

Open work:

- statistical test envelopes for expected counterfeit success rates;
- tolerance/noise sensitivity curves;
- multi-copy and copy-complexity experiments;
- better mapping to Molina–Vidick–Watrous-style security games.

### 2. Adaptive verifier-query attacker

The attacker submits modified notes and learns from accept/reject behavior.

Current coverage:

- `adaptive_replacement_probe(...)` demonstrates that verifier interaction can leak information.

Open work:

- repeated-query strategies;
- near-valid note probing;
- basis-recovery experiments;
- impact of tolerance on leakage;
- limits on retries per serial or per ownership session.

### 3. Malicious claimant or recipient

The attacker tries to spend a note they do not own, replay a transfer, race a transfer, or exploit a remint failure.

Current coverage:

- `Ledger.owner_of(...)` and `Ledger.is_spent(...)` provide toy in-memory checks.

Open work:

- signed transfer-intent objects;
- replay protection;
- transaction IDs;
- concurrent double-spend races;
- recipient acknowledgement;
- explicit failure states for consumed-but-not-reminted notes.

### 4. Unavailable verifier nodes

Some verifier nodes fail to participate.

Current coverage:

- `threshold` currently acts as a **minimum live-participant count**. If fewer nodes have the secret, verification does not start and the note remains live.

Important caveat:

- This is an availability model, not yet threshold secret sharing or Byzantine consensus.

Open work:

- distinguish availability quorum, voting quorum, and cryptographic threshold;
- define liveness assumptions;
- model partial verification attempts;
- define who selects verifier participants.

### 5. Compromised verifier nodes

Some verifier nodes leak secrets, forge attestations, censor verification, or collude with counterfeiters.

Current coverage:

- not modeled beyond every `QuorumNode` storing the same full `BillSecret`.

Open work:

- threshold secret sharing or split verification data;
- attestation signatures;
- compromise thresholds;
- accountability/slashing model if using a public network;
- secret rotation and remint after suspected compromise;
- tests for partial-secret leakage.

### 6. Malicious or inconsistent ledger service

The ledger records conflicting ownership or spent-state data.

Current coverage:

- in-memory `Ledger` object only.

Open work:

- persistence;
- consensus/finality model;
- atomic compare-and-set semantics for spending serials;
- audit log of remint lineage;
- recovery if verification and ledger update disagree.

## Quorum semantics: current vs future

The word **quorum** can mean several different things. QMoney should keep them separate.

| Quorum meaning | Current simulator status | Future design question |
| --- | --- | --- |
| Availability quorum | Implemented: enough nodes must have the secret before verification starts | What liveness assumptions are acceptable? |
| Voting/attestation quorum | Not implemented | Which signatures count as a final verification attestation? |
| Threshold-secret quorum | Not implemented | Can verifier secrets be split so no single node knows the whole recipe? |
| Byzantine quorum | Not implemented | How many malicious nodes can be tolerated? |
| Remint authority quorum | Not implemented separately | Who is authorized to issue replacement notes? |

Near-term docs and CLI help should describe the current code as an **availability-quorum simulator with replicated verifier secrets**, not as threshold cryptography.

## Verify-and-remint failure modes

The core transfer flow has four phases:

1. present note and transfer intent;
2. consume note by measurement;
3. decide accept/reject;
4. mint/register replacement note if accepted.

Important failure cases to model next:

- verification accepts but remint fails;
- remint succeeds but ledger update fails;
- ledger marks old note spent before replacement is durable;
- two verifier groups race on the same serial;
- claimant loses value because a note was consumed without a replacement path;
- recipient receives a note that not all ledgers agree is live.

A production design must make these states explicit. The simulator can start by adding a transfer-result object with enough detail to distinguish them.

## Noise and tolerance questions

The simulator exposes `noise_bitflip_p` and `tolerance`, but the security consequences are not yet characterized.

Required analysis:

- false accept probability for counterfeit notes as tolerance increases;
- false reject probability for honest notes under noise;
- how tolerance changes adaptive-query leakage;
- whether mismatch counts should be revealed to users or only accept/reject;
- how many failed attempts are allowed before a serial is locked or consumed.

## Near-term implementation checklist

Before QMoney claims anything stronger than a research simulator, Track A should add:

1. direct API validation for note size, probability, basis, bit, and tolerance inputs;
2. a signed transfer-intent data structure or at least a stubbed interface for one;
3. a transfer-result object that records verification, spend, and remint outcomes;
4. statistical counterfeit tests for small `n`;
5. explicit docs/tests for availability quorum vs threshold-secret quorum;
6. TLA+ lifecycle rules for spent serials, remint, and ownership transfer;
7. a persistence/atomicity abstraction for `Ledger`.

## Bottom line

The current private-key quorum path is a strong research baseline because it is simple, honest, and close to Wiesner/BB84 intuition. Its next milestone is not public-key money. Its next milestone is a sharper **private-key quorum security model** that treats adaptive leakage, quorum compromise, remint atomicity, and noise/tolerance as first-class design questions.
