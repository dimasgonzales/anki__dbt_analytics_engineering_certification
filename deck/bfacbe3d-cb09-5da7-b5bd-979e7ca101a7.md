---
tags:
  - exposures
  - lineage
  - modularity
citations:
- cleaned_docs/exposures/rank_10.md
guid: 0cf7a75680
source: llm
uuid: bfacbe3d-cb09-5da7-b5bd-979e7ca101a7
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
