# Latest Quantum Money Literature and QMoney

This note surveys the most relevant **recent quantum money research** for QMoney, prioritizing the authors and research lines already referenced in the repo:

- Stephen Wiesner
- Peter Shor
- Scott Aaronson / Paul Christiano
- and the nearest modern continuations of those lines, especially Mark Zhandry and newer public-key / oracle / unclonable-cryptography work

The goal is not to list every paper with the words *quantum money*, but to identify which recent directions actually matter for QMoney's architecture and research roadmap.

## Executive summary

The latest serious momentum in the field is **not** a direct continuation of the BB84/Wiesner-style private-key line. Instead, current activity is concentrated in:

1. **new public-key constructions** based on richer algebraic structure,
2. **noise-tolerant verification models** that move closer to realistic hardware,
3. **cryptanalysis** of candidate public-key schemes,
4. and a broader **unclonable-cryptography framework** where quantum money is only one primitive among many.

For QMoney, the core conclusion is:

> The current private-key / quorum / verify-and-remint baseline still looks like the right honest present-day position, while the public-key frontier remains active but fragile, cryptanalysis-heavy, and structurally quite different from the repo's BB84-style baseline.

---

## 1. Wiesner: still the conceptual anchor

The field still treats Wiesner as the origin of the discipline:
- private-key verification,
- hidden note information,
- no-cloning as the anti-counterfeiting primitive,
- banknote-style quantum states that are physically hard to copy.

A recent practical-facing signal is:
- **Kukharchyk et al. (2026), _Practical quantum tokens: challenges and perspectives_**, `arXiv:2602.10621`

This is not a new public-key breakthrough. It is more of a systems-and-engineering reality check: the community is increasingly asking what token-like quantum cryptography would look like under actual hardware constraints.

### QMoney relevance
- reinforces keeping Wiesner as the historical baseline,
- supports the repo's continued emphasis on honest private-key framing,
- and suggests that practical token engineering is still far behind elegant theory.

---

## 2. Peter Shor: important historically, cautionary in recent public-key directions

Peter Shor remains central to QMoney's framing because his perspective helps motivate why quantum-era money and settlement systems matter at all.

The most relevant recent Shor-linked public-key item found here is:
- **Khesin, Lu, Shor (2022), _Publicly verifiable quantum money from random lattices_**, `arXiv:2207.13135`

However, this paper is now explicitly marked on arXiv as **withdrawn** because a central calculation was incorrect, with an accompanying warning that schemes of similar form may fail more generally.

Older Shor-linked work remains historically important:
- _Breaking and making quantum money_ (2009)
- _Quantum money from knots_ (2010)

### QMoney relevance
The main lesson is not “Shor gives QMoney a clean public-key route.” The lesson is almost the opposite:

- candidate public-key constructions can look promising and still break,
- elegant public-verification ideas are brittle,
- and QMoney should remain conservative about public-key claims.

---

## 3. Aaronson / Christiano: still the canonical conceptual dividing line

The foundational public-key reference remains:
- **Aaronson, Christiano (2012), _Quantum Money from Hidden Subspaces_**, `arXiv:1203.4740`

This remains the canonical paper for explaining why public-key quantum money is a fundamentally different note-family/verifier problem from Wiesner-style private-key money.

But the recent literature also shows that hidden-subspace-style thinking should be treated as:
- conceptually decisive,
- historically foundational,
- and still useful as a prototype template,
- but **not automatically secure merely because it is elegant**.

A major follow-up here is:
- **Bilyk, Doliskani, Gong (2022), _Cryptanalysis of Three Quantum Money Schemes_**, `arXiv:2205.10488`

That cryptanalysis specifically reinforces the broader lesson that older public-key candidates need to be treated as attack surfaces, not finished blueprints.

### QMoney relevance
For QMoney, Aaronson/Christiano still matters in three ways:

1. it justifies keeping the public-key track **separate** from the private-key baseline,
2. it motivates the repo's `pubkey_hidden_subspace/` namespace as a research area rather than a production claim,
3. and it warns against confusing conceptual prototype progress with cryptographic closure.

---

## 4. Zhandry and the group-action line: one of the strongest modern public-key directions

The most important modern continuation I found is:
- **Mark Zhandry (2023 / journal 2025), _Quantum Money from Abelian Group Actions_**, `arXiv:2307.12120`

This is a major shift away from BB84-style product states and toward algebraic public-key structure. It is one of the clearest modern candidates for a real public-key quantum money / quantum lightning direction.

Related follow-on work includes:
- **Mutreja, Zhandry (2024), _Quantum State Group Actions_**, `arXiv:2410.08547`
- **Bostanci, Nehoran, Zhandry (2024), _A General Quantum Duality for Representations of Groups with Applications to Quantum Money, Lightning, and Fire_**, `arXiv:2411.00529`

### QMoney relevance
If QMoney wants a serious public-key research track, this group-action family is more promising than trying to stretch the current BB84/quorum baseline into something it is not.

This does **not** mean QMoney should pivot immediately into implementation. It means that the repo's future note-family comparison work should treat group-action constructions as first-class reference points.

---

## 5. Noise-tolerant public-key money: especially relevant to QMoney's oracle/formal workflow

A particularly relevant recent paper is:
- **Peter Yuen (2024 / Quantum 2025), _Noise-tolerant public-key quantum money from a classical oracle_**, `arXiv:2407.06463`

This matters because it addresses something older public-key literature often idealized away:
- **noise tolerance**
- and explicitly **classical-oracle-mediated** public verification structure.

### QMoney relevance
This paper is unusually relevant to QMoney's current formal-research direction because:
- the repo already has a public-key/oracle workflow,
- the repo already distinguishes runtime math from oracle/lifecycle/formal layers,
- and any realistic public-key future for QMoney will eventually need noise tolerance.

If the public-key track keeps evolving, this is one of the best papers to prioritize after the classical Aaronson-Christiano background.

---

## 6. Anonymous public-key money: beyond bare counterfeiting

Another major newer direction is:
- **Çakan, Goyal, Yamakawa (2024), _Anonymous Public-Key Quantum Money and Quantum Voting_**, `arXiv:2411.04482`

This expands the design question from simple public verification toward:
- holder privacy,
- anonymity,
- and composability with higher-level systems such as voting.

### QMoney relevance
For QMoney this matters mostly at the systems layer:
- if the project ever wants to connect quantum notes with Bitcoin-like circulation and ownership semantics,
- then public verifiability alone is not enough,
- and anonymity/privacy properties may become first-class design criteria.

---

## 7. New construction variants and transform choices

A recent example here is:
- **Doliskani, Mirzaei, Mousavi (2025), _Public-Key Quantum Money and Fast Real Transforms_**, `arXiv:2503.18890`

The key idea is that the field is still actively experimenting with **which transform family** should underwrite public verification, including choices that keep amplitudes real rather than complex.

### QMoney relevance
This is less immediately actionable than the group-action or noise-tolerant oracle lines, but it is strong evidence that the public-key frontier remains highly exploratory. QMoney should track this as part of a note-family comparison discipline rather than prematurely settling on one public-key template.

---

## 8. The field is broadening into unclonable cryptography

Several recent papers are not just “quantum money papers,” but they matter because they generalize the entire area:

- **Ananth, Behera (2023), _A Modular Approach to Unclonable Cryptography_**, `arXiv:2311.11890`
- **Ananth, Kaleoglu, Liu (2023), _Cloning Games: A General Framework for Unclonable Primitives_**, `arXiv:2302.01874`
- **Çakan, Goyal, Kitagawa, Nishimaki, Yamakawa (2025), _Multi-Copy Security in Unclonable Cryptography_**, `arXiv:2510.12626`
- **Ananth, Goldin (2025), _Less is More: On Copy Complexity in Quantum Cryptography_**, `arXiv:2510.04992`

### QMoney relevance
This meta-cryptographic shift matters because it says the next generation of questions is not just:
- “can notes be cloned?”

but also:
- how many copies matter,
- what adversarial copy access is allowed,
- how to modularize unclonable primitives,
- which assumptions are actually minimal.

This strongly supports QMoney evolving from a single counterfeit narrative into a **family of attack models** and **copy-complexity-sensitive security questions**.

---

## 9. Recommended prioritization for QMoney

## Read next
These are the most useful next reading targets for the repo:

1. **Yuen (2024/2025)** — _Noise-tolerant public-key quantum money from a classical oracle_ (`2407.06463`)
2. **Zhandry (2023/2025)** — _Quantum Money from Abelian Group Actions_ (`2307.12120`)
3. **Bilyk, Doliskani, Gong (2022)** — _Cryptanalysis of Three Quantum Money Schemes_ (`2205.10488`)
4. **Çakan, Goyal, Yamakawa (2024)** — _Anonymous Public-Key Quantum Money and Quantum Voting_ (`2411.04482`)
5. **Doliskani, Mirzaei, Mousavi (2025)** — _Public-Key Quantum Money and Fast Real Transforms_ (`2503.18890`)

## Prototype next
If QMoney wants to deepen Track B, the most promising prototype inspirations are:

1. **noise-tolerant oracle models**
2. **group-action / representation-based constructions**
3. **explicit copy-complexity / multi-copy threat modeling**

## Monitor only
Worth tracking, but not immediate implementation targets:

- practical quantum token engineering papers
- anonymity/voting extensions until the base note family is stronger
- transform-family variants unless QMoney adopts a stronger public-key backbone first

## Avoid / treat skeptically
- withdrawn or already-broken public-key candidates
- any attempt to relabel the BB84/quorum baseline as “basically public-key”
- any construction that ignores noise, leakage, or cryptanalysis pressure

---

## Bottom line for QMoney

The modern literature supports a very specific position:

> QMoney's current private-key / quorum / verify-and-remint baseline remains the right honest architecture for the repo today. The public-key frontier is active and exciting, but it has moved into group actions, oracle/noise-tolerant verification, anonymity extensions, and unclonable-cryptography frameworks that are structurally different from the current BB84-style baseline.

That means QMoney should keep doing two things at once:
- continue strengthening the current private-key baseline and its attack models,
- while treating public-key quantum money as a genuinely separate note-family research program.

## Selected references

- Peter Yuen, *Noise-tolerant public-key quantum money from a classical oracle*, `arXiv:2407.06463`
- Mark Zhandry, *Quantum Money from Abelian Group Actions*, `arXiv:2307.12120`
- Alper Çakan, Vipul Goyal, Takashi Yamakawa, *Anonymous Public-Key Quantum Money and Quantum Voting*, `arXiv:2411.04482`
- Jake Doliskani, Morteza Mirzaei, Ali Mousavi, *Public-Key Quantum Money and Fast Real Transforms*, `arXiv:2503.18890`
- Andriyan Bilyk, Javad Doliskani, Zhiyong Gong, *Cryptanalysis of Three Quantum Money Schemes*, `arXiv:2205.10488`
- Scott Aaronson, Paul Christiano, *Quantum Money from Hidden Subspaces*, `arXiv:1203.4740`
- Peter W. Shor et al., *Publicly verifiable quantum money from random lattices*, `arXiv:2207.13135` (withdrawn)
