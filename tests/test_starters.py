"""Test starters API."""
import json
from unittest.mock import mock_open
from unittest.mock import patch

from python_starters.starters_api import initialize_starter
from python_starters.starters_api import update_starter


def test_initialize_starter():
    """Test init starter."""
    template_url = "https://example.com/cookiecutter-repo.git"

    with patch("python_starters.starters_api.cookiecutter") as mock_cookiecutter, patch(
        "python_starters.starters_api.save_starter_config"
    ) as mock_save_config:
        initialize_starter(template_url)

        mock_cookiecutter.assert_called_once_with(template_url, no_input=False)
        mock_save_config.assert_called_once()


def test_update_starter():
    """Test update starter."""
    starter_path = "/path/to/starter"
    metadata = {
        "template_url": "https://example.com/cookiecutter-repo.git",
        "commit_hash": "abcdef1234567890",
        "branch": "main",
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(metadata))), patch(
        "subprocess.run"
    ) as mock_run:
        update_starter(starter_path)

        mock_run.assert_called_once_with(
            [
                "git",
                "subtree",
                "pull",
                "--prefix",
                starter_path,
                metadata["template_url"],
                metadata["branch"],
                "--squash",
            ],
            check=True,
        )
