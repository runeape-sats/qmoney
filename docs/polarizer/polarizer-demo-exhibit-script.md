# Polarizer Demo Exhibit Script

This script is for presenting the **QMoney polarizer demo** in a way that is accurate, short, and repeatable.

Use it for:
- live demos,
- booth presentations,
- investor walk-throughs,
- research intros,
- recorded short explainers.

## Core message

> This demo illustrates the **private-key** path in QMoney. It shows how hidden basis choices and measurement disturbance can make copying difficult, and why verification consumes the original note and requires remint. It is an intuition demo, not yet a full hardware or public-key implementation.

---

## 1. 30-second version

QMoney's current baseline is best thought of as a **private-key quantum cash** system. This demo uses polarization as an intuition bridge. A note is imagined as many tiny slots, each secretly prepared in one of four BB84-style states. If you probe a slot in the wrong basis, you disturb it. That is the anti-counterfeiting intuition. The verifier knows the hidden checking recipe, so verification works like a secret exam. But checking consumes the note, so after a successful transfer the system remints a fresh replacement note.

---

## 2. 90-second version

This demo is a physical intuition model for QMoney's current private-key note family.

Imagine a banknote made of many tiny polarization slots. For each slot, the mint secretly chooses one of four states: `0°`, `90°`, `45°`, or `135°`. That is the BB84-style alphabet. A counterfeiter who does not know the hidden basis recipe cannot safely inspect every slot, because measuring in the wrong orientation disturbs the state.

That gives the basic anti-counterfeiting intuition: unlike a classical bill, you cannot just read out the full hidden pattern and copy it perfectly.

The verifier side is also important. In QMoney's current private-key baseline, the verifier quorum already knows the hidden answer key for how each slot should be checked. So this is not public-key quantum money. It is a secret-holding verification service. The verifier checks the note against the hidden recipe, and that measurement consumes the original note. If the note passes, the system mints a fresh replacement note for the receiver. That is why the current architecture is **verify-and-remint**.

---

## 3. 3-minute version

Here is the clean way to read this demo.

First, this is **not** a claim that the current repo already runs as a production optical quantum-money system. The current repo's baseline is a classical simulator of a BB84-style private-key note family plus a classical settlement layer. This demo is a physical intuition bridge for that private-key quantum layer.

Second, the reason polarization is useful is that it makes basis mismatch intuitive. We can picture four allowed states: `0°`, `90°`, `45°`, and `135°`. Those correspond to two incompatible basis families. If an honest verifier knows the hidden basis recipe, they can test whether the note behaves correctly. But if an attacker guesses wrong while trying to inspect it, they disturb the state and degrade their ability to copy it.

Third, this explains why QMoney's current architecture is private-key. The verifier must know hidden per-slot checking information. That hidden recipe is what the public does not get to see. So the system is not yet true public-key quantum money. Instead, it is more like a decentralized private-key verification service run by a quorum.

Fourth, verification is consumptive. In classical money, you might imagine checking the same token repeatedly without changing it. In QMoney, the check itself uses up the original quantum state. So after acceptance, the system invalidates the old serial and remints a fresh replacement note for the receiver.

That is the main takeaway:
- hidden basis choices give the anti-counterfeiting intuition,
- verifier-held secrets make the current baseline private-key,
- and consumptive verification leads naturally to verify-and-remint.

---

## 4. Physical demo narration beats

Use these beats during a live walkthrough.

### Beat 1: Set expectations
Say:

> This is an intuition demo for QMoney's private-key path, not a claim of a finished optical payment network.

### Beat 2: Introduce the state alphabet
Say:

> Think of the note as many tiny slots. Each slot is secretly prepared in one of four BB84-style states: `0°`, `90°`, `45°`, or `135°`.

### Beat 3: Explain incompatible bases
Say:

> The key fact is that there are two incompatible measurement families. If you know the right basis, you can test correctly. If you guess the wrong one, you disturb the state.

### Beat 4: Explain counterfeit difficulty
Say:

> That means a counterfeiter cannot safely learn the whole note recipe just by inspecting it. Probing the note risks damaging the very information they want to copy.

### Beat 5: Explain verifier privilege
Say:

> In the current QMoney baseline, the verifier already knows the hidden checking recipe. That is why this is private-key quantum cash, not public-key quantum money.

### Beat 6: Explain consumptive verification
Say:

> Verification is not free. Checking the note consumes the original state, so a successful transfer requires reminting a fresh note for the receiver.

### Beat 7: Close honestly
Say:

> So this demo is best understood as a tangible explanation of the private-key anti-counterfeiting layer and the verify-and-remint transfer model.

---

## 5. What to say if someone asks “Is this public-key quantum money?”

Recommended answer:

> No. This demo supports the private-key BB84-style intuition. In public-key quantum money, anyone should be able to verify using public information without learning how to mint valid counterfeits. That is a separate research track for QMoney.

---

## 6. What to say if someone asks “Is this the real hardware implementation?”

Recommended answer:

> Not yet. This is a physical intuition demo. The current repo baseline is still a classical simulator of BB84-style behavior. A real hardware implementation would require much more around state preparation, loss handling, calibration, detection, throughput, and protocol engineering.

---

## 7. What to say if someone asks “Why not just verify the same note again later?”

Recommended answer:

> Because the act of verification measures the quantum state and consumes it. In the current architecture, successful circulation works by verify-and-remint: the old note is checked and retired, and a fresh note is issued to the next holder.

---

## 8. What to avoid saying

Avoid:
- “This proves QMoney is production-ready.”
- “This is public-key quantum money.”
- “Anyone can verify the note directly from public information.”
- “This optical toy is the full protocol.”
- “No-cloning alone solves the system design problem.”

---

## 9. Slide / signage copy

## Short wall text

**QMoney Polarizer Demo**

This exhibit illustrates the private-key quantum layer of QMoney using a BB84-style polarization analogy. It shows how hidden basis choices and measurement disturbance can make copying difficult, and why verification consumes the original note and requires reminting a fresh replacement note.

## One-line subtitle

**Private-key QMoney intuition demo — not yet a full hardware or public-key implementation**

---

## 10. Recommended close

> The value of this demo is not that it finishes the research problem. The value is that it makes the current private-key QMoney architecture legible: hidden-basis verification, counterfeit pressure from disturbance, and verify-and-remint as the natural transfer model.
