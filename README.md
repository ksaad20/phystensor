# PhysTensor

<p align="center">
  <img src="docs/assets/logo.png" alt="PhysTensor Logo" width="180">
</p>

<h1 align="center">PhysTensor</h1>

<p align="center">
<strong>A strictly-typed physical tensor library for deterministic scientific computing.</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Build](https://img.shields.io/github/actions/workflow/status/OWNER/phystensor/ci.yml?branch=main)
[![PyPI](https://img.shields.io/pypi/v/phystensor.svg)](https://pypi.org/project/phystensor/)
![Typing](https://img.shields.io/badge/typing-strict-blueviolet)
[![CI](https://github.com/ksaad20/phystensor/workflows/CI/badge.svg)](https://github.com/ksaad20/phystensor/actions)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21693589.svg)](https://doi.org/10.5281/zenodo.21693589)

</p>

---

## Overview

Scientific computing libraries excel at numerical operations but generally treat tensors as dimensionless arrays. This allows mathematically valid yet physically incorrect computations—for example, adding pressure to velocity or multiplying incompatible quantities without warning.

**PhysTensor** closes this gap by embedding **physical dimensions and units directly into tensor operations**. Every computation preserves dimensional information, enabling automatic validation of physical consistency while maintaining a familiar tensor programming experience.

Rather than replacing existing numerical backends, PhysTensor acts as a **physics-aware layer** that integrates dimensional analysis with modern tensor computation.

---

## Why PhysTensor?

PhysTensor is designed around one principle:

> **A computation should be mathematically valid *and* physically meaningful.**

The library combines:

- Strictly typed tensor objects
- Physical units and dimensions
- Automatic dimensional analysis
- Deterministic execution
- Backend-agnostic tensor computation
- Engineering-oriented validation

---

# Features

## Physics-Aware Tensors

Every tensor carries physical dimensional information alongside its numerical values.

Example quantities include:

- Length
- Time
- Mass
- Temperature
- Current
- Velocity
- Acceleration
- Force
- Pressure
- Energy
- Power

---

## Automatic Dimensional Analysis

PhysTensor validates every operation.

Examples:

✅ Force × Distance → Energy

✅ Velocity × Time → Distance

❌ Pressure + Velocity

❌ Energy + Temperature

Invalid operations raise informative exceptions before incorrect results propagate through a scientific workflow.

---

## Strict Typing

Designed for modern Python tooling.

- mypy
- pyright
- Ruff
- IDE autocompletion

---

## Deterministic Scientific Computing

PhysTensor prioritizes reproducibility by ensuring computations produce consistent results across scientific and engineering workflows.

---

## Backend Agnostic

PhysTensor is designed to integrate with existing numerical ecosystems rather than replace them.

Potential backends include:

- NumPy
- PyTorch
- JAX

---

## Extensible Unit System

Define custom physical dimensions and derived quantities for specialized engineering domains.

---

# Installation

```bash
pip install phystensor
```

For development:

```bash
git clone https://github.com/OWNER/phystensor.git

cd phystensor

pip install -e .[dev]
```

---

# Quick Start

```python
from phystensor import Tensor
from phystensor.units import Meter, Second

distance = Tensor([10], unit=Meter)
time = Tensor([2], unit=Second)

velocity = distance / time

print(velocity)
```

Output

```text
5 m/s
```

---

# Safety Example

```python
pressure + velocity
```

Output

```text
DimensionMismatchError:
Cannot add Pressure to Velocity.
```

---

# Applications

PhysTensor is suitable for:

- Scientific computing
- Computational physics
- Physics-informed machine learning
- Digital twins
- Robotics
- Aerospace engineering
- Mechanical engineering
- Electrical engineering
- Renewable energy systems
- Battery modeling
- Industrial simulation

---

# Architecture

```text
                 User Application
                        │
                ┌───────▼────────┐
                │   PhysTensor   │
                ├────────────────┤
                │ Typed Tensors  │
                │ Unit System    │
                │ Validation     │
                │ Dimensional    │
                │ Analysis       │
                └───────┬────────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
      NumPy          PyTorch          JAX
```

---

# Roadmap

## Core

- [x] Typed physical tensors
- [x] Automatic dimensional analysis
- [x] Unit propagation

## Future

- [ ] Sparse tensors
- [ ] GPU acceleration
- [ ] Automatic differentiation
- [ ] Symbolic dimensions
- [ ] PDE utilities
- [ ] Finite element helpers
- [ ] Physics-informed optimization

---

# Testing

```bash
pytest
```

Static analysis:

```bash
ruff check .

black --check .

mypy .
```

---

# Contributing

Contributions are welcome.

Please:

1. Fork the repository.
2. Create a feature branch.
3. Add tests.
4. Ensure all CI checks pass.
5. Submit a pull request.

---

# Citation

If you use PhysTensor in research, please cite:

```bibtex
@software{phystensor,
  title  = {PhysTensor},
  author = {Asif Kazi},
  year   = {2026},
  url    = {https://github.com/ksaad20/phystensor}
}
```

---

# License

Released under the **Apache License 2.0**.

See the `LICENSE` file for details.

---

# Vision

PhysTensor aims to provide a reliable foundation for **physics-aware tensor computing**, enabling researchers and engineers to write software that respects both mathematical correctness and physical laws.

---

<p align="center">
<b>PhysTensor</b><br>
<i>Tensor computing with physical meaning.</i>
</p>
