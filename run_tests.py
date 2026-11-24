"""Run the workspace test suites with one pytest process per project.

ttsim and gettsim-personas both import helpers from a top-level `tests` package.
Within one pytest process whichever is imported first owns `sys.modules["tests"]`
and the other's imports fail, so each project gets its own process.

Arguments are forwarded to every pytest call. Path arguments (optionally with a
`::node` suffix) select the projects to run; without any, all configured
`testpaths` run.
"""

import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).parent
EXIT_NO_TESTS_COLLECTED = 5


def main(args: list[str]) -> int:
    """Run pytest once per project and return the combined exit status."""
    options, paths_by_project = _split_args(args)
    if not paths_by_project:
        paths_by_project = _group_by_project(paths=_configured_testpaths())
    statuses = {
        project: subprocess.call([sys.executable, "-m", "pytest", *paths, *options])  # noqa: S603
        for project, paths in paths_by_project.items()
    }
    for project, status in statuses.items():
        sys.stdout.write(f"{project}: pytest exited with {status}\n")
    return _combine_statuses(statuses=list(statuses.values()))


def _split_args(args: list[str]) -> tuple[list[str], dict[str, list[str]]]:
    options = [arg for arg in args if not _is_path(arg)]
    paths = [arg for arg in args if _is_path(arg)]
    return options, _group_by_project(paths=paths)


def _is_path(arg: str) -> bool:
    return not arg.startswith("-") and (ROOT / arg.split("::", maxsplit=1)[0]).exists()


def _group_by_project(paths: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for path in paths:
        groups.setdefault(Path(path.split("::")[0]).parts[0], []).append(path)
    return groups


def _configured_testpaths() -> list[str]:
    config = tomllib.loads((ROOT / "pyproject.toml").read_text())
    return config["tool"]["pytest"]["ini_options"]["testpaths"]


def _combine_statuses(statuses: list[int]) -> int:
    # A project whose tests a `-k` filter deselects entirely is not a failure,
    # but a run that collected nothing anywhere is.
    if all(status == EXIT_NO_TESTS_COLLECTED for status in statuses):
        return EXIT_NO_TESTS_COLLECTED
    return max(
        (status for status in statuses if status != EXIT_NO_TESTS_COLLECTED),
        default=0,
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
