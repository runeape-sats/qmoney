from __future__ import annotations

import math
from dataclasses import dataclass
from itertools import product
from typing import Dict, Iterable, List, Sequence, Tuple

Vector = Tuple[int, ...]
AmplitudeMap = Dict[Vector, float]


def _xor_vectors(left: Vector, right: Vector) -> Vector:
    return tuple((a ^ b) for a, b in zip(left, right))


def _dot_mod2(left: Vector, right: Vector) -> int:
    return sum(a & b for a, b in zip(left, right)) % 2


def _all_binary_vectors(dimension: int) -> List[Vector]:
    return [tuple(bits) for bits in product((0, 1), repeat=dimension)]


def span(generators: Sequence[Vector]) -> List[Vector]:
    if not generators:
        return [tuple()]
    dimension = len(generators[0])
    vectors = {tuple(0 for _ in range(dimension))}
    for generator in generators:
        vectors |= {_xor_vectors(existing, generator) for existing in list(vectors)}
    return sorted(vectors)


def orthogonal_complement(vectors: Sequence[Vector]) -> List[Vector]:
    if not vectors:
        return [tuple()]
    dimension = len(vectors[0])
    complement = []
    for candidate in _all_binary_vectors(dimension):
        if all(_dot_mod2(candidate, vector) == 0 for vector in vectors):
            complement.append(candidate)
    return sorted(complement)


@dataclass(frozen=True)
class HiddenSubspaceNote:
    serial: str
    dimension: int
    amplitudes: AmplitudeMap

    def support(self, tolerance: float = 1e-9) -> List[Vector]:
        return [basis for basis, amplitude in sorted(self.amplitudes.items()) if abs(amplitude) > tolerance]

    def norm_squared(self) -> float:
        return sum(amplitude * amplitude for amplitude in self.amplitudes.values())

    def is_uniform_on(self, support: Iterable[Vector], tolerance: float = 1e-9) -> bool:
        support_set = set(support)
        actual_support = set(self.support(tolerance))
        if actual_support != support_set or not support_set:
            return False
        magnitudes = {round(abs(self.amplitudes[basis]), 12) for basis in support_set}
        signs = {1 if self.amplitudes[basis] > tolerance else -1 if self.amplitudes[basis] < -tolerance else 0 for basis in support_set}
        return len(magnitudes) == 1 and len(signs) == 1 and 0 not in signs


@dataclass(frozen=True)
class HiddenSubspacePublicKey:
    serial: str
    dimension: int
    subspace_vectors: Tuple[Vector, ...]
    dual_vectors: Tuple[Vector, ...]

    def verify(self, note: HiddenSubspaceNote, tolerance: float = 1e-9) -> bool:
        if note.serial != self.serial or note.dimension != self.dimension:
            return False
        if abs(note.norm_squared() - 1.0) > tolerance:
            return False
        if not note.is_uniform_on(self.subspace_vectors, tolerance):
            return False
        transformed = hadamard_transform(note)
        if abs(transformed.norm_squared() - 1.0) > tolerance:
            return False
        return transformed.is_uniform_on(self.dual_vectors, tolerance)

    def summary(self) -> dict:
        subspace_dimension = int(round(math.log2(len(self.subspace_vectors)))) if self.subspace_vectors else 0
        dual_dimension = int(round(math.log2(len(self.dual_vectors)))) if self.dual_vectors else 0
        return {
            "serial": self.serial,
            "dimension": self.dimension,
            "subspace_dimension": subspace_dimension,
            "dual_subspace_dimension": dual_dimension,
            "subspace_vectors": list(self.subspace_vectors),
            "dual_subspace_vectors": list(self.dual_vectors),
        }


@dataclass(frozen=True)
class HiddenSubspaceMint:
    serial: str
    generators: Tuple[Vector, ...]
    public_key: HiddenSubspacePublicKey

    @classmethod
    def from_generators(cls, serial: str, generators: Sequence[Vector]) -> "HiddenSubspaceMint":
        if not generators:
            raise ValueError("generators must not be empty")
        dimension = len(generators[0])
        if any(len(generator) != dimension for generator in generators):
            raise ValueError("all generators must have the same dimension")
        subspace_vectors = tuple(span(tuple(generators)))
        dual_vectors = tuple(orthogonal_complement(subspace_vectors))
        public_key = HiddenSubspacePublicKey(
            serial=serial,
            dimension=dimension,
            subspace_vectors=subspace_vectors,
            dual_vectors=dual_vectors,
        )
        return cls(serial=serial, generators=tuple(tuple(g) for g in generators), public_key=public_key)

    def mint_note(self) -> HiddenSubspaceNote:
        support = self.public_key.subspace_vectors
        amplitude = 1.0 / math.sqrt(len(support))
        return HiddenSubspaceNote(
            serial=self.serial,
            dimension=self.public_key.dimension,
            amplitudes={basis: amplitude for basis in support},
        )


def basis_state(dimension: int, basis: Vector, *, serial: str) -> HiddenSubspaceNote:
    if len(basis) != dimension:
        raise ValueError("basis vector length must equal dimension")
    return HiddenSubspaceNote(serial=serial, dimension=dimension, amplitudes={basis: 1.0})


def hadamard_transform(note: HiddenSubspaceNote) -> HiddenSubspaceNote:
    all_vectors = _all_binary_vectors(note.dimension)
    scale = 1.0 / math.sqrt(2 ** note.dimension)
    transformed: AmplitudeMap = {}
    for target in all_vectors:
        amplitude = 0.0
        for source, source_amplitude in note.amplitudes.items():
            phase = -1.0 if _dot_mod2(source, target) else 1.0
            amplitude += source_amplitude * phase * scale
        if abs(amplitude) > 1e-12:
            transformed[target] = amplitude
    return HiddenSubspaceNote(serial=note.serial, dimension=note.dimension, amplitudes=transformed)
