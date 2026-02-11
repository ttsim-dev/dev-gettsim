# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in
this repository.

## Project Overview

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

## Development Commands

```bash
# Run all tests (specify environment due to ambiguity)
pixi run -e py314-jax tests

# Run tests for a specific project
pixi run -e py314-jax tests ttsim/tests/
pixi run -e py314-jax tests gettsim/src/gettsim/tests_germany/
pixi run -e py314-jax tests gettsim-personas/tests/

# Run specific test
pixi run -e py314-jax tests -k "test_end_to_end"

# Type checking
pixi run -e py314-jax ty

# Quality checks (linting, formatting)
prek run --all-files

# Available environments: py313, py314, py314-jax, py314-cuda, py314-metal
```

## Command Rules

Always use these command mappings:

- **Python**: Use `pixi run python` instead of `python` or `python3`
- **Type checker**: Use `pixi run -e py314-jax ty` instead of running ty/mypy/pyright
  directly
- **Tests**: Use `pixi run tests` instead of `pytest` directly
- **Linting/formatting**: Use `prek run --all-files` instead of `ruff` directly
- **All quality checks**: Use `prek run --all-files`

Before finishing any task that modifies code, always run these three verification steps
in order:

1. `pixi run -e py314-jax ty` (type checker)
1. `prek run --all-files` (quality checks: linting, formatting, yaml, etc.)
1. `pixi run -e py314-jax tests -n 7` (full test suite)

## Key Architectural Points

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

## pytest Configuration

The workspace uses `--import-mode=importlib` to handle test files with identical names
across projects. This is configured in the root `pyproject.toml`.
