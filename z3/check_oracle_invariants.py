from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Callable, Dict, List

from z3 import And, Bool, BoolVal, If, Implies, Int, Not, Or, Solver, sat


NOTE_UNISSUED = 0
NOTE_AUTHENTIC = 1
NOTE_COUNTERFEIT = 2
NOTE_ACCEPTED = 3
NOTE_REJECTED = 4

OUTCOME_IDLE = 0
OUTCOME_ACCEPT = 1
OUTCOME_REJECT = 2

CANDIDATE_AUTHENTIC = 0
CANDIDATE_COUNTERFEIT = 1

KIND_SUBSPACE = 0
KIND_DUAL = 1


@dataclass(frozen=True)
class SymbolicState:
    issued: object
    note_state: object
    verifier_outcome: object
    subspace_published: object
    dual_published: object
    query_log_len: object
    queries_only_reference_issued: object
    query_answers_respect_rule: object
    subspace_queries_tagged_correctly: object
    dual_queries_tagged_correctly: object


@dataclass(frozen=True)
class TransitionSpec:
    name: str
    formula_builder: Callable[[SymbolicState, SymbolicState], object]


def _state(prefix: str) -> SymbolicState:
    return SymbolicState(
        issued=Bool(f"{prefix}_issued"),
        note_state=Int(f"{prefix}_note_state"),
        verifier_outcome=Int(f"{prefix}_verifier_outcome"),
        subspace_published=Bool(f"{prefix}_subspace_published"),
        dual_published=Bool(f"{prefix}_dual_published"),
        query_log_len=Int(f"{prefix}_query_log_len"),
        queries_only_reference_issued=Bool(f"{prefix}_queries_only_reference_issued"),
        query_answers_respect_rule=Bool(f"{prefix}_query_answers_respect_rule"),
        subspace_queries_tagged_correctly=Bool(f"{prefix}_subspace_queries_tagged_correctly"),
        dual_queries_tagged_correctly=Bool(f"{prefix}_dual_queries_tagged_correctly"),
    )


def type_ok(state: SymbolicState):
    return And(
        state.note_state >= NOTE_UNISSUED,
        state.note_state <= NOTE_REJECTED,
        state.verifier_outcome >= OUTCOME_IDLE,
        state.verifier_outcome <= OUTCOME_REJECT,
        state.query_log_len >= 0,
    )


def oracle_tables_match_issued(state: SymbolicState):
    return And(
        state.subspace_published == state.issued,
        state.dual_published == state.issued,
    )


def oracle_tables_stay_coupled(state: SymbolicState):
    return state.subspace_published == state.dual_published


def queries_only_reference_issued_serials(state: SymbolicState):
    return state.queries_only_reference_issued


def query_answers_respect_oracle_rule(state: SymbolicState):
    return state.query_answers_respect_rule


INVARIANTS: Dict[str, Callable[[SymbolicState], object]] = {
    "oracle_tables_match_issued": oracle_tables_match_issued,
    "oracle_tables_stay_coupled": oracle_tables_stay_coupled,
    "queries_only_reference_issued_serials": queries_only_reference_issued_serials,
    "query_answers_respect_oracle_rule": query_answers_respect_oracle_rule,
}


def _unchanged_except(pre: SymbolicState, post: SymbolicState, *field_names: str):
    changed = set(field_names)
    clauses = []
    for field in pre.__dataclass_fields__:
        if field not in changed:
            clauses.append(getattr(post, field) == getattr(pre, field))
    return And(*clauses) if clauses else BoolVal(True)


def mint_transition(pre: SymbolicState, post: SymbolicState):
    return And(
        Not(pre.issued),
        post.issued,
        post.note_state == NOTE_AUTHENTIC,
        post.verifier_outcome == OUTCOME_IDLE,
        post.subspace_published,
        post.dual_published,
        post.query_log_len == pre.query_log_len,
        post.queries_only_reference_issued == pre.queries_only_reference_issued,
        post.query_answers_respect_rule == pre.query_answers_respect_rule,
        post.subspace_queries_tagged_correctly == pre.subspace_queries_tagged_correctly,
        post.dual_queries_tagged_correctly == pre.dual_queries_tagged_correctly,
    )


def present_authentic_transition(pre: SymbolicState, post: SymbolicState):
    return And(
        pre.issued,
        Or(pre.note_state == NOTE_AUTHENTIC, pre.note_state == NOTE_ACCEPTED, pre.note_state == NOTE_REJECTED),
        _unchanged_except(pre, post, "note_state", "verifier_outcome"),
        post.note_state == NOTE_AUTHENTIC,
        post.verifier_outcome == OUTCOME_IDLE,
    )


def present_counterfeit_transition(pre: SymbolicState, post: SymbolicState):
    return And(
        pre.issued,
        Or(pre.note_state == NOTE_AUTHENTIC, pre.note_state == NOTE_ACCEPTED, pre.note_state == NOTE_REJECTED),
        _unchanged_except(pre, post, "note_state", "verifier_outcome"),
        post.note_state == NOTE_COUNTERFEIT,
        post.verifier_outcome == OUTCOME_IDLE,
    )


def _query_transition(pre: SymbolicState, post: SymbolicState, *, query_kind: int):
    candidate_kind = Int(f"candidate_kind_{query_kind}")
    serial_is_published = pre.subspace_published if query_kind == KIND_SUBSPACE else pre.dual_published
    return And(
        serial_is_published,
        Or(candidate_kind == CANDIDATE_AUTHENTIC, candidate_kind == CANDIDATE_COUNTERFEIT),
        pre.query_log_len < 2,
        _unchanged_except(
            pre,
            post,
            "query_log_len",
            "queries_only_reference_issued",
            "query_answers_respect_rule",
            "subspace_queries_tagged_correctly",
            "dual_queries_tagged_correctly",
        ),
        post.query_log_len == pre.query_log_len + 1,
        post.queries_only_reference_issued == And(pre.queries_only_reference_issued, pre.issued),
        post.query_answers_respect_rule == pre.query_answers_respect_rule,
        post.subspace_queries_tagged_correctly
        == And(pre.subspace_queries_tagged_correctly, If(query_kind == KIND_SUBSPACE, pre.subspace_published, BoolVal(True))),
        post.dual_queries_tagged_correctly
        == And(pre.dual_queries_tagged_correctly, If(query_kind == KIND_DUAL, pre.dual_published, BoolVal(True))),
    )


def query_subspace_oracle_transition(pre: SymbolicState, post: SymbolicState):
    return _query_transition(pre, post, query_kind=KIND_SUBSPACE)


def query_dual_oracle_transition(pre: SymbolicState, post: SymbolicState):
    return _query_transition(pre, post, query_kind=KIND_DUAL)


def verify_authentic_transition(pre: SymbolicState, post: SymbolicState):
    return And(
        pre.issued,
        pre.subspace_published,
        pre.dual_published,
        pre.note_state == NOTE_AUTHENTIC,
        _unchanged_except(pre, post, "note_state", "verifier_outcome"),
        post.note_state == NOTE_ACCEPTED,
        post.verifier_outcome == OUTCOME_ACCEPT,
    )


def reject_counterfeit_transition(pre: SymbolicState, post: SymbolicState):
    return And(
        pre.issued,
        pre.subspace_published,
        pre.dual_published,
        pre.note_state == NOTE_COUNTERFEIT,
        _unchanged_except(pre, post, "note_state", "verifier_outcome"),
        post.note_state == NOTE_REJECTED,
        post.verifier_outcome == OUTCOME_REJECT,
    )


def noop_transition(pre: SymbolicState, post: SymbolicState):
    return And(*[getattr(post, field) == getattr(pre, field) for field in pre.__dataclass_fields__])


TRANSITIONS = [
    TransitionSpec("mint", mint_transition),
    TransitionSpec("present_authentic", present_authentic_transition),
    TransitionSpec("present_counterfeit", present_counterfeit_transition),
    TransitionSpec("query_subspace_oracle", query_subspace_oracle_transition),
    TransitionSpec("query_dual_oracle", query_dual_oracle_transition),
    TransitionSpec("verify_authentic", verify_authentic_transition),
    TransitionSpec("reject_counterfeit", reject_counterfeit_transition),
    TransitionSpec("noop", noop_transition),
]


def _base_solver_for_transition(pre: SymbolicState, post: SymbolicState, transition: TransitionSpec) -> Solver:
    solver = Solver()
    solver.add(type_ok(pre), type_ok(post))
    for invariant in INVARIANTS.values():
        solver.add(invariant(pre))
    solver.add(transition.formula_builder(pre, post))
    return solver


def check_all_invariants() -> dict:
    report_checks: List[dict] = []
    pre = _state("pre")
    post = _state("post")
    overall_ok = True

    for transition in TRANSITIONS:
        for invariant_name, invariant in INVARIANTS.items():
            solver = _base_solver_for_transition(pre, post, transition)
            solver.add(Not(invariant(post)))
            result = solver.check()
            result_str = str(result)
            entry = {
                "transition": transition.name,
                "invariant": invariant_name,
                "result": result_str,
            }
            if result == sat:
                overall_ok = False
                entry["counterexample"] = solver.model().sexpr()
            report_checks.append(entry)

    return {
        "result": "all_passed" if overall_ok else "violations_found",
        "checks": report_checks,
    }


if __name__ == "__main__":
    print(json.dumps(check_all_invariants(), indent=2))
