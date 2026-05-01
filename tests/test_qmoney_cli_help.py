import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class QMoneyCliHelpTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "qmoney_cli", *args],
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def assert_help_contains(self, args, *needles):
        result = self.run_cli(*args, "--help")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = result.stdout + result.stderr
        for needle in needles:
            self.assertIn(needle, text)

    def test_python_module_help_imports_and_explains_tracks(self):
        self.assert_help_contains((), "private-key", "public-key", "formal", "Examples:")

    def test_track_help_explains_roles_and_caveats(self):
        self.assert_help_contains(("pkey",), "consumptive verification")
        self.assert_help_contains(("pubkey",), "research-only")
        self.assert_help_contains(("formal",), "Z3", "TLC")

    def test_track_without_leaf_prints_track_help(self):
        result = self.run_cli("pkey")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("consumptive verification", result.stdout)
        self.assertNotIn("Tracks:\n  private-key:", result.stdout)

    def test_leaf_help_has_examples_and_output_contract(self):
        self.assert_help_contains(("pkey", "demo"), "Examples:", "Output contract:")


if __name__ == "__main__":
    unittest.main()
