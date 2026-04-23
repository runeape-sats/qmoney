# Shor’s Quantum Money Arguments and How to Integrate Them with QMoney

Source context:
- Peter Shor seminar on quantum money (`hnY40A5fde0`)
- Companion architecture note:
  - `docs/architecture/public-vs-private-key-qmoney.md`

This note is the repo-facing synthesis: not just what Shor argued, but how those arguments should change the way QMoney is described, structured, and extended.

---

## Executive summary

Peter Shor’s talk gives QMoney three important lessons.

### 1. QMoney must be described honestly
If the note-verification rule depends on hidden per-note measurement data, then the scheme is **private-key quantum cash**, not public-key quantum money.

That means current QMoney should be framed as:
- quorum-verified private-key quantum cash,
- with classical public-key ownership and settlement,
- and verify-and-remint semantics.

### 2. Public-key quantum money is a separate research track
Shor’s arguments do **not** support the idea that a BB84-style note can be made public-key by revealing more metadata, commitments, or verifier hints. If enough information is published to reproduce the valid state, the note becomes forgeable.

So the public-key roadmap for QMoney must mean:
- a **different note family**,
- a **different verifier model**,
- and probably a **separate namespace in code and docs**.

### 3. Verification must certify quantum coherence, not just classical proximity
One of Shor’s most important arguments is that a verification procedure can fail if it cannot distinguish:
- a genuine quantum superposition,
from
- a classically sampled or partially collapsed substitute.

For QMoney, this means any future public-key or advanced note-family work must treat **coherence-sensitive verification** as a first-class requirement.

---

## 1. Shor’s core arguments

### 1.1 What quantum money is
Shor defines quantum money as a state with two properties:
- it can be **verified** from its serial number,
- but it cannot be **duplicated** into two states that both pass verification.

This is the clean target that matters for QMoney too. A note is not “quantum money” just because it uses qubits. It has to satisfy both:
- **validity under verification**, and
- **anti-counterfeiting by unclonability**.

### 1.2 Why no-cloning is not enough
Shor emphasizes that the no-cloning theorem is only the starting intuition.

A usable money system also needs a verifier model that does not accidentally reveal enough information to recreate the note. So the hard design problem is not merely preparing exotic states. It is building a verification procedure that is both:
- informative enough to accept honest notes,
- but not informative enough to let verifiers or adversaries mint new ones.

### 1.3 Why Wiesner money is private-key
Shor’s discussion of Wiesner is directly relevant to QMoney.

Wiesner’s scheme works because the verifier knows hidden basis information. That means:
- the bank can verify,
- but merchants cannot safely verify if they are not trusted,
- and if enough secret information spreads outward, counterfeitability returns.

This is exactly the right mental model for current QMoney: if a committee/quorum holds hidden note-verification data, then the system is in the **private-key quantum money family**, even if verification access is decentralized.

### 1.4 Why public-key quantum money is structurally different
Shor’s candidate directions beyond Wiesner—knots, modular forms, lattices—are not “Wiesner plus more metadata.” They are different constructions aimed at a different target.

That matters because it means the correct QMoney roadmap is not:
- “reveal enough about the current BB84 note family until it becomes public-key.”

It is instead:
- “keep the current BB84/quorum design as the private-key baseline,”
- “build separate public-key research note families next to it.”

### 1.5 Why lattice verification is conceptually hard
In Shor’s lattice discussion, the first protocol fails because the verifier cannot tell the difference between:
- the intended coherent quantum superposition,
- and a weaker mixture/classicalized substitute.

This is one of the deepest arguments in the talk.

It says a note family can fail even if the verifier checks something mathematically meaningful, if the verifier does not really test the *quantum-ness* needed for security. That is the exact kind of failure QMoney should try to avoid in future note-family experiments.

### 1.6 Why practical quantum money is still far away
Shor is explicit that current constructions are mostly theoretical. His own estimates suggest that lattice-style schemes may need:
- many component states,
- many logical qubits,
- and perhaps tens of thousands of logical qubits overall.

So QMoney should not position itself as “close to productizing true public-key quantum money.” The honest near-term role is:
- research platform,
- conceptual simulator,
- architecture clarifier,
- and testbed for comparing note families.

---

## 2. What Shor’s arguments imply for current QMoney

## 2.1 Current QMoney is a two-layer system
Shor’s framing helps cleanly separate the two layers in QMoney.

### Quantum layer
Current QMoney note validity depends on hidden note-specific data such as basis/outcome secrets. That means:
- the quantum note family is private-key,
- the security story is Wiesner-like in structure,
- even if the implementation is distributed across a quorum rather than a single bank.

### Classical layer
QMoney also uses ordinary public-key cryptographic concepts for:
- owner identities,
- transaction signatures,
- quorum attestations,
- spent-state tracking,
- and ledger finality.

This classical public-key layer is real and important, but it does **not** upgrade the quantum note family into public-key quantum money.

### Required repo language
Shor’s arguments support the following repo-safe phrasing:

> QMoney currently implements a quorum-verified, private-key quantum cash design with verify-and-remint, plus a classical public-key settlement layer.

That description should be preferred over any phrasing that suggests current QMoney is already public-key quantum money.

---

## 2.2 “Public verification” must be disambiguated
Shor’s lecture makes it clear that “public verification” can mean two different things.

### Sense A: public access to a verification service
Anyone can submit a note to a verifier or quorum.

### Sense B: true public-key verification
Anyone can run the verification algorithm themselves from public information, without hidden note secrets, and without gaining the ability to forge notes.

Current QMoney only supports something like **Sense A**.

That means docs should avoid ambiguous claims like:
- “QMoney supports public verification”

unless immediately qualified as:
- “publicly accessible verification by a secret-holding quorum,” or
- “public access to verification requests, not non-interactive public-key quantum verification.”

---

## 2.3 Verify-and-remint is the right current model
Shor’s analysis also reinforces why QMoney’s current verify-and-remint framing is the correct one.

In a consumptive quantum verification model:
- a note is presented,
- measured,
- consumed by verification,
- and replaced with a fresh note if valid.

That is fundamentally different from a purely classical “same token gets checked repeatedly without being consumed” model.

So QMoney should continue to lean into:
- **consumptive verification**,
- **serial invalidation**,
- **fresh note issuance**,
- **ledger atomicity around remint**.

These are not implementation quirks; they are architecture-defining features.

---

## 3. What Shor’s arguments imply for the future QMoney roadmap

## 3.1 Do not try to “public-key-ify” the BB84 baseline
This is the most important roadmap constraint.

If the current note family depends on hidden basis/outcome data, then publishing enough information to let everyone verify directly will also tend to let everyone reconstruct the valid state.

So the wrong path is:
- publish the basis strings,
- publish commitment openings,
- publish verifier-derived reconstruction hints,
- or otherwise leak enough per-note structure to make verification public.

That does not convert the design into public-key quantum money. It destroys the hidden-information assumption the note family depends on.

## 3.2 Create a separate public-key namespace
Shor’s talk strongly supports separating note families.

Recommended split:

### Private-key baseline track
- current BB84/product-state notes
- quorum-held verification secrets
- verify-and-remint
- classical settlement layer
- engineering hardening, noise models, tests

### Public-key research track
- new note families under `pubkey_hidden_subspace/`
- hidden-subspace / oracle-backed prototypes
- later noise-tolerant public-key experiments
- possibly later frontier tracks like group actions

This helps the repo maintain conceptual honesty.

## 3.3 Add coherence-sensitive verification requirements to new note-family work
The failed first lattice proposal in Shor’s talk should become an explicit design warning inside QMoney.

Any future note-family proposal should answer:
1. What exactly is the valid quantum state family?
2. What does the verifier actually test?
3. Can a classically sampled substitute pass?
4. Can a partially collapsed mixture pass?
5. Does verification test coherence or only geometric/statistical closeness?

This should become part of the review rubric for any future public-key experiments.

## 3.4 Treat practicality as a research variable, not a marketing claim
Shor is explicit that current constructions are large and expensive.

So QMoney should present public-key work as:
- cryptographic architecture research,
- not near-term deployable payments infrastructure.

A good standard for future docs is:
- separate **conceptual correctness** from **practical feasibility**,
- include qubit-count and verification-overhead discussions early,
- avoid implying that simulated note families are near-hardware-ready.

---

## 4. Concrete integration plan for QMoney

## 4.1 Documentation integration

### A. Keep the current architecture note as the canonical description of the baseline
Existing file:
- `docs/architecture/public-vs-private-key-qmoney.md`

Role:
- explain the current baseline honestly,
- define the two-layer architecture,
- prevent category confusion.

### B. Keep local Shor source notes outside the committed repo tree
Existing source material:
- local, uncommitted seminar notes / timestamped extraction

Role:
- timestamped extraction,
- seminar-specific citations,
- raw evidence for the repo’s wording choices.

### C. Use this note as the synthesis doc
This file should serve as:
- the “why this matters for QMoney” explanation,
- the bridge between literature and repo architecture.

### D. Add a future literature index
Recommended future file:
- `docs/research/public-key-qmoney-literature-review.md`

That file should place Shor alongside:
- Wiesner,
- Aaronson-Christiano / hidden subspaces,
- noise-tolerant oracle work,
- Zhandry / group-action directions,
- negative results and broken templates.

---

## 4.2 Codebase integration

### A. Preserve the current simulator as the honest private-key baseline
Current simulator-style work should remain the baseline implementation of:
- distributed private-key quantum cash,
- not public-key quantum money.

### B. Create a research namespace before adding public-key code
Recommended paths:
- `pubkey_hidden_subspace/__init__.py`
- `pubkey_hidden_subspace/README.md`
- `pubkey_hidden_subspace/note_family.py`

This enforces the distinction in code, not just prose.

### C. Add note-family comparison criteria
Recommended future comparison doc or module comments should track:
- verifier type: secret-holding vs public
- mint type: secret-bearing vs measurement-randomized
- verification type: consumptive / non-consumptive
- coherence sensitivity: yes / no / unclear
- practicality estimate: qubits, samples, verification repetitions
- current status: baseline engineering / research prototype / literature-only

This would make QMoney more of a disciplined research platform.

---

## 4.3 Terminology integration

These terms should be used consistently.

### Preferred current-system labels
- private-key quantum cash
- quorum-verified private-key quantum cash
- verify-and-remint quantum cash
- classical public-key settlement layer

### Labels to avoid for the current system
- public-key quantum money
- trustless public verifier
- universally self-verifiable quantum money

unless the sentence explicitly says this is future work or a separate research track.

---

## 5. Recommended next documents or tasks

## Task 1: Add README-safe language
Add a short section to the README clarifying:
- current QMoney is private-key at the quantum note layer,
- classical public-key at the settlement layer,
- public-key quantum money remains future research.

## Task 2: Add a literature review note
Create:
- `docs/research/public-key-qmoney-literature-review.md`

Include:
- Wiesner,
- Shor seminar takeaways,
- hidden-subspace track,
- noise-tolerant public-key track,
- group-action frontier,
- broken or dangerous directions.

## Task 3: Add a note-family evaluation checklist
Create:
- `docs/research/note-family-evaluation-checklist.md`

Checklist items should include:
- what hidden information remains,
- what exactly the verifier learns,
- whether verification is coherence-sensitive,
- whether the mint can issue duplicates with the same serial,
- whether the proposal is really public-key or only access-public.

## Task 4: Establish `pubkey_hidden_subspace/`
Even before real implementation, a namespace and README would force conceptual separation.

## Task 5: Preserve the current simulator as baseline, not stepping stone rhetoric
The current simulator should be described as:
- a valid and useful baseline for distributed private-key quantum cash,
- not as a nearly-public-key construction waiting for a metadata tweak.

---

## Bottom line

Shor’s arguments should change how QMoney talks about itself.

They imply:
- current QMoney is best understood as **private-key quantum cash with a classical public-key settlement layer**,
- true public-key quantum money should be developed as a **separate research program**,
- and future note-family work must pay special attention to whether verification actually checks the required quantum coherence rather than accepting classically collapsed stand-ins.

That is the honest integration path:
- preserve the current baseline,
- document it clearly,
- separate future public-key work,
- and use Shor’s arguments as a guardrail against overclaiming and architectural confusion.
