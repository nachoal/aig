# AI-powered Git Helper (AIG)

AIG is a command-line interface (CLI) tool that uses OpenAI to generate commit messages for your Git repositories. It checks the status of your Git repository, generates a commit message based on the changes, and commits those changes.

## Installation

To install AIG, you need Python 3.10 and pip installed on your system. Clone the repository and navigate to the project directory. Then, run the following command:

```bash
pip install .
```

This will install the AIG package and its dependencies.

## Configuration

Before using AIG, you need to configure your OpenAI API key. Run the following command and enter your API key when prompted:

```bash
aig --config
```

## Usage

To use AIG, navigate to your Git repository and run the following command:

```bash
aig
```

AIG will check the status of your Git repository, generate a commit message, and ask for your confirmation before committing the changes. If you want to auto commit without confirmation, use the `-y` or `--yes` option:

```bash
aig -y
```

## WIP: Testing

The [tests](file:///Users/ia/code/projects/aig/aig.egg-info/top_level.txt#2%2C1-2%2C1) directory contains tests for AIG. To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

AIG is open-source software licensed under the MIT license.
