from __future__ import annotations

BitVector = tuple[int, ...]


def parse_basis_vector(text: str) -> BitVector:
    """Parse a compact binary basis vector such as ``101``."""
    if text is None or text == "":
        raise ValueError("basis vector must not be empty")
    if any(ch not in "01" for ch in text):
        raise ValueError("basis vector must contain only binary digits 0 or 1")
    return tuple(int(ch) for ch in text)


def parse_generators(text: str) -> tuple[BitVector, ...]:
    """Parse comma-separated binary generator vectors such as ``101,011``."""
    if text is None or text.strip() == "":
        raise ValueError("generators must not be empty")

    parts = [part.strip() for part in text.split(",")]
    if any(part == "" for part in parts):
        raise ValueError("generators must not contain empty vectors")

    vectors = tuple(parse_basis_vector(part) for part in parts)
    lengths = {len(vector) for vector in vectors}
    if len(lengths) != 1:
        raise ValueError("all generator vectors must have the same length")
    return vectors
