# Contributing to phystensor

Thank you for your interest in contributing to **phystensor** — the century-proof industrial physics engine.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Setup](#development-setup)
3. [Running Tests](#running-tests)
4. [Code Style](#code-style)
5. [Submitting Changes](#submitting-changes)
6. [Commit Messages](#commit-messages)
7. [Reporting Issues](#reporting-issues)
8. [License](#license)

---

## Getting Started

- Fork the repository on GitHub.
- Clone your fork locally:
  ```bash
  git clone https://github.com/YOUR_USERNAME/phystensor.git
  cd phystensor
  ```
- Create a new branch for your work:
  ```bash
  git checkout -b feature/your-feature-name
  ```

---

## Development Setup

Install the package in editable mode with all development dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### Requirements

- Python 3.10, 3.11, or 3.12
- `numpy`, `scipy`, `sympy`, `matplotlib`
- `pytest`, `pytest-cov`, `pytest-xdist`
- `ruff` (linting and formatting)

---

## Running Tests

Run the full test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=phystensor --cov-report=term-missing
```

Run in parallel (faster):

```bash
pytest -n auto
```

All tests must pass before a pull request can be merged.

---

## Code Style

We use **ruff** for linting and formatting.

Check your code:

```bash
ruff check .
```

Auto-fix issues:

```bash
ruff check --fix .
```

Format code:

```bash
ruff format .
```

Run both before every commit:

```bash
ruff check --fix . && ruff format .
```

### Key style rules

- Line length: **100 characters**
- Use type hints with `from __future__ import annotations`
- Prefer `X | Y` over `Union[X, Y]`
- Prefer `dict`, `list`, `tuple` over `Dict`, `List`, `Tuple`
- All public functions and classes must have docstrings

---

## Submitting Changes

1. **Write tests** for any new functionality.
2. **Run the test suite** and ensure everything passes.
3. **Run ruff** and fix any linting or formatting issues.
4. **Update documentation** if your change affects the public API.
5. **Open a Pull Request** with a clear description of the changes.

### Pull Request checklist

- [ ] Tests pass locally (`pytest`)
- [ ] Code is formatted (`ruff format .`)
- [ ] Linting passes (`ruff check .`)
- [ ] Docstrings added for new public APIs
- [ ] No breaking changes without justification

---

## Commit Messages

Use clear, descriptive commit messages:

```
feat: add metric prefix support for unit registry
fix: resolve dimension mismatch in solvers.py
docs: update README with maritime physics example
test: add coverage for tensor conversion edge cases
refactor: simplify Dimensions.__add__ logic
```

### Prefixes

| Prefix | Meaning |
|--------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `test` | Adding or updating tests |
| `refactor` | Code restructuring without behavior change |
| `style` | Formatting, whitespace, semicolons |
| `chore` | Maintenance, dependencies, CI |

---

## Reporting Issues

When reporting a bug, please include:

1. **Python version** (`python --version`)
2. **phystensor version** (`pip show phystensor`)
3. **Minimal reproducible example**
4. **Expected behavior** vs **actual behavior**
5. **Full traceback** if applicable

Feature requests are welcome — open an issue with the `enhancement` label.

---

## License

By contributing to phystensor, you agree that your contributions will be licensed under the same license as the project (see `LICENSE.md`).

---

## Questions?

Open a [GitHub Discussion](https://github.com/ksaad20/phystensor/discussions) or reach out via the issue tracker.

Happy coding!
