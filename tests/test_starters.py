"""Test starters API."""
from unittest.mock import patch

from python_starters.starters_api import initialize_starter


def test_initialize_starter():
    """Test init starter."""
    template_url = "https://example.com/cookiecutter-repo.git"

    with patch("python_starters.starters_api.cookiecutter") as mock_cookiecutter, patch(
        "python_starters.starters_api.save_starter_config"
    ) as mock_save_config:
        initialize_starter(template_url)

        mock_cookiecutter.assert_called_once_with(template_url, no_input=False)
        mock_save_config.assert_called_once()
