import argparse
import os

from termcolor import cprint

from ._renamer import Renamer

LOGO = r"""
   ____    U _____ u _   _       _   _   __  __
U |  _"\ u \| ___"|/| \ |"|   U |"|u| |U|' \/ '|u
 \| |_) |/  |  _|" <|  \| |>   \| |\| |\| |\/| |/
  |  _ <    | |___ U| |\  |u    | |_| | | |  | |
  |_| \_\   |_____| |_| \_|    <<\___/  |_|  |_|
  //   \\_  <<   >> ||   \\,-.(__) )(  <<,-,,-.
 (__)  (__)(__) (__)(_")  (_/     (__)  (./  \.)
"""

cprint(LOGO, color="magenta")


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
    parser.add_argument(
        "-od", "--dir-only", action="store_true", help="Rename dir only."
    )
    parser.add_argument(
        "-of", "--file-only", action="store_true", help="Rename file only."
    )
    args = parser.parse_args()

    if args.dir_only and args.file_only:
        parser.error(
            "'--dir-only' and '--file-only' cannot be used at the same time."
        )
    os.makedirs(args.output_root, exist_ok=True)

    if args.dir_only:
        restriction = "dir"
    elif args.file_only:
        restriction = "file"
    else:
        restriction = None

    renamer = Renamer(
        in_root=args.input_root,
        out_root=args.output_root,
        prefix=args.prefix,
        starts=args.starts,
        digits=args.digits,
        delimiter=args.delimiter,
        restriction=restriction,
    )
    renamer.rename()
