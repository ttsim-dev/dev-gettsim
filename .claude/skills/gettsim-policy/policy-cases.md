# Policy-cases brief

Turn the reviewed dossier into GETTSIM policy cases: the **oracle** a separate agent
must later reproduce without editing. You write YAML cases and
`<dossier>/policy-cases.md`; the policy's code and parameters stay untouched. Work
inside the `gettsim/` submodule: every path below is relative to it, and its
`AGENTS.md` binds, except for its closing verification: your cases are red by design
until the implementation lands, so the checks below replace the full suite.

`<dossier>/research.md` is the spec, its "Decisions" section settles every open
question, `<dossier>/worked-examples.md` supplies the published worked examples, and
`<dossier>/design.md` fixes the qnames, units, and scope. Use its names exactly; a case
that needs a name the design lacks is a gap to report, not one to fill. Where the
dossier is silent or contradicts itself, stop and report rather than choose.

## 1. Write the cases

In `src/gettsim/tests_germany/policy_cases/<namespace>/<regime start date>/`, copying
the shape of a neighbouring case.

- Every worked example in the dossier becomes a case with the source's inputs exactly
  as published; where the source leaves an input open, fill it under
  `inputs.assumed`. Intermediate results the source states become extra outputs.
  `info.source` locates the calculation precisely (document, edition, Beispiel / Rn. /
  page, URL); a bare statute or BGBl link locates nothing.
- Every gap in the dossier's coverage table gets a **regression test** (each threshold
  from both sides): a case whose expected values you derived yourself. The statute is
  the spec, never a source of cases, so these carry `source: Regression test.`, and so
  does a published example whose checked outputs depend on your assumptions.
- `info.note` says in one line what the case is about ("Vermögen knapp über der
  Grenze"). The YAML already shows the inputs, outputs, and arithmetic.
- `info.precision_atol` is the precision the source reports (cents: `0.01`).
- Expected values come from the source or from your derivation, in a calculation
  kept apart from GETTSIM: running GETTSIM to obtain a number makes the oracle
  circular.
- File names describe the scenario in German (`vermögen_zu_hoch.yaml`).

## 2. Record

Write `<dossier>/policy-cases.md`:

- every case file, with its regime, what it exercises, whether its expected values
  are published or hand-derived, and whether it is already green;
- one command, run from the workspace root, that runs exactly these cases
  (`pixi run -e py314-jax tests gettsim/src/gettsim/tests_germany/test_policy_cases.py -k "<expression>"`).

Done when that command collects every listed case, each case for a new or changed
regime fails on the missing behaviour (a missing column or a wrong number, not a YAML
error), each case for a regime GETTSIM already models is green and listed as such, and
`prek run --files <case files>` passes. Reply with the file path and the case list.
