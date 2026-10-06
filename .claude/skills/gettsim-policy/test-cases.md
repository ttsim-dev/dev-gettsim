# Test-case brief

Find published **worked examples** for the rule in `<dossier>/research.md` and write
them to `<dossier>/test-cases.md`. You search and report; the repository stays
untouched outside the dossier.

A worked example is a calculation with concrete inputs and a concrete result,
published by someone other than GETTSIM. Best first:

1. authorities applying the rule: DRV Gemeinsame Rechtliche Anweisungen,
   Rundschreiben of the Spitzenverbände, Fachliche Weisungen of the BA, BMF-Schreiben,
   Durchführungsanweisungen;
2. official calculators and ministry brochures;
3. Bundestag Drucksachen (Begründung with example calculations), court decisions with
   the arithmetic spelled out;
4. commentary, textbooks, other microsimulation models' test suites.

## Report

One section per case:

- **Source**: title, publisher, date, URL, page or example number.
- **Regime**: the row of the research report's regime table it falls in, by the date
  the example applies to (not its publication date).
- **Inputs** and **expected results**, in the source's own terms and numbers, with the
  passage quoted. Include intermediate results the source states: they become
  additional test targets.
- **Assumptions**: every input the source leaves implicit that a simulation needs
  (age, household, other income), marked as assumed.
- **Fit**: what the example exercises (which branch, which threshold) and anything in
  it that the research report's rule does not explain.

Then **Coverage**: a table of every regime and every branch of the rule against the
cases that exercise it, and **Gaps**: each regime or branch without a case, with where
you looked.

A result that disagrees with the research report's rule is a finding: report it under
**Conflicts**, with both readings, and leave the resolution to review.

Done when every regime and branch appears in the coverage table, every case's numbers
have been copied from the opened source (not from a search snippet), and each gap
lists the source classes searched. Reply with the file path, the coverage table, and
the conflicts.
