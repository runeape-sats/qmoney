import math
import unittest

from pubkey_hidden_subspace import (
    AUTHENTIC_CANDIDATE,
    COUNTERFEIT_CANDIDATE,
    DUAL_QUERY,
    HiddenSubspaceMint,
    HiddenSubspaceNote,
    HiddenSubspaceVerifier,
    HiddenSubspacePublicKey,
    OraclePublicationError,
    OracleRegistry,
    SUBSPACE_QUERY,
    basis_state,
    hadamard_transform,
)


class HiddenSubspaceMoneyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mint = HiddenSubspaceMint.from_generators(
            serial="note-1",
            generators=((1, 0, 1), (0, 1, 1)),
        )
        self.public_key = self.mint.public_key
        self.note = self.mint.mint_note()

    def test_mint_note_is_normalized_uniform_superposition_over_subspace(self):
        expected_support = {
            (0, 0, 0),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 0),
        }

        self.assertEqual(set(self.note.support()), expected_support)
        self.assertAlmostEqual(self.note.norm_squared(), 1.0)
        self.assertTrue(self.note.is_uniform_on(expected_support))

    def test_public_verifier_accepts_authentic_hidden_subspace_note(self):
        self.assertTrue(self.public_key.verify(self.note))

    def test_public_verifier_rejects_basis_state_counterfeit_inside_subspace(self):
        counterfeit = basis_state(self.public_key.dimension, (1, 0, 1), serial="note-1")

        self.assertFalse(self.public_key.verify(counterfeit))

    def test_hadamard_image_of_authentic_note_is_uniform_over_dual_subspace(self):
        transformed = hadamard_transform(self.note)
        expected_dual_support = set(self.public_key.dual_vectors)

        self.assertEqual(set(transformed.support()), expected_dual_support)
        self.assertTrue(transformed.is_uniform_on(expected_dual_support))

    def test_public_key_summary_exposes_subspace_and_dual_dimensions(self):
        summary = self.public_key.summary()

        self.assertEqual(summary["serial"], "note-1")
        self.assertEqual(summary["dimension"], 3)
        self.assertEqual(summary["subspace_dimension"], 2)
        self.assertEqual(summary["dual_subspace_dimension"], 1)
        self.assertEqual(len(summary["subspace_vectors"]), 4)
        self.assertEqual(len(summary["dual_subspace_vectors"]), 2)

    def test_public_key_material_currently_allows_reconstruction_of_an_accepting_note(self):
        amplitude = 1.0 / math.sqrt(len(self.public_key.subspace_vectors))
        forged = HiddenSubspaceNote(
            serial=self.public_key.serial,
            dimension=self.public_key.dimension,
            amplitudes={basis: amplitude for basis in self.public_key.subspace_vectors},
        )

        self.assertTrue(self.public_key.verify(forged))

    def test_oracle_registry_requires_publication_before_queries(self):
        registry = OracleRegistry()

        with self.assertRaises(OraclePublicationError):
            registry.query_subspace("note-1", (0, 0, 0), AUTHENTIC_CANDIDATE)

    def test_oracle_registry_logs_subspace_and_dual_queries(self):
        registry = OracleRegistry()
        registry.publish(self.public_key)

        self.assertTrue(registry.query_subspace("note-1", (0, 0, 0), AUTHENTIC_CANDIDATE))
        self.assertFalse(registry.query_dual("note-1", (1, 0, 0), COUNTERFEIT_CANDIDATE))

        self.assertEqual([record.kind for record in registry.query_log], [SUBSPACE_QUERY, DUAL_QUERY])
        self.assertEqual([record.serial for record in registry.query_log], ["note-1", "note-1"])

    def test_oracle_registry_publish_is_idempotent_for_matching_publication(self):
        registry = OracleRegistry()

        first_publication = registry.publish(self.public_key)
        second_publication = registry.publish(self.public_key)

        self.assertIs(first_publication, second_publication)

    def test_oracle_registry_rejects_conflicting_republication_for_same_serial(self):
        registry = OracleRegistry()
        conflicting_public_key = HiddenSubspaceMint.from_generators(
            serial="note-1",
            generators=((1, 0, 0),),
        ).public_key
        registry.publish(self.public_key)

        with self.assertRaises(OraclePublicationError):
            registry.publish(conflicting_public_key)

    def test_oracle_backed_verifier_requires_publication_before_acceptance(self):
        verifier = HiddenSubspaceVerifier(OracleRegistry())

        decision = verifier.verify(self.note, self.public_key)

        self.assertFalse(decision.accepted)
        self.assertEqual(decision.reason, "oracle_not_published")

    def test_oracle_backed_verifier_rejects_publication_mismatch(self):
        registry = OracleRegistry()
        conflicting_public_key = HiddenSubspaceMint.from_generators(
            serial="note-1",
            generators=((1, 0, 0),),
        ).public_key
        registry.publish(conflicting_public_key)
        verifier = HiddenSubspaceVerifier(registry)

        decision = verifier.verify(self.note, self.public_key)

        self.assertFalse(decision.accepted)
        self.assertEqual(decision.reason, "oracle_publication_mismatch")
        self.assertEqual(registry.query_log, ())

    def test_oracle_backed_verifier_accepts_authentic_note_and_logs_queries(self):
        registry = OracleRegistry()
        registry.publish(self.public_key)
        verifier = HiddenSubspaceVerifier(registry)

        decision = verifier.verify(self.note, self.public_key)

        self.assertTrue(decision.accepted)
        self.assertEqual(decision.reason, "accepted")
        self.assertTrue(any(record.kind == SUBSPACE_QUERY for record in registry.query_log))
        self.assertTrue(any(record.kind == DUAL_QUERY for record in registry.query_log))

    def test_oracle_backed_verifier_rejects_basis_state_counterfeit(self):
        registry = OracleRegistry()
        registry.publish(self.public_key)
        verifier = HiddenSubspaceVerifier(registry)
        counterfeit = basis_state(self.public_key.dimension, (1, 0, 1), serial="note-1")

        decision = verifier.verify(counterfeit, self.public_key, candidate_kind=COUNTERFEIT_CANDIDATE)

        self.assertFalse(decision.accepted)
        self.assertEqual(decision.reason, "dual_oracle_rejected")


if __name__ == "__main__":
    unittest.main()
