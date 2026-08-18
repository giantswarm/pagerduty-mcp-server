"""Import-level checks for the server entrypoint.

The rest of the suite imports `pagerduty_mcp.tools` and `pagerduty_mcp.models`
directly and never reaches `pagerduty_mcp.server`, so a dependency whose API
moved is invisible to it while the container fails on startup.
"""

import importlib


def test_server_module_imports():
    """The server module imports and exposes the Typer app."""
    module = importlib.import_module("pagerduty_mcp.server")

    assert module.app is not None


def test_main_module_imports():
    """The console-script entrypoint imports and is callable."""
    module = importlib.import_module("pagerduty_mcp.__main__")

    assert callable(module.main)


def test_cli_help_lists_run_command():
    """The CLI builds far enough to render its own help."""
    from typer.testing import CliRunner

    from pagerduty_mcp.server import app

    result = CliRunner().invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "run" in result.stdout
