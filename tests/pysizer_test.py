import pytest
from click.testing import CliRunner
from PIL import Image
from pysizer import main
from pysizer.pysizer import resize


@pytest.fixture
def runner():
    yield CliRunner()


def test_pysizer_main(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("test.jpg", "w") as f:
            Image.new("RGB", (100, 100), (150, 0, 0)).save(f)
        result = runner.invoke(main)
        assert result.exit_code == 0
        assert "Picture resizing took" in result.output


def test_pysizer_main_fail(runner: CliRunner):
    with runner.isolated_filesystem():
        result = runner.invoke(main)
        assert result.exit_code == 0
        assert "No pictures found!" in result.output


def test_pysizer_resize(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("test.jpg", "w") as f:
            Image.new("RGB", (100, 100), (150, 0, 0)).save(f)
            resize("test.jpg", ".", 1920, 1080)
