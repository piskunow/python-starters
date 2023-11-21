"""Test convert templates."""
import json
from unittest.mock import mock_open
from unittest.mock import patch

from python_starters.convert_templates import save_starter_config


def test_save_starter_config():
    """Test save starter config."""
    project_dir = "/path/to/project"

    with patch("os.path.exists", return_value=True), patch(
        "builtins.open", new_callable=mock_open, read_data='{"config_key": "value"}'
    ) as mock_file:
        save_starter_config(project_dir)

        mock_file.assert_called_with("/path/to/project/cookiecutter.json", "r")
        mock_file.assert_called_with("/path/to/project/.startersrc", "w")
        handle = mock_file()
        handle.write.assert_called_once_with(
            json.dumps({"config_key": "value"}, indent=4)
        )
