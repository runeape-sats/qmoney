from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from typing import Any


def _is_bit_vector(value: Any) -> bool:
    return isinstance(value, (tuple, list)) and all(isinstance(item, int) and item in (0, 1) for item in value)


def to_jsonable(value: Any) -> Any:
    """Convert CLI results to JSON-safe values, compacting bit vectors."""
    if is_dataclass(value):
        return to_jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(key): to_jsonable(item) for key, item in value.items()}
    if _is_bit_vector(value):
        return "".join(str(bit) for bit in value)
    if isinstance(value, tuple):
        return [to_jsonable(item) for item in value]
    if isinstance(value, list):
        return [to_jsonable(item) for item in value]
    return value


def dumps_json(payload: Any, *, pretty: bool = False) -> str:
    if pretty:
        return json.dumps(to_jsonable(payload), indent=2, sort_keys=True) + "\n"
    return json.dumps(to_jsonable(payload), separators=(",", ":"), sort_keys=True) + "\n"
