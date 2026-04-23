import math
import unittest

from pubkey_hidden_subspace import (
    HiddenSubspaceMint,
    HiddenSubspaceNote,
    HiddenSubspacePublicKey,
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


if __name__ == "__main__":
    unittest.main()
