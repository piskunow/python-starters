"""Convert Cookiecutter templates to starters."""
import json
import os


def save_starter_config(project_dir: str) -> None:
    """Save the starter configuration in a .startersrc file.

    Args:
    project_dir (str): Directory of the generated project.
    """
    config_file = os.path.join(project_dir, "cookiecutter.json")
    output_file = os.path.join(project_dir, ".startersrc")

    if os.path.exists(config_file):
        with open(config_file) as infile:
            config_data = json.load(infile)

        with open(output_file, "w") as outfile:
            json.dump(config_data, outfile, indent=4)
