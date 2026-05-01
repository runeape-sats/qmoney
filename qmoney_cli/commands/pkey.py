from __future__ import annotations

import argparse
import math
import random
from typing import Any

from pkey_quorum import Ledger, QuorumNode, QuorumService, counterfeit_intercept_resend
from pkey_quorum.demo import DEFAULT_QUBITS, SIMULATION_SETUP, SUPPORTED_QUBIT_COUNTS


def positive_int(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a positive integer") from exc
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def nonnegative_int(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a non-negative integer") from exc
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return parsed


def probability(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a finite probability in [0, 1]") from exc
    if not math.isfinite(parsed) or parsed < 0.0 or parsed > 1.0:
        raise argparse.ArgumentTypeError("must be a finite probability in [0, 1]")
    return parsed


def run_demo(args: argparse.Namespace) -> dict[str, Any]:
    if args.threshold > args.nodes:
        raise ValueError("threshold must be in [1, nodes]")
    if args.tolerance > args.n:
        raise ValueError("tolerance must be in [0, n]")

    nodes = [QuorumNode(i) for i in range(args.nodes)]
    quorum = QuorumService(nodes, threshold=args.threshold)
    ledger = Ledger()

    bill = quorum.mint_bill(args.n, owner="alice", ledger=ledger)
    accepted, new_bill = quorum.verify_and_remint(
        bill,
        claimant="alice",
        receiver="bob",
        ledger=ledger,
        tolerance=args.tolerance,
        noise_bitflip_p=args.noise_bitflip,
        seed=args.seed,
    )

    double_spend_accepted, _ = quorum.verify_and_remint(
        bill,
        claimant="alice",
        receiver="carol",
        ledger=ledger,
        tolerance=args.tolerance,
        noise_bitflip_p=args.noise_bitflip,
        seed=args.seed,
    )

    rng = random.Random(args.seed)
    forge_successes = 0
    for _ in range(args.forge_trials):
        fresh = quorum.mint_bill(args.n, owner="mallory", ledger=ledger)
        forged = counterfeit_intercept_resend(fresh, rng)
        ok_forge, _ = quorum.verify_and_remint(
            forged,
            claimant="mallory",
            receiver="mallory",
            ledger=ledger,
            tolerance=args.tolerance,
            noise_bitflip_p=args.noise_bitflip,
            seed=rng.getrandbits(32),
        )
        if ok_forge:
            forge_successes += 1

    return {
        "track": "pkey_quorum",
        "command": "demo",
        "setup": SIMULATION_SETUP,
        "qubits": args.n,
        "transfer_accepted": accepted,
        "double_spend_accepted": double_spend_accepted,
        "new_serial": new_bill.serial if new_bill is not None else None,
        "forge_trials": args.forge_trials,
        "forge_successes": forge_successes,
    }


def render_text(payload: dict[str, Any]) -> str:
    lines = [
        f"setup={payload['setup']}; qubits={payload['qubits']}",
        f"transfer alice->bob accepted={payload['transfer_accepted']}",
        f"double-spend accepted={payload['double_spend_accepted']}",
    ]
    if payload["new_serial"] is not None:
        lines.append(f"new serial minted to bob: {payload['new_serial']}")
    lines.append(f"forge success rate: {payload['forge_successes']}/{payload['forge_trials']}")
    return "\n".join(lines) + "\n"
