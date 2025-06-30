import pathlib

import pytest

from src import main


def test_2_for_file_doesnot_exist(tmp_path: pathlib.Path):
    filepath = tmp_path / "doesnot_exist.json"

    code = main.main(filepath)

    assert code == 2

## homework:start
## homework:end