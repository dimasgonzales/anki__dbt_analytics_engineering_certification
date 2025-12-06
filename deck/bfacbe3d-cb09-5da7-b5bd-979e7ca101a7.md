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
  verdict: NOT_FOUND
  explanation: "The reference text provides general information on dbt CLI selection and mentions exposures, but it does not include details on the specific syntax using the '+' prefix for running an exposure and its upstream dependencies."
  citation:
    quote: null
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
