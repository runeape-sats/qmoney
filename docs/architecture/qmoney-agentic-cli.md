# QMoney Agentic CLI Design Doc

> **Status:** proposed v1 design  
> **Audience:** AI agents, implementers, and human operators working in `~/code/qmoney`

---

## 1. Purpose

This document defines the architecture and help-contract for a new `qmoney` CLI.

The CLI is meant to turn the current repo into a stable **agent-facing command surface** without collapsing the repo’s conceptual boundaries.

It must do two jobs at once:

1. expose runnable functionality from the repo in a consistent command hierarchy
2. explain the **idea** behind each path through multi-level `--help`

The second requirement is not optional. In this design, `--help` is part of the product surface, not an afterthought.

---

## 2. Design goal

Build a first-class `qmoney` command that lets AI agents and humans:

- run the current private-key quorum baseline
- inspect and exercise the research-only public-key hidden-subspace path
- use oracle-backed verifier workflow commands
- run formal lifecycle/stability checks
- learn the conceptual meaning of each path directly from `--help`

The CLI should make a new user or agent understand:

- what QMoney is
- what QMoney is **today**
- what is private-key vs public-key in this repo
- what each command does
- what each command does **not** claim

---

## 3. Non-goals

This CLI is **not** meant to:

- rebrand the repo as deployable public-key quantum money
- hide the difference between simulation, prototype, and formal model
- replace the repo’s architecture docs entirely
- introduce a heavy dependency stack for terminal UX
- claim that passing formal checks proves production cryptographic security

---

## 4. Core architectural principle

The CLI must preserve the repo’s existing split:

- `pkey_quorum/` = current private-key quorum baseline
- `pubkey_hidden_subspace/` = research-only public-key hidden-subspace track
- `tla/` = lifecycle/protocol structure
- `z3/` = symbolic transition-stability checks

The CLI is a **wrapper and explainer**, not a new protocol layer.

It should expose these layers cleanly instead of mixing them together.

---

## 5. Why an agentic CLI is needed

Right now the repo already contains useful components, but they are scattered across:

- Python modules
- demo scripts
- formal tooling
- architecture docs

That is workable for a human who already knows the repo, but brittle for AI agents.

An agent-friendly CLI improves:

- discoverability
- deterministic invocation
- machine-readable output
- boundary clarity
- explainability at the command surface

In practice, this CLI is the repo’s **operational contract for agents**.

---

## 6. Top-level command model

```text
qmoney
├── pkey
│   ├── demo
│   ├── forge-intercept
│   ├── counterfeit-pair
│   └── adaptive-probe
├── pubkey
│   ├── mint
│   ├── summarize-key
│   ├── verify-note
│   ├── hadamard
│   └── oracle
│       ├── publish
│       ├── query-subspace
│       ├── query-dual
│       └── verify
├── formal
│   ├── z3-check
│   └── tlc-check
└── explain
    ├── qmoney
    ├── pkey-path
    ├── pubkey-path
    └── command-contract
```

---

## 7. Root-level help contract

The user requirement is explicit:

- `qmoney --help` must explain the **idea of QMoney**
- `qmoney pubkey --help` must explain the **idea of the public-key path**
- `qmoney pkey --help` must explain the **idea of the private-key quorum path**

That means help text is layered by conceptual scope.

### 7.1 `qmoney --help` must explain the idea of QMoney

Root help should answer:

- What is QMoney?
- Why is quantum money interesting?
- What does this repo currently implement?
- Why does the repo split private-key and public-key paths?
- What do `pkey`, `pubkey`, `formal`, and `explain` represent?

### Required root-help themes

- QMoney uses **no-cloning** as the anti-counterfeiting primitive.
- QMoney combines a quantum note idea with a classical ownership/settlement layer.
- The repo’s **current baseline** is private-key, quorum-verified, and verify-and-remint.
- The public-key path is a **research track**, not a production claim.
- Formal commands check consistency of lifecycle logic, not deployability.

### Example root-help content target

```text
QMoney agent CLI

Idea:
  QMoney explores quantum money as a hybrid system: quantum states provide the
  anti-counterfeiting primitive, while classical systems handle ownership,
  attestations, and settlement.

What this repo is today:
  The current baseline is private-key, quorum-verified, and verify-and-remint.
  A separate research path explores public-key hidden-subspace ideas.

Command families:
  pkey    Current private-key quorum path.
  pubkey  Research-only public-key hidden-subspace path.
  formal  Lifecycle and invariant checks for the research workflow.
  explain Conceptual explanations for agents and humans.
```

---

## 8. `qmoney pkey --help` contract

This help screen should explain the **private-key quorum path as an idea**, not just list subcommands.

It should answer:

- Why is this path private-key?
- Why does verification require hidden verifier information?
- Why is verification consumptive?
- Why does the system use verify-and-remint instead of preserving the same note forever?
- Why is quorum verification useful in this repo?

### Required `pkey` help themes

- this is the repo’s current practical baseline
- notes are BB84-style/product-state notes with hidden verifier secrets
- verification depends on private secret data held by a quorum
- measurement consumes the note
- successful transfer means accepting the note and minting a fresh one
- this is not public-key quantum money

### Example `pkey --help` content target

```text
qmoney pkey

Idea:
  This path models QMoney as distributed private-key quantum cash.

Why it is private-key:
  A valid note can only be checked by parties who hold hidden verification data.
  Public visibility of that data would undermine the note family.

Why quorum exists:
  Instead of a single verifier, the repo models a distributed verifier set that
  collectively checks notes and attests outcomes.

Why verify-and-remint exists:
  Measurement consumes the note, so successful transfer means minting a fresh
  note for the receiver rather than preserving the old one unchanged.
```

---

## 9. `qmoney pubkey --help` contract

This help screen should explain the **public-key path as an idea**.

It should answer:

- What is the goal of the public-key path?
- Why is public verification hard?
- What is the hidden-subspace prototype trying to model?
- Why is this repo careful not to over-claim security here?
- Where do oracle and formal checks fit in?

### Required `pubkey` help themes

- this path explores **public verification**
- it is research-only
- it uses a hidden-subspace toy model for conceptual clarity
- current software publication exposes too much structure for deployable security
- oracle commands model publication/query workflow
- formal commands live separately because protocol consistency is not the same as note-family math

### Example `pubkey --help` content target

```text
qmoney pubkey

Idea:
  This path explores what public-key quantum money would need: public
  verification without revealing enough structure to mint counterfeits.

What this repo models:
  A hidden-subspace prototype that makes the verifier workflow explicit.

Important caveat:
  The current software prototype is research-only and publishes enough structure
  to reconstruct an accepting note. It demonstrates workflow and note-family
  ideas, not deployable public-key security.

Related paths:
  oracle  Publication/query workflow around the public verifier.
```

---

## 10. `qmoney formal --help` contract

Although the user’s specific requirement focused on root, `pubkey`, and `pkey`, the formal path should follow the same design standard.

It should answer:

- what “formal” means in this repo
- why there are both TLA+ and Z3 checks
- why formal checking is separate from runtime simulation
- what passing these checks does and does not imply

### Required formal-help themes

- TLA+ / TLC checks lifecycle structure and reachable-state invariants
- Z3 checks one-step transition stability
- these are consistency tools for the research workflow
- they do not establish production cryptographic soundness

---

## 11. Help content standard for all levels

Every command group and leaf command should include these sections in either `description` or `epilog`:

1. **Idea** or **What this is**
2. **Why it exists**
3. **How it works**
4. **What it does not prove**
5. **Output contract**
6. **Examples**

This is especially important for AI agents, because agents often need conceptual framing before choosing a command.

---

## 12. CLI implementation approach

### 12.1 Parser library
Use Python stdlib `argparse` for v1.

Reasons:
- already consistent with existing repo CLI patterns
- zero external dependency cost
- stable in CI and simple Python environments
- good enough for nested subcommand trees
- compatible with custom formatter classes for rich help text

### 12.2 Custom help formatter
Add a small formatter/helper layer to preserve:
- multi-paragraph descriptions
- section headers
- readable examples
- stable wrapping

Likely file:
- `qmoney_cli/helptext.py`

### 12.3 Command registration
Use a modular registration pattern:
- `qmoney_cli/app.py` builds the root parser
- each command family registers itself

Likely files:
- `qmoney_cli/commands/pkey.py`
- `qmoney_cli/commands/pubkey.py`
- `qmoney_cli/commands/oracle.py`
- `qmoney_cli/commands/formal.py`
- `qmoney_cli/commands/explain.py`

---

## 13. Output contract

Every operational command should support:

- `--json` for deterministic machine-readable output
- `--pretty` for formatted JSON or readable structured output
- exit code `0` on success
- non-zero exit code on validation/runtime/tool failure

Default output should stay concise for human terminal use.

### Recommended rule
- human-readable text by default
- canonical JSON when `--json` is supplied

### Why this matters
AI agents need:
- stable field names
- predictable exit behavior
- explicit failure reporting
- minimal ambiguity around result parsing

---

## 14. Command family responsibilities

## 14.1 `pkey`
Wrap the current private-key baseline in `pkey_quorum/`.

Primary responsibilities:
- simulate mint → verify → consume → remint
- expose attack experiments
- expose verifier-leakage probes

This family is the CLI representation of the repo’s **current baseline**.

## 14.2 `pubkey`
Wrap the hidden-subspace runtime path in `pubkey_hidden_subspace/`.

Primary responsibilities:
- mint toy hidden-subspace notes
- summarize public key structure
- verify authentic/counterfeit toy notes
- show Hadamard/dual-subspace behavior

This family is the CLI representation of the repo’s **research public-key path**.

## 14.3 `pubkey oracle`
Wrap the publication/query/verifier workflow.

Primary responsibilities:
- publish oracle state
- answer subspace membership queries
- answer dual-subspace membership queries
- run lifecycle-aware verification

This family exists to make the public-verification workflow explicit.

## 14.4 `formal`
Wrap the research consistency tools.

Primary responsibilities:
- run Z3 transition/invariant checks
- run TLC lifecycle checks

This family exists to validate structure, not to replace runtime experiments.

## 14.5 `explain`
Provide pure explanation commands.

Primary responsibilities:
- explain QMoney idea
- explain private-key quorum path
- explain public-key path
- explain the CLI contract

This prevents operational commands from becoming bloated with tutorial content.

---

## 15. Relationship to current repo code

### Existing code used directly
- `pkey_quorum/demo.py`
- `pubkey_hidden_subspace/note_family.py`
- `pubkey_hidden_subspace/oracles.py`
- `pubkey_hidden_subspace/verifier.py`
- `z3/check_oracle_invariants.py`

### Existing docs that define semantics
- `README.md`
- `docs/architecture/public-vs-private-key-qmoney.md`
- `docs/architecture/public-key-implementation-workflow.md`
- `docs/architecture/public-key-agent-implementation-contract.md`

The CLI should derive its conceptual language from those docs instead of inventing a parallel vocabulary.

---

## 16. Suggested file layout

### New files
- `pyproject.toml`
- `qmoney_cli/__init__.py`
- `qmoney_cli/__main__.py`
- `qmoney_cli/app.py`
- `qmoney_cli/helptext.py`
- `qmoney_cli/parsers.py`
- `qmoney_cli/output.py`
- `qmoney_cli/commands/__init__.py`
- `qmoney_cli/commands/pkey.py`
- `qmoney_cli/commands/pubkey.py`
- `qmoney_cli/commands/oracle.py`
- `qmoney_cli/commands/formal.py`
- `qmoney_cli/commands/explain.py`

### Tests
- `tests/test_qmoney_cli_help.py`
- `tests/test_qmoney_cli_pkey.py`
- `tests/test_qmoney_cli_pubkey.py`
- `tests/test_qmoney_cli_formal.py`

---

## 17. Testing requirements

## 17.1 Help tests
Must verify:

- `qmoney --help` explains QMoney as an idea, not just command names
- `qmoney pkey --help` explains the private-key quorum path
- `qmoney pubkey --help` explains the public-key path
- `qmoney formal --help` explains TLA+/Z3 roles
- leaf commands include examples and output contract sections

## 17.2 Behavioral tests
Must verify:

- `pkey` wrappers produce deterministic outputs with fixed seeds
- `pubkey` wrappers distinguish authentic vs counterfeit toy notes
- `oracle` wrappers log and report publication/query behavior correctly
- `formal` wrappers report clear success/failure/missing-tool states

---

## 18. Risks

### Risk: help becomes too long
Mitigation:
- keep root/group help concise but meaningful
- move larger explanations into `qmoney explain ...`
- preserve the idea-first paragraphs while keeping command option sections compact

### Risk: CLI overstates public-key security
Mitigation:
- repeat the research-only caveat in `pubkey --help`
- repeat caveats in leaf pubkey/oracle help where appropriate
- keep operational/public-key/formal boundaries explicit

### Risk: formal checks get mistaken for full security proofs
Mitigation:
- always state that TLA+/Z3 check lifecycle/stability consistency, not production cryptographic soundness

### Risk: duplicated logic diverges from runtime modules
Mitigation:
- keep wrappers thin
- prefer importing existing functions/classes over re-implementing protocol logic

---

## 19. Recommended implementation order

1. add package entrypoint
2. add custom help framework
3. implement root / `pkey` / `pubkey` / `formal` help contracts first
4. add parser/output helpers
5. implement `pkey` operational commands
6. implement `pubkey` operational commands
7. implement `oracle` commands
8. implement `formal` commands
9. add `explain` commands
10. update README and architecture docs

This ordering ensures the conceptual contract is defined before operational details sprawl.

---

## 20. Definition of done

This design is satisfied when:

- `qmoney --help` explains the idea of QMoney
- `qmoney pkey --help` explains the private-key quorum path
- `qmoney pubkey --help` explains the public-key path
- operational commands are grouped along the repo’s real architecture
- `--json` outputs are deterministic and documented
- formal commands clearly distinguish consistency checks from security claims
- tests cover both help quality and operational behavior

---

## 21. One-sentence design summary

The `qmoney` CLI should be an **agent-first operational interface whose help system teaches the architecture of QMoney while its command tree preserves the repo’s private-key baseline, public-key research path, oracle workflow, and formal verification boundaries**.
