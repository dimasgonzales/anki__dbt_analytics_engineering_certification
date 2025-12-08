---
tags:
- card_type/factual
- development/modularity
- documentation/exposures
- documentation/lineage
citations:
- cleaned_docs/exposures/rank_10.md
guid: 0cf7a75680
source: llm
uuid: bfacbe3d-cb09-5da7-b5bd-979e7ca101a7
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text confirms that using the '+' operator with the exposure selector selects upstream dependencies, which directly supports the answer's claim about the syntax for running a specific exposure and all its upstream dependencies."
  citation:
    evidence_source: "https://docs.getdbt.com/reference/node-selection/methods"
    quote: "The `exposure` method is used to select parent resources of a specified exposure. Use in conjunction with the `+` operator."
    is_quote_valid: false
---

<front>

Which dbt CLI selector syntax is used to run a specific exposure and all its upstream dependencies?

</front>

---

<back>

Use the `+` prefix before the exposure selector.
Example:
```bash
dbt run --select +exposure:financial_dashboard
```
This ensures all models required to populate the exposure are rebuilt.

</back>
