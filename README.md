# QMoney: A Peer-to-Peer Quantum Money System

v0.0.2

## Abstract
QMoney introduces a novel quantum money system that combines the unforgeable nature of quantum states with a peer-to-peer (P2P) transaction framework inspired by Bitcoin. Using a 2-qubit quantum bill, QMoney leverages the **no-cloning theorem** to ensure that currency cannot be counterfeited, while a decentralized network of nodes verifies and transfers ownership without a central mint or bank. This white paper details the preparation, verification, and P2P exchange of quantum bills, illustrated through a toy example using photon polarization and polarizers. By merging quantum security with Bitcoin’s P2P philosophy, QMoney offers a vision for a trustless, quantum-secure digital currency.

---

## 1. Introduction
Traditional currencies and even modern cryptocurrencies like Bitcoin face challenges in achieving absolute unforgeability. Physical money can be replicated with advanced techniques, while Bitcoin, though secure against double-spending via its blockchain, relies on computational assumptions vulnerable to quantum attacks (e.g., Shor’s algorithm breaking ECDSA). Quantum money, first proposed by Stephen Wiesner in 1969, encodes currency in quantum states—such as superpositions of qubits—that cannot be perfectly copied due to the **no-cloning theorem**, offering a physics-based solution to counterfeiting.

**QMoney** extends this concept into a **peer-to-peer quantum money system**, integrating Bitcoin’s decentralized ethos. In Bitcoin, a P2P network of nodes validates transactions without a central authority, using a public ledger (the blockchain) to track ownership. QMoney adapts this model: instead of a mint and bank, users and nodes in a network collectively issue, verify, and transfer 2-qubit quantum bills. This white paper presents a minimal 2-qubit scheme to illustrate QMoney’s core mechanisms—quantum state preparation, decentralized verification, and P2P exchange—while providing a practical example with photon polarization. As of March 2025, quantum hardware remains experimental, but QMoney lays a theoretical foundation for a future where quantum and P2P technologies converge.

---

## 2. Theoretical Background
### 2.1 The No-Cloning Theorem
The **no-cloning theorem**, established by Wootters and Zurek in 1982, underpins QMoney’s security. It asserts that no unitary operation can duplicate an unknown quantum state |ψ⟩ = α|0⟩ + β|1⟩ into |ψ⟩ ⊗ |ψ⟩. Attempts to copy—e.g., by measuring and reconstructing—collapse the state, losing superposition information (e.g., |+⟩ becomes |0⟩ or |1⟩). In QMoney, this ensures that quantum bills cannot be forged, as any duplication attempt introduces detectable errors, a feature Bitcoin lacks, relying instead on cryptographic hardness.

### 2.2 Qubits and Measurement Bases
A **qubit**, unlike Bitcoin’s classical bits, exists in a superposition within a two-dimensional Hilbert space:
- |0⟩: e.g., horizontal polarization;
- |1⟩: e.g., vertical polarization;
- |+⟩ = (|0⟩ + |1⟩)/√2 or |-⟩ = (|0⟩ - |1⟩)/√2, superpositions akin to diagonal polarizations.

Measurement occurs in bases:
- **Standard basis**: |0⟩, |1⟩;
- **Hadamard basis**: |+⟩, |-⟩, accessed via the Hadamard gate H = (1/√2) * [1 1; 1 -1].

QMoney uses these bases to encode bills, with verification performed by P2P nodes rather than a central authority, mirroring Bitcoin’s distributed validation.

### 2.3 Bitcoin’s Peer-to-Peer Model
Bitcoin operates on a P2P network where nodes—computers running the Bitcoin protocol—validate transactions using a proof-of-work consensus mechanism. Transactions are broadcast to the network, recorded on a blockchain, and verified without intermediaries. QMoney adopts this P2P structure, replacing Bitcoin’s digital signatures with quantum state measurements, aiming for a decentralized quantum currency resilient to both classical and quantum threats.

---

## 3. QMoney: 2-Qubit Peer-to-Peer Quantum Money Scheme
### 3.1 State Preparation
In QMoney, a 2-qubit quantum bill is created by any user (a “minter”) in the P2P network:
1. **Random Basis Selection**: For each qubit, choose:
   - 0 (standard basis: |0⟩, |1⟩), 50% probability;
   - 1 (Hadamard basis: |+⟩, |-⟩), 50% probability.
2. **Random Bit Value**: 0 or 1, 50% probability.
3. **State Preparation**:
   - Basis 0, bit 0: |0⟩;
   - Basis 0, bit 1: |1⟩;
   - Basis 1, bit 0: |+⟩;
   - Basis 1, bit 1: |-⟩.

The minter broadcasts the quantum state (e.g., |0⟩ ⊗ |-⟩) and a classical “serial number” (basis and bit pairs, e.g., “0:0, 1:1”) encrypted with their quantum-resistant public key. Unlike Bitcoin’s mining, issuance is lightweight, requiring only quantum state generation.

### 3.2 Verification
Verification is decentralized, performed by P2P nodes:
- **Serial Number Decryption**: Nodes decrypt the serial number using the minter’s public key.
- **Measurement**:
  - Basis 0: Measure in the standard basis.
  - Basis 1: Apply a Hadamard gate, then measure in the standard basis.
- **Consensus**: Nodes broadcast measurement results. If the majority match the serial number’s bit values (e.g., 0 for Qubit 0, 1 for Qubit 1), the bill is valid. This mirrors Bitcoin’s consensus but uses quantum measurements instead of hash validation.

### 3.3 Peer-to-Peer Transfer
To spend a bill, the owner transfers the quantum state to a recipient via a quantum channel (e.g., optical fiber) and broadcasts a transaction to the P2P network, akin to Bitcoin’s transaction propagation. Nodes re-verify the state, updating a quantum-aware blockchain—a ledger recording ownership transitions without storing the fragile quantum states themselves. Double-spending is prevented by network consensus: once spent, the original state is measured (destroyed), and only the new owner’s state is valid.

### 3.4 Security
QMoney’s security combines quantum and P2P strengths:
- **No-Cloning**: Prevents state duplication.
- **Basis Secrecy**: Encrypted serial numbers hide bases from adversaries.
- **P2P Consensus**: Decentralized verification thwarts centralized attacks, unlike traditional quantum money’s reliance on a bank.

---

## 4. Simulating QMoney with Polarizers
### 4.1 Setup
We simulate a QMoney bill using photon polarization:
- |0⟩: Horizontal (H);
- |1⟩: Vertical (V);
- |+⟩: Diagonal (D);
- |-⟩: Anti-diagonal (A).
- **Hadamard Simulation**: Half-wave plate (HWP) at 22.5°.

Nodes use polarizers and HWPs to verify states in a P2P setting.

### 4.2 Example QMoney Bill
A user prepares:
- **Qubit 0**: Basis 0, bit 0 → |0⟩ (H);
- **Qubit 1**: Basis 1, bit 1 → |-⟩ (A).

State: |0⟩ ⊗ |-⟩ (H ⊗ A). Serial number (“0:0, 1:1”) is encrypted and broadcast.

### 4.3 Verification Process
Nodes in the P2P network:
- **Qubit 0**: Measure with H polarizer → Passes, yields |0⟩.
- **Qubit 1**: Apply HWP (A → V), measure with V polarizer → Passes, yields |1⟩.

Results (‘10’) are broadcast; majority consensus confirms validity.

### 4.4 Simulating a Counterfeiting Attempt
An adversary measures in the standard basis:
- Qubit 0 (H): H → |0⟩;
- Qubit 1 (A): H or V (50% each), e.g., V.

Prepares H ⊗ V copies. Nodes verify:
- Qubit 0: Passes;
- Qubit 1: HWP (V → A), V polarizer → 50% pass rate.

Copies fail consensus 50% of the time, detected by the network.

---

## 5. Security Analysis
QMoney’s dual-layer security includes:
- **Quantum Protection**: No-cloning ensures unforgeability.
- **P2P Resilience**: Decentralized nodes prevent single-point failures, unlike Bitcoin’s reliance on computational puzzles vulnerable to quantum speedup.
- **Error Detection**: Wrong-basis measurements yield inconsistent results across nodes.

For two qubits, counterfeiting success drops to 25% with one Hadamard-basis qubit; more qubits amplify this exponentially.

---

## 6. Challenges and Limitations
- **Scalability**: Two qubits are insufficient for robust security; 100+ qubits would resist quantum attacks like Grover’s algorithm.
- **Noise**: Decoherence in quantum channels (e.g., fiber optics) risks false rejections.
- **Infrastructure**: Quantum hardware and networks (e.g., quantum repeaters) are nascent in 2025.
- **Blockchain Integration**: A quantum-aware ledger must handle state destruction and P2P verification efficiently.

---

## 7. Conclusion
QMoney fuses quantum unforgeability with Bitcoin’s P2P framework, offering a trustless, quantum-secure currency. This 2-qubit model, demonstrated with polarizers, showcases its potential. Future work could scale QMoney with advanced quantum networks and ledgers, heralding a new era of decentralized finance.

---

## Appendix A: 512/1024-Qubit QMoney in a Pure Software Simulator (Quorum Public Verification + MPS)
This appendix describes a simplest-possible path to **512 or 1024 qubits** that:
- Supports **public verification** in the sense that *anyone can request verification from the network*;
- Avoids exotic public-key quantum money constructions;
- Runs on consumer hardware by keeping the bill state **very low entanglement** (product-state MPS with bond dimension D=1).

### A.1 Design choice: verification by a quorum (not by the bill holder)
The simplest way to get “public verification” while keeping the quantum state easy (MPS-friendly) is to make verification an **online service provided by a verifier quorum**:
- A verifier quorum collectively holds the bill’s secret measurement data (bases/bits).
- The bill holder never learns the full secret.
- Verification **consumes** the presented quantum state.
- If valid, the quorum **re-mints a fresh bill** for the recipient (new serial, new secret, new quantum state).

This keeps the quantum component “unforgeable by physics” (no-cloning), while the “public” property comes from decentralized access (anyone can ask), not from non-interactive public verifiability.

### A.2 Data model (one bill)
For a bill with `n ∈ {512, 1024}` qubits:
- `serial`: unique identifier (e.g., 128-bit random).
- `owner_pk`: current owner public key (ledger field).
- `C`: public commitment (e.g., `C = H(serial || B || V || nonce)`).
- Secret strings (known only to the verifier quorum):
  - `B ∈ {0,1}^n` where `B[i]=0` means Z-basis, `B[i]=1` means X-basis.
  - `V ∈ {0,1}^n` target outcomes in that basis.

### A.3 Quantum state preparation (BB84 product state)
Each qubit `i` is prepared as:
- If `B[i]=0` and `V[i]=0`: `|0⟩`
- If `B[i]=0` and `V[i]=1`: `|1⟩`
- If `B[i]=1` and `V[i]=0`: `|+⟩`
- If `B[i]=1` and `V[i]=1`: `|−⟩`

This state is a tensor product of single-qubit states, so it is an MPS with **bond dimension D=1**.

### A.4 Public verification + transfer protocol (verify-and-remint)
1. **Transfer intent**: sender creates a classical transaction `tx` naming `(old_serial, receiver_pk, fee, ...)` and signs it.
2. **Present bill**: sender submits the bill’s quantum state plus `tx` to a verifier quorum (in software, this can be passing an object/handle).
3. **Quorum verification**:
   - The quorum measures the submitted state in the secret bases `B`.
   - It checks outcomes against `V` with an acceptance rule (exact match, or thresholded for noise).
4. **Ledger update (atomic)**:
   - If accepted: mark `old_serial` spent; set ownership of a newly minted bill to `receiver_pk`.
   - If rejected: mark `old_serial` invalid/spent (the state was consumed by measurement anyway).
5. **Re-mint**: quorum generates fresh `(new_serial, B', V')` and prepares a new `n`-qubit product state for the receiver.

This is “one-time spend” at the quantum layer, but supports repeated circulation via re-minting.

### A.5 MPS simulation requirements (consumer hardware)
For this BB84 product-state design, you only need:
- Single-qubit gates: Hadamard `H` (to implement X-basis measurement as `H` then Z-measure).
- Projective measurement with collapse.

Implementation notes:
- Represent the bill as an MPS with tensors `A[i]` of shape `(1, 2, 1)`.
- Applying a single-qubit unitary is a `2x2` multiply on the physical index of `A[i]`.
- Z-basis measurement samples probabilities from the local 2-vector and collapses it to `|0⟩` or `|1⟩`.
- For `n=1024`, this remains linear-time and linear-memory in `n` as long as you do not introduce entangling gates (bond dimension stays 1).

### A.6 Security level (toy intercept/resend counterfeiter)
In the simplest threat model where a counterfeiter must produce a state that passes verification without knowing `B`, a per-qubit basis guess succeeds with probability `3/4`. If the quorum checks all qubits with exact matching:
- Forgery success: `P_forge = (3/4)^n`
- Security bits: `s = -log2(P_forge) = n * log2(4/3) ≈ 0.415 * n`

So:
- `n=512`: `s ≈ 212.5` bits (`P_forge ≈ 2^-212.5`)
- `n=1024`: `s ≈ 425.0` bits (`P_forge ≈ 2^-425`)

If you allow up to `t` mismatches for noise, replace the exact-match probability with a binomial tail `Pr[Binomial(n, 3/4) ≥ n - t]`, which increases attacker success; choose `t` based on your simulated noise model.

### A.7 Suggested parameters (software-only v0)
- Qubits per bill: `n=1024` (or `n=512` for faster iteration).
- Verification: measure all `n` qubits; accept if `matches ≥ n - t`.
- Noise tolerance: start with `t=0` (no noise) and later try `t = floor(0.01 * n)` in a noisy simulator.
- Verifier quorum: `N = 3f + 1` nodes; require `2f + 1` signed approvals to finalize “accepted + reminted” on the ledger.
- Secret storage: for a toy, replicate `(B,V)` across the quorum; for stronger fault tolerance, store `B` and `V` via threshold secret sharing.

## 8. Citations
- Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System. Retrieved from https://bitcoin.org/bitcoin.pdf
(The original Bitcoin white paper introducing the P2P transaction framework and blockchain, which QMoney adapts for its decentralized verification.)
- Wiesner, S. (1983). Conjugate coding. SIGACT News, 15(1), 78–88.
(Originally written in 1969, published later; introduces quantum money using quantum states, foundational to QMoney’s unforgeability.)
- Wootters, W. K., & Zurek, W. H. (1982). A single quantum cannot be cloned. Nature, 299(5886), 802–803.
(Establishes the no-cloning theorem, the core security principle preventing counterfeiting in QMoney.)
- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information. Cambridge University Press.
(A standard reference for quantum mechanics concepts like qubits, superposition, and the Hadamard gate, used in QMoney’s 2-qubit scheme.)
- Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM Journal on Computing, 26(5), 1484–1509.
(Describes Shor’s algorithm, highlighting Bitcoin’s vulnerability to quantum attacks, motivating QMoney’s quantum-resistant design.)
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. Proceedings of the 28th Annual ACM Symposium on Theory of Computing (STOC '96), 212–219.
(Introduces Grover’s algorithm, relevant to QMoney’s scalability challenges with larger qubit counts.)

## Demo (Software MPS Quorum)
Run the pure software simulator demo:
- `python qmoney_mps_quorum_demo.py --n 512`
- `python qmoney_mps_quorum_demo.py --n 1024`
