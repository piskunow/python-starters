# 🌟 Basic Usage of Python Starters

In this tutorial, we'll cover the basic usage of Python Starters, guiding you through its fundamental commands and operations. Whether you're adding a new starter, updating an existing one, or removing a starter from your project, this guide has you covered.

## Adding a Starter

To add a new starter to your project, use the `add` command followed by the URL of the starter's Git repository. Here's how you do it:

```bash
python-starters add https://github.com/your-username/your-starter-repo.git
```

Replace `https://github.com/your-username/your-starter-repo.git` with the URL of the starter you wish to use. This will clone the starter into your project and set it up based on its configuration.

## Updating a Starter

To ensure your starter stays up to date with the latest changes, use the `update` command. This command will fetch the latest version of the starter and merge any updates into your project:

```bash
python-starters update your-starter-name
```

Replace `your-starter-name` with the name of the starter you want to update. Python Starters will handle fetching the latest changes and applying them to your project.

## Removing a Starter

If you need to remove a starter from your project, Python Starters provides an easy command for this:

```bash
python-starters remove your-starter-name
```

Again, replace `your-starter-name` with the name of the starter you wish to remove. This command will safely detach and remove the starter from your project.

## Listing All Starters

To view a list of all starters currently added to your project, use the `list` command:

```bash
python-starters list
```

This command will display a list of all starters, providing a quick overview of the starters integrated into your project.

## Customizing a Starter

After adding a starter, you can customize it to suit your project's needs. Navigate to the starter's directory in your project and modify the files as required. Python Starters respects these customizations and will consider them during updates.

## Resolving Merge Conflicts

In case you encounter merge conflicts while updating a starter, Python Starters offers tools to help resolve these conflicts:

```bash
python-starters resolve your-starter-name
```

This command will assist you in resolving any conflicts between your local changes and the updates from the starter repository.

## Conclusion

With these basic commands, you can effectively manage and update starters within your project using Python Starters. The tool's simplicity and power make it an invaluable addition to your development workflow. Stay tuned for more advanced tutorials and features!
