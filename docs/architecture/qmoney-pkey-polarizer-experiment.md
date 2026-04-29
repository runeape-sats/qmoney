# QMoney Private-Key Path Explained with a Polarizer Experiment

This note gives a layman-friendly explanation of QMoney's **private-key quorum** path using a polarization thought experiment.

It is an analogy for the current `pkey_quorum/` track in this repository. It is **not** a literal claim that the current code implements optical hardware with physical polarizers.

---

## 1. Why use a polarizer analogy?

QMoney's private-key path is based on a BB84-style note family.

In the code, each slot of a note is secretly prepared as one of four quantum states:

- `|0⟩`
- `|1⟩`
- `|+⟩`
- `|−⟩`

For a lay explanation, it is helpful to picture those as four polarization orientations:

- `|0⟩` → `0°`
- `|1⟩` → `90°`
- `|+⟩` → `45°`
- `|−⟩` → `135°`

That picture is useful because it makes two important ideas intuitive:

1. there are **two different measurement families**
2. checking in the wrong orientation can **disturb** the thing being checked

Those are exactly the two ideas QMoney needs for its private-key anti-counterfeiting story.

---

## 2. The warm-up: the three-polarizer surprise

A famous optics demo goes like this:

- if one polarizer is at `0°`
- and another is at `90°`
- then light that passes the first can be blocked by the second

But if you insert a third polarizer in the middle at an intermediate angle like `45°`, some light can get through again.

The point of this demo is not that light is "cheating." The point is that **measurement orientation matters**. What happens later depends on the basis/orientation used in the middle.

That is a good warm-up intuition for QMoney: the outcome is not determined only by a visible final test. It depends on the hidden sequence of how the state is prepared and measured.

Still, the three-polarizer demo by itself is too small to explain QMoney. QMoney is better imagined as a note made from **many tiny polarization slots**, not one beam through three filters.

---

## 3. The better analogy: an n-slot polarization banknote

Imagine a banknote made of `n` tiny light-polarization slots.

For each slot, the mint secretly chooses one of four allowed states:

- `0°`
- `90°`
- `45°`
- `135°`

Equivalently, the mint secretly chooses:

- which basis family to use
- and which outcome in that family should be correct

In QMoney's private-key path, that hidden information is the note's secret verification recipe.

In the current simulator this corresponds to hidden per-slot data like:

- which basis to use for measurement
- which result is expected in that basis

A genuine note is prepared to match that secret pattern.

---

## 4. Why a counterfeiter has a problem

Suppose a counterfeiter gets hold of the note but does **not** know the hidden polarization recipe.

They want to learn the state of every slot so they can copy it.

The problem is:

- if they guess the right orientation for a slot, they can learn something useful
- if they guess the wrong orientation, they disturb the slot and lose information

So the attacker faces a basic tradeoff:

- measure and risk disturbing the note
- or avoid measuring and remain ignorant

This is the layman core of the anti-counterfeiting story.

QMoney private-key notes are hard to copy because the verifier knows the hidden recipe, but the attacker does not.

---

## 5. What the verifier knows

In the private-key path, the verifier is not trying to *discover* the hidden recipe from the note.

The verifier already knows it.

That is why this path is called **private-key**.

A better picture is:

- the mint/verifier quorum secretly knows the correct tilt for each slot
- the presented note is tested against that secret answer key
- the public does not get to see the answer key

So QMoney private-key is **not**:

> guess the hidden tilt from the final light brightness

It is closer to:

> secretly know the correct tilt recipe, then test whether the submitted note behaves correctly under that hidden recipe

---

## 6. Why final brightness is not the main story

A single chain of polarizers often makes people think in terms of one output number: bright, dim, or blocked.

That is not the best mental model for QMoney.

QMoney is closer to:

- many independent slots
- many small checks
- many hidden measurement choices
- then a final accept/reject decision based on how many checks match

So the best layman image is **not** one beam with one final brightness.

It is a banknote made of many tiny polarization challenges, each secretly configured.

---

## 7. Why verification consumes the note

This is one of the most important parts of QMoney.

To verify the note, the verifier must actually measure it.

In the analogy:

- the verifier runs each slot through the secret polarizer test
- that very act of checking uses up or disturbs the original state

So after successful verification, the system does **not** hand back the exact same quantum object.

Instead, it issues a **fresh replacement note** for the receiver.

This is why the current QMoney private-key path is described as **verify-and-remint**.

In lay terms:

> the banknote is authentic if it passes the secret exam, but the exam itself consumes the original, so a fresh note must be minted after a successful transfer.

---

## 8. Why there is a quorum

The current QMoney path does not model one all-powerful central verifier.

Instead, it uses a **verifier quorum**.

In the analogy, you can imagine that the hidden answer key is held by a trusted group rather than one person.

That group:

- receives the note
- checks it using the hidden recipe
- attests whether it passed
- mints a fresh replacement note if it was valid

This is why the path is called **private-key quorum** rather than just private-key money.

The secrecy still matters, but the secret is managed by a group service rather than a single checker.

---

## 9. What this analogy gets right

The polarizer analogy is good for explaining:

- why there are four BB84-style states
- why there are two incompatible basis families
- why wrong-basis probing disturbs the note
- why the verifier must know a hidden measurement recipe
- why copying is hard without that recipe
- why verification consumes the original state

---

## 10. What this analogy does **not** prove

This analogy is only an explanatory bridge.

It does **not** by itself prove:

- full cryptographic security
- a hardware implementation
- a production optical design
- true public-key quantum money

It is specifically an explanation of the current **private-key** QMoney baseline.

The repo's public-key research path is a separate track with a different security goal.

---

## 11. One-paragraph layman version

QMoney's private-key path can be imagined as a banknote made of many tiny polarization slots. In each slot, the mint secretly chooses one of four allowed states: `0°`, `90°`, `45°`, or `135°`. The verifier quorum knows that hidden recipe, but counterfeiters do not. If a counterfeiter tries to inspect the note using the wrong orientation, they disturb it and cannot reliably copy the full pattern. To verify the note, the quorum measures each slot using the secret recipe. If enough slots match, the note is accepted. But that check consumes the original quantum state, so the system mints a fresh replacement note for the receiver instead of reusing the same note.

---

## 12. Short CLI-help version

`qmoney pkey` is the private-key quorum path. You can think of it as a banknote made from many tiny hidden polarization states chosen from `0°`, `90°`, `45°`, and `135°`. The verifier quorum secretly knows how each slot should be checked. A counterfeiter does not, so probing the note tends to disturb it. Verification therefore works like a secret exam: the quorum checks the note against its hidden answer key, and if it passes, the old note is consumed and a fresh replacement note is minted.
