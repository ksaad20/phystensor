# Test Policy — PhysTensor

> **Status:** Active  
> **Applies to:** All pull requests, releases, and commits to `main`  
> **Owner:** @ksaad20

---

## 1. Philosophy

Every line of code that touches dimensional analysis, unit conversion, or tensor operations must be backed by tests. Untested code is broken code.

---

## 2. Required Test Types

| Type | When Required | Framework |
|------|--------------|-----------|
| **Unit tests** | Every new function / method | `pytest` |
| **Property-based tests** | Invariants (e.g., `a + b == b + a`) | `hypothesis` |
| **Integration tests** | Cross-module workflows | `pytest` |
| **Regression tests** | Every bug fix | `pytest` |

---

## 3. Coverage Requirements

| Stage | Minimum Coverage | Maximum Drop Allowed |
|-------|-------------------|----------------------|
| PR merge | **70%** | **2%** |
| Release tag | **75%** | **1%** |

Coverage is measured with `pytest-cov`. CI fails if coverage falls below the threshold.

---

## 4. Running Tests Locally

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run all tests
python -m pytest -v

# Run with coverage
python -m pytest --cov=phystensor --cov-fail-under=70

# Run specific test file
python -m pytest tests/test_units.py -v

# Run property-based tests only
python -m pytest -m hypothesis -v
```

---

## 5. CI Enforcement

All tests run on every pull request via `.github/workflows/ci.yml` across:

- Python 3.10
- Python 3.11
- Python 3.12

A PR **cannot merge** unless:
1. All tests pass
2. Coverage ≥ 70%
3. No new warnings from `ruff` or `mypy`

---

## 6. Test Naming Conventions

```
tests/
├── test_<module>.py          # Unit tests for src/phystensor/<module>.py
├── test_integration_<flow>.py # Cross-module integration tests
└── conftest.py                # Shared fixtures
```

Function naming:
```python
def test_<function>_<scenario>_<expected>():
    ...

# Example:
def test_tensor_add_incompatible_units_raises_error():
    ...
```

---

## 7. Fixtures & Mocks

Shared fixtures (common tensors, units) live in `tests/conftest.py`.

Do **not** mock NumPy or SciPy unless absolutely necessary — test against real backends.

---

## 8. Property-Based Testing Rules

Use `hypothesis` for invariants that must hold for **all** inputs:

- Commutativity: `a + b == b + a`
- Associativity: `(a + b) + c == a + (b + c)`
- Dimensional preservation: `unit(a * b) == unit(a) * unit(b)`
- Identity: `a + 0 == a`

---

## 9. Bug Fix Protocol

Every bug fix must include:
1. A regression test that fails before the fix
2. A comment linking to the issue: `# Regression test for #42`
3. Passes on the fixed branch

---

## 10. Skipping Tests

Tests may only be skipped with an explicit reason and issue reference:

```python
@pytest.mark.skip(reason="Blocked by #123 — waiting for numpy 2.0 compat")
def test_future_feature():
    ...
```

---

## 11. Review Checklist

Before approving a PR, reviewers verify:

- [ ] New code has corresponding tests
- [ ] All tests pass locally and in CI
- [ ] Coverage did not drop
- [ ] No `print()` or `breakpoint()` left in tests
- [ ] Tests are deterministic (no randomness without seeding)

---

## 12. Contact

Questions about this policy: open an issue or email kazisaadasif29@gmail.com
