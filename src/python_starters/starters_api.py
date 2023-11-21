# File: starters_cli.py
"""High level API."""
from cookiecutter.main import cookiecutter

from .convert_templates import save_starter_config


def initialize_starter(template_url: str, save_config: bool = True) -> None:
    """Initialize a starter using a cookiecutter template.

    Args:
    template_url (str): URL of the cookiecutter template repository.
    save_config (bool): Whether to save the user's responses in a config file.
    """
    # Generate project using cookiecutter
    project_dir = cookiecutter(template_url, no_input=False)

    # If save_config is True, save the user's responses
    if save_config:
        save_starter_config(project_dir)


def initialize_project() -> None:
    """Backend logic to initialize the project."""


def add_new_starter(url: str) -> None:
    """Backend logic to add a new starter."""


def update_existing_starter(name: str) -> None:
    """Backend logic to update an existing starter."""


def remove_starter(name: str) -> None:
    """Backend logic to remove a starter."""


def list_all_starters() -> None:
    """Backend logic to list all starters."""


def resolve_starter_conflicts(name: str) -> None:
    """Backend logic to resolve starter conflicts."""
