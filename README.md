# QMoney: A Peer-to-Peer Quantum Money System

The idea of quantum money has been around since the 70s-80s. It is the right time to revisit and turn it into an alternative form of freedom money. Ideally, QMoney (quantum money implementation suggested here) serves like the other side of Bitcoin (i.e., yin and yang). As Bitcoin security being weaker compared to current quantum computing technology development, QMoney becomes stronger because it is more feasible to implement QMoney as more logical qubits are avaiable to daily users.

QMoney is a _work-in-progress_ research repo for "distributed private-key quantum cash" inspired by:

- **[Stephen Wiesner](https://scottaaronson.blog/?p=5730) / [Peter Shor](https://math.mit.edu/~shor/)'s quantum money ideas**: unclonable quantum states, hidden verification data, and the distinction between private-key and public-key quantum money
- **[Scott Aaronson / Paul Christiano](https://www.scottaaronson.com/papers/moneyfull.pdf)'s private-key quantum money ideas**: adaptive-query security, compact-secret tradeoffs, mini-scheme vs full-scheme thinking, and the importance of rigorous verifier models
- **Artur Ekert's quantum cryptography ideas**: Bell-inequality security witnesses, entanglement-based key distribution, noisy-channel privacy amplification, and the distinction between note-family security and infrastructure/session certification
- **[Satoshi Nakamoto](https://bitcoin.org/bitcoin.pdf)'s Bitcoin**: public ownership, signed transfer intent, distributed validation, and ledger finality
- and more...(to be added here).

The core idea:

> use **no-cloning** for the quantum anti-counterfeiting layer, and use a **Bitcoin-like classical settlement layer** for ownership transfer, attestations, and spent-state tracking.

The current repo does **not** yet implement true public-key quantum money. It implements a **quorum-verified, private-key quantum cash** model with **verify-and-remint** semantics.

---

## Historical background

Scott Aaronson's memorial post on [Stephen Wiesner](https://scottaaronson.blog/?p=5730) is an important reminder that "quantum money" began as a strangely early idea, not as a late product of the modern quantum-computing boom.

A few historical stories matter for how QMoney frames itself:

- **Wiesner wrote the core idea in the late 1960s.** His *Conjugate Coding* manuscript already treated quantum states as useful for cryptographic tasks that are impossible classically.
- **The paper was not celebrated immediately.** As Aaronson recounts, the manuscript was rejected once, then shelved for years before finally appearing in 1983. Quantum money started as an idea that sounded too early, too weird, and too far ahead of the surrounding field.
- **No-cloning was part of the original intuition before it was formalized.** Wiesner used the impossibility of copying unknown quantum states as obvious background well before the no-cloning theorem was named and published in 1982.
- **The line from Wiesner to BB84 is direct.** Bennett and Brassard later transformed related ideas into quantum key distribution, and the modern field of quantum cryptography grew partly out of that same conceptual seed.
- **Ekert pushed that cryptographic line further through Bell nonlocality.** Entanglement-based QKD and Bell-inequality security tests showed that the same quantum foundations behind Wiesner's hidden-state intuition could also certify channel integrity, randomness, and eavesdropping resistance.
- **Private-key quantum money came first.** Wiesner's banknote scheme relied on hidden verification data held by the issuing bank, which is exactly why QMoney is careful to distinguish its current private-key baseline from future public-key ambitions.

That history matters because it shows that quantum money was never just about a flashy quantum token. From the beginning, it was about what uniquely quantum information lets you do: create states that are easy to verify with the right hidden information but fundamentally hard to copy.

---

## QMoney is currently work-in-progress. THERE IS NO CRYPTO TOKENS!!

QMoney (inspired by Bitcoin and quantum money research) can be best described as:

- **private-key quantum cash** at the quantum layer
- **quorum-verified** rather than universally self-verifiable
- **verify-and-remint** rather than “verify the same note forever”
- **classical public-key settlement** at the ownership / ledger layer

In the current simulator family, a bill is a BB84-style product state with hidden per-qubit verification data. A verifier quorum holds the secret measurement information, checks the note, consumes it by measurement, and if valid re-mints a fresh note for the recipient.

That means:
- the note family is **Wiesner-like / private-key** in structure
- the system-level circulation model is **distributed and Bitcoin-inspired**
- the public-facing part is the **classical ledger/attestation layer**, not a public quantum verifier

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

## Comparison with public-key hidden subspace and Bitcoin

| Dimension | Current private-key quorum | Public-key hidden subspace | Standard BTC transaction |
| --- | --- | --- | --- |
| Repo track | `pkey_quorum` | `pubkey_hidden_subspace` | External reference model |
| Thing being spent | BB84-style private-key bill: `serial + qubits` | Hidden-subspace note: `serial + quantum state over a subspace` | One or more UTXOs |
| Ownership proof | Possession of a valid bill plus ledger claimant check | Possession of a note that passes public hidden-subspace verification | Digital signature from the private key controlling the UTXO |
| Verification | Private quorum nodes check hidden per-qubit basis/bit secrets | Public verifier checks subspace and dual-subspace structure/oracles | Anyone checks signatures, scripts, UTXO existence, and consensus rules |
| Transfer model | Verify old bill, consume it by measurement, mint a fresh bill to the receiver | Research model verifies a note against public key/oracle publication; production transfer semantics are not the baseline yet | Consume old UTXOs, create new UTXOs |
| Double-spend prevention | Local `Ledger` marks serials spent | Not fully modeled as production settlement; would still need lifecycle/ledger rules | Global consensus and UTXO-set validation |
| Trust model | Requires quorum nodes to hold secrets and be available | Aims toward public verification, but the current prototype exposes too much structure | Trust-minimized public validation by full nodes |
| Secret material | Quorum holds private basis/bit secrets | Mint has subspace generators; verifier uses public key/oracle data | Sender holds private signing key |
| Who can verify | Only quorum participants with the bill secrets | Anyone with the public key/oracle publication in the model | Anyone running a Bitcoin verifier/full node |
| Counterfeit resistance | BB84 disturbance/no-cloning intuition in a private-key setting | Hidden-subspace quantum money idea, but the current prototype is not an unforgeability claim | Signature unforgeability plus consensus against double spends |
| Public auditability | Low to medium; verifier secrets are private | Higher in concept; public key/oracle workflow is visible | High; transactions are public on-chain |
| Current repo status | Current private-key baseline | Research-only prototype, tiny `n`, conceptual clarity over cryptographic realism | Real production protocol |
| Main caveat | Trusted/private verifier quorum | Current `HiddenSubspacePublicKey` publishes enough structure to reconstruct an accepting note | Requires network fees, block inclusion, and probabilistic finality |

Mental model:

```text
pkey_quorum:
    bill serial + BB84 qubits + quorum secrets
    ~= private-banknote-style money

pubkey_hidden_subspace:
    serial + hidden-subspace state + public verification structure
    ~= public-verifiable quantum banknote research model

Bitcoin:
    UTXO + signature + consensus inclusion
    ~= public ledger money
```

The major upgrade that `pubkey_hidden_subspace` explores over `pkey_quorum` is
public verification. In `pkey_quorum`, the verifier must know private basis/bit
secrets. In a public-key hidden-subspace design, the goal is for anyone to verify
a note without learning enough to mint counterfeits.

The current implementation does **not** claim that full result. The
`pubkey_hidden_subspace` prototype publishes enough subspace structure that
software can reconstruct an accepting note. It is therefore a research model of
the public-verification workflow, not a deployable transaction system. Compared
with Bitcoin, QMoney's current tracks are note-family and verifier experiments;
Bitcoin is a production classical ledger protocol with public validation and
consensus settlement.

---

## Bitcoin system architecture

- distributed validation
- signed transactions
- public ownership tracking
- ledger finality
- no reliance on a single monolithic bank server

QMoney tries to combine that system architecture with a quantum anti-counterfeiting primitive. The result is not “quantum Bitcoin,” but a hybrid design:

- **quantum** for unclonable notes
- **classical distributed systems** for circulation and settlement

--

## Can QMoney use Bitcoin blocks?
QMoney should carry on the immutability of the BTC blocks.

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
- [`docs/architecture/classical-simulation-hardware-breakdown.md`](docs/architecture/classical-simulation-hardware-breakdown.md) — RAM/VRAM breakdown for MPS, sparse state-vector, and BB84 symbolic simulation approaches.
- [`docs/architecture/public-key-implementation-workflow.md`](docs/architecture/public-key-implementation-workflow.md) — implementation source of truth for AI agents and human implementers extending the public-key/oracle track in any language.

### Research notes
- [`docs/research/shor-arguments-and-qmoney-integration.md`](docs/research/shor-arguments-and-qmoney-integration.md) — how Peter Shor’s arguments should shape QMoney’s architecture split, terminology, and public-key research boundaries.
- [`docs/research/aaronson-private-key-quantum-money-and-qmoney.md`](docs/research/aaronson-private-key-quantum-money-and-qmoney.md) — transcript-backed note on Aaronson’s private-key quantum money ideas, adaptive-query security, compact-secret tradeoffs, and why QMoney fits the distributed private-key lineage.
- [`docs/research/wiesner-counterfeiting-attacks-and-qmoney.md`](docs/research/wiesner-counterfeiting-attacks-and-qmoney.md) — evaluation of Molina–Vidick–Watrous (2012) for QMoney, including why the paper's one-note-to-two-notes counterfeiting model is a strong fit for the current private-key baseline.
- [`docs/research/latest-quantum-money-literature-and-qmoney.md`](docs/research/latest-quantum-money-literature-and-qmoney.md) — survey of the latest quantum money literature most relevant to QMoney, prioritizing Wiesner, Shor, Aaronson/Christiano, Zhandry, and recent oracle/noise-tolerant directions.
- [`docs/research/ekert-quantum-cryptography-and-qmoney.md`](docs/research/ekert-quantum-cryptography-and-qmoney.md) — review of Artur Ekert’s quantum-cryptography work and what Bell-certified security, entanglement-based key exchange, noisy-channel privacy amplification, and measurement-independence assumptions imply for QMoney.
- [`docs/research/quantum-money-literature-roadmap.md`](docs/research/quantum-money-literature-roadmap.md) — ranked reading and prototyping roadmap for QMoney: what to read next, prototype next, monitor, and avoid.
- [`docs/research/note-family-evaluation-checklist.md`](docs/research/note-family-evaluation-checklist.md) — checklist for evaluating future note families across verifier leakage, coherence sensitivity, counterfeiting, public/private status, noise, and repo integration.

---

## Current simulator / demo

Default setup:
- **512 BB84 qubits per bill**
- **BB84 symbolic product-state simulation**
- private-key quorum verification with hidden basis/bit data
- no required GPU or dense state-vector simulation

Run the pure software simulator demo:

- `python pkey_quorum/demo.py`
- `python pkey_quorum/demo.py --n 512`
- `python pkey_quorum/demo.py --n 1024`

The current simulator keeps the note family intentionally simple:
- BB84 product states
- quorum-held verification secrets
- very low entanglement
- MPS-friendly scaling for larger software-only experiments

### BB84 abstraction: simulator vs quantum hardware

For the current baseline, BB84 only requires:
- preparation in the `Z` or `X` basis
- basis-dependent measurement
- classical reconciliation about which basis was used

The important distinction is:
- **classical simulator** = models those qubits and measurements as software objects and computed probabilities
- **quantum hardware** = prepares and measures real physical qubits, so disturbance, noise, and loss happen in the physical system

In other words:
- a **classical simulator models BB84**
- **quantum hardware performs BB84**

This repo's current baseline is a **classical simulator** for a BB84-style private-key note family. It is a useful research and engineering environment, not a claim that the current implementation already runs on production quantum hardware.

A useful baseline attack model for this simulator family is the **simple one-note-to-two-notes counterfeiting attack** analyzed by Molina, Vidick, and Watrous (2012): given one valid note, what is the best probability of producing two notes that both pass verification? See [`docs/research/wiesner-counterfeiting-attacks-and-qmoney.md`](docs/research/wiesner-counterfeiting-attacks-and-qmoney.md).

The code now exposes small attack-model helpers for this baseline:
- `one_note_to_two_counterfeit_trial(...)`
- `adaptive_replacement_probe(...)`

These are research utilities for testing verifier leakage and counterfeit behavior, not production security proofs.

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

### Concrete 10-unit transfer mental model

If Alice transfers `10` units to Bob, the current repo should be read in one of two ways:

- **single-note model:** Alice spends one 10-unit note, which is consumed and replaced by one fresh 10-unit note for Bob
- **UTXO model:** Alice spends a bundle of input notes whose values sum to `10`, and the quorum re-mints fresh output notes for Bob, plus change back to Alice if needed

The important invariant is the same in both cases:

> Alice's submitted quantum note(s) are consumed during verification, and Bob receives fresh replacement note(s) with new serial numbers.

For the fuller step-by-step UTXO explanation and a transfer sequence diagram, see [`docs/architecture/software-mps-quorum-design.md`](docs/architecture/software-mps-quorum-design.md).

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
- group-action, oracle/noise-tolerant, and anonymity-aware literature tracked as separate design directions

---

## Latest research directions

Recent literature reinforces that QMoney's public-key future should be treated as a separate research program rather than as a small extension of the current BB84/quorum baseline.

The most important newer directions to watch are:
- **noise-tolerant public-key money from classical oracles** — especially promising for QMoney's formal/oracle workflow
- **public-key money from abelian group actions** — one of the strongest modern public-key directions
- **cryptanalysis of public-key money schemes** — essential to keep prototype claims honest
- **anonymous public-key money** — relevant if QMoney ever combines public verification with privacy-sensitive circulation
- **copy-complexity / unclonable-cryptography frameworks** — useful for broadening QMoney's attack models beyond a single counterfeit story

See:
- [`docs/research/latest-quantum-money-literature-and-qmoney.md`](docs/research/latest-quantum-money-literature-and-qmoney.md)
- [`docs/research/quantum-money-literature-roadmap.md`](docs/research/quantum-money-literature-roadmap.md)

---

## Citations

- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://bitcoin.org/bitcoin.pdf
- Wiesner, S. (1983). *Conjugate coding*. SIGACT News, 15(1), 78–88. (Written in the late 1960s; foundational private-key quantum money idea.)
- Wootters, W. K., & Zurek, W. H. (1982). *A single quantum cannot be cloned*. Nature, 299(5886), 802–803.
- Aaronson, S., & Christiano, P. (2012). *Quantum Money from Hidden Subspaces*. https://www.scottaaronson.com/papers/moneyfull.pdf
- Molina, A., Vidick, T., & Watrous, J. (2012). *Optimal counterfeiting attacks and generalizations for Wiesner's quantum money*. https://arxiv.org/abs/1202.4010
- Zhandry, M. (2023). *Quantum Money from Abelian Group Actions*. https://arxiv.org/abs/2307.12120
- Yuen, P. (2024). *Noise-tolerant public-key quantum money from a classical oracle*. https://arxiv.org/abs/2407.06463

## Additional references
- Scott Aaronson, *Stephen Wiesner (1942-2021)*: https://scottaaronson.blog/?p=5730
- Peter Shor seminar transcript notes in this repo: [`docs/research/shor-arguments-and-qmoney-integration.md`](docs/research/shor-arguments-and-qmoney-integration.md)
- Scott Aaronson seminar transcript notes in this repo: [`docs/research/aaronson-private-key-quantum-money-and-qmoney.md`](docs/research/aaronson-private-key-quantum-money-and-qmoney.md)
- Artur Ekert review note in this repo: [`docs/research/ekert-quantum-cryptography-and-qmoney.md`](docs/research/ekert-quantum-cryptography-and-qmoney.md)
