import unittest
from types import MethodType

from pkey_quorum import (
    Ledger,
    QuorumNode,
    QuorumService,
    adaptive_replacement_probe,
    one_note_to_two_counterfeit_trial,
)


class QuorumVerificationTests(unittest.TestCase):
    def test_verify_and_remint_measures_all_qubits_even_when_threshold_is_lower_than_node_count(self):
        nodes = [QuorumNode(i) for i in range(4)]
        quorum = QuorumService(nodes, threshold=3)
        ledger = Ledger()
        bill = quorum.mint_bill(8, owner="alice", ledger=ledger)

        calls = []

        def recording_verify(self, bill, indices, *, noise_bitflip_p, rng):
            calls.append((self.node_id, tuple(indices)))
            return len(indices), len(indices)

        for node in nodes:
            node.verify_indices = MethodType(recording_verify, node)

        accepted, new_bill = quorum.verify_and_remint(
            bill,
            claimant="alice",
            receiver="bob",
            ledger=ledger,
            seed=123,
        )

        self.assertTrue(accepted)
        self.assertIsNotNone(new_bill)
        self.assertCountEqual([node_id for node_id, _ in calls], [0, 1, 2, 3])
        measured_indices = [idx for _, indices in calls for idx in indices]
        self.assertEqual(sorted(measured_indices), list(range(8)))

    def test_verify_and_remint_does_not_spend_bill_when_not_enough_verifiers_are_available(self):
        nodes = [QuorumNode(i) for i in range(4)]
        quorum = QuorumService(nodes, threshold=4)
        ledger = Ledger()
        bill = quorum.mint_bill(8, owner="alice", ledger=ledger)

        nodes[-1]._secrets.pop(bill.serial)

        accepted, new_bill = quorum.verify_and_remint(
            bill,
            claimant="alice",
            receiver="bob",
            ledger=ledger,
            seed=123,
        )

        self.assertFalse(accepted)
        self.assertIsNone(new_bill)
        self.assertFalse(ledger.is_spent(bill.serial))
        self.assertEqual(ledger.owner_of(bill.serial), "alice")

    def test_one_note_to_two_counterfeit_trial_tracks_both_candidate_verifications(self):
        import random

        nodes = [QuorumNode(i) for i in range(3)]
        quorum = QuorumService(nodes, threshold=2)
        ledger = Ledger()
        bill = quorum.mint_bill(6, owner="alice", ledger=ledger)
        secret = nodes[0]._secrets[bill.serial]

        trial = one_note_to_two_counterfeit_trial(bill, secret, random.Random(7))

        self.assertEqual(trial.first.measured, 6)
        self.assertEqual(trial.second.measured, 6)
        self.assertEqual(trial.pair_accepted, trial.first.accepted and trial.second.accepted)

    def test_adaptive_replacement_probe_exposes_accept_reject_leakage_for_single_qubit_guess(self):
        nodes = [QuorumNode(i) for i in range(3)]
        quorum = QuorumService(nodes, threshold=2)
        ledger = Ledger()
        bill = quorum.mint_bill(4, owner="alice", ledger=ledger)
        secret = nodes[0]._secrets[bill.serial]

        matching_probe = adaptive_replacement_probe(
            bill,
            secret,
            index=0,
            basis_guess=secret.basis[0],
            bit_guess=secret.bits[0],
            seed=123,
        )
        wrong_bit_probe = adaptive_replacement_probe(
            bill,
            secret,
            index=0,
            basis_guess=secret.basis[0],
            bit_guess=1 - secret.bits[0],
            seed=123,
        )

        self.assertTrue(matching_probe.verification.accepted)
        self.assertFalse(wrong_bit_probe.verification.accepted)


if __name__ == "__main__":
    unittest.main()
