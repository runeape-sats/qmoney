#!/usr/bin/env python3
"""QMoney quorum + BB84 symbolic demo.

This is a pure software simulator for the Appendix-A design in README.md:
- The default bill size is 512 qubits.
- Bills are simulated symbolically as BB84 product states.
- A verifier quorum holds the secret bases/bits for each serial.
- Verification consumes the submitted bill; on success the quorum re-mints a fresh bill to the receiver.

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import math
import random
import secrets
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

Qubit = Tuple[complex, complex]  # (alpha, beta) in computational basis

DEFAULT_QUBITS = 512
SUPPORTED_QUBIT_COUNTS = (32, 128, 512, 1024)
SIMULATION_SETUP = "BB84 symbolic product-state private-key quorum"

_SQRT2 = math.sqrt(2.0)

KET0: Qubit = (1.0 + 0.0j, 0.0 + 0.0j)
KET1: Qubit = (0.0 + 0.0j, 1.0 + 0.0j)
KETP: Qubit = (1.0 / _SQRT2 + 0.0j, 1.0 / _SQRT2 + 0.0j)  # |+>
KETM: Qubit = (1.0 / _SQRT2 + 0.0j, -1.0 / _SQRT2 + 0.0j)  # |->


def _abs2(z: complex) -> float:
    return (z.real * z.real) + (z.imag * z.imag)


def apply_h(qubit: Qubit) -> Qubit:
    a, b = qubit
    return ((a + b) / _SQRT2, (a - b) / _SQRT2)


def apply_x(qubit: Qubit) -> Qubit:
    a, b = qubit
    return (b, a)


def prepare_bb84(basis: int, bit: int) -> Qubit:
    if basis == 0:
        return KET0 if bit == 0 else KET1
    return KETP if bit == 0 else KETM


def measure_z(qubit: Qubit, rng: random.Random) -> Tuple[int, Qubit]:
    a, b = qubit
    p0 = _abs2(a)
    r = rng.random()
    outcome = 0 if r < p0 else 1
    collapsed = KET0 if outcome == 0 else KET1
    return outcome, collapsed


def measure_x(qubit: Qubit, rng: random.Random) -> Tuple[int, Qubit]:
    rotated = apply_h(qubit)
    outcome, _ = measure_z(rotated, rng)
    collapsed = KETP if outcome == 0 else KETM
    return outcome, collapsed


def measure_in_basis(qubit: Qubit, basis: int, rng: random.Random) -> Tuple[int, Qubit]:
    if basis == 0:
        return measure_z(qubit, rng)
    return measure_x(qubit, rng)


def maybe_bitflip(qubit: Qubit, p: float, rng: random.Random) -> Qubit:
    if p <= 0.0:
        return qubit
    return apply_x(qubit) if rng.random() < p else qubit


@dataclass(frozen=True)
class Bill:
    serial: str
    qubits: List[Qubit]  # MPS with D=1: one tensor per site

    @property
    def n(self) -> int:
        return len(self.qubits)


@dataclass(frozen=True)
class BillSecret:
    basis: List[int]  # 0=Z, 1=X
    bits: List[int]  # expected measurement results


@dataclass(frozen=True)
class VerificationSample:
    accepted: bool
    matches: int
    measured: int


@dataclass(frozen=True)
class CounterfeitPairTrial:
    first: VerificationSample
    second: VerificationSample

    @property
    def pair_accepted(self) -> bool:
        return self.first.accepted and self.second.accepted


@dataclass(frozen=True)
class AdaptiveProbeResult:
    index: int
    basis_guess: int
    bit_guess: int
    verification: VerificationSample


class Ledger:
    def __init__(self) -> None:
        self._spent: set[str] = set()
        self._owner: Dict[str, str] = {}

    def register(self, serial: str, owner: str) -> None:
        self._owner[serial] = owner

    def owner_of(self, serial: str) -> Optional[str]:
        return self._owner.get(serial)

    def is_spent(self, serial: str) -> bool:
        return serial in self._spent

    def mark_spent(self, serial: str) -> None:
        self._spent.add(serial)

    def transfer_owner(self, serial: str, new_owner: str) -> None:
        self._owner[serial] = new_owner


class QuorumNode:
    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self._secrets: Dict[str, BillSecret] = {}

    def store_secret(self, serial: str, secret: BillSecret) -> None:
        self._secrets[serial] = secret

    def has_secret(self, serial: str) -> bool:
        return serial in self._secrets

    def verify_indices(
        self,
        bill: Bill,
        indices: Sequence[int],
        *,
        noise_bitflip_p: float,
        rng: random.Random,
    ) -> Tuple[int, int]:
        secret = self._secrets[bill.serial]
        matches = 0
        for i in indices:
            qubit = maybe_bitflip(bill.qubits[i], noise_bitflip_p, rng)
            outcome, collapsed = measure_in_basis(qubit, secret.basis[i], rng)
            bill.qubits[i] = collapsed
            if outcome == secret.bits[i]:
                matches += 1
        return matches, len(indices)


class QuorumService:
    def __init__(self, nodes: List[QuorumNode], threshold: int) -> None:
        if threshold <= 0 or threshold > len(nodes):
            raise ValueError("threshold must be in [1, N]")
        self.nodes = nodes
        self.threshold = threshold

    def _mint_secret(self, n: int) -> BillSecret:
        basis = [secrets.randbelow(2) for _ in range(n)]
        bits = [secrets.randbelow(2) for _ in range(n)]
        return BillSecret(basis=basis, bits=bits)

    def mint_bill(self, n: int, owner: str, ledger: Ledger) -> Bill:
        serial = secrets.token_hex(16)
        secret = self._mint_secret(n)

        qubits = [prepare_bb84(secret.basis[i], secret.bits[i]) for i in range(n)]
        bill = Bill(serial=serial, qubits=qubits)

        for node in self.nodes:
            node.store_secret(serial, secret)

        ledger.register(serial, owner)
        return bill

    def verify_and_remint(
        self,
        bill: Bill,
        *,
        claimant: str,
        receiver: str,
        ledger: Ledger,
        tolerance: int = 0,
        noise_bitflip_p: float = 0.0,
        seed: Optional[int] = None,
    ) -> Tuple[bool, Optional[Bill]]:
        if ledger.is_spent(bill.serial):
            return False, None
        if ledger.owner_of(bill.serial) != claimant:
            return False, None
        if tolerance < 0 or tolerance > bill.n:
            raise ValueError("tolerance must be in [0, n]")

        rng = random.Random(seed)

        participants = [node for node in self.nodes if node.has_secret(bill.serial)]

        # If we cannot assemble a quorum, verification never starts and the bill remains live.
        if len(participants) < self.threshold:
            return False, None

        # Partition indices across participating nodes so the whole bill is checked.
        assignments: List[List[int]] = [[] for _ in range(len(participants))]
        for i in range(bill.n):
            assignments[i % len(participants)].append(i)

        matches_total = 0
        measured_total = 0
        for node_idx, node in enumerate(participants):
            # Each node gets an independent RNG stream.
            node_rng = random.Random(rng.getrandbits(64) ^ (node_idx << 32) ^ node.node_id)
            matches, measured = node.verify_indices(
                bill,
                assignments[node_idx],
                noise_bitflip_p=noise_bitflip_p,
                rng=node_rng,
            )
            matches_total += matches
            measured_total += measured

        # Bill was consumed by measurement; spend it regardless of outcome.
        ledger.mark_spent(bill.serial)

        accepted = matches_total >= (measured_total - tolerance)
        if not accepted:
            return False, None

        new_bill = self.mint_bill(bill.n, owner=receiver, ledger=ledger)
        return True, new_bill


def counterfeit_intercept_resend(bill: Bill, rng: random.Random) -> Bill:
    # Attacker measures each qubit in a random basis, then re-prepares that measured state.
    forged_qubits: List[Qubit] = []
    for q in bill.qubits:
        basis_guess = rng.randrange(2)
        outcome, _collapsed = measure_in_basis(q, basis_guess, rng)
        forged_qubits.append(prepare_bb84(basis_guess, outcome))
    return Bill(serial=bill.serial, qubits=forged_qubits)


def clone_bill(bill: Bill) -> Bill:
    """Return a Bill with a separate qubit list; individual qubit tuples are immutable."""
    return Bill(serial=bill.serial, qubits=list(bill.qubits))


def evaluate_bill_against_secret(
    bill: Bill,
    secret: BillSecret,
    *,
    tolerance: int = 0,
    noise_bitflip_p: float = 0.0,
    seed: Optional[int] = None,
) -> VerificationSample:
    if bill.n != len(secret.basis) or bill.n != len(secret.bits):
        raise ValueError("bill and secret dimensions must match")
    if tolerance < 0 or tolerance > bill.n:
        raise ValueError("tolerance must be in [0, n]")

    rng = random.Random(seed)
    matches = 0
    for i, qubit in enumerate(bill.qubits):
        noisy = maybe_bitflip(qubit, noise_bitflip_p, rng)
        outcome, collapsed = measure_in_basis(noisy, secret.basis[i], rng)
        bill.qubits[i] = collapsed
        if outcome == secret.bits[i]:
            matches += 1

    return VerificationSample(
        accepted=matches >= bill.n - tolerance,
        matches=matches,
        measured=bill.n,
    )


def one_note_to_two_counterfeit_trial(
    bill: Bill,
    secret: BillSecret,
    rng: random.Random,
    *,
    tolerance: int = 0,
    noise_bitflip_p: float = 0.0,
) -> CounterfeitPairTrial:
    forged = counterfeit_intercept_resend(clone_bill(bill), rng)
    first = clone_bill(forged)
    second = clone_bill(forged)
    return CounterfeitPairTrial(
        first=evaluate_bill_against_secret(
            first,
            secret,
            tolerance=tolerance,
            noise_bitflip_p=noise_bitflip_p,
            seed=rng.getrandbits(64),
        ),
        second=evaluate_bill_against_secret(
            second,
            secret,
            tolerance=tolerance,
            noise_bitflip_p=noise_bitflip_p,
            seed=rng.getrandbits(64),
        ),
    )


def adaptive_replacement_probe(
    bill: Bill,
    secret: BillSecret,
    *,
    index: int,
    basis_guess: int,
    bit_guess: int,
    tolerance: int = 0,
    seed: Optional[int] = None,
) -> AdaptiveProbeResult:
    if index < 0 or index >= bill.n:
        raise ValueError("index must be in [0, n)")
    candidate = clone_bill(bill)
    candidate.qubits[index] = prepare_bb84(basis_guess, bit_guess)
    return AdaptiveProbeResult(
        index=index,
        basis_guess=basis_guess,
        bit_guess=bit_guess,
        verification=evaluate_bill_against_secret(candidate, secret, tolerance=tolerance, seed=seed),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=f"QMoney {SIMULATION_SETUP} software demo",
        epilog=f"Defaults: --n {DEFAULT_QUBITS}; setup: {SIMULATION_SETUP}.",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=DEFAULT_QUBITS,
        choices=SUPPORTED_QUBIT_COUNTS,
        help=f"number of BB84 qubits per bill (default: {DEFAULT_QUBITS})",
    )
    parser.add_argument("--nodes", type=int, default=4, help="quorum size N")
    parser.add_argument("--threshold", type=int, default=3, help="minimum live participants required to attempt verification")
    parser.add_argument("--tolerance", type=int, default=0, help="allowed mismatches")
    parser.add_argument("--noise-bitflip", type=float, default=0.0, help="bit-flip probability per measured qubit")
    parser.add_argument("--seed", type=int, default=123, help="RNG seed for reproducible demo")
    parser.add_argument("--forge-trials", type=int, default=0, help="run intercept/resend forge trials (use small n)")

    args = parser.parse_args()

    print(f"setup={SIMULATION_SETUP}; qubits={args.n}")

    nodes = [QuorumNode(i) for i in range(args.nodes)]
    quorum = QuorumService(nodes, threshold=args.threshold)
    ledger = Ledger()

    bill = quorum.mint_bill(args.n, owner="alice", ledger=ledger)
    ok, new_bill = quorum.verify_and_remint(
        bill,
        claimant="alice",
        receiver="bob",
        ledger=ledger,
        tolerance=args.tolerance,
        noise_bitflip_p=args.noise_bitflip,
        seed=args.seed,
    )
    print(f"transfer alice->bob accepted={ok}")

    ok2, _ = quorum.verify_and_remint(
        bill,
        claimant="alice",
        receiver="carol",
        ledger=ledger,
        tolerance=args.tolerance,
        noise_bitflip_p=args.noise_bitflip,
        seed=args.seed,
    )
    print(f"double-spend accepted={ok2}")

    if new_bill is not None:
        print(f"new serial minted to bob: {new_bill.serial}")

    if args.forge_trials > 0:
        if args.n > 128:
            print("forge trials with n>128 are unlikely to ever succeed; use --n 32 or --n 128")
        rng = random.Random(args.seed)
        successes = 0
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
            successes += 1 if ok_forge else 0
        print(f"forge success rate: {successes}/{args.forge_trials}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
