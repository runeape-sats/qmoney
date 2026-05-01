# Polarizer Demo Script Variants

This file adapts the base polarizer exhibit script for three different audiences:
- founders / investors,
- researchers,
- museum / public exhibit visitors.

Use these variants when the same underlying demo needs different framing while staying honest about what QMoney currently is.

## Shared boundary

All three versions should preserve the same core truth:

> The polarizer demo is an intuition demo for QMoney's current **private-key** BB84-style path. It explains hidden basis choices, disturbance under wrong-basis probing, and why verification consumes the original note and requires remint. It is not yet a full hardware implementation or public-key quantum money.

---

## 1. Founder / investor pitch version

### 20-second opener

QMoney uses quantum anti-counterfeiting ideas to explore a new kind of money primitive. This polarizer demo makes the current private-key architecture tangible: hidden basis choices make naive copying fail, and verification consumes the note, so successful transfer works through verify-and-remint rather than by reusing the same object forever.

### 60-second founder version

What this demo shows is the intuition behind QMoney's current private-key quantum layer. Imagine a note made of many tiny polarization slots. Each slot is secretly prepared in one of four BB84-style states. A counterfeiter who does not know the hidden basis recipe cannot safely inspect and clone the whole note, because probing in the wrong basis disturbs the state.

That gives us an anti-counterfeiting primitive that behaves fundamentally differently from classical copying. The verifier side matters too: in the current architecture, a secret-holding verifier quorum knows how the note should be checked. Verification consumes the original note, so a successful transfer means retiring the old note and minting a fresh replacement note for the next holder.

The important business point is that this demo is **not** claiming full product readiness. It is making the architecture legible: private-key quantum note security on one side, and classical ownership / settlement logic on the other.

### Founder emphasis points
- New money primitive: unclonable note intuition rather than purely signature-based scarcity
- Clear current scope: private-key baseline, not overclaimed public-key quantum money
- Architectural differentiation: quantum anti-counterfeiting layer plus classical settlement layer
- Honest roadmap: simulator and concept clarity now, harder hardware and public-key research later

### If an investor asks “So is this a product demo?”

Recommended answer:

> It is better understood as an architecture demo than a finished product demo. It demonstrates the anti-counterfeiting intuition and transfer model behind the current private-key QMoney path, while the repo itself remains a research and simulation platform.

---

## 2. Research talk version

### 30-second research opener

This demo is a pedagogical bridge for the current `pkey_quorum` track in QMoney. It uses a polarization analogy to explain a BB84-style private-key note family: hidden basis choices, disturbance under incompatible measurement, verifier-held secret checking information, and consumptive verification with remint semantics.

### 90-second research version

The clean way to interpret this polarizer demo is as a physical intuition layer for the current private-key baseline, not as evidence of true public-key quantum money. The note is modeled as many independent BB84-style slots, each prepared in one of four polarization-like states: `0°`, `90°`, `45°`, or `135°`. An adversary without the hidden basis schedule cannot safely extract the full preparation pattern, because wrong-basis probing disturbs the state.

That gives the standard Wiesner/BB84 anti-counterfeiting intuition, but the verifier model is the key classification issue. In the current QMoney baseline, verification depends on hidden per-slot checking information held by a quorum. So this is properly described as **private-key quantum cash** with **verify-and-remint** semantics, plus a classical public-key settlement layer.

The demo is useful because it makes the current verifier model legible. It is not a proof of optimal counterfeit resistance, not a hardware-complete protocol, and not a public-key construction. In particular, it does not resolve the stronger coherence-sensitive verification questions that future public-key note families must answer.

### Research emphasis points
- Correct classification: private-key quantum cash, not public-key quantum money
- Verifier model matters more than visual optics elegance
- Consumptive verification naturally implies remint semantics
- Demo should not be mistaken for a coherence-sensitive public-key verifier
- Good explanatory bridge for `pkey_quorum`, not `pubkey_hidden_subspace`

### If a researcher asks “What is the main limitation of this demo?”

Recommended answer:

> Its main limitation is that it explains basis disturbance well but does not by itself establish the deeper verifier properties we would need for stronger claims, especially around coherence-sensitive verification, verifier leakage, and public-key unforgeability.

---

## 3. Museum / public exhibit placard version

### Short placard

**QMoney Polarizer Demo**

This exhibit uses polarization as an analogy for a quantum banknote. Each tiny “slot” in the note is secretly prepared in one of several possible states. If someone tries to inspect it the wrong way, they disturb it, making reliable copying difficult. That is the anti-counterfeiting intuition.

In QMoney's current design, a trusted verifier group knows the hidden checking recipe. Checking the note uses it up, so a successful transfer requires creating a fresh replacement note. This is why the design is described as **private-key** and **verify-and-remint**.

### One-sentence museum subtitle

**A physical intuition model for unclonable notes — not yet a finished quantum payment device**

### 45-second public explainer

Think of this as a banknote made of many tiny light-orientation secrets. If you know the right way to check each one, you can test whether the note is authentic. But if you guess wrong while trying to inspect and copy it, you disturb the note and lose information. That makes copying fundamentally harder than copying an ordinary image or barcode. In QMoney's current design, the note is checked by a trusted verifier group, and the checking process consumes the original, so a fresh replacement note has to be issued after a successful transfer.

### Public exhibit emphasis points
- Focus on intuition, not formal proof
- Emphasize “copying disturbs the thing being copied”
- Explain that checking uses up the original note
- Avoid jargon unless the audience asks for it

---

## 4. Quick chooser

Use this audience map:

- **Founder / investor** → emphasize architecture, differentiation, and honest roadmap
- **Research talk** → emphasize verifier model, classification, and limitations
- **Museum / public exhibit** → emphasize intuition, anti-copying, and consumptive checking

---

## 5. Universal closing line

> The point of the polarizer demo is not to claim that QMoney is finished. The point is to make the current private-key architecture understandable: hidden basis choices create counterfeit pressure, verification consumes the original note, and transfer therefore works by verify-and-remint.
