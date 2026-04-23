# QMoney Public-Key / Oracle Implementation Workflow

> **Implementation source of truth.** If an AI coding agent or human implementer is extending the QMoney public-key track, this document defines the required workflow and architecture checkpoints. Follow this before writing language-specific code.

## Purpose

This document exists to keep QMoney's public-key research track consistent across:
- Python prototypes
- TLA+ / TLC formal lifecycle specs
- Z3 symbolic invariant checks
- future ports to other languages

It is intentionally **language-agnostic**. The implementation language may change, but the workflow and architecture obligations should not.

For an agent-facing execution checklist, see:
- [`docs/architecture/public-key-agent-implementation-contract.md`](./public-key-agent-implementation-contract.md)

---

## Core rule

QMoney public-key work must be implemented in **three coordinated layers**:

1. **Math / note-family layer**
   - represents the note family itself
   - mints notes
   - defines verifier mathematics
   - demonstrates authentic vs counterfeit behavior

2. **Protocol / oracle lifecycle layer**
   - models issuance, oracle publication, query flow, and accept/reject transitions
   - captures what actions are allowed and in what order
   - is the home of lifecycle invariants

3. **Transition-stability / proof-checking layer**
   - checks whether invariants remain true after each supported transition
   - catches local rule mistakes early
   - should produce machine-checkable UNSAT/no-counterexample results where possible

No implementation should jump straight from note-family math to an ad hoc verifier API without explicitly defining the protocol/oracle lifecycle.

---

## What each tool is for

### A. Runtime implementation language (Python today, any language later)
Use the runtime language for:
- note-family math
- constructive examples
- minted note generation
- public verifier functions
- test fixtures for authentic and counterfeit notes
- developer-facing APIs and module boundaries

### B. TLA+ / TLC
Use TLA+ for:
- protocol state machine design
- oracle publication semantics
- allowed action ordering
- lifecycle invariants over reachable states
- bounded finite-state exploration via TLC

TLA+ is the source of truth for **protocol structure**, not for amplitude-level math.

### C. Z3
Use Z3 for:
- one-step inductiveness checks
- transition-local invariant preservation
- fast detection of invariant-breaking transition rules
- counterexample generation when a transition encoding is wrong

Z3 is the source of truth for **symbolic transition stability**, not for full protocol reachability.

---

## Current QMoney mapping

### Existing private-key baseline
- `pkey_quorum/demo.py`
- BB84/product-state notes
- quorum-held verification secrets
- verify-and-remint semantics

### Current public-key research track
- `pubkey_hidden_subspace/note_family.py`
- `tests/test_pubkey_hidden_subspace.py`
- `docs/research/hidden-subspace-notes.md`

### Current formal lifecycle track
- `tla/hidden_subspace_money.tla`
- `tla/hidden_subspace_money.cfg`

### Current symbolic stability track
- `z3/check_oracle_invariants.py`
- `tests/test_oracle_invariants_z3.py`

Today this Z3 layer intentionally covers the **core oracle publication/query consistency subset** rather than every invariant checked by TLC. If the TLA+ invariant set grows, either extend Z3 coverage for the relevant subset or document clearly why a given invariant class remains TLC-only.

This split is deliberate. Do not collapse it by mixing lifecycle logic directly into the note-family math layer.

---

## Non-negotiable implementation sequence

Any new public-key/oracle feature should be implemented in this order.

### Step 1: Define the note-family goal
Before coding, write down:
- what the valid note family is
- what the verifier is supposed to check
- what makes an authentic note pass
- what counterfeit class should fail first
- whether the construction is really public-key or only access-public

If these are not explicit, implementation should not start.

### Step 2: Write or update the runtime math prototype
Implement the smallest useful note-family runtime model.

Required properties:
- authentic note can be minted deterministically or reproducibly enough for tests
- verifier has a clear public API
- at least one counterfeit class is implemented and shown to fail
- tests prove the intended authentic/counterfeit distinction

For QMoney hidden-subspace work, this means the runtime layer should always make clear:
- what `A` is
- what `A^⊥` is
- what support/uniformity conditions are being checked

### Step 3: Update the TLA+ lifecycle model
If the runtime implementation changes the protocol surface, update TLA+.

Examples:
- new oracle publication rule
- new verifier transition
- new candidate presentation mode
- new query type
- new accept/reject precondition

The TLA+ spec must capture:
- what state exists
- what actions mutate it
- what invariants should always hold

If the runtime layer adds a protocol action but the TLA+ model does not mention it, the implementation is incomplete.

### Step 4: Add or update Z3 transition checks
For every new transition or invariant class, update the Z3 checker **or explicitly document why that invariant remains TLC-only**.

Required question:

> assuming invariants hold in pre-state `s`, can this transition produce a post-state `s'` that violates them?

The Z3 checker should answer this with:
- `unsat` when the transition preserves the invariant
- a concrete model/counterexample when it does not

If a new transition is added to TLA+ but not modeled in Z3 and no TLC-only rationale is documented, the transition-stability layer is incomplete.

### Step 5: Update tests
Every new behavior should have:
- runtime tests for authentic/counterfeit or verifier behavior
- symbolic/tests for Z3 checker coverage where applicable
- TLC rerun for lifecycle invariants when the spec changes

### Step 6: Update explanatory docs and diagrams
When the architecture meaningfully changes, update:
- research notes
- diagrams
- workflow docs like this one

If an AI agent changes the implementation flow but leaves the docs stale, the work is incomplete.

---

## Required invariants for oracle-style work

For any QMoney public-key/oracle prototype, the implementation should explicitly track some version of these invariant classes.

### Publication invariants
Examples:
- issued serials are the only serials with published oracle state
- subspace and dual oracle publication remain coupled
- acceptance cannot occur before publication

### Query-log invariants
Examples:
- queries only reference published/issued serials
- query records are tagged correctly by query kind
- logged answers match the declared oracle rule

### Decision invariants
Examples:
- authentic presentation has a defined accept path
- counterfeit presentation has a defined reject path
- verifier decisions cannot bypass required oracle preconditions

### Namespace invariants
Examples:
- public-key research code remains separate from the private-key baseline
- hidden-subspace work is not described as a BB84 metadata tweak

Not every prototype needs the exact same invariant list, but every prototype must declare its invariant families explicitly.

---

## Implementation pattern for AI coding agents

An AI coding agent should follow this exact loop.

### Phase 1: Read context
Read at minimum:
- this file
- `docs/research/hidden-subspace-notes.md`
- the relevant TLA+ spec
- the relevant Z3 checker
- the relevant runtime tests

### Phase 2: Classify the requested change
Decide whether the request affects:
- note-family math only
- lifecycle/oracle protocol only
- transition-stability checks only
- or multiple layers

Default assumption: most meaningful public-key/oracle changes affect **multiple layers**.

### Phase 3: Implement in this order
1. write or update failing tests
2. update runtime layer
3. update TLA+ lifecycle model
4. update Z3 checker
5. rerun runtime tests
6. rerun TLC
7. rerun Z3 checker
8. update docs/diagrams if architecture changed

### Phase 4: Report results in layer order
The implementation report should be structured as:
1. runtime change
2. TLA+ change
3. Z3 change
4. tests / TLC / Z3 verification results
5. architectural implications

---

## Language-porting rules

If this workflow is reimplemented in another language (Rust, Go, TypeScript, Haskell, etc.), preserve these boundaries:

### Must stay the same
- runtime note-family layer exists
- lifecycle state-machine layer exists
- symbolic/inductive checking layer exists
- docs explain the relationship between the three

### May change
- exact module names
- syntax
- testing framework
- SMT binding/library
- runtime data structures

### Must not change
- protocol rules without updating the formal model
- transition rules without updating the symbolic checker
- verifier meaning without updating tests
- note-family claims without updating explanatory docs

---

## What TLA+ and Z3 should teach implementers

### What TLA+ teaches
TLA+ should force the implementer to answer:
- what are the legal states?
- what transitions are legal?
- what must always remain true globally?
- what actions require prior oracle publication?

### What Z3 teaches
Z3 should force the implementer to answer:
- can this single transition break a claimed invariant?
- is the transition encoding missing a precondition?
- is a query/update rule locally inconsistent?

### What the runtime layer teaches
The runtime implementation should answer:
- does the note family actually exhibit the intended authentic/counterfeit distinction?
- does the verifier API reflect the protocol design honestly?
- are the mathematical claims testable in code?

---

## Current QMoney design guidance

For the hidden-subspace track specifically, future agents should prefer this decomposition:

- `pkey_quorum/demo.py`
  - note-family math
  - quorum transfer demo

- `pubkey_hidden_subspace/note_family.py`
  - note-family math
  - subspace and dual-space construction
  - authentic/counterfeit examples

- `pubkey_hidden_subspace/oracles.py`
  - explicit oracle/query abstraction
  - publication state
  - query logging helpers

- `pubkey_hidden_subspace/verifier.py`
  - verifier workflow matching the formal lifecycle
  - presentation / query / decision path

- `tla/hidden_subspace_money.tla`
  - protocol state machine

- `z3/check_oracle_invariants.py`
  - symbolic transition-stability checks

This is the preferred next-step architecture. Agents should move toward it unless there is a strong documented reason not to.

---

## Definition of done

A public-key/oracle implementation change is only done when all of the following are true:

- runtime behavior is implemented and tested
- TLA+ lifecycle model reflects the current protocol surface
- Z3 checker reflects the current transition set and invariant set
- TLC passes
- Z3 checker passes
- explanatory docs are updated
- the change preserves the private-key/public-key architectural separation

If any one of those is missing, the implementation is incomplete.

---

## Bottom line

This document is the implementation source of truth for QMoney public-key/oracle work.

The rule is simple:

> build the math layer, formalize the lifecycle, prove transition stability, and keep all three synchronized.

Any AI agent implementing QMoney in any language should follow that workflow.