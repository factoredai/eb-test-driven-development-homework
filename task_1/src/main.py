import pathlib
from collections.abc import Iterator

from src import parser, lexer


def main(file: pathlib.Path) -> int:
    ## homework:start
    ## homework:end


def _cli() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=pathlib.Path)
    args = parser.parse_args()
    code = main(args.file)
    sys.exit(code)


if __name__ == "__main__":
    _cli()
