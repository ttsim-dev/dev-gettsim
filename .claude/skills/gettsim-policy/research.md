# Research brief

Write the legislative history of the rule named in the request to
`<dossier>/research.md`. You research and report; the repository stays untouched
outside the dossier.

The **statute** is the subject: the text of the law in force at each date. A **regime**
is a date range within which the statute's rule is constant. The history runs from the
rule's introduction (or the earliest date the request asks for) to today, including
enacted changes not yet in force.

## Sources

Preferred first; every claim in the report names which kind it rests on.

1. **BGBl**: the amending act itself. Scans of Teil I:
   `https://media.offenegesetze.de/bgbl1/<year>/bgbl1_<year>_<issue>.pdf`, issue index
   at `https://offenegesetze.de/veroeffentlichung/bgbl1/<year>`; from 2023,
   recht.bund.de. <!-- codespell:ignore bund -->
   `pdftotext`, then grep values with thin spaces (`123 600`).
2. **Consolidated text**: gesetze-im-internet.de for the current version; buzer.de for
   the amendment history of a norm (reliable back to ~2006).
3. **Secondary**: Bundestag Drucksachen, ministry and agency publications,
   commentary. Use them to find the act, and cite them alone only where 1 and 2 are
   out of reach.

The consolidated text shows what a norm says; only the act shows which act said it and
from when. Take an act's date from its "Vom ..." line and a regime's start date from
the act's Inkrafttreten article (issue dates and TOC datelines differ from both).

## Report

- **Scope**: the rule, the norms that carry it, what the request asks for.
- **Regime table**: one row per regime: start date, end date, the rule in one
  sentence, the norm (§, Abs., Satz), the amending act as
  `<Gesetz> v. DD.MM.YYYY BGBl. I S. NNNN`, source kind (1/2/3), URL.
- **Rule per regime**: who is covered, the conditions, the computation step by step,
  rounding, with the statute's wording quoted where the computation hangs on it.
- **Values**: every number the statute fixes, per date, in the statute's own currency
  and reference period (DM stays DM, a yearly amount stays yearly), each with its
  citation. Per-year values cite that year's Verordnung; an Anlage alone is too coarse.
- **Divergences**: where the statute differs from the request (an expected value, a
  date, who is covered). The statute wins; say what differs.
- **Open questions**: ambiguities in the statute, and sub-cases a model would
  plausibly simplify, each with the options.
- **Unverified**: every claim resting on source kind 3 or on memory, listed.
- **Decisions**: empty; filled at review.

Done when every regime row has a citation and URL you opened and read, every value has
been compared against the text it cites, and the "Unverified" list is complete. Reply
with the file path and the regime table.
