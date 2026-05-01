ROOT_DESCRIPTION = """QMoney agentic CLI.

Use this tool to run small, explicit simulations across the repo's separated
tracks: private-key quorum cash, public-key research prototypes, and formal
model checks.
"""

ROOT_EPILOG = """Tracks:
  private-key: current BB84 quorum baseline with hidden verifier secrets.
  public-key: hidden-subspace research prototypes for public verification ideas.
  formal: Z3/TLC models for invariants and protocol-state exploration.

Examples:
  qmoney pkey demo --n 32 --forge-trials 0 --json
  qmoney pubkey --help
  qmoney formal --help
"""

PKEY_DESCRIPTION = """Private-key QMoney track.

This is the current quorum-verified BB84 baseline. It uses consumptive verification:
verifier nodes measure the submitted bill using hidden basis/bit secrets, the old
serial is spent, and success remints a fresh bill for the receiver.
"""

PKEY_EPILOG = """Examples:
  qmoney pkey demo --n 32 --forge-trials 0 --json
"""

PUBKEY_DESCRIPTION = """Public-key QMoney research track.

research-only caveat: this repo's hidden-subspace code is a conceptual public
verification prototype, not a deployable public-key quantum money system and not
a production transaction layer.
"""

PUBKEY_EPILOG = """Examples:
  qmoney pubkey --help
"""

FORMAL_DESCRIPTION = """Formal methods track.

Z3 checks local invariants and satisfiability-style properties of verifier
logic. TLC (the TLA+ model checker) explores protocol state machines, traces,
and temporal properties. They have complementary roles: Z3 is for logical
constraints; TLC is for transition-system behavior.
"""

FORMAL_EPILOG = """Examples:
  qmoney formal --help
"""

PKEY_DEMO_DESCRIPTION = """Run the private-key quorum demo.

The demo mints a BB84 symbolic bill, performs an alice-to-bob transfer through a
private verifier quorum, demonstrates that a second spend of the consumed serial
is rejected, and optionally runs intercept/resend forge trials.
"""

PKEY_DEMO_EPILOG = """Examples:
  qmoney pkey demo --n 32 --forge-trials 0 --json
  qmoney pkey demo --n 128 --nodes 4 --threshold 3 --json --pretty

Output contract:
  JSON fields: track, command, setup, qubits, transfer_accepted,
  double_spend_accepted, new_serial, forge_trials, forge_successes.
"""
