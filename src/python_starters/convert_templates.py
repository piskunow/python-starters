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


def track_starter_metadata(
    starter_path: str, template_url: str, commit_hash: str, branch: str
) -> None:
    """Write to `.startersrc` the metadata of the starter."""
    metadata = {
        "template_url": template_url,
        "commit_hash": commit_hash,
        "branch": branch,
    }
    metadata_file = os.path.join(starter_path, ".startersrc")
    with open(metadata_file, "w") as file:
        json.dump(metadata, file, indent=4)
