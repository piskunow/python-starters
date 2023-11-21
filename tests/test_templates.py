"""Test convert templates."""
import json
from unittest.mock import mock_open
from unittest.mock import patch

from python_starters.convert_templates import track_starter_metadata
from python_starters.starters_api import initialize_starter
from python_starters.starters_api import save_starter_config


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


def test_initialize_starter_calls_cookiecutter():
    """Test that cookiecutter is called."""
    template_url = "https://example.com/cookiecutter-repo.git"

    with patch("python_starters.starters_api.cookiecutter") as mock_cookiecutter:
        initialize_starter(template_url)

        mock_cookiecutter.assert_called_once_with(template_url, no_input=False)


def test_track_starter_metadata():
    """Test tracking starter metadata."""
    starter_path = "/path/to/starter"
    template_url = "https://example.com/cookiecutter-repo.git"
    commit_hash = "abcdef1234567890"
    branch = "main"

    expected_content = json.dumps(
        {"template_url": template_url, "commit_hash": commit_hash, "branch": branch},
        indent=4,
    )

    with patch("builtins.open", mock_open()) as mock_file:
        track_starter_metadata(starter_path, template_url, commit_hash, branch)

        mock_file.assert_called_once_with(f"{starter_path}/.startersrc", "w")

        # Check the content written to the file
        written_content = "".join(
            [call.args[0] for call in mock_file().write.mock_calls]
        )
        assert written_content == expected_content
