# QMoney Note-Family Evaluation Checklist

Use this checklist before adding or promoting any QMoney note-family track.

## Classification

- Is the scheme private-key, public-key, or only publicly accessible through a verifier service?
- What hidden information remains?
- Who holds that hidden information?
- Does classical public-key ownership play any role in quantum verification, or only in settlement?

## Verifier model

- What exactly does the verifier test?
- Is verification consumptive or non-consumptive?
- Can the same note be verified repeatedly, or does circulation require verify-and-remint?
- What does the verifier learn from each accept/reject decision?
- Can repeated verifier interaction leak enough information to reconstruct valid notes?

## Coherence sensitivity

- Does verification distinguish a coherent quantum state from a classically sampled substitute?
- Can a basis state, collapsed mixture, or partially dephased state pass?
- Is the Hadamard/dual-space or equivalent coherence check explicit?

## Counterfeiting model

- What is the one-note-to-two-notes counterfeit success question?
- What multi-copy or copy-complexity attack model is in scope?
- Are adaptive verification attacks in scope?
- Are malicious claimant, malicious recipient, and partial quorum compromise scenarios in scope?

## Minting and serials

- Can the mint issue duplicate quantum states under the same serial?
- Are serials tied unambiguously to note-family state?
- Does reminting atomically spend the old serial and create a fresh note?

## Public-key claims

- Can anyone verify using only public information?
- Does public verification reveal enough structure to mint valid notes?
- If the construction uses oracles, are oracle publication and query rules explicit?
- Is any obfuscation, computational assumption, or trusted setup clearly named?

## Practicality and noise

- What qubit count and state representation are required?
- What noise model is assumed?
- What mismatch tolerance is accepted?
- What are the expected false-accept and false-reject behaviors?

## Repo integration

- Does private-key work stay under the private-key baseline namespace?
- Does public-key research stay under a separate public-key namespace?
- Are runtime code, tests, TLA+, Z3, and docs synchronized when protocol behavior changes?
