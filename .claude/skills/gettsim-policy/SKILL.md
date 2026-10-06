---
name: gettsim-policy
description: Implement a German tax or transfer rule in GETTSIM from the statute. Use when adding a policy, modelling a reform, or updating parameter values.
---

# Implement a policy

You orchestrate four subagents and one human review. Each subagent starts fresh: its
prompt is the user's request verbatim, the path of its brief in this folder, and the
absolute dossier path. The **dossier** is `policy-dossiers/<slug>/` in the `.claude/`
folder holding this skill (slug: the policy in German, e.g.
`versicherungsfreiheit-rente`); it is the only channel between the agents.

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

## 4. Implementation

Spawn an agent on [`implement.md`](implement.md). Relay its summary: what it changed,
new and renamed inputs, the verification commands' outcome, and anything it could not
reconcile with the dossier.

## 5. PR description

Spawn an agent on [`pr-description.md`](pr-description.md). It writes
`<dossier>/pr-description.md`. Show the description in the reply, with the session's
attribution line appended; open the PR only when the user asks.
