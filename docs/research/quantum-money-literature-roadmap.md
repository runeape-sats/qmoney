# QMoney Quantum Money Literature Roadmap

This roadmap ranks current literature directions by how useful they are for QMoney **right now**.

## Read next

### 1. Noise-tolerant public-key money from a classical oracle
- **Peter Yuen (2024 / Quantum 2025)**
- `arXiv:2407.06463`

Why:
- unusually close to QMoney's public-key/oracle workflow,
- explicitly addresses noise tolerance,
- bridges abstract public-key theory with more realistic verifier conditions.

### 2. Quantum Money from Abelian Group Actions
- **Mark Zhandry (2023 / journal 2025)**
- `arXiv:2307.12120`

Why:
- one of the strongest modern public-key directions,
- structurally different from BB84/Wiesner notes,
- important for any serious Track B roadmap.

### 3. Cryptanalysis of Three Quantum Money Schemes
- **Bilyk, Doliskani, Gong (2022)**
- `arXiv:2205.10488`

Why:
- reminds QMoney that public-key elegance is not enough,
- directly relevant to how prototype claims should be bounded,
- useful as an honesty check for hidden-subspace-style work.

### 4. Anonymous Public-Key Quantum Money and Quantum Voting
- **Çakan, Goyal, Yamakawa (2024)**
- `arXiv:2411.04482`

Why:
- extends the conversation from counterfeit-resistance to privacy and holder anonymity,
- relevant if QMoney ever tries to combine quantum notes with Bitcoin-like public circulation.

### 5. Public-Key Quantum Money and Fast Real Transforms
- **Doliskani, Mirzaei, Mousavi (2025)**
- `arXiv:2503.18890`

Why:
- evidence that the public-key frontier is still experimenting with transform choices,
- useful for note-family comparison, even if not the first prototype target.

---

## Prototype next

These are not immediate production candidates, but they are the best directions for deeper QMoney experimentation.

### A. Noise-tolerant oracle models
Best near-term fit for QMoney's existing formal/oracle workflow.

### B. Group-action / representation-based note families
Best candidate family for a truly separate public-key note track.

### C. Copy-complexity and multi-copy attack modeling
Important for strengthening the current private-key baseline and for preventing overly narrow counterfeit models.

---

## Monitor only

These are worth watching, but should not outrank the items above.

### Practical quantum token engineering
- e.g. `arXiv:2602.10621`

Why monitor:
- valuable for eventual implementation realism,
- but too early to drive core cryptographic architecture.

### Anonymity / voting extensions
Why monitor:
- important for future systems design,
- but secondary until the base note-family direction is stronger.

### Transform-family variants
Why monitor:
- useful comparison points,
- but not a reason to reorient QMoney by themselves.

---

## Avoid / treat skeptically

### Withdrawn or broken public-key schemes
Example:
- **Khesin, Lu, Shor (2022)**, `arXiv:2207.13135` — withdrawn

Lesson:
- public-key quantum money proposals can fail in subtle ways,
- so QMoney should treat cryptanalysis as part of the mainline literature, not an afterthought.

### Rebranding the private-key baseline as public-key
Avoid:
- suggesting the current BB84/quorum model is “close enough” to public-key money,
- collapsing the difference between public ownership tracking and public quantum verification.

### Ignoring noise or leakage
Avoid:
- public-key prototypes that rely on unrealistically clean verification,
- security narratives that omit repeated-query leakage or verifier-side attack surfaces.

---

## What to do in the repo

## For Track A — private-key baseline
Prioritize:
- adaptive verification attacks,
- verifier leakage,
- one-note-to-two-notes counterfeit modeling,
- remint-side-channel analysis,
- multi-copy / copy-complexity framing.

## For Track B — public-key research
Prioritize:
- oracle/noise-tolerant note-family comparisons,
- group-action references and conceptual mapping,
- explicit “prototype only” documentation for any hidden-subspace or public-key experiments,
- cryptanalysis notes alongside constructions.

---

## Short version

If time is limited, QMoney should do this in order:

1. read **Yuen 2024/2025**
2. read **Zhandry 2023/2025**
3. read **cryptanalysis of public-key schemes**
4. only then deepen implementation experiments

That ordering keeps the project anchored in realistic public-key research rather than in optimism alone.
