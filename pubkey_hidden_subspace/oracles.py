from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Sequence, Tuple

from .note_family import HiddenSubspacePublicKey, Vector

SUBSPACE_QUERY = "subspace"
DUAL_QUERY = "dual"
AUTHENTIC_CANDIDATE = "authentic_candidate"
COUNTERFEIT_CANDIDATE = "counterfeit_candidate"


class OraclePublicationError(ValueError):
    pass


@dataclass(frozen=True)
class OracleQueryRecord:
    serial: str
    kind: str
    candidate_kind: str
    vector: Vector
    answer: bool


@dataclass(frozen=True)
class OraclePublication:
    serial: str
    dimension: int
    subspace_vectors: Tuple[Vector, ...]
    dual_vectors: Tuple[Vector, ...]

    @classmethod
    def from_public_key(cls, public_key: HiddenSubspacePublicKey) -> "OraclePublication":
        return cls(
            serial=public_key.serial,
            dimension=public_key.dimension,
            subspace_vectors=public_key.subspace_vectors,
            dual_vectors=public_key.dual_vectors,
        )


@dataclass
class OracleRegistry:
    _publications: Dict[str, OraclePublication] = field(default_factory=dict)
    _query_log: List[OracleQueryRecord] = field(default_factory=list)

    def publish(self, public_key: HiddenSubspacePublicKey) -> OraclePublication:
        publication = OraclePublication.from_public_key(public_key)
        self._publications[publication.serial] = publication
        return publication

    def is_published(self, serial: str) -> bool:
        return serial in self._publications

    def publication_for(self, serial: str) -> OraclePublication:
        try:
            return self._publications[serial]
        except KeyError as exc:
            raise OraclePublicationError(f"oracle state for serial {serial!r} has not been published") from exc

    @property
    def query_log(self) -> Tuple[OracleQueryRecord, ...]:
        return tuple(self._query_log)

    def query_subspace(self, serial: str, vector: Sequence[int], candidate_kind: str) -> bool:
        publication = self.publication_for(serial)
        answer = tuple(vector) in set(publication.subspace_vectors)
        self._query_log.append(
            OracleQueryRecord(
                serial=serial,
                kind=SUBSPACE_QUERY,
                candidate_kind=candidate_kind,
                vector=tuple(vector),
                answer=answer,
            )
        )
        return answer

    def query_dual(self, serial: str, vector: Sequence[int], candidate_kind: str) -> bool:
        publication = self.publication_for(serial)
        answer = tuple(vector) in set(publication.dual_vectors)
        self._query_log.append(
            OracleQueryRecord(
                serial=serial,
                kind=DUAL_QUERY,
                candidate_kind=candidate_kind,
                vector=tuple(vector),
                answer=answer,
            )
        )
        return answer
