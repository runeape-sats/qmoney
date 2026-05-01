from __future__ import annotations

import argparse
import sys

from pkey_quorum.demo import DEFAULT_QUBITS, SUPPORTED_QUBIT_COUNTS

from . import helptext
from .commands.pkey import nonnegative_int, positive_int, probability, render_text, run_demo
from .output import dumps_json


class QMoneyArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        self.print_usage(sys.stderr)
        self.exit(2, f"{self.prog}: error: {message}\n")


def build_parser() -> argparse.ArgumentParser:
    parser = QMoneyArgumentParser(
        prog="qmoney",
        description=helptext.ROOT_DESCRIPTION,
        epilog=helptext.ROOT_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="track", metavar="TRACK")

    pkey = subparsers.add_parser(
        "pkey",
        aliases=["private-key"],
        help="private-key quorum simulator commands",
        description=helptext.PKEY_DESCRIPTION,
        epilog=helptext.PKEY_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    pkey.set_defaults(func=print_help)
    pkey_subparsers = pkey.add_subparsers(dest="pkey_command", metavar="COMMAND")

    demo = pkey_subparsers.add_parser(
        "demo",
        help="run the private-key quorum demo",
        description=helptext.PKEY_DEMO_DESCRIPTION,
        epilog=helptext.PKEY_DEMO_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    demo.add_argument("--n", type=int, default=DEFAULT_QUBITS, choices=SUPPORTED_QUBIT_COUNTS, help="number of BB84 qubits per bill")
    demo.add_argument("--nodes", type=positive_int, default=4, help="quorum node count N")
    demo.add_argument("--threshold", type=positive_int, default=3, help="minimum live participants required")
    demo.add_argument("--tolerance", type=nonnegative_int, default=0, help="allowed mismatches")
    demo.add_argument("--noise-bitflip", type=probability, default=0.0, help="bit-flip probability per measured qubit")
    demo.add_argument("--seed", type=int, default=123, help="RNG seed for reproducible demo")
    demo.add_argument("--forge-trials", type=nonnegative_int, default=0, help="run intercept/resend forge trials")
    demo.add_argument("--json", action="store_true", help="emit compact JSON")
    demo.add_argument("--pretty", action="store_true", help="pretty-print JSON when used with --json")
    demo.set_defaults(func=handle_pkey_demo)

    pubkey = subparsers.add_parser(
        "pubkey",
        aliases=["public-key"],
        help="public-key hidden-subspace research commands",
        description=helptext.PUBKEY_DESCRIPTION,
        epilog=helptext.PUBKEY_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    pubkey.set_defaults(func=print_help)

    formal = subparsers.add_parser(
        "formal",
        help="formal model checking commands",
        description=helptext.FORMAL_DESCRIPTION,
        epilog=helptext.FORMAL_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    formal.set_defaults(func=print_help)

    parser.set_defaults(func=print_help)
    return parser


def print_help(args: argparse.Namespace) -> int:
    # argparse stores the parser object only for explicit defaults we set below.
    args._parser.print_help()
    return 0


def handle_pkey_demo(args: argparse.Namespace) -> int:
    try:
        payload = run_demo(args)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if args.json:
        sys.stdout.write(dumps_json(payload, pretty=args.pretty))
    else:
        sys.stdout.write(render_text(payload))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args._parser = parser
    # If a subparser was selected, attach that parser for help-only skeletons.
    subparser_choices = next(action for action in parser._actions if isinstance(action, argparse._SubParsersAction)).choices
    if args.track in ("pkey", "private-key") and getattr(args, "pkey_command", None) is None:
        args._parser = subparser_choices[args.track]
    elif args.track in ("pubkey", "public-key"):
        args._parser = subparser_choices[args.track]
    elif args.track == "formal":
        args._parser = subparser_choices["formal"]
    try:
        return args.func(args)
    except argparse.ArgumentTypeError as exc:
        parser.exit(2, f"qmoney: error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
