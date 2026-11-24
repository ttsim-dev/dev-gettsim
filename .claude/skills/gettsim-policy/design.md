# Design brief

Propose how the rule in `<dossier>/research.md` enters GETTSIM, at the level a
reviewer approves before any case or code exists: the **big picture**, not a change
list. Write `<dossier>/design.md`; the repository stays untouched outside the dossier.
Work inside the `gettsim/` submodule: every path below is relative to it, and its
`AGENTS.md` binds, its naming conventions above all.

Read the modules, YAMLs, and existing cases of the namespace being extended and of
each namespace it reads from. `<dossier>/worked-examples.md` shows which inputs real
calculations need.

## Report

- **Inputs**: each new `@policy_input`, with its qname (an existing column wherever
  one carries the quantity, else a new German name with the GEP 1 suffixes), its unit
  (`docs/geps/gep-10.md`, "Contributors and users extending policy environments"; a
  stock has no period, a flow does), and one line on what the user supplies.
- **Results**: new and renamed result columns, qname and unit.
- **Functions**: per namespace, the functions added, changed, or retired, and the
  parameters added, one line each on why.
- **Out of scope**: each sub-case from the research report's open questions that the
  design leaves unmodelled, with what modelling it would take.
- **Breaking changes**: inputs existing users must newly supply, columns renamed.

Done when every regime in the research report maps to a function, a parameter entry,
or an out-of-scope item, and every qname has a unit and has been checked against the
existing names (no clash, no second name for a quantity GETTSIM already computes).
Reply with the file path and the report.
