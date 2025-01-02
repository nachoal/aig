# AI-powered Git Helper (AIGIT)

AIGIT is a command-line interface (CLI) tool that uses OpenAI to generate commit messages for your Git repositories. It checks the status of your Git repository, generates a commit message based on the changes, and commits those changes.

## Installation

To install AIGIT, you need Python 3.6+ installed on your system. You have several options:

### Global Installation (Recommended)

Using uv (fastest):
```bash
uv tool install aigit
```

Using pipx (alternative):
```bash
pipx install aigit
```

These methods install AIGIT globally and isolate its dependencies, making it available as the `aig` command anywhere on your system.

### Regular Installation

If you prefer a regular installation:

```bash
pip install aigit
```

Or using uv:
```bash
uv pip install aigit
```

## Configuration

Before using AIGIT, you need to configure your OpenAI API key. Run the following command and enter your API key when prompted:

```bash
aig --config
```

## Usage

```bash
$ aig -h
usage: aig [-h] [--config] [-y]

AI-powered Git Helper

options:
  -h, --help  show this help message and exit
  --config    Configure API Key
  -y, --yes   Auto commit without asking for confirmation
```

To use AIGIT, navigate to your Git repository and run the following command:

```bash
aig
```

AIGIT will check the status of your Git repository, generate a commit message, and ask for your confirmation before committing the changes. If you want to auto commit without confirmation, use the `-y` or `--yes` option:

```bash
aig -y
```

## Development

### Setup Development Environment

1. Clone the repository
2. Install uv if you haven't already: `pip install uv`
3. Install dependencies:
   ```bash
   uv pip install .
   ```

### Making Changes

The project uses `pyproject.toml` for dependency management and build configuration. To add new dependencies:

```bash
uv add <package-name>
```

To remove dependencies:

```bash
uv remove <package-name>
```

### Version Updates

When releasing a new version, update the version number in both:
1. `pyproject.toml`: Update the `version = "x.x.x"` field under `[project]`
2. `aigit/__init__.py`: Update the `__version__ = "x.x.x"` variable

### Building and Publishing

1. Update the version as described above
2. Run the deployment script:
   ```bash
   ./scripts/deploy.sh
   ```

The script will:
- Clean any existing build artifacts
- Build the package with uv
- Upload to PyPI
- Clean up build artifacts if successful
- Keep build artifacts for inspection if upload fails

For manual deployment, you can run these commands individually:
```bash
# Clean artifacts
rm -rf dist/ build/ *.egg-info/

# Build
uv build

# Upload to PyPI
uvx twine upload dist/*
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

AIGIT is open-source software licensed under the MIT license.
