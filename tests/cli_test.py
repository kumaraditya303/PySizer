# -*- coding: utf-8 -*-
import os

import pytest
from click.testing import CliRunner
from PIL import Image

from pysizer import main
from pysizer.cli import resize


@pytest.fixture
def runner():
    yield CliRunner()


def test_main(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("test.jpg", "w+b") as f:
            Image.new("RGB", (100, 100), (150, 0, 0)).save(f)
        result = runner.invoke(main)
        assert result.exit_code == 0
        assert "1 pictures resized in" in result.output
        assert len(os.listdir("resized")) == 1


def test_main_recursive(runner: CliRunner):
    with runner.isolated_filesystem():
        os.mkdir("test")
        with open(os.path.join("test", "testing.jpg"), "w+") as f:
            Image.new("RGB", (100, 100), (150, 0, 0)).save(f)
        result = runner.invoke(main, "-r")
        assert result.exit_code == 0
        assert "1 pictures resized in" in result.output
        assert len(os.listdir("resized")) == 1


def test_main_fail(runner: CliRunner):
    with runner.isolated_filesystem():
        result = runner.invoke(main)
        assert result.exit_code == 0
        assert "No pictures found!" in result.output


def test_resize(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("test.jpg", "w+b") as f:
            Image.new("RGB", (100, 100), (150, 0, 0)).save(f)
            os.mkdir("resized")
            resize("test.jpg", "resized", (1920, 1080))
            assert len(os.listdir("resized")) == 1
