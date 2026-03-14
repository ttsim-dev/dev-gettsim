@.ai-instructions/profiles/tier-a.md @.ai-instructions/modules/jax.md
@.ai-instructions/modules/pandas.md @.ai-instructions/modules/optimagic.md
@.ai-instructions/modules/plotting.md @.ai-instructions/modules/project-structure.md
@.ai-instructions/modules/pytask.md @.ai-instructions/modules/ml-econometrics.md

# dev-gettsim

## Overview

This is a [pixi](https://pixi.sh) workspace containing four related projects for the
German tax and transfer microsimulation system:

- **ttsim** (`ttsim/`) - Core computation engine with DAG-based architecture supporting
  NumPy and JAX backends
- **gettsim** (`gettsim/`) - German policy implementations (functions, parameters,
  tests)
- **gettsim-personas** (`gettsim-personas/`) - Example household personas for testing
  and exploration
- **soep-preparation** (`soep-preparation/`) - Data preparation for SOEP survey data

Each subdirectory has its own `CLAUDE.md` with project-specific guidance. Refer to
`ttsim/CLAUDE.md` and `gettsim/CLAUDE.md` for detailed architecture and conventions.

## Build & Test

```bash
# Run all tests across all projects
pixi run -e py314 tests

# Run tests with JAX backend
pixi run -e py314-jax tests-jax

# Run tests for a specific project
pixi run -e py314 tests ttsim/tests/
pixi run -e py314 tests gettsim/src/gettsim/tests_germany/
pixi run -e py314 tests gettsim-personas/tests/
pixi run -e py314 tests soep-preparation/tests/

# Run specific test
pixi run -e py314 tests -k "test_end_to_end"

# Type checking (all projects)
pixi run ty

# Type checking with JAX backend
pixi run ty-jax

# Quality checks (linting, formatting)
prek run --all-files

# Available environments: py314, py314-jax, py314-cuda, py314-metal, type-checking, type-checking-jax
```

## Command Rules

Always use these command mappings:

- **Python**: Use `pixi run python` instead of `python` or `python3`
- **Type checker**: Use `pixi run ty` instead of running ty/mypy/pyright directly
- **Tests**: Use `pixi run tests` instead of `pytest` directly
- **Linting/formatting**: Use `prek run --all-files` instead of `ruff` directly
- **All quality checks**: Use `prek run --all-files`

Before finishing any task that modifies code, always run these three verification steps
in order:

1. `pixi run ty` (type checker)
1. `prek run --all-files` (quality checks: linting, formatting, yaml, etc.)
1. `pixi run -e py314 tests -n 7` (full test suite)

## Architecture

- **Two-level DAG system**: Interface DAG (high-level orchestration) and TT DAG (core
  computation)
- **Single entry point**: `gettsim.main()` or `ttsim.main()` with `MainTarget`,
  `InputData`, `TTTargets` helpers
- **Backend abstraction**: `"numpy"` or `"jax"` backends; use `xnp(backend)` for array
  operations
- **Qualified names (qnames)**: Double-underscore separated paths (e.g.,
  `"kindergeld__betrag_m"`)
- **German naming**: Policy code uses German (Kindergeld, Bürgergeld), infrastructure
  uses English

## Python Version

The root workspace sets `requires-python = ">=3.11"` to match the most permissive
sub-project (ttsim, gettsim, gettsim-personas all require `>=3.11`; soep-preparation
requires `>=3.14`). The `ty` type checker uses this to determine what's valid at
runtime, so it must stay consistent with the individual projects' constraints.

## pytest Configuration

The workspace uses `--import-mode=importlib` to handle test files with identical names
across projects. This is configured in the root `pyproject.toml`.
