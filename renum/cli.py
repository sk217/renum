import argparse
import os

from ._renamer import Renamer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input-root",
        required=True,
        help="Path to input root directory.",
    )
    parser.add_argument(
        "-o",
        "--output-root",
        required=True,
        help="Path to output root directory.",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        default="",
        help="Prefix before serial numbers. Defaults to ''.",
    )
    parser.add_argument(
        "-s",
        "--starts",
        default=0,
        type=int,
        help="Starts number. Defaults to 0.",
    )
    parser.add_argument(
        "-d",
        "--digits",
        default=0,
        type=int,
        help="Digits of serial numbers. Defaults to 0."
        "Adjust to the optimal digits by setting to 0.",
    )
    parser.add_argument(
        "-dd",
        "--delimiter",
        default="_",
        help="Delimiter between prefix and serial numbers." "Defaults to '_'.",
    )
    args = parser.parse_args()

    os.makedirs(args.output_root, exist_ok=True)

    renamer = Renamer(
        in_root=args.input_root,
        out_root=args.output_root,
        prefix=args.prefix,
        starts=args.starts,
        digits=args.digits,
        delimiter=args.delimiter,
    )
    renamer.rename()
