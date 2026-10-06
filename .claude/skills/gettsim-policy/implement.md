# Implementation brief

Implement the rule in GETTSIM from the reviewed dossier: `<dossier>/research.md` is
the spec, its "Decisions" section settles every open question, and
`<dossier>/test-cases.md` supplies the expected values. Work inside the `gettsim/`
submodule: every path below is relative to it, and its `AGENTS.md` binds throughout.
Where the dossier is silent or contradicts itself, stop and report rather than choose.

A parameter-only update (new values, same rule) runs steps 2, 3, 5, 6.

## 1. Map the statute onto the namespace

Read the modules and YAMLs of the namespace you extend and of each namespace you read
from. For every quantity in the research report, settle:

- the qname: an existing column or parameter, or a new German name with the GEP 1
  suffixes (`_m`, `_y`, `_bg`, ...);
- its unit (`docs/geps/gep-10.md`, "Contributors and users extending policy
  environments"); a stock has no period, a flow does;
- whether it is computed, a parameter, or a new `@policy_input` the user must supply.

Done when every quantity has a qname and unit, and new or renamed inputs are listed
(they are API changes).

## 2. Red: policy cases

Write the cases before any code, in
`src/gettsim/tests_germany/policy_cases/<namespace>/<regime start date>/`, copying the
shape of a neighbouring case.

- Every case in the dossier becomes a YAML case: URL in `info.source`, the dossier's
  assumed inputs under `inputs.assumed`, stated intermediate results as extra outputs.
- Every gap in the dossier's coverage table gets a hand-derived case (each threshold
  from both sides), the derivation from the statute in `info.note`. Values produced by
  running GETTSIM are not expected values.
- File names describe the scenario in German (`vermögen_zu_hoch.yaml`).

Run `pixi run -e py314-jax tests -k "<namespace>"`. Done when every new case is red on
the missing behaviour (a wrong number or a missing target, not a YAML or input error).

## 3. Parameters

Enter the report's values in the YAML beside the module exactly as given: the
statute's currency (`unit: DM_...` before 2002) and reference period (a yearly amount
is a `_y` parameter; the DAG converts). Every dated entry carries its `reference:`
from the regime table. A rule that ends gets a dated entry with only a `note:`.

Done when `prek run check-jsonschema --all-files` passes and every value and reference
matches the report.

## 4. Functions

One function per regime, sharing a `leaf_name` and partitioned by
`start_date`/`end_date`; a regime that differs only in numbers is a parameter entry,
not a function. Each docstring cites its § (and the amending act where the function
exists because of it). Declare `unit=` on every function and input.

On a `UnitConsistencyError`, fix in this order: the declaration (rename the leaf if its
suffix forbids the true unit), then `cast_ttsim_unit` at the one irregular operand,
last `verify_units=False`. Casts and opt-outs must also be added to the reviewed
baselines in `tests_germany/test_policy_cases.py`.

Done when the step 2 cases are green. A dossier case that stays red after the code
matches the report is a finding about the dossier: report it, leave it red.

## 5. Whole suite

A new required input breaks every existing case and docs notebook that reaches the
changed function: add the input to each rather than defaulting it in code. Then run
the two verification commands from `AGENTS.md`.

Done when both pass, on their own exit status.

## 6. Record

Add a `CHANGES.md` entry under "Unreleased" in the style of its neighbours: what is
modelled, then new and renamed inputs by qname. Leave the changes uncommitted.

Reply with: files changed, new and renamed inputs, casts and opt-outs added, each
verification command with its summary line, and every point where code and dossier
could not be reconciled.
