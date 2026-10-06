---
name: gettsim-policy
description: Implement a German tax or transfer rule in GETTSIM from the statute. Use when adding a policy, modelling a reform, or updating parameter values.
---

# Implement a policy

You orchestrate five subagents, one human review, and one check of your own. Each
subagent starts fresh: its prompt is the user's request verbatim, the path of its brief
in this folder, and the absolute dossier path. The **dossier** is
`policy-dossiers/<slug>/` in the `.claude/` folder holding this skill (slug: the policy
in German, e.g. `versicherungsfreiheit-rente`); it is the only channel between the
agents.

The policy cases are the **oracle**: written from the dossier by one agent, then frozen,
then reproduced by another agent that may not touch them. Your job in steps 5 to 7 is
to keep those two apart.

## 1. Research

Spawn an agent on [`research.md`](research.md). It writes `<dossier>/research.md`.

Done when the file exists and its regime table has no row without a citation.

## 2. Test cases

Spawn an agent on [`test-cases.md`](test-cases.md). It reads the research report and
writes `<dossier>/test-cases.md`.

Done when the file exists and accounts for every regime in the research report, with a
case or as a named gap.

## 3. Human review

Stop. Give the user both file paths and, in the reply itself:

- the regime table;
- every open question, divergence from the request, and proposed simplification;
- the cases found, and the regimes and branches left without one.

The user edits the dossier or answers in chat; write their answers into the dossier
under "Decisions" in `research.md`. Done when the user approves and no open question
is left unanswered.

## 4. Policy cases

In the `gettsim/` submodule, branch off `main`. Spawn an agent on
[`policy-cases.md`](policy-cases.md). It writes the YAML cases and
`<dossier>/policy-cases.md`.

Done when that file lists the case files and the command that runs them.

## 5. Freeze the oracle

Commit exactly the listed case files on the branch ("Add policy cases for <policy>").
From here their content is fixed; `git diff <that commit> -- <case files>` is the
tamper check.

## 6. Implementation

Spawn an agent on [`implement.md`](implement.md).

## 7. Check the implementation against the oracle

Yourself, in `gettsim/`: run the command from `<dossier>/policy-cases.md`, and the
tamper check from step 5.

- Every case green and the diff empty: relay the implementer's summary (what changed,
  new and renamed inputs, the verification commands' outcome) and go to step 8.
- Otherwise stop and put the **discrepancy** to the user, per case: the case and its
  source, expected against computed for each failing target, any change to a frozen
  file, and the implementer's own account of it. Offer the three ways out: the case
  is wrong (correct the dossier and the case, re-freeze), the research is wrong
  (correct the dossier, back to step 6), the code is wrong (back to step 6 with the
  discrepancy as the request). The choice is the user's.

## 8. PR description

Spawn an agent on [`pr-description.md`](pr-description.md). It writes
`<dossier>/pr-description.md`. Show the description in the reply, with the session's
attribution line appended; open the PR only when the user asks.
