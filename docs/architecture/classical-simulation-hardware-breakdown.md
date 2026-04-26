# Classical Simulation Hardware Breakdown

This note summarizes the RAM and VRAM implications of three classical simulation styles relevant to QMoney:

1. low-entanglement tensor-network / MPS simulation
2. sparse state-vector simulation
3. BB84 symbolic simulation

The current private-key baseline uses BB84 product states and verify-and-remint semantics. That makes the symbolic representation the most natural hardware target today, while MPS remains the best general-purpose upgrade path if future note families introduce limited entanglement.

---

## Summary

| Simulation style | RAM requirement | VRAM requirement | Best fit |
| --- | --- | --- | --- |
| Tensor network / MPS | Moderate when bond dimension is small; can grow quickly with entanglement | Optional; useful only if tensor contractions are large enough to justify GPU transfer overhead | Low-entanglement quantum notes and future limited-entanglement experiments |
| Sparse state vector | Low only when the number of nonzero amplitudes stays small | Optional; sparse GPU support may help for large linear algebra, but is not needed for the baseline | Tiny public-key/oracle prototypes or states with explicitly small support |
| BB84 symbolic simulation | Very low; linear in qubit count | None | Current private-key BB84/quorum simulator |

---

## 1. Tensor-network / MPS simulation

An MPS stores a quantum state as a chain of small tensors. Its memory cost is controlled mainly by:

- `n`: number of qubits
- `χ`: maximum bond dimension
- numeric precision, usually complex64 or complex128

Approximate memory:

```text
RAM ≈ O(n × χ² × complex_number_size)
```

For complex64, each complex number is about 8 bytes. For complex128, each complex number is about 16 bytes.

Example order-of-magnitude RAM for `n = 1,000` qubits with complex64:

| Bond dimension `χ` | Approximate RAM |
| ---: | ---: |
| 2 | ~32 KB |
| 16 | ~2 MB |
| 64 | ~33 MB |
| 256 | ~524 MB |
| 1024 | ~8 GB |

For the current BB84 product-state baseline, the bond dimension is effectively `χ = 1`, so MPS memory is tiny and scales linearly. If future designs add entangling gates or entangled note families, `χ` may grow and become the dominant hardware constraint.

### VRAM

VRAM is not required for MPS simulation. A GPU can help when tensor contractions are large and batched enough to offset CPU-to-GPU transfer overhead. For the current product-state simulator, GPU acceleration is usually unnecessary.

---

## 2. Sparse state-vector simulation

A sparse state vector stores only nonzero computational-basis amplitudes. Its memory cost is controlled mainly by:

- `k`: number of nonzero amplitudes
- amplitude precision
- index/key overhead

Approximate memory:

```text
RAM ≈ O(k × (amplitude_size + basis_index_size + container_overhead))
```

In compact numeric implementations this can be roughly 16-32 bytes per nonzero amplitude. In Python dictionary-style prototypes, overhead can be much higher.

Example compact-storage order of magnitude:

| Nonzero amplitudes `k` | Approximate RAM |
| ---: | ---: |
| 1,000 | ~16-32 KB |
| 1,000,000 | ~16-32 MB |
| 1,000,000,000 | ~16-32 GB |

Sparse simulation is attractive only when `k` stays small. It becomes dangerous for BB84-style states in the computational basis because each `|+⟩` or `|−⟩` qubit doubles the number of nonzero amplitudes. With `m` X-basis qubits:

```text
k = 2^m
```

That means sparse state vectors can become infeasible even when the underlying BB84 product state is simple.

### VRAM

VRAM is optional. Sparse GPU kernels can help for some large sparse linear algebra workloads, but they are not needed for QMoney's current baseline and may not help small Python research prototypes.

---

## 3. BB84 symbolic simulation

BB84 symbolic simulation stores the note as classical metadata rather than as amplitudes. Each qubit only needs:

- basis: Z or X
- bit: 0 or 1
- optional measurement/consumption state

Conceptual memory:

```text
RAM ≈ O(n)
```

The theoretical minimum is only a few bits per qubit. Practical implementations may use more because of Python object, list, or dataclass overhead, but the scaling remains linear and far smaller than dense or sparse amplitude simulation.

This is the best fit for the current private-key QMoney baseline because the simulator does not need to store the full quantum wavefunction to model:

- BB84 note preparation
- hidden basis/bit verification
- measurement consumption
- verify-and-remint behavior
- simple bit-flip noise

### VRAM

No VRAM is required. The workload is metadata-heavy and branch-heavy rather than dense numeric linear algebra. CPU RAM is the right hardware target.

---

## Practical recommendation for QMoney

For the current repo:

1. Use **BB84 symbolic simulation** for the private-key quorum baseline.
2. Use **MPS/tensor-network simulation** only when exploring future low-entanglement note families or when a more explicit quantum-state representation is needed.
3. Use **sparse state-vector simulation** only for tiny public-key/oracle prototypes or states whose support is intentionally small.

The safest default hardware assumption is therefore:

- ordinary CPU
- enough system RAM for the number of simulated bills, verifier secrets, logs, and tests
- no required GPU or VRAM

For `n = 512` or `n = 1024` BB84 product-state bills, the current simulator should be limited by Python/runtime overhead and experiment count, not by quantum-state memory.
