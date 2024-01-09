# AI-powered Git Helper (AIGIT)

AIGIT is a command-line interface (CLI) tool that uses OpenAI to generate commit messages for your Git repositories. It checks the status of your Git repository, generates a commit message based on the changes, and commits those changes.

## Installation

To install AIGIT, you need Python 3.10 and pip installed on your system. Clone the repository and navigate to the project directory. Then, run the following command:

```bash
pip install aigit
```

This will install the AIGIT package and its dependencies.

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

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

AIGIT is open-source software licensed under the MIT license.
