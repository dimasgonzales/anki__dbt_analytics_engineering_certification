---
tags:
- card_type/factual
- debugging/compiled-code
- development/jinja-macros
- development/materializations
citations:
- cleaned_docs/sql-performance/rank_8.md
guid: b4421fe4e4
source: llm
uuid: b72907ea-debf-5989-97bf-cbb5db9e37ca
claim_meta:
  verdict: SUPPORTED
  explanation: "The answer is supported because the reference text explicitly lists 'apply', 'continue', and 'fail' as valid values for on_configuration_change in materialized views (e.g., in sql-performance/rank_8.md), and describes the purpose as handling configuration changes directly without recreation, which matches the answer's description of responding to differences during a run."
  citation:
    quote: "This setting tells dbt to attempt to make configuration changes directly to the object when possible, as opposed to completely recreating the object to implement the updated configuration."
    is_quote_valid: true
---

<front>

What are the three valid values for the `on_configuration_change` config in materialized views, and what is the purpose of this setting?

</front>

---

<back>

The valid values are `apply`, `continue`, and `fail`. This setting determines how dbt responds when the existing database object differs from the dbt model configuration (e.g., missing indexes or configuration mismatch) during a run.

</back>
