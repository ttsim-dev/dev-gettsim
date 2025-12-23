#!/usr/bin/env zsh
#
# Pull updates for all four repos in this workspace.
# Repos: gettsim, gettsim-personas, soep-preparation, ttsim
#
# Usage:
#   ./pull_all_repos.zsh
#

set -euo pipefail

script_dir="${0:a:h}"
repos=(
  "ttsim"
  "gettsim"
  "gettsim-personas"
  "soep-preparation"
)

cd "$script_dir"

for repo in "${repos[@]}"; do
  echo "==> ${repo}"

  if [[ ! -d "$repo" ]]; then
    echo "    skip: directory not found: $repo"
    continue
  fi

  if ! (cd "$repo" && git rev-parse --is-inside-work-tree >/dev/null 2>&1); then
    echo "    skip: not a git repository: $repo"
    continue
  fi

  pushd "$repo" >/dev/null

  if [[ -n "$(git status --porcelain)" ]]; then
    echo "    note: working tree not clean (pull may fail depending on changes)"
  fi

  git pull
  popd >/dev/null
done
