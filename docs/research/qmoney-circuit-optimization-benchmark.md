# Can QMoney Become a Circuit-Optimization Benchmark?

## Executive answer

> **Implementation design:** [`../architecture/qmoney-quantum-circuit-contest-design.md`](../architecture/qmoney-quantum-circuit-contest-design.md) turns this feasibility study into a concrete pilot track, trusted harness, score, packaging contract, governance model, and launch plan.

**Yes, but the repository does not yet contain a “QMoney core circuit” comparable to the ECDLP 5-bit contest oracle.** The current private-key track is a symbolic BB84 product-state simulator, and the public-key track is a tiny amplitude-dictionary model. Neither emits a reversible gate stream, freezes a circuit ABI, or measures circuit resources.

The strongest first benchmark is **not** the current BB84 mint/measure loop. That loop has no entangling gates and no Toffoli bottleneck, so an ECDLP-style Toffoli score would collapse to zero. The best first target is a small **hidden-subspace verifier circuit** whose standard-basis and Hadamard-basis membership tests are compiled into parity/syndrome networks.

Recommended program:

1. **Build first:** `qmoney-subspace-verifier-8`, a verifier-circuit optimization benchmark.
2. **Build second:** `qmoney-wiesner-counterfeit-1to2`, an adversarial circuit optimization benchmark.
3. **Keep as a microbenchmark only:** coherent/programmable BB84 verification.

This would create two complementary optimization questions:

- **Implementation optimization:** What is the cheapest circuit that implements the fixed QMoney verifier semantics?
- **Security optimization:** What is the cheapest attack circuit that maximizes the probability that two outputs both pass?

These questions must remain separate. A cheaper verifier is not evidence of stronger quantum-money security, and a toy attack benchmark is not a proof against the full system.

---

## 1. What exists in QMoney today

### 1.1 Private-key quorum track

`pkey_quorum/demo.py` models each bill as a list of independent BB84 qubits. For every qubit `i`, hidden classical data specifies:

- `B[i]`: prepare/measure in the `Z` or `X` basis;
- `V[i]`: expected bit in that basis.

At the quantum-operation level, an idealized bill uses only:

```text
mint qubit i:
    if V[i] = 1: X
    if B[i] = 1: H

verify qubit i:
    if B[i] = 1: H
    measure in Z
    compare outcome with V[i] classically
```

The qubits are independent. The full state has MPS bond dimension `D=1`. The current implementation stores `B` and `V` as ordinary secret lists and performs the outcome comparison in classical Python.

Consequences for optimization:

- no `CNOT`/two-qubit network;
- no Toffoli arithmetic;
- all single-qubit work can be parallelized;
- threshold/tolerance processing is naturally classical after measurement;
- the interesting open problems are verifier leakage, noise, quorum behavior, and counterfeiting—not arithmetic circuit synthesis.

Therefore, the actual current BB84 circuit is too small and separable to support a useful ECDLP-style gate-count leaderboard.

### 1.2 Public-key hidden-subspace track

`pubkey_hidden_subspace/note_family.py` currently:

- expands the span of explicit generators over `F_2`;
- represents the uniform note state with an amplitude dictionary;
- computes a Walsh-Hadamard transform in Python;
- checks support and uniformity against explicit `A` and `A^perp` vectors.

This is still not a gate circuit, but it contains a nontrivial circuit-shaped kernel:

1. test membership in `A` in the standard basis;
2. apply `H` to the note register;
3. test membership in `A^perp`;
4. restore the basis if the verifier is meant to be non-destructive on an authentic note.

For a linear subspace, membership can be checked with parity-check matrices and reversible `CNOT` networks. That gives a precise circuit-compilation problem with count/depth/ancilla tradeoffs.

Important caveat: the current prototype publishes enough structure to prepare an accepting note. Optimizing its circuit demonstrates verifier compilation, **not public-key unforgeability**.

---

## 2. What makes the ECDLP 5-bit contest a useful model

The ECDLP contest works because it freezes a crisp semantic contract:

```text
|a>|b>|P>|Q>|0> -> |a>|b>|P>|Q>|aP + bQ>
```

It then separates:

- a trusted composer and evaluator;
- narrowly editable implementation paths;
- a primitive operation stream;
- hidden deterministic test shots;
- input preservation, phase-cleanliness, and ancilla-cleanup checks;
- a resource score balancing qubits, Toffoli count, and Toffoli depth.

The reusable pattern is:

```text
fixed semantics
    -> restricted implementation API
    -> untrusted circuit build
    -> trusted semantic validation
    -> trusted resource measurement
    -> ranked score
```

QMoney should reuse this control-plane pattern, but it should **not copy the ECDLP score blindly**. Hidden-subspace verifier circuits are primarily Clifford/linear-reversible networks, so their dominant primitive is the two-qubit `CNOT`, not Toffoli.

---

## 3. Candidate optimization problems

## 3.1 Track A — hidden-subspace verifier synthesis (recommended first)

### Goal

Build the cheapest exact circuit for the two complementary hidden-subspace membership tests used by the QMoney research verifier.

### Pilot parameters

```text
track: qmoney-subspace-verifier-8
n = 8 note qubits
k = 4 dimensional subspace A <= F_2^8
rank(H_A) = 4
```

Use a versioned suite of full-rank generator matrices `G` and parity-check matrices `H_A`, selected deterministically by the trusted harness. Start with tiny `n=8`, then add `n=12`, `n=16`, and hardware-topology variants.

The semantic object is the subspace, not one arbitrary matrix basis. Contestants should be allowed to replace `G` or `H_A` with row-equivalent full-rank matrices when that preserves the same membership projector. Choosing better generator/parity bases is part of the intended optimization surface.

Use two explicitly different modes rather than mixing their claims:

- **Transparent CSS synthesis mode (recommended pilot):** the builder receives `G`/`H_A` and optimizes their state-preparation or syndrome circuits. This is a compiler benchmark and makes no cryptographic secrecy claim.
- **Opaque-oracle verifier mode (later):** contestant code receives only capability handles such as `query_A` and `query_A_perp`; the trusted layer hides generators/support and ranks oracle-query count before gate resources. This is closer to the black-box verifier model but requires a much stronger sandbox boundary.

A useful public smoke fixture before the held-out `n=8` suite is `n=3`, with generators `101` and `011`. Its support is `{000, 101, 011, 110}`, and a baseline mint uses `H(0)`, `H(1)`, `CX(0,2)`, `CX(1,2)`.

### Mathematical contract

For a basis vector `x in F_2^n`:

```text
x in A       iff H_A x = 0
x in A^perp  iff G x = 0
```

The verifier instrument is:

```text
standard test:
    coherently compute syndrome H_A x
    measure syndrome; require all zero

complementary test:
    H^tensor-n on note
    coherently compute syndrome G x
    measure syndrome; require all zero
    H^tensor-n on note to restore the original basis
```

On the authentic state `|A>`, both tests accept with certainty and the restored note remains `|A>` in the ideal model.

### Circuit ABI

The trusted composer should own the complete verifier sequence. The contestant implementation should only synthesize the two linear maps through opaque handles:

```text
note[n]               quantum input; preserved on the authentic accepting path
standard_syndrome[n-k] initialized to zero
complement_syndrome[k] initialized to zero
scratch[*]            must be returned to zero
measurement record    fixed by trusted composer
```

Contestant API:

```text
emit_standard_syndrome(note, standard_syndrome, matrix_descriptor)
emit_complement_syndrome(note, complement_syndrome, matrix_descriptor)
```

Allowed operations in the first track:

- `CNOT` through opaque wire handles;
- optional allocation/free of clean ancillas;
- no direct access to raw qubit IDs;
- no process, filesystem, environment, or network state;
- no state-vector or truth-table lookup;
- no mutation of the trusted `H`, measurement, or acceptance sequence.

The trusted layer should own `H`, measurement, reset/uncompute semantics, op emission, score calculation, and hidden matrix instances.

### Correctness gate

Checking only computational-basis inputs is insufficient because it misses relative-phase errors. Use two independent gates:

1. **Exact linear-semantic check:** multiply the candidate elementary matrices over `F_2`, then verify that each emitted syndrome map has the required rank and row space/kernel. Do not require byte-for-byte equality with one canonical `G` or `H_A`; row-equivalent syndrome bases are valid.
2. **Exact Clifford/instrument check:** compare a stabilizer tableau or equivalent channel representation for the full trusted-composed verifier, including Hadamards, measurements, record bits, and ancilla cleanup. Syndrome outcomes may be relabeled by an invertible linear map, but the projectors and final accept/reject instrument must be equivalent.

Also run named fixtures:

- authentic `|A>` state: both tests accept with probability `1`;
- computational basis state `|x>` with `x notin A`: standard test rejects;
- basis state `|x>` with `x in A` but not a coherent uniform superposition: complementary test rejects with the expected distribution;
- dephased uniform mixture over `A`: standard test may pass, complementary test must expose lost coherence;
- random stabilizer states and adversarial phase-flipped subspace states;
- all input note wires preserved where the contract requires preservation;
- all scratch returned to zero; no residual phase or undeclared measurement dependence.

For the pilot sizes, exact tableau/channel comparison should be the promotion gate; random shots are additional evidence, not the proof of equivalence.

### Score

A balanced first score is:

```text
score = logical_qubits * sqrt((1 + two_qubit_gates) * (1 + two_qubit_depth))
```

where:

- `two_qubit_gates` counts `CNOT` after trusted primitive expansion;
- `two_qubit_depth` is dependency-layer depth, not source-code order;
- `+1` prevents degenerate zero scores for trivial instances;
- logical qubits include live scratch and syndrome ancillas.

Report, but do not initially combine into the primary score:

- total `H` count/depth;
- measurement count/depth;
- reset count;
- topology-routed `SWAP`/two-qubit cost;
- accepted-note preservation fidelity under a named noise model.

A later hardware-specific track can score native entangling error budget rather than abstract `CNOT` count.

For a multi-instance suite, normalize each score against a versioned reference circuit and aggregate with a weighted geometric mean. Publish the worst normalized instance as a secondary tie-breaker so one pathological matrix cannot be hidden by many easy wins.

### Optional mint companion

A closely related `qmoney-subspace-mint-8` subtrack can optimize preparation of the authentic state:

```text
|0^n> -> |A>
```

The candidate may choose any generator basis for the fixed subspace and synthesize the corresponding `H`/`CNOT` preparation network. The trusted evaluator should compare the final stabilizer state exactly up to global phase and then test it with an independently composed trusted verifier. Keep mint and verifier implementations independently editable so a matching bug in both cannot validate itself. A later combined score can report mint cost plus verification cost, but the two kernels should retain separate metrics.

### Why this track is good

- exact semantic map;
- cheap deterministic evaluator;
- real count/depth/ancilla tradeoffs;
- no need for a full universal state-vector simulator;
- natural progression from all-to-all to hardware topology;
- directly derived from the current hidden-subspace verifier story.

### What it does not prove

- hidden-subspace public-key unforgeability;
- security of the currently explicit public key;
- noise tolerance on physical quantum money;
- safety of the classical settlement or quorum layer.

---

## 3.2 Track B — one-note-to-two-notes counterfeit optimizer (recommended second)

### Goal

Given one valid Wiesner/BB84 note and blank output/ancilla registers, synthesize an attack channel that maximizes the probability that **both** candidate outputs pass independent verification.

This is an adversarial optimization problem, not a verifier-cost problem.

### Pilot contract

Start with one input qubit:

```text
input ensemble: {|0>, |1>, |+>, |->}, uniformly random
attacker input: one unknown ensemble state + clean blanks
attacker output: candidate A + candidate B + discarded environment
verifier: independent secret-basis checks on A and B
objective: expected probability that both accept
```

Then add product-note tracks at `n=2`, `n=3`, and `n=4`.

The trusted evaluator should model a valid CPTP channel, including discarded environment, and evaluate the exact ensemble-average pair acceptance. For tiny dimensions, use density matrices/process matrices rather than Monte Carlo as the promotion gate.

### Security reference

Molina, Vidick, and Watrous prove the optimal simple one-note-to-two-notes success for Wiesner's `n`-qubit product scheme is:

```text
(3/4)^n
```

That gives the benchmark a known target/upper-bound check for the idealized model.

### Ranking model

Do not hide the science behind one arbitrary resource penalty. Use constrained Pareto tiers:

```text
primary: maximize exact pair-acceptance probability
first tie-break: fewer two-qubit gates
second tie-break: lower two-qubit depth
third tie-break: fewer logical qubits
```

Publish separate leaderboards for fixed resource envelopes, for example:

```text
ancilla <= 1, two-qubit depth <= 2
ancilla <= 2, two-qubit depth <= 4
unrestricted tiny-instance exact track
```

This avoids a fragile formula that could rank a useless low-success circuit above a scientifically meaningful attack merely because it is small.

### Correctness and anti-cheating gates

- candidate must define a physical CPTP map;
- no access to secret basis/bit labels;
- no verifier queries unless the track explicitly budgets oracle interaction;
- no postselection hidden from the score;
- any measurement/feed-forward must be represented in the emitted instrument;
- evaluator computes acceptance from the final joint state, so entangled outputs are allowed;
- exact known upper bound acts as a harness sanity check;
- report attack success separately from empirical finite-shot estimates.

### Why this track matters

This directly operationalizes the repo's existing one-note-to-two-notes threat model and can compare:

- intercept/resend;
- measure-and-prepare attacks;
- universal or phase-covariant cloners;
- variationally synthesized cloning channels;
- depth/ancilla-constrained attacks.

It is more security-relevant than reducing the gate count of the BB84 verifier itself.

The current `one_note_to_two_counterfeit_trial(...)` helper is not yet this physical attack interface. It performs intercept/resend in a guessed basis and then duplicates an already-classical Python state description. For one BB84 qubit its exact joint-pass probability is `5/8`: a correct basis guess occurs with probability `1/2` and then both pass, while a wrong basis guess occurs with probability `1/2` and both independently pass with probability `1/4`. The optimal quantum one-to-two channel reaches `3/4`. The benchmark must therefore score a physical CPTP map, not reuse the current helper as its correctness oracle.

---

## 3.3 Track C — coherent programmable BB84 verifier (microbenchmark only)

A reversible or coherent kernel could take basis/bit descriptions as fixed classical instance data, rotate the candidate qubits, compute mismatch bits, and coherently aggregate an acceptance flag. For `P_(B,V) = H^B X^V`, a precise non-consumptive contract is:

```text
|psi_y>_Q |0^w>_W |a>_A
    -> |psi_y>_Q |0^w>_W |a XOR [wt(y) <= t]>_A
```

where `|psi_y> = P_(B,V)|y>`. A reference circuit applies `P†`, reversibly computes the Hamming-weight threshold, toggles the decision flag, uncomputes the predicate, and restores `P`. For `t > 0`, popcount/threshold comparison creates genuine qubit/Toffoli/depth tradeoffs and can use the ECDLP score `Q * sqrt(T_count * T_depth)`.

Possible ABI:

```text
|B>|V>|candidate>|0 mismatch>|0 accept>|0 scratch>
    -> secret registers preserved
    -> mismatch/accept result produced
    -> scratch cleaned
```

This can create controlled-H, population-count, threshold-compare, and uncomputation tradeoffs. It would look more like a Toffoli benchmark.

However, it is **not the operational circuit in the current QMoney architecture**:

- `B` and `V` are classical verifier-held data;
- candidate qubits are physically measured;
- mismatch counting naturally happens classically;
- making the secrets coherent adds quantum cost that the real design does not require.

Therefore this track is useful as a fault-tolerant compiler microbenchmark or a study of coherent verification, but it should not be called the QMoney production core.

---

## 3.4 Track D — quorum/settlement optimization (not a quantum-circuit contest)

The current production-facing system also has meaningful optimization questions:

- assign note indices to verifier nodes;
- minimize communication and verification latency;
- choose threshold/tolerance under failure and compromise models;
- atomically verify, spend, and remint bundles of notes;
- optimize false-accept/false-reject tradeoffs under noise.

These are distributed-systems, reliability, and statistical optimization problems. They should use protocol simulators/model checking, not circuit gate scores.

---

## 4. Recommended repository architecture

Use an ECDLP-like trusted/untrusted split:

```text
qmoney_circuit_bench/
  README.md
  benchmark.py
  tracks/
    subspace_verifier/
      contract.md
      architecture.mmd
      candidate.py                 # editable
      memory/
    wiesner_counterfeit/
      contract.md
      architecture.mmd
      candidate.py                 # editable
      memory/
  trusted/
    circuit_ir.py
    compose_subspace_verifier.py
    evaluate_clifford_instrument.py
    evaluate_counterfeit_channel.py
    metrics.py
    fixtures.py
  tests/
```

For a public contest, package the trusted evaluator separately so contestant code cannot import it. The repository pilot can keep both sides visible while the ABI and metrics stabilize.

Use public conformance fixtures plus server-held randomized instances generated after candidate circuit construction. Functional shots alone do not define admissibility: the capability API and computational model must independently forbid support tables, hidden test-ID branching, and direct accepting-state reconstruction.

The existing QMoney TLA+/Z3 lifecycle checks should remain hard release gates for issuance, oracle publication, query logging, and verification transitions, but they should not be mixed into the circuit-resource score.

### Required workflow

```text
setup
  -> preflight/static policy scan
  -> build candidate op stream
  -> exact semantic validation
  -> resource measurement
  -> lifecycle/formal release gates
  -> package editable paths only
  -> validate package independently
  -> submit/poll terminal result
```

### Required submission artifacts

- candidate implementation;
- `architecture.mmd` with fixed anchor labels;
- short experiment ledger under `memory/`;
- machine-readable metrics;
- semantic-validation receipt;
- declared model/tool attribution.

---

## 5. Anti-trivialization boundaries

A QMoney benchmark will be easy to accidentally game unless the contract is explicit.

### Hidden-subspace verifier track

Reject:

- precomputed truth tables over all `2^n` basis strings;
- state-vector inspection inside candidate code;
- direct acceptance lookup keyed by hidden fixture IDs;
- raw access to trusted matrix/test internals outside the descriptor API;
- circuits that match basis-state truth tables but alter phase/coherence;
- residual scratch, hidden postselection, or undeclared measurement dependence.

Decide explicitly whether instance-specific hand optimization is allowed. A good split is:

- **fixed-instance synthesis:** hardcoding the published matrix is allowed, but truth-table acceptance lookup is not;
- **generic compiler track:** candidate must work for a hidden suite of full-rank matrices supplied through an opaque linear-map API.

The generic compiler track is harder to game and scientifically more reusable.

### Counterfeit track

Reject:

- access to the secret state label;
- nonphysical maps;
- success conditioned on undisclosed postselection;
- verifier-oracle calls outside the declared query budget;
- reporting only marginal clone fidelity when the objective is joint pair acceptance.

---

## 6. Pilot milestones

### Phase 0 — freeze semantics before optimizing

1. Define the ideal hidden-subspace verifier as a quantum instrument.
2. Decide whether an accepted note is restored or consumed.
3. Freeze matrix dimensions and a deterministic fixture suite.
4. Freeze allowed operations and ancilla rules.
5. Define exact equivalence and score versions.

### Phase 1 — executable local benchmark

1. Implement a tiny circuit IR with `H`, `X`, `CNOT`, measurement, reset, allocate, and free.
2. Implement exact `F_2` linear-map validation.
3. Implement stabilizer-tableau or equivalent Clifford-instrument validation.
4. Emit a baseline Gaussian-elimination/parity-network circuit.
5. Produce `score.json`, `results.tsv`, and a validation receipt.
6. Add mutation tests proving that phase errors, wrong syndromes, and dirty ancillas are rejected.
7. Hash source archives and emitted circuit artifacts; delete stale op/score files before every build; rebuild submitted source inside a locked, offline sandbox.

### Phase 2 — optimization surface

1. Add alternative CNOT synthesis strategies.
2. Search row/column elimination orders.
3. Trade clean ancillas against CNOT depth.
4. Add connectivity-constrained variants.
5. Add a generic hidden-matrix compiler track.

### Phase 3 — adversarial benchmark

1. Implement exact one-qubit CPTP attack evaluation.
2. Add intercept/resend and a known optimal cloner baseline.
3. Verify the evaluator does not exceed the `(3/4)^n` reference bound.
4. Add resource-constrained Pareto tiers.
5. Extend only while exact validation remains tractable.

---

## 7. Go/no-go decision

### Go

Proceed with `qmoney-subspace-verifier-8` if the objective is to create a circuit-optimization challenge similar in engineering discipline to ECDLP 5-bit. It has the clearest ABI, trusted evaluator, and nontrivial circuit tradeoffs.

Proceed with `qmoney-wiesner-counterfeit-1to2` if the objective is to turn QMoney's security question into a competitive optimization problem. It is scientifically closer to the anti-counterfeiting claim, but its score and evaluator are more specialized.

### No-go

Do not launch a leaderboard around the current BB84 prepare/measure loop with the ECDLP score. Its Toffoli count is zero and its qubits are independent, so the score would be degenerate and the optimization would not target the real research bottlenecks.

Do not describe hidden-subspace circuit optimization as evidence that QMoney has achieved secure public-key quantum money. The current explicit-public-key prototype remains reconstructible.

---

## 8. Bottom line

QMoney can support a serious optimization benchmark, but the right abstraction is:

```text
not “optimize the current Python simulator”

instead:

freeze a quantum channel/oracle contract
  -> emit a primitive circuit
  -> validate exact semantics independently
  -> score implementation resources or attack success
```

The recommended first move is a hidden-subspace verifier compiler contest scored on qubits, two-qubit count, and two-qubit depth. The recommended second move is a one-note-to-two-notes attack-circuit contest scored primarily on exact joint acceptance probability under fixed resource envelopes.

Together, those tracks would let QMoney study both sides of the problem: **how cheaply can we verify, and how effectively can an adversary counterfeit?**

## References

- QMoney private-key simulator: [`pkey_quorum/demo.py`](../../pkey_quorum/demo.py)
- QMoney hidden-subspace prototype: [`pubkey_hidden_subspace/note_family.py`](../../pubkey_hidden_subspace/note_family.py)
- QMoney note-family evaluation checklist: [`note-family-evaluation-checklist.md`](note-family-evaluation-checklist.md)
- Scott Aaronson and Paul Christiano, *Quantum Money from Hidden Subspaces*, 2012: https://eprint.iacr.org/2012/171
- Abel Molina, Thomas Vidick, and John Watrous, *Optimal counterfeiting attacks and generalizations for Wiesner's quantum money*, arXiv:1202.4010: https://arxiv.org/abs/1202.4010
- Benjamin Coyle et al., *Variational Quantum Cloning: Improving Practicality for Quantum Cryptanalysis*, arXiv:2012.11424 / Phys. Rev. A 105, 042604 (2022): https://arxiv.org/abs/2012.11424
- Ketan N. Patel, Igor L. Markov, and John P. Hayes, *Optimal Synthesis of Linear Reversible Circuits*, Quantum Information and Computation 8 (2008), 282–294.
- ECDLP 5-bit contest contract and repository: https://github.com/ecdlp-contest/ecdlp-5-bit
