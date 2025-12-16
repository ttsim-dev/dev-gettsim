## dev-gettsim Pixi workspace

This directory contains a Pixi-based workspace that ties together the following
projects:

- [`ttsim`](https://github.com/ttsim-dev/ttsim)
- [`gettsim`](https://github.com/ttsim-dev/gettsim)
- [`gettsim-personas`](https://github.com/ttsim-dev/gettsim-personas)
- [`soep-preparation`](https://github.com/OpenSourceEconomics/soep-preparation)

The workspace is configured via `pyproject.toml` and uses Pixi for environment
management.

### Clone all repositories (SSH, copy-paste)

Run the following in an empty directory where you want to keep the workspace (for
example, this `dev-gettsim` directory):

```bash
git clone git@github.com:ttsim-dev/ttsim.git
git clone git@github.com:ttsim-dev/gettsim.git
git clone git@github.com:ttsim-dev/gettsim-personas.git
git clone git@github.com:ttsim-dev/soep-preparation.git
```

After cloning, your layout should look like:

```text
dev-gettsim/
  pyproject.toml
  README.md
  ttsim/
  gettsim/
  gettsim-personas/
  soep-preparation/
```

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
