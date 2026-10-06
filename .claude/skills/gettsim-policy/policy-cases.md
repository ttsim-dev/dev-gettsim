# Policy-cases brief

Turn the reviewed dossier into GETTSIM policy cases: the **oracle** a separate agent
must later reproduce without editing. You write YAML cases and
`<dossier>/policy-cases.md`; the policy's code and parameters stay untouched. Work
inside the `gettsim/` submodule: every path below is relative to it, and its
`AGENTS.md` binds.

`<dossier>/research.md` is the spec, its "Decisions" section settles every open
question, and `<dossier>/test-cases.md` supplies the published worked examples. Where
the dossier is silent or contradicts itself, stop and report rather than choose.

## 1. Settle the interface

The cases fix the names the implementation must provide. Read the modules, YAMLs, and
existing cases of the namespace being extended and of each namespace it reads from.
For every input and result the cases need, settle:

- the qname: an existing column, or a new German name with the GEP 1 suffixes (`_m`,
  `_y`, `_bg`, ...);
- its unit (`docs/geps/gep-10.md`, "Contributors and users extending policy
  environments"); a stock has no period, a flow does;
- whether it is computed or a new `@policy_input` the user must supply.

## 2. Write the cases

In `src/gettsim/tests_germany/policy_cases/<namespace>/<regime start date>/`, copying
the shape of a neighbouring case.

- Every worked example in the dossier becomes a case: URL in `info.source`, the
  dossier's assumed inputs under `inputs.assumed`, intermediate results the source
  states as extra outputs.
- Every gap in the dossier's coverage table gets a hand-derived case (each threshold
  from both sides), the arithmetic from the statute written out in `info.note` so a
  reviewer can follow it line by line.
- Expected values come from the source or from your derivation, in a calculation
  kept apart from GETTSIM: running GETTSIM to obtain a number makes the oracle
  circular.
- File names describe the scenario in German (`vermögen_zu_hoch.yaml`).

## 3. Record

Write `<dossier>/policy-cases.md`:

- every case file, with its regime, what it exercises, and whether its expected
  values are published or hand-derived;
- the interface from step 1: new and renamed qnames with unit and kind;
- one command that runs exactly these cases
  (`pixi run -e py314-jax tests -k "<expression>"`).

Done when that command collects every listed case and each fails on the missing
behaviour (a missing column or a wrong number, not a YAML error), and
`prek run --files <case files>` passes. Reply with the file path and the case list.
