# Wiesner Counterfeiting Attacks and QMoney

This note evaluates **Molina, Vidick, and Watrous (2012)** — [*Optimal counterfeiting attacks and generalizations for Wiesner's quantum money*](https://arxiv.org/abs/1202.4010) — against QMoney's current architecture and future research direction.

## Why this paper matters

This paper is not primarily about public-key hidden-subspace money. It is about **Wiesner-style private-key quantum money** and the best known success probabilities for a counterfeiter who tries to turn **one valid note into two notes that both pass verification**.

That makes it highly relevant to QMoney's **current baseline**, which is still explicitly:
- private-key at the quantum layer,
- Wiesner-like / BB84-like in note-family structure,
- quorum-verified rather than publicly self-verifiable,
- and built around verify-and-remint semantics.

## Main result relevant to QMoney

For Wiesner's original `n`-qubit scheme, the paper proves that the optimal probability of producing **two valid notes from one valid note** is exactly:

```text
(3/4)^n
```

This is important because it replaces a vague no-cloning intuition with a **tight quantitative counterfeit bound** for a specific attack model.

The paper also shows:
- a classical-verification analogue with exact success rate `((3/4) + (sqrt(2)/8))^n`,
- a 4-state single-qubit repetition scheme with simple-counterfeiting success `(2/3)^n`,
- and broader dimensional lower bounds for generalized note families.

## The attack model QMoney should explicitly name

The paper studies a **simple counterfeiting attack**:

- input: **one valid note**
- goal: produce **two candidate notes**
- success condition: **both notes verify independently**

For QMoney, this attack model should be treated as a named baseline question:

> If an attacker gets one valid QMoney note, what is the best probability that they can transform it into two notes or note-presentations that are both accepted by the verifier model?

This is narrower than the full QMoney threat surface, but it is still foundational.

## Why the paper fits QMoney well

### 1. It strengthens the current private-key framing
QMoney's present note family is still in the Wiesner/private-key lineage. This paper therefore supports the repo's current claim that the baseline should be evaluated as **private-key quantum cash**, not as a prematurely claimed public-key system.

### 2. It gives QMoney a better evaluation language
Instead of only saying that no-cloning should make counterfeiting hard, QMoney can ask for concrete statements like:
- forge-two-from-one success as a function of note size,
- best independent/simple counterfeit success,
- how modified alphabets or verifier styles change that bound,
- whether repeated product-state structure leaves the scheme closer to Wiesner-style limits than to richer note-family behavior.

### 3. It aligns with QMoney's architecture split
The paper is about the security of a **private-key note family**. QMoney's architecture already separates:
- the quantum anti-counterfeiting layer,
- from the classical settlement / ownership layer.

This means the paper is most relevant to the **note-level counterfeit model**, not to ledger semantics by themselves.

## Where the paper does not solve QMoney's problem

This paper does **not** provide:
- a public-key verifier,
- a hidden-subspace construction,
- a secure public-verification path,
- or a replacement for the `pubkey_hidden_subspace/` research track.

So it should not be used to imply that QMoney is closer to public-key money than it really is. It sharpens the theory of the **current private-key baseline** rather than moving the project into the public-key regime.

## What QMoney should take from it

### A. Add the attack model to repo language
The repo should explicitly talk about the **one-note-to-two-notes counterfeiting problem** as a baseline security question for the private-key simulator family.

### B. Treat it as one attack class among several
QMoney still needs broader analysis beyond this paper's model, including:
- adaptive verification attacks,
- repeated-query leakage,
- remint-side channels,
- malicious claimant interaction,
- and partially compromised quorum members.

So the simple counterfeit model should be documented as a **baseline attack model**, not as the whole security story.

### C. Use it to benchmark the current simulator family
Even if QMoney does not yet implement a formal counterfeit optimizer, the paper suggests a disciplined research direction:
- define counterfeit success experiments explicitly,
- compare empirical attacks against Wiesner-like expectations,
- and keep note-family claims honest when moving beyond product-state constructions.

## Bottom line for QMoney

This paper is a strong match for **Track A** of QMoney:
- distributed private-key quantum cash,
- verifier-held hidden information,
- note-level counterfeit analysis.

It is only indirectly relevant to **Track B**:
- true public-key note families,
- hidden-subspace/oracle constructions,
- and future public verification.

In short:

> `1202.4010` gives QMoney a sharper theoretical lens for analyzing its current Wiesner-like baseline, but it does not solve the transition from private-key quantum cash to public-key quantum money.

## Citation

- Abel Molina, Thomas Vidick, John Watrous, *Optimal counterfeiting attacks and generalizations for Wiesner's quantum money*, arXiv:1202.4010, 2012. https://arxiv.org/abs/1202.4010
