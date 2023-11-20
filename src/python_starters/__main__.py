"""Command-line interface."""
import typer
from starters_cli import add_starter
from starters_cli import init_starter
from starters_cli import list_starters
from starters_cli import remove_starter
from starters_cli import resolve_conflicts
from starters_cli import update_starter


app = typer.Typer()


@app.command()
def init():
    """Initialize Python Starters in the current project."""
    init_starter()


@app.command()
def add(starter_git_url: str):
    """Add a new starter to the project."""
    add_starter(starter_git_url)


@app.command()
def update(starter_name: str):
    """Update the specified starter."""
    update_starter(starter_name)


@app.command()
def remove(starter_name: str):
    """Remove the specified starter."""
    remove_starter(starter_name)


@app.command()
def list():
    """List all starters in the project."""
    list_starters()


@app.command()
def resolve(starter_name: str):
    """Resolve merge conflicts for the specified starter."""
    resolve_conflicts(starter_name)


@app.callback()
def main(ctx: typer.Context):
    """Python Starters - A tool to manage and update project starters."""
    ctx.ensure_object(dict)


if __name__ == "__main__":
    app()
