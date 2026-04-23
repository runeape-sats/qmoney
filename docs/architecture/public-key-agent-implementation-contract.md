# QMoney Public-Key Agent Implementation Contract

> **Agent-facing execution contract.** Any AI coding agent implementing QMoney public-key/oracle work should treat this file as an operational checklist to follow before reporting completion.

## Mandatory reading set

Before implementing anything, read:
- [`README.md`](../../README.md)
- [`docs/architecture/public-key-implementation-workflow.md`](./public-key-implementation-workflow.md)
- [`docs/research/hidden-subspace-notes.md`](../research/hidden-subspace-notes.md)
- the relevant TLA+ spec in `tla/`
- the relevant Z3 checker in `z3/`
- the relevant runtime tests in `tests/`

Do not implement first and read later.

---

## Execution contract

### 1. Classify the change
State explicitly whether the requested change affects:
- runtime note-family math
- protocol/oracle lifecycle
- symbolic transition-stability checks
- docs/diagrams
- or multiple layers

If unsure, assume it affects multiple layers.

### 2. Write failing tests first
Before production code:
- add or update runtime tests
- add/update symbolic checker coverage if transition semantics change
- ensure the new test fails for the intended reason

No greenfield implementation without a red test.

### 3. Implement in required layer order
Always implement in this order:
1. runtime math / verifier layer
2. TLA+ lifecycle model
3. Z3 transition-stability layer
4. docs / diagrams

If a protocol action changes in code, the TLA+ and Z3 layers must be updated in the same task.

### 4. Required verification commands
Agents should not claim completion without running the applicable commands.

#### Runtime tests
```bash
python -m unittest discover -s tests -v
```
Or the repo-local venv equivalent if the task depends on local packages:
```bash
.venv/bin/python -m unittest discover -s tests -v
```

#### Z3 checker
```bash
.venv/bin/python z3/check_oracle_invariants.py
```
Expected shape of result:
- `"result": "all_passed"`
- every covered invariant/transition check returns `"unsat"`

Note: the current Z3 checker covers the documented oracle-consistency subset; TLC remains the fuller lifecycle invariant pass.

#### TLC model check
```bash
java -jar .tools/tla2tools.jar -config tla/hidden_subspace_money.cfg tla/hidden_subspace_money.tla
```
Expected result:
- `Model checking completed. No error has been found.`

If the change affects only one layer, the agent must still explain why the other verification steps are unchanged or not applicable.

---

## Required architectural assertions

Before completion, confirm all of the following remain true.

### Separation assertions
- public-key research code remains separate from the private-key baseline
- hidden-subspace work is not described as a BB84 metadata tweak
- lifecycle logic is not buried inside note-family math without a formal counterpart

### Oracle assertions
- issued serials are the only serials with published oracle state
- subspace and dual oracle publication stay coupled
- query records only reference valid published/issued serials
- verifier decisions cannot bypass required oracle preconditions

### Documentation assertions
- if architecture meaning changed, docs changed too
- if workflow meaning changed, the workflow doc changed too
- if agent execution expectations changed, this contract changed too

---

## Completion report format

Agents should report completion in this order:

1. **Runtime layer**
   - what code changed
   - what authentic/counterfeit behavior changed

2. **TLA+ layer**
   - what states/actions/invariants changed

3. **Z3 layer**
   - what transition checks/invariants changed

4. **Verification results**
   - runtime tests
   - Z3 checker
   - TLC run

5. **Architectural impact**
   - how the change affects future public-key/oracle work

This report format is mandatory for non-trivial public-key/oracle changes.

---

## Stop conditions

An agent must stop and escalate instead of guessing if:
- the requested change would merge private-key and public-key layers ambiguously
- the verifier math changes but the lifecycle implications are unclear
- the TLA+ model and runtime code disagree on action meaning
- the Z3 checker produces a satisfiable counterexample and the cause is not understood
- the docs would need a conceptual rewrite, not a local patch

---

## One-sentence rule

> For QMoney public-key/oracle work: implement the math, formalize the lifecycle, prove transition stability, verify all three, then update the docs.
