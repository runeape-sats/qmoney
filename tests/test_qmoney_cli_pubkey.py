import io
import json
import unittest

from qmoney_cli.output import dumps_json, to_jsonable
from qmoney_cli.parsers import parse_basis_vector, parse_generators


class QMoneyCliParserTests(unittest.TestCase):
    def test_parse_generators_returns_tuple_of_bit_tuples(self):
        self.assertEqual(parse_generators("101,011"), ((1, 0, 1), (0, 1, 1)))

    def test_parse_generators_rejects_empty(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            parse_generators("")

    def test_parse_generators_rejects_inconsistent_lengths(self):
        with self.assertRaisesRegex(ValueError, "same length"):
            parse_generators("101,01")

    def test_parse_generators_rejects_non_binary_characters(self):
        with self.assertRaisesRegex(ValueError, "binary"):
            parse_generators("101,02A")

    def test_parse_basis_vector_returns_bit_tuple(self):
        self.assertEqual(parse_basis_vector("101"), (1, 0, 1))

    def test_parse_basis_vector_rejects_empty_and_non_binary(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            parse_basis_vector("")
        with self.assertRaisesRegex(ValueError, "binary"):
            parse_basis_vector("10x")

    def test_output_helper_compacts_bit_vectors_and_emits_json(self):
        payload = {
            "basis": (1, 0, 1),
            "generators": ((1, 0, 1), (0, 1, 1)),
            "mixed": [1, 2, 3],
        }
        self.assertEqual(
            to_jsonable(payload),
            {"basis": "101", "generators": ["101", "011"], "mixed": [1, 2, 3]},
        )
        self.assertEqual(json.loads(dumps_json(payload))["basis"], "101")


if __name__ == "__main__":
    unittest.main()
