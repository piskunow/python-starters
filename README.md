# Python Starters

[![PyPI](https://img.shields.io/pypi/v/python-starters.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/python-starters.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/python-starters)][python version]
[![License](https://img.shields.io/pypi/l/python-starters)][license]

[![Read the documentation at https://python-starters.readthedocs.io/](https://img.shields.io/readthedocs/python-starters/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/piskunow/python-starters/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/piskunow/python-starters/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/python-starters/
[status]: https://pypi.org/project/python-starters/
[python version]: https://pypi.org/project/python-starters
[read the docs]: https://python-starters.readthedocs.io/
[tests]: https://github.com/piskunow/python-starters/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/piskunow/python-starters
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

# 🚀 Python Starters Documentation

Welcome to the Python Starters documentation! Python Starters is a tool designed to streamline the process of initializing, managing, and updating project starters based on cookiecutter templates. This tool simplifies Git operations, specifically working with subtrees and submodules, and provides a user-friendly interface for project scaffolding.

## 📦 Installation

To install Python Starters via [pip] from [PyPI], run the following command:

```bash
pip install python-starters
```

This will install _Python Starters_

Ensure you have Git installed on your system, as Python Starters relies on Git for version control of starters.

## 🛠️ Quick Start

To quickly start using Python Starters, follow these steps:

1. Initialize your project:

```bash
python-starters init
```

2. Add a starter to your project:

```bash
python-starters add <starter_git_url>
```

3. Customize your starter as needed and enjoy streamlined project setup!

## 🌟 Basic Usage

Python Starters simplifies the process of working with project starters. Below are the basic commands:

- **Initializing Python Starters**:

  ```bash
  python-starters init
  ```

- **Adding a Starter**:

  ```bash
  python-starters add <starter_git_url>
  ```

- **Updating a Starter**:

  ```bash
  python-starters update <starter_name>
  ```

- **Removing a Starter**:

  ```bash
  python-starters remove <starter_name>
  ```

## ⚙️ Advanced Usage

For advanced usage of Python Starters, consider the following commands:

- **Resolving Merge Conflicts**:

  ```bash
  python-starters resolve <starter_name>
  ```

- **Listing All Starters**:

  ```bash
  python-starters list
  ```

- **Customizing Starters**:

  Customize your starter by editing the generated configuration files. Python Starters will respect these customizations during updates.

Please see the [Command-line Reference] for details.

## 📘 API Reference

Python Starters also provides an API for programmatic access to its functionalities. Below is the reference for the API:

- **`initialize_project()`**:
  Initializes Python Starters in the current project.

- **`add_new_starter(starter_git_url: str)`**:
  Adds a new starter to the project from the given Git URL.

- **`update_existing_starter(starter_name: str)`**:
  Updates the specified starter to its latest version.

- **`remove_starter(starter_name: str)`**:
  Removes the specified starter from the project.

- **`resolve_starter_conflicts(starter_name: str)`**:
  Assists in resolving merge conflicts for the specified starter.

- **`list_all_starters()`**:
  Lists all starters added to the current project.

Each function is designed to be intuitive and easy to use, mirroring the simplicity of the CLI commands.

## Requirements

- Python >=3.11

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Python Starters_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/piskunow/python-starters/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/piskunow/python-starters/blob/main/LICENSE
[contributor guide]: https://github.com/piskunow/python-starters/blob/main/CONTRIBUTING.md
[command-line reference]: https://python-starters.readthedocs.io/en/latest/usage.html
