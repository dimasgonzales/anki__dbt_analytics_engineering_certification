---
tags:
- card_type/factual
- development/jinja-macros
- state/selectors
citations:
- cleaned_docs/selectors/rank_6.md
guid: b21886ea8c
source: llm
uuid: 40c99af2-3e5b-5bc1-bfac-75eaad3b63cf
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text confirms that union and intersection are set operators available in YAML selectors, and exclude always operates as a set difference and is applied last within its scope, matching the answer."
  citation:
    quote: "Here, `exclude` *always* returns a set difference, and it is always applied *last* within its scope."
    is_quote_valid: false
---

<front>

What are the three boolean logic operations available in `selectors.yml`, and how does the `exclude` operation behave?

</front>

---

<back>

The three operations are `union`, `intersection`, and `exclude`. The `exclude` keyword always operates as a set difference (removing items from the current selection) and is applied last within its specific scope.

</back>
