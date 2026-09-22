@.ai-instructions/profiles/tier-a.md @.ai-instructions/modules/jax.md
@.ai-instructions/modules/pandas.md @.ai-instructions/modules/plotting.md
@.ai-instructions/modules/dags.md

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

Each subdirectory has its own `AGENTS.md` with project-specific guidance. Refer to
`ttsim/AGENTS.md` and `gettsim/AGENTS.md` for detailed architecture and conventions.

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

# Type checking (all projects; ty runs as a prek hook)
prek run ty --all-files

# Type checking with JAX backend
prek run ty-jax --all-files

# Quality checks (linting, formatting, type checking)
prek run --all-files

# Available environments: py314, py314-jax, py314-cuda, py314-metal
```

## Command Rules

Always use these command mappings:

- **Python**: Use `pixi run python` instead of `python` or `python3`
- **Type checker**: Use `prek run ty --all-files` instead of running ty/mypy/pyright
  directly
- **Tests**: Use `pixi run tests` instead of `pytest` directly
- **Linting/formatting**: Use `prek run --all-files` instead of `ruff` directly
- **All quality checks**: Use `prek run --all-files`

Before finishing any task that modifies code, always run these two verification steps in
order:

1. `prek run --all-files` (quality checks: type checking, linting, formatting, yaml,
   etc.)
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

The `tests` and `tests-jax` tasks run `run_tests.py`, which starts one pytest process
per project: ttsim and gettsim-personas both import from a top-level `tests` package,
and a single process can only hold one of them. Path arguments select the projects; all
other arguments are forwarded to every pytest call.
