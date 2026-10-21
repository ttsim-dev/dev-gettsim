---
name: gettsim-policy
description: Implement a German tax or transfer rule in GETTSIM from the statute. Use when adding a policy, modelling a reform, correcting an existing rule, or updating parameter values.
---

# Implement a policy

You orchestrate six subagents, one human review, and one check of your own. Each
subagent starts fresh: its prompt is the user's request verbatim, the path of its brief
in this folder, and the absolute dossier path. The **dossier** is
`policy-dossiers/<slug>/` in the `.claude/` folder holding this skill (slug: the policy
in German, e.g. `versicherungsfreiheit-rente`); it is the only channel between the
agents. A **regime** is a date range within which the statute's rule is constant.
A parameter-only update (new values, same rule) runs all nine steps too: the values
need their citations and cases like any rule.

The policy cases are the **oracle**: written from the dossier by one agent, then frozen,
then reproduced by another agent that may not touch them. Once frozen in step 6, the
oracle is the truth: it changes only through a step 5 rerun the user chose. Your
job in steps 6 to 8 is to keep the two agents apart.

## 1. Research

Spawn an agent on [`research.md`](research.md). It writes `<dossier>/research.md`.

Done when the file exists and its regime table has no row without a citation.

## 2. Worked examples

Spawn an agent on [`worked-examples.md`](worked-examples.md). It reads the research
report and writes `<dossier>/worked-examples.md`.

Done when the file exists and accounts for every regime in the research report, with a
case or as a named gap.

## 3. Design

Spawn an agent on [`design.md`](design.md). It writes `<dossier>/design.md`.

Done when every regime maps to a function, a parameter entry, or an out-of-scope item.

## 4. Human review

Stop. The user wants to grasp the law and the plan in a minute, not read the dossier:
write **at a glance**, short lines, no citations, no step-by-step computation (those
stay in the files, whose paths you give). In the reply:

1. **The law**: how the rule works, in three to five sentences, then one line per
   regime (dates and what changes).
2. **The plan**: the new inputs with their proposed names, the results, and the
   functions touched, per namespace; the big picture, not each change.
3. **Decisions needed**: what to leave out of scope (the design's proposals), open
   questions, and divergences from the request, each with the options.
4. **Cases**: how many worked examples were found, and the regimes left without one.

The user answers in chat or edits the dossier. Write their answers into "Decisions" in
`research.md` and carry name and scope changes into `design.md`. Done when the user
approves the plan and no decision is left open; from here the names and the scope are
fixed.

## 5. Policy cases

In `ttsim/`, check out `main` and pull, unless the user names another ref: every test
run starts from the workspace root, whose environment installs this checkout. In the
`gettsim/` submodule, fetch and branch off `origin/main`. Spawn an agent on
[`policy-cases.md`](policy-cases.md). It writes the YAML cases and
`<dossier>/policy-cases.md`.

Done when that file lists the case files and the command that runs them.

## 6. Freeze the oracle

Commit exactly the listed case files on the branch ("Add policy cases for <policy>").
From here their content is fixed; `git diff <that commit> -- <case files>` is the
tamper check.

## 7. Implementation

Spawn an agent on [`implement.md`](implement.md).

Done when the implementer replies with its summary. If it reports a **ttsim limit**,
stop and put it to the user (what the rule needs, what ttsim does instead, the
reproduction); the user decides whether to fix ttsim first or to model the rule
differently.

## 8. Check the implementation against the oracle

Yourself: from the workspace root, the command from `<dossier>/policy-cases.md`; in
`gettsim/`, the tamper check from step 6.

- Every case green and the diff empty: relay the implementer's summary (what changed,
  new and renamed inputs, the final checks' outcome, the personas changes) and go to
  step 9.
- Otherwise restore any changed frozen file (`git checkout <freeze commit> -- <case
  files>`), stop, and put the **discrepancy** to the user, per case: the case and its
  source, expected against computed for each failing target, any change to a frozen
  file, and the implementer's own account of it. Offer the ways out; the choice is the
  user's, never yours:
  - the code is wrong: back to step 7 with the discrepancy as the request;
  - the dossier is wrong (research or design): correct it yourself, then back to
    step 7 with the correction as the request;
  - the case is wrong: correct the dossier, then back to step 5 for only the named
    cases, re-freeze (step 6), then back to step 8, or to step 7 if cases are still
    red.

## 9. Pull requests

Spawn an agent on [`pr-description.md`](pr-description.md). It writes
`<dossier>/pr-description.md`; append the session's attribution line. If the
implementer changed `gettsim-personas`, write a short description for that PR too:
which personas changed and why, naming the gettsim PR.

Then open the PRs, in order:

1. Commit the implementation on the gettsim branch, and the personas changes on the
   personas branch; push both.
2. Open the gettsim PR, then the personas PR. Put the gettsim PR number into its
   `CHANGES.md` entry.
3. If there is a personas PR, pin the two branches to each other: in
   `gettsim-personas/pyproject.toml` point `gettsim` at the gettsim branch; in
   `gettsim/pyproject.toml` point every `gettsim-personas` entry at the personas
   branch. Run `pixi lock` in both submodules.
4. Commit each submodule's `pyproject.toml`, `pixi.lock`, and `CHANGES.md` together;
   push both.

Done when both PRs are open and both branches' pushed heads include their lock files.
Reply with the PR URLs.
