# PR-description brief

Write `<dossier>/pr-description.md` for the implemented policy. You write that one
file; the repository stays otherwise untouched.
The reader is a reviewer who knows GETTSIM and has neither the dossier nor the
conversation: every claim about the law carries its § inline.

Sources, each for what it alone knows:

- `research.md`: the rule, the regimes, the citations, the "Decisions".
- `test-cases.md`: where each case's expected values come from.
- `policy-cases.md`: the case files, and which are published or hand-derived.
- `git diff main...HEAD` plus the working tree, inside the `gettsim/` submodule: what was actually built. Where diff and
  dossier disagree, the diff is what the PR does; say so in the description.

## Shape

**Title**: imperative, the policy by its German name ("Model Versicherungsfreiheit in
der Rentenversicherung").

**Opening**: `Closes #N.` if an issue exists, then two or three sentences: what
GETTSIM got wrong or lacked, and what this PR models. If the statute diverged from the
issue, say how.

**What changes**: one paragraph per regime-bearing rule, led by its name in bold and
its norm in parentheses, stating the rule and its dates as a reader of the law would.
Corrected parameter values get their own paragraph with the act that fixes the value.

**Simplifications**: each sub-case deliberately left unmodelled, from "Decisions".
Omit the heading when there are none.

**API impact**: new required inputs, renamed columns, changed dependencies, by qname.
Omit the heading when there are none.

**Tests**: a table of case path against source for every case with a published worked
example; one sentence for the hand-derived ones. Name any case that caught a mistake.

Done when every regime in `research.md` is either in "What changes" or in
"Simplifications", every qname under "API impact" appears in the diff, and every
table row's case file exists. Reply with the file path and the description in full.
