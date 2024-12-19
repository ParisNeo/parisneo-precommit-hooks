# ParisNeo Pre-commit Hooks

A collection of pre-commit hooks used across ParisNeo projects.

## Installation

1. Install pre-commit:
```bash
pip install pre-commit
```

2. Add to your `.pre-commit-config.yaml`:
```yaml
repos:
-   repo: https://github.com/ParisNeo/parisneo-precommit-hooks
    rev: v0.1.0
    hooks:
    -   id: parisneo-python-check  # For Python projects
    -   id: parisneo-js-check      # For JavaScript projects
```

3. Install the pre-commit hooks:
```bash
pre-commit install
```

## Available Hooks

### parisneo-python-check
- Runs black for code formatting
- Runs isort for import sorting
- Runs flake8 for style checking

### parisneo-js-check
- Runs prettier for code formatting
- Runs eslint for style checking

## Configuration

Create a `setup.cfg` in your project root:
```ini
[flake8]
max-line-length = 100
extend-ignore = E203
exclude = .git,__pycache__,build,dist

[isort]
profile = black
multi_line_output = 3
line_length = 100
```
