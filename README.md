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

7. Create GitHub workflow file `.github/workflows/test.yml`:
```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - uses: actions/setup-python@v2
      with:
        python-version: '3.10'
        
    - uses: actions/setup-node@v2
      with:
        node-version: '16'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
        pip install pytest
        npm install -g eslint prettier
        
    - name: Run tests
      run: pytest
        
    - name: Run hooks
      run: |
        pip install pre-commit
        pre-commit run --all-files
```

To use in your projects:

1. Add to your project's `.pre-commit-config.yaml`:
```yaml
repos:
-   repo: https://github.com/ParisNeo/parisneo-precommit-hooks
    rev: v0.1.0  # Use the latest version
    hooks:
    -   id: parisneo-python-check
    -   id: parisneo-js-check
```

2. Initialize:
```bash
pre-commit install
```