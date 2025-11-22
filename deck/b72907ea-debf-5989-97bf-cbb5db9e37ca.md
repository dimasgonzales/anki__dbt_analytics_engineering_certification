---
tags:
  - compiled-code
  - materializations
  - jinja-macros
citations:
- cleaned_docs/sql-performance/rank_8.md
guid: b4421fe4e4
source: llm
uuid: b72907ea-debf-5989-97bf-cbb5db9e37ca
---

<front>

What are the three valid values for the `on_configuration_change` config in materialized views, and what is the purpose of this setting?

</front>

---

<back>

The valid values are `apply`, `continue`, and `fail`. This setting determines how dbt responds when the existing database object differs from the dbt model configuration (e.g., missing indexes or configuration mismatch) during a run.

</back>
