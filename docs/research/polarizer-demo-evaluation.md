# Polarizer Demo Evaluation for QMoney

This memo evaluates a **polarizer-style physical demo** for QMoney.

It is written to help the project present the demo honestly to researchers, builders, funders, and curious users.

## Executive summary

A polarizer demo is a **good educational and intuition-building artifact** for QMoney's current private-key baseline.

It is **not**, by itself:
- a proof of full cryptographic security,
- a production optical architecture,
- a hardware implementation of the current repo,
- or evidence that QMoney has reached true public-key quantum money.

The clean framing is:

> The polarizer demo is a physical intuition demo for QMoney's current **private-key BB84-style note family**. It demonstrates hidden-basis verification, disturbance under wrong-basis probing, and why verification consumes the note. It does not yet demonstrate a deployable hardware protocol or true public-key quantum money.

---

## 1. What the current repo actually supports

Per the current repo architecture, QMoney today is:
- **private-key quantum cash** at the quantum note layer,
- **quorum-verified** rather than universally self-verifiable,
- **verify-and-remint** rather than repeated non-consumptive checking,
- and equipped with a **classical public-key settlement layer** for ownership and ledger logic.

Important repo-aligned boundaries:
- `pkey_quorum/` is the current private-key baseline.
- `pubkey_hidden_subspace/` is a separate research track for future public-key experiments.
- `docs/architecture/qmoney-pkey-polarizer-experiment.md` explicitly frames the polarizer story as an **analogy**, not a literal claim that the current code already runs on optical hardware.

That means a polarizer demo should be presented as a visualization of the **private-key path**, not the public-key research path.

---

## 2. What the polarizer demo explains well

A good polarizer demo is excellent for explaining the following ideas:

### 2.1 Four BB84-style states
The private-key baseline can be explained using four polarization-like states:
- `0°`
- `90°`
- `45°`
- `135°`

This gives a simple physical picture for the BB84-style state alphabet.

### 2.2 Two incompatible basis families
The demo makes it intuitive that there are two different measurement families:
- rectilinear / `Z`-like
- diagonal / `X`-like

That helps non-specialists understand why there is no single public test that reveals everything safely.

### 2.3 Wrong-basis probing disturbs the note
This is the central anti-counterfeiting intuition.

If an attacker probes a slot in the wrong basis/orientation, they disturb the state and lose information. That makes “look at it and copy it” fundamentally different from classical duplication.

### 2.4 Verifier-held hidden recipe
The demo helps explain why the verifier must know a hidden per-slot recipe:
- which basis to use,
- which result is expected,
- and how many mismatches are allowed.

This is exactly why the current QMoney baseline is **private-key** rather than public-key.

### 2.5 Consumptive verification and remint
A strong demo can show that the act of checking the note uses it up.

That maps naturally to the repo's current **verify-and-remint** model:
1. present note,
2. verify by measurement,
3. consume original,
4. mint fresh replacement note for the receiver.

---

## 3. What the demo does not prove

This is the section that prevents overclaiming.

A polarizer demo does **not** prove:
- full cryptographic security,
- optimal counterfeit resistance,
- composable transfer security,
- resilience to adaptive verifier-query leakage,
- correctness of a production optical networking stack,
- or true public-key quantum money.

More specifically, it does not answer the deeper public-key question:

> Can anyone verify using only public information **without** learning enough structure to mint valid counterfeit notes?

That is a different research problem and belongs to the public-key track, not the private-key polarizer analogy.

---

## 4. Evaluation scorecard

## 4.1 As a public explanation
**Score: 8.5/10**

Strengths:
- immediately visual,
- intuitive basis mismatch story,
- memorable unclonability intuition,
- easy to connect to Wiesner/BB84 explanations.

Weaknesses:
- can oversimplify multi-slot note behavior,
- can mislead viewers into thinking a single optical setup equals a real money protocol.

## 4.2 As an explanation of the current QMoney baseline
**Score: 8/10**

Strong fit if it is clearly labeled as:
- private-key,
- quorum-verified,
- verify-and-remint,
- and educational rather than production-hardware-ready.

## 4.3 As a physical prototype of QMoney itself
**Score: 4/10**

Weak unless qualified very carefully.

Why:
- a toy optical path is not yet an `n`-slot note architecture,
- real systems need source quality, alignment, calibration, detector assumptions, loss handling, and repetition control,
- the repo currently models the baseline as a **classical simulator** of BB84-style behavior rather than a working optical implementation.

## 4.4 As evidence for future public-key QMoney
**Score: 1/10**

A polarizer demo strongly supports **Wiesner/private-key intuition**.
It does not meaningfully validate hidden-subspace or other true public-key note-family ideas.

---

## 5. Biggest conceptual risk: overclaiming

The main risk is saying something stronger than the demo actually shows.

### Bad framing
- “This proves QMoney works physically.”
- “This is a prototype of public-key quantum money.”
- “This shows a deployable payment architecture.”
- “This demonstrates a trustless public verifier.”

### Good framing
- “This is a physical intuition demo for the current private-key note family.”
- “This illustrates hidden-basis verification and measurement disturbance.”
- “This helps explain why verification is consumptive and why remint is needed.”
- “This is not yet the public-key track.”

---

## 6. How to present the demo honestly

The recommended one-paragraph positioning is:

> QMoney's polarizer demo should be presented as a physical intuition model for the current private-key BB84-style note family. It explains hidden basis choices, disturbance under wrong-basis probing, and why verification consumes the original state and requires remint. It does not by itself establish a deployable hardware implementation or true public-key quantum money.

Recommended short label for slides or booth signage:

> **Private-key QMoney intuition demo — not yet a full hardware or public-key implementation**

---

## 7. Best next-step ladder

If the project wants to evolve the demo into something more rigorous, the next steps should be staged.

### Stage 1: Pedagogical optics demo
Show:
- H/V versus D/A basis behavior,
- disturbance from wrong-basis measurement,
- why basis choice matters.

### Stage 2: Many-slot note demo
Represent a note as many independent polarization slots.
Show:
- hidden recipe per slot,
- threshold acceptance,
- mismatch counting,
- counterfeit degradation as note size increases.

### Stage 3: Verify-and-remint protocol demo
Tie the physical intuition to system behavior:
- present note,
- consume note in verification,
- invalidate old serial,
- mint fresh replacement note.

This is where the demo begins to feel architecturally QMoney-like rather than just optics-like.

### Stage 4: Attack-model demo
Add explicit demonstrations of:
- guessed-basis counterfeit attempts,
- one-note-to-two-notes attack intuition,
- leakage versus note-size tradeoffs.

This would connect the physical story to the repo's counterfeit-analysis language much more strongly.

---

## 8. Relation to the note-family evaluation checklist

Using the repo's checklist, the polarizer demo scores as follows:

### Classification
- **Private-key**: yes
- **Public-key**: no
- **Publicly accessible verifier service**: potentially, but only if hidden verification remains behind a service/quorum

### Verifier model
- Consumptive verification: yes
- Same note repeatedly verified: no, not as the core model
- Verifier learns from interaction: yes, so leakage questions remain important

### Coherence sensitivity
- Good first intuition for basis disturbance
- Still not enough by itself to prove that the verifier distinguishes a genuine coherent state from a merely classically sampled substitute in a stronger note family

### Counterfeiting model
- Helpful for explaining simple counterfeit pressure
- Not a substitute for attack analysis or formal security work

### Public-key claims
- Should make none beyond educational inspiration

### Practicality and noise
- Real hardware issues would dominate quickly:
  - alignment,
  - source fidelity,
  - detector noise,
  - optical loss,
  - calibration drift,
  - throughput constraints.

---

## 9. Bottom line

The polarizer demo is worth doing **if the message is disciplined**.

It is a:
- **strong educational demo**,
- **strong narrative bridge for the current private-key baseline**,
- **weak hardware claim**,
- and **near-zero evidence for public-key QMoney**.

That is not a problem. It is only a problem if the project markets the demo as more than it is.

The right use is:
- teach the private-key intuition,
- make verify-and-remint feel tangible,
- and clearly separate this demo from future public-key research claims.
