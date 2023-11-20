"""Test cases for the __main__ module."""
import pytest
from typer.testing import CliRunner

from python_starters.__main__ import app


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(
        app, ["--help"]
    )  # Using "--help" to trigger the CLI without executing a command
    assert result.exit_code == 0


def test_init_command(runner: CliRunner) -> None:
    """Test the init command."""
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    # Add more assertions here based on the expected output
