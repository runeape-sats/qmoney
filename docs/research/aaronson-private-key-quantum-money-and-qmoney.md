# Aaronson on Private-Key Quantum Money and Implications for QMoney

Primary materials used for this note:
- Local Whisper transcript of Scott Aaronson’s QCrypt 2013 talk, `Private-key quantum money`
- Scott Aaronson and Paul Christiano, *Quantum Money from Hidden Subspaces*
  - `https://www.scottaaronson.com/papers/moneyfull.pdf`
- Scott Aaronson, *Two announcements* / talk abstract on *Shtetl-Optimized*
  - `https://scottaaronson.blog/?p=1064`

This note rewrites the earlier Aaronson summary using the actual talk transcript plus the related papers. The goal is not just to summarize Aaronson’s results, but to extract what they imply for how QMoney should be described and developed.

---

## Executive summary

Aaronson’s private-key quantum money talk matters for QMoney because it reframes the current repo direction as a **serious cryptographic target in its own right**, not merely as an incomplete attempt at public-key money.

The three most important takeaways are:

### 1. Private-key quantum money has real unresolved structure
Aaronson’s talk is not a retreat from public-key quantum money. It is an argument that the private-key setting still contains deep problems:
- rigorous security proofs for Wiesner / BBBW-style schemes,
- the giant-database vs computational-assumption tradeoff,
- and security against **adaptive interactive attacks**.

### 2. Interactive security is central
The most QMoney-relevant part of the talk is Aaronson’s discussion of how Wiesner and BBBW-style schemes fail if the adversary can repeatedly query the bank while modifying candidate bills. He then explains how the hidden-subspace framework can be repurposed to get a **private-key** scheme secure even against those attacks.

### 3. QMoney should explicitly identify itself with the private-key quantum cash tradition
Current QMoney belongs much more naturally in the lineage:
- Wiesner,
- BBBW-style compact-secret variants,
- Aaronson/Christiano-style private-key hardening,
- distributed/quorum verification,

than in the lineage of true public-key quantum money.

So the best description remains:

> QMoney currently implements a quorum-verified, private-key quantum cash design with verify-and-remint, plus a classical public-key ownership and settlement layer.

---

## 1. What Aaronson argues in the talk

## 1.1 Classical cash is copyable; quantum cash becomes plausible because of no-cloning
Aaronson begins by contrasting ordinary cash with quantum information.

- `00:01:48–00:02:15` — as classical information, a bill is just a string, and copying a string is easy.
- `00:03:31–00:03:40` — the escape hatch is the no-cloning theorem.

This is standard background, but it matters because Aaronson frames quantum money as an answer to a problem that looks fundamentally impossible classically: **offline, physically unclonable cash without needing a trusted intermediary on every transaction**.

For QMoney, this reinforces the high-level motivation: the quantum part is meant to solve a different problem from classical signatures or ledgers.

---

## 1.2 Wiesner’s scheme is conceptually brilliant but operationally awkward
Aaronson gives a clean description of Wiesner’s original scheme:
- `00:04:13–00:05:18` — each bill has a serial number plus BB84 qubits;
- the bank stores the preparation data in a giant secret database;
- verification means measuring each qubit in the secret basis.

He then highlights three issues that drive the rest of the talk:

### A. Engineering fragility
- `00:05:56–00:06:41` — long-term coherent qubits are still an engineering fantasy for actual wallet-like money.

### B. Verification need not destroy valid money
- `00:06:57–00:07:53` — by the gentle measurement / “almost as good as new” lemma, a valid note can survive verification approximately if acceptance was already highly predictable.

### C. The giant-database problem
- `00:08:04–00:08:33` — it is cumbersome for the bank to store preparation info for every bill in circulation.

Why this matters for QMoney:
- it shows that **destructive verification is not the only possible model**, but also that engineering and verifier-state management are central design axes.
- it gives a clean language for distinguishing note-level verification physics from system-level architecture.

---

## 1.3 BBBW is best understood as a compact-secret variant of Wiesner
Aaronson explains BBBW as replacing the giant random database with a pseudorandom function key:
- `00:08:38–00:09:18` — keep only a single secret key `k` and derive bill preparation from `f_k(s)`.

He then gives a useful conceptual reinterpretation:
- `00:10:53–00:11:18` — Wiesner can be viewed as the BBBW idea instantiated with a **random oracle**.

This is a very helpful conceptual move for QMoney, because it shows that:
- giant-secret and compact-secret private-key money are not unrelated species;
- they are points in a common design space.

That suggests QMoney should explicitly track where it sits on this axis:
- replicated verifier secret,
- threshold-shared secret,
- per-note state description,
- compact seed-derived note description,
- or some hybrid.

---

## 1.4 Public-key money is a different target and requires computational assumptions
Aaronson revisits public-key quantum money only to pivot away from it:
- `00:11:42–00:12:05` — public-key quantum money means the verification procedure is public.
- `00:12:06–00:12:17` — if it is possible at all, it must require a computational assumption beyond no-cloning.

He gives the core reason:
- `00:12:29–00:12:38` — if the verification procedure is public, then an unbounded adversary can brute-force search over states until one passes.

This aligns with the architecture split already emerging in QMoney docs:
- private-key note verification is one category;
- public-key quantum money is a different, harder category;
- classical public-key settlement does not erase that distinction.

---

## 1.5 The talk’s real goal: use public-key insights to solve private-key problems
Aaronson states the goal explicitly:
- `00:14:54–00:15:04` — leverage understanding from public-key quantum money to solve remaining open problems about private-key quantum money.

That is a subtle but important point. The talk is not saying “private-key money is obsolete now that we have public-key ideas.” It says the opposite:

> public-key work gave tools that can now be pushed back into the private-key setting.

For QMoney, this is a strong endorsement of keeping the private-key track active and intellectually ambitious.

---

## 2. The three private-key problems Aaronson focuses on

## 2.1 Rigorous security proof for Wiesner / BBBW-style schemes
Aaronson says he was surprised that no rigorous security proof had really been written down for Wiesner / BBBW:
- `00:15:24–00:15:45` — one of the talk’s results is a unified proof of security for these schemes.

He then uses the mini-scheme → full-scheme construction:
- `00:24:31–00:26:34` — define a mini-scheme, add serial numbers plus a random/pseudorandom function, and prove the full scheme is secure unless either:
  1. the underlying mini-scheme was insecure, or
  2. the pseudorandom function was distinguishable from random.

Why it matters for QMoney:
- this is a strong reminder that “the idea seems right” is not enough;
- the bridge from note-level mini-scheme to full circulating money system needs an explicit theorem/story;
- QMoney should likely adopt the language of **mini-scheme vs full scheme** in future docs.

---

## 2.2 Giant-database vs computational-assumption tradeoff
Aaronson asks whether the following tradeoff is inherent:
- `00:15:54–00:16:19` — Wiesner is unconditionally secure but needs a giant database;
- BBBW avoids the giant database but needs a computational assumption.

He then states a tradeoff theorem:
- `00:18:24–00:18:45` — if the bank only has a small key, the scheme must depend on a computational assumption.
- `00:28:06–00:29:05` — more formally, any money scheme with an `n`-bit secret key can be broken using polynomially many legitimate bills, linearly many bank queries, and **exponential computation time**.

That means compact-secret private-key money is not information-theoretically secure against unbounded adversaries. If it works, it works for computational reasons.

Why it matters for QMoney:
- if QMoney moves toward compact per-system secrets or seed-derived note families, it should treat that as a computationally secure design, not an information-theoretic one;
- docs should distinguish “large replicated note descriptions” from “compact secret / PRF-like derivation” as a real security tradeoff, not just an implementation convenience.

---

## 2.3 Adaptive interactive attacks are devastating for naive private-key money
This is the most immediately relevant part of the talk for QMoney.

Aaronson explains the adaptive attack on Wiesner / BBBW:
- `00:16:30–00:17:43` — repeatedly submit a legitimate bill while varying one qubit at a time;
- use bank accept/reject behavior to learn the correct state qubit-by-qubit;
- in near-linear time, recover the note’s state.

This is a simple but devastating observation:
- a private-key verifier can become an oracle that helps reverse-engineer valid notes.

For QMoney, this is extremely important because current designs also involve secret-holding verifiers/quorums. The question is no longer just:
- “Can the adversary clone the note directly?”

It is also:
- “Can the adversary learn the hidden note structure by interacting with verification over time?”

That should become a first-class security category in QMoney.

---

## 3. Aaronson’s private-key response to the interactive-attack problem

## 3.1 Hidden-subspace ideas can be repurposed for private-key security
Aaronson says:
- `00:19:22–00:19:39` — the earlier hidden-subspace public-key scheme immediately yields a private-key scheme provably secure even against interactive attacks.

He later explains the key observation:
- `00:44:00–00:44:18` — if the hidden-subspace scheme is already secure as a public-key mini-scheme, then viewed as a private-key mini-scheme it is also secure against interactive attacks;
- otherwise an interactive private-key attacker could be converted into a public-key attacker by simulating bank verification using the public hidden-subspace oracles.

This is the cleanest transcript-backed bridge between the public-key and private-key worlds.

For QMoney, the lesson is:
- if a note family is strong enough to survive public exposure of the verifier structure, then it is often automatically strong against private-key verifier interaction;
- conversely, if the note family fundamentally relies on hidden BB84-style preparation data, verifier interaction becomes a much more dangerous attack surface.

---

## 3.2 Highly entangled bills may be necessary for interactive security under projective verification
Aaronson highlights a limitation based on Farhi–Shor et al.:
- `00:40:21–00:40:48` — if verification is projective and you want interactive security, then the bill cannot just be a bunch of unentangled Wiesner-style qubits.
- `00:40:46–00:40:51` — at least in that regime, the bill must be a **highly entangled state**.

This matters for QMoney because it warns against a tempting but naive hope:
- keep simple product-state notes,
- keep strong interactive security,
- keep simple projective verification,
- and somehow get all of this at once.

Aaronson’s argument suggests those desiderata are in tension.

---

## 3.3 The hidden-subspace verifier structure
Aaronson gives a concise description of the hidden-subspace state:
- `00:41:13–00:41:38` — the note is a superposition over all elements of a random subspace `A ⊆ GF(2)^n`.
- `00:41:46–00:42:25` — verification works using membership tests for both `A` and `A^⊥`.
- `00:42:25–00:42:38` — in the public-key setting, multivariate polynomials instantiate these membership oracles without revealing `A` directly.

The paper adds the canonical statement:
- public-key money from hidden subspaces,
- black-box security relative to a classical oracle,
- and private-key schemes with unlimited verifications secure even under adaptive bank interaction.

This is important for QMoney not because it should immediately adopt hidden subspaces, but because it shows what a more robust note family looks like:
- highly structured,
- verification-aware from the beginning,
- and not reducible to “secret basis strings on independent qubits.”

---

## 4. What the transcript + papers imply for QMoney

## 4.1 QMoney should explicitly claim membership in the private-key lineage
Aaronson’s talk gives strong support for describing QMoney as part of the private-key quantum money / quantum cash tradition.

That is not a consolation prize. In the talk, private-key money is a domain with:
- theorem-worthy security definitions,
- nontrivial composition results,
- tradeoff theorems,
- and open questions around interaction, entanglement, and verification structure.

So the repo should not speak as though “private-key” means “preliminary.”

It should instead say, confidently:

> QMoney’s current note family lies in the private-key quantum cash tradition: hidden note-verification information is held by a verifier quorum, while ownership and settlement are handled by a classical public-key layer.

---

## 4.2 QMoney’s quorum is best viewed as a distributed bank/verifier
Aaronson’s language is bank-centric because the verifier holds secret information.

QMoney’s architecture is naturally interpreted as a distributed version of that:
- the quorum collectively plays the role of the bank;
- hidden verification information may be replicated or secret-shared across quorum members;
- a classical attestation layer exposes only the accept/reject result plus ownership transition.

This framing is better than calling current QMoney “public verification,” because it makes the trust and secrecy model explicit.

---

## 4.3 Adaptive-query security should become a named QMoney workstream
From the transcript, the single most concrete attack class to port into QMoney is the adaptive verifier-query attack.

For QMoney that translates into research/test questions like:
- can repeated submission of near-valid notes reveal hidden basis data?
- can repeated remint attempts leak serial-linked structure?
- can malicious recipients manipulate verification rounds to infer quorum-held secrets?
- can partially compromised quorum members accumulate enough view data over many verifications to reconstruct mintable note descriptions?
- can one-bit accept/reject leakage over many trials become enough to learn the note family?

This should become an explicit section in future docs, something like:
- **adaptive verification attacks**
- **verifier leakage attacks**
- **remint-side-channel attacks**

---

## 4.4 QMoney should distinguish note-level reuse from system-level circulation
Aaronson emphasizes that valid notes can survive verification approximately because of the gentle measurement lemma, but also studies schemes that remain secure under repeated interactions.

QMoney currently uses verify-and-remint semantics, so the right integration is:
- do not claim non-destructive note-level reuse unless the note family truly supports it;
- instead ask whether the *system* supports indefinite circulation through safe reminting without leaking note structure.

So QMoney should distinguish:

### Note-level repeat verification
Can the same quantum note survive many direct verifications?

### System-level repeat circulation
Can value keep circulating indefinitely through verify-and-remint while preserving security under repeated adversarial interaction?

Aaronson’s talk shows those are separate questions.

---

## 4.5 Mini-scheme vs full-scheme should become part of QMoney’s architecture vocabulary
The transcript repeatedly uses the mini-scheme/full-scheme distinction:
- `00:21:40–00:22:20` — define a private-key mini-scheme;
- `00:24:31–00:26:34` — build a full scheme by adding serial numbers plus a random/pseudorandom function.

QMoney would benefit from using the same split:

### Note-family / mini-scheme layer
What is the quantum state family and its verifier relation?

### Currency-system / full-scheme layer
How are serials, ownership, remint, signatures, attestations, and ledger finality composed around that note family?

This would make it easier to compare very different note families while holding the classical circulation layer fixed.

---

## 5. Concrete integration recommendations

## 5.1 Documentation language
Future QMoney docs should explicitly connect current work to the Aaronson lineage.

Recommended wording:

> QMoney’s current architecture should be understood as distributed private-key quantum cash: the quantum note layer relies on hidden verification information held by a quorum, while the classical layer handles ownership, attestation, and settlement.

And where useful:

> In the Aaronson/Christiano framing, the key unresolved issue for this family is not only counterfeiting in the abstract, but security under adaptive interaction with the verifier.

---

## 5.2 Add a private-key robustness checklist
A dedicated private-key note-family checklist should ask:
- what secret note data exists?
- who holds it?
- can repeated verification queries reveal it?
- does accept/reject feedback leak per-qubit or per-substructure information?
- does verify-and-remint create additional leakage?
- can partial quorum compromise accumulate over time?
- is the note family product-state or highly entangled?
- does the security story depend on information-theoretic secrecy or computational hardness?

Aaronson’s talk makes almost every one of these questions unavoidable.

---

## 5.3 Split roadmap into private-key hardening vs public-key research
The transcript supports preserving two distinct streams:

### Private-key hardening
- adaptive verifier-query resistance
- leakage analysis
- compact-secret vs explicit-note-description tradeoffs
- entanglement requirements for interaction security
- repeated verify-and-remint security models

### Public-key research
- hidden-subspace prototypes
- oracle-backed public verifiers
- multivariate-polynomial instantiations
- later public-key constructions beyond hidden subspaces

Aaronson’s contribution is that the private-key track deserves equal seriousness, not just maintenance status.

---

## 5.4 Treat compact secret state as a security choice, not just an implementation choice
The giant-database vs computational-assumption theorem is particularly important for QMoney.

If the system moves toward:
- compact seeds,
- PRF-style note derivation,
- or otherwise small verifier secrets,

then that should be presented as a deliberate move into **computational** security territory.

That’s not bad. It just needs to be explicit.

---

## 6. How this complements the Shor note

The existing Shor note mainly helps QMoney avoid overclaiming about public-key money and highlights the need for coherence-sensitive verification.

The Aaronson note contributes something different:
- it legitimizes private-key money as a deep standalone research problem;
- it turns adaptive verification into a central attack surface;
- it introduces a useful vocabulary of mini-scheme vs full scheme, tradeoff theorems, and interaction security;
- and it suggests that the current quorum/private-key direction can be understood as part of a serious historical line of work rather than a halfway house toward “real” quantum money.

Taken together:
- **Shor** is the note that keeps QMoney honest about the public/private distinction.
- **Aaronson** is the note that explains why the private-key track is worth building seriously.

---

## Bottom line

The strongest transcript-backed lesson from Aaronson’s talk is:

> QMoney should not treat its present architecture as “almost public-key quantum money.” It should treat it as a serious distributed private-key quantum cash architecture, with the main open problems centered on verifier interaction, leakage, compact-secret tradeoffs, and system-level secure circulation.

That framing is better because it:
- matches the actual cryptographic structure of the current repo,
- aligns QMoney with the right literature lineage,
- and points directly to concrete next research questions that matter for this design family.
