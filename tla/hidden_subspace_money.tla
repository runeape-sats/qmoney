---- MODULE hidden_subspace_money ----
EXTENDS Naturals, Sequences

(***************************************************************************)
(* This spec remains intentionally abstract: it does not model amplitudes   *)
(* or the full hidden-subspace mathematics. It now models oracle-facing     *)
(* invariants explicitly by tracking oracle publication and query answers.   *)
(***************************************************************************)

CONSTANT Serials, MaxQueries

NoteStates == {"unissued", "authentic", "counterfeit", "accepted", "rejected"}
VerifierOutcomes == {"idle", "accept", "reject"}
QueryKinds == {"subspace", "dual"}
CandidateKinds == {"authenticCandidate", "counterfeitCandidate"}
QueryRecord == [serial : Serials, kind : QueryKinds, candidateKind : CandidateKinds, answer : BOOLEAN]

OracleAnswer(candidateKind) == candidateKind = "authenticCandidate"

VARIABLES issued, noteState, verifierOutcome, subspaceOraclePublished, dualOraclePublished, oracleQueryLog

vars == <<issued, noteState, verifierOutcome, subspaceOraclePublished, dualOraclePublished, oracleQueryLog>>

Init ==
    /\ issued = {}
    /\ noteState = [s \in Serials |-> "unissued"]
    /\ verifierOutcome = "idle"
    /\ subspaceOraclePublished = {}
    /\ dualOraclePublished = {}
    /\ oracleQueryLog = <<>>

Mint(s) ==
    /\ s \in Serials \ issued
    /\ issued' = issued \cup {s}
    /\ noteState' = [noteState EXCEPT ![s] = "authentic"]
    /\ verifierOutcome' = "idle"
    /\ subspaceOraclePublished' = subspaceOraclePublished \cup {s}
    /\ dualOraclePublished' = dualOraclePublished \cup {s}
    /\ UNCHANGED oracleQueryLog

PresentAuthentic(s) ==
    /\ s \in issued
    /\ noteState[s] \in {"authentic", "accepted", "rejected"}
    /\ issued' = issued
    /\ noteState' = [noteState EXCEPT ![s] = "authentic"]
    /\ verifierOutcome' = "idle"
    /\ UNCHANGED <<subspaceOraclePublished, dualOraclePublished, oracleQueryLog>>

PresentCounterfeit(s) ==
    /\ s \in issued
    /\ noteState[s] \in {"authentic", "accepted", "rejected"}
    /\ issued' = issued
    /\ noteState' = [noteState EXCEPT ![s] = "counterfeit"]
    /\ verifierOutcome' = "idle"
    /\ UNCHANGED <<subspaceOraclePublished, dualOraclePublished, oracleQueryLog>>

QuerySubspaceOracle(s, candidateKind) ==
    /\ s \in subspaceOraclePublished
    /\ candidateKind \in CandidateKinds
    /\ Len(oracleQueryLog) < MaxQueries
    /\ issued' = issued
    /\ noteState' = noteState
    /\ verifierOutcome' = verifierOutcome
    /\ subspaceOraclePublished' = subspaceOraclePublished
    /\ dualOraclePublished' = dualOraclePublished
    /\ oracleQueryLog' = Append(oracleQueryLog, [serial |-> s, kind |-> "subspace", candidateKind |-> candidateKind, answer |-> OracleAnswer(candidateKind)])

QueryDualOracle(s, candidateKind) ==
    /\ s \in dualOraclePublished
    /\ candidateKind \in CandidateKinds
    /\ Len(oracleQueryLog) < MaxQueries
    /\ issued' = issued
    /\ noteState' = noteState
    /\ verifierOutcome' = verifierOutcome
    /\ subspaceOraclePublished' = subspaceOraclePublished
    /\ dualOraclePublished' = dualOraclePublished
    /\ oracleQueryLog' = Append(oracleQueryLog, [serial |-> s, kind |-> "dual", candidateKind |-> candidateKind, answer |-> OracleAnswer(candidateKind)])

VerifyAuthentic(s) ==
    /\ s \in issued
    /\ s \in subspaceOraclePublished
    /\ s \in dualOraclePublished
    /\ noteState[s] = "authentic"
    /\ issued' = issued
    /\ noteState' = [noteState EXCEPT ![s] = "accepted"]
    /\ verifierOutcome' = "accept"
    /\ UNCHANGED <<subspaceOraclePublished, dualOraclePublished, oracleQueryLog>>

RejectCounterfeit(s) ==
    /\ s \in issued
    /\ s \in subspaceOraclePublished
    /\ s \in dualOraclePublished
    /\ noteState[s] = "counterfeit"
    /\ issued' = issued
    /\ noteState' = [noteState EXCEPT ![s] = "rejected"]
    /\ verifierOutcome' = "reject"
    /\ UNCHANGED <<subspaceOraclePublished, dualOraclePublished, oracleQueryLog>>

NoOp ==
    /\ UNCHANGED vars

Next ==
    \/ (\E s \in Serials: Mint(s))
    \/ (\E s \in Serials: PresentAuthentic(s))
    \/ (\E s \in Serials: PresentCounterfeit(s))
    \/ (\E s \in Serials: VerifyAuthentic(s))
    \/ (\E s \in Serials: RejectCounterfeit(s))
    \/ (\E s \in Serials: \E candidateKind \in CandidateKinds: QuerySubspaceOracle(s, candidateKind))
    \/ (\E s \in Serials: \E candidateKind \in CandidateKinds: QueryDualOracle(s, candidateKind))
    \/ NoOp

TypeOK ==
    /\ issued \subseteq Serials
    /\ noteState \in [Serials -> NoteStates]
    /\ verifierOutcome \in VerifierOutcomes
    /\ subspaceOraclePublished \subseteq Serials
    /\ dualOraclePublished \subseteq Serials
    /\ oracleQueryLog \in Seq(QueryRecord)
    /\ MaxQueries \in Nat

AuthenticImpliesIssued ==
    \A s \in Serials:
        noteState[s] \in {"authentic", "accepted", "counterfeit", "rejected"} => s \in issued

AcceptImpliesAcceptedState ==
    verifierOutcome = "accept" => \E s \in Serials: noteState[s] = "accepted"

RejectImpliesRejectedState ==
    verifierOutcome = "reject" => \E s \in Serials: noteState[s] = "rejected"

OracleTablesMatchIssued ==
    /\ subspaceOraclePublished = issued
    /\ dualOraclePublished = issued

OracleTablesStayCoupled ==
    subspaceOraclePublished = dualOraclePublished

QueriesOnlyReferenceIssuedSerials ==
    \A i \in 1..Len(oracleQueryLog): oracleQueryLog[i].serial \in issued

QueryAnswersRespectOracleRule ==
    \A i \in 1..Len(oracleQueryLog):
        oracleQueryLog[i].answer = OracleAnswer(oracleQueryLog[i].candidateKind)

SubspaceQueriesTaggedCorrectly ==
    \A i \in 1..Len(oracleQueryLog):
        oracleQueryLog[i].kind = "subspace" => oracleQueryLog[i].serial \in subspaceOraclePublished

DualQueriesTaggedCorrectly ==
    \A i \in 1..Len(oracleQueryLog):
        oracleQueryLog[i].kind = "dual" => oracleQueryLog[i].serial \in dualOraclePublished

Spec == Init /\ [][Next]_vars

THEOREM Spec => []TypeOK
====
