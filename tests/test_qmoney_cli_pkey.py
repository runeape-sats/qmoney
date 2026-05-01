import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class QMoneyCliPkeyDemoTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "qmoney_cli", *args],
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_pkey_demo_json_contract(self):
        result = self.run_cli("pkey", "demo", "--n", "32", "--forge-trials", "0", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["track"], "pkey_quorum")
        self.assertEqual(payload["command"], "demo")
        self.assertIn("BB84", payload["setup"])
        self.assertEqual(payload["qubits"], 32)
        self.assertTrue(payload["transfer_accepted"])
        self.assertFalse(payload["double_spend_accepted"])
        self.assertIsInstance(payload["new_serial"], str)
        self.assertEqual(payload["forge_trials"], 0)
        self.assertEqual(payload["forge_successes"], 0)

    def test_invalid_threshold_fails_cleanly(self):
        result = self.run_cli("pkey", "demo", "--nodes", "2", "--threshold", "3", "--json")
        self.assertNotEqual(result.returncode, 0)
        text = result.stdout + result.stderr
        self.assertIn("threshold", text)
        self.assertNotIn("Traceback", text)

    def test_noise_probability_rejects_nan(self):
        result = self.run_cli("pkey", "demo", "--noise-bitflip", "nan", "--json")
        self.assertNotEqual(result.returncode, 0)
        text = result.stdout + result.stderr
        self.assertIn("finite probability", text)
        self.assertNotIn("Traceback", text)


if __name__ == "__main__":
    unittest.main()
