# Implementation brief

Implement the rule in GETTSIM so that it reproduces the **oracle**: the frozen policy
cases listed in `<dossier>/policy-cases.md`. `<dossier>/research.md` is the spec and
its "Decisions" section settles every open question; `policy-cases.md` fixes the
qnames and units to provide. Work inside the `gettsim/` submodule: every path below is
relative to it, and its `AGENTS.md` binds throughout. Where the dossier is silent or
contradicts itself, stop and report rather than choose.

The oracle's files are read-only for you. A case you believe is wrong (a value, an
input, a qname that cannot work) is a **discrepancy**: leave the file as it is, leave
the case red, and report expected against computed with your reading of the statute.

A parameter-only update (new values, same rule) runs steps 1, 3, 4.

## 1. Parameters

Enter the report's values in the YAML beside the module exactly as given: the
statute's currency (`unit: DM_...` before 2002) and reference period (a yearly amount
is a `_y` parameter; the DAG converts). Every dated entry carries its `reference:`
from the regime table. A rule that ends gets a dated entry with only a `note:`.

Done when `prek run check-jsonschema --all-files` passes and every value and reference
matches the report.

## 2. Functions

One function per regime, sharing a `leaf_name` and partitioned by
`start_date`/`end_date`; a regime that differs only in numbers is a parameter entry,
not a function. Each docstring cites its § (and the amending act where the function
exists because of it). Declare `unit=` on every function and input.

On a `UnitConsistencyError`, fix in this order: the declaration (rename the leaf if its
suffix forbids the true unit), then `cast_ttsim_unit` at the one irregular operand,
last `verify_units=False`. Casts and opt-outs must also be added to the reviewed
baselines in `tests_germany/test_policy_cases.py`.

Done when every oracle case is green or reported as a discrepancy.

## 3. Whole suite

A new required input breaks every existing case and docs notebook that reaches the
changed function: add the input to each rather than defaulting it in code. An
existing case whose expected output moves is a behaviour change: list each one with
the § that justifies it. Then run the two verification commands from `AGENTS.md`.

Done when both pass on their own exit status, or fail only on reported discrepancies.

## 4. Record

Add a `CHANGES.md` entry under "Unreleased" in the style of its neighbours: what is
modelled, then new and renamed inputs by qname. Leave the changes uncommitted.

Reply with: files changed, new and renamed inputs, casts and opt-outs added, existing
cases whose expected outputs moved, each verification command with its summary line,
and every discrepancy.
