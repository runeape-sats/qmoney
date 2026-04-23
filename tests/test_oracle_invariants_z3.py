import importlib.util
import sys
import unittest
from pathlib import Path

_MODULE_PATH = Path(__file__).resolve().parent.parent / "z3" / "check_oracle_invariants.py"
_SPEC = importlib.util.spec_from_file_location("qmoney_z3_checker", _MODULE_PATH)
_MODULE = importlib.util.module_from_spec(_SPEC)
assert _SPEC is not None and _SPEC.loader is not None
sys.modules[_SPEC.name] = _MODULE
_SPEC.loader.exec_module(_MODULE)
check_all_invariants = _MODULE.check_all_invariants


class OracleInvariantZ3Tests(unittest.TestCase):
    def test_all_oracle_invariants_are_one_step_stable_for_supported_transitions(self):
        report = check_all_invariants()

        self.assertEqual(report["result"], "all_passed")
        self.assertGreater(len(report["checks"]), 0)
        self.assertTrue(all(check["result"] == "unsat" for check in report["checks"]))

    def test_expected_oracle_invariants_are_covered(self):
        report = check_all_invariants()
        invariant_names = {check["invariant"] for check in report["checks"]}

        self.assertEqual(
            invariant_names,
            {
                "oracle_tables_match_issued",
                "oracle_tables_stay_coupled",
                "queries_only_reference_issued_serials",
                "query_answers_respect_oracle_rule",
            },
        )

    def test_supported_transitions_include_query_and_verification_steps(self):
        report = check_all_invariants()
        transition_names = {check["transition"] for check in report["checks"]}

        self.assertTrue(
            {
                "mint",
                "present_authentic",
                "present_counterfeit",
                "query_subspace_oracle",
                "query_dual_oracle",
                "verify_authentic",
                "reject_counterfeit",
                "noop",
            }.issubset(transition_names)
        )


if __name__ == "__main__":
    unittest.main()
