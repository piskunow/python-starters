"""Test convert templates."""
from unittest.mock import mock_open
from unittest.mock import patch

from python_starters.convert_templates import save_starter_config


def test_save_starter_config():
    """Test save starter config."""
    project_dir = "/path/to/project"

    # Set up the mock to return a specific content when a specific file is read
    mock_file_read = mock_open(read_data='{"config_key": "value"}')
    with patch("os.path.exists", return_value=True), patch(
        "builtins.open", mock_file_read, create=True
    ) as mock_file:
        save_starter_config(project_dir)

        # Check if cookiecutter.json was read
        mock_file.assert_any_call("/path/to/project/cookiecutter.json")

        # Check if .startersrc was written
        mock_file.assert_called_with("/path/to/project/.startersrc", "w")
