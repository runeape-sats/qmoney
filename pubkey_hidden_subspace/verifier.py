from __future__ import annotations

from dataclasses import dataclass

from .note_family import HiddenSubspaceNote, HiddenSubspacePublicKey, hadamard_transform
from .oracles import AUTHENTIC_CANDIDATE, OracleRegistry


@dataclass(frozen=True)
class VerificationDecision:
    serial: str
    accepted: bool
    reason: str


class HiddenSubspaceVerifier:
    def __init__(self, oracle_registry: OracleRegistry) -> None:
        self.oracle_registry = oracle_registry

    def verify(
        self,
        note: HiddenSubspaceNote,
        public_key: HiddenSubspacePublicKey,
        *,
        candidate_kind: str = AUTHENTIC_CANDIDATE,
        tolerance: float = 1e-9,
    ) -> VerificationDecision:
        if note.serial != public_key.serial:
            return VerificationDecision(note.serial, False, "serial_mismatch")
        if note.dimension != public_key.dimension:
            return VerificationDecision(note.serial, False, "dimension_mismatch")
        if not self.oracle_registry.is_published(public_key.serial):
            return VerificationDecision(note.serial, False, "oracle_not_published")
        if abs(note.norm_squared() - 1.0) > tolerance:
            return VerificationDecision(note.serial, False, "note_not_normalized")

        support = note.support(tolerance)
        if not all(self.oracle_registry.query_subspace(note.serial, vector, candidate_kind) for vector in support):
            return VerificationDecision(note.serial, False, "subspace_oracle_rejected")

        transformed = hadamard_transform(note)
        dual_support = transformed.support(tolerance)
        if not all(self.oracle_registry.query_dual(note.serial, vector, candidate_kind) for vector in dual_support):
            return VerificationDecision(note.serial, False, "dual_oracle_rejected")

        accepted = public_key.verify(note, tolerance)
        return VerificationDecision(note.serial, accepted, "accepted" if accepted else "public_key_check_rejected")
