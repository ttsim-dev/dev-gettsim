## dev-gettsim Pixi workspace

This directory contains a Pixi-based workspace that ties together the following
projects:

- [`ttsim`](https://github.com/ttsim-dev/ttsim)
- [`gettsim`](https://github.com/ttsim-dev/gettsim)
- [`gettsim-personas`](https://github.com/ttsim-dev/gettsim-personas)
- [`soep-preparation`](https://github.com/ttsim-dev/soep-preparation)

The workspace is configured via `pyproject.toml` and uses Pixi for environment
management.

### Clone the workspace

The four projects are git submodules pinned to specific commits. Clone everything at
once:

```bash
git clone --recursive git@github.com:ttsim-dev/dev-gettsim.git
```

In an existing checkout, fetch the pinned commits with:

```bash
git submodule update --init
```

To pull the latest state of each project's current branch:

```bash
git submodule foreach git pull
```

Commit the updated pins in `dev-gettsim` when the combination should be shared.

### Using Pixi

1. **Install the environment**

   ```bash
   pixi install
   ```

1. **Use the workspace**

   For example, to start a Python REPL inside the Pixi environment:

   ```bash
   pixi run python
   ```

   Or to run a one-off check that the main packages import correctly (after cloning
   them):

   ```bash
   pixi run python -c "import ttsim, gettsim"
   ```
