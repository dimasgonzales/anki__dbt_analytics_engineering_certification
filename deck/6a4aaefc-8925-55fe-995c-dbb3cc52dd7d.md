---
tags:
- card_type/factual
- development/modularity
- documentation/exposures
- documentation/lineage
citations:
- cleaned_docs/exposures/rank_3.md
guid: eb985f7ace
source: llm
uuid: 6a4aaefc-8925-55fe-995c-dbb3cc52dd7d
claim_meta:
  verdict: NOT_FOUND
  explanation: "The reference text confirms that exposures appear in the dbt DAG and discusses their role, but it does not provide details on how to configure dependencies for exposures, such as the use of the 'depends_on' key or specific syntax like 'ref()' and 'source()'."
  citation:
    quote: null
    is_quote_valid: false
---

<front>

How do you define dependencies for an exposure to ensure it appears in the dbt DAG?

</front>

---

<back>

Use the `depends_on` key within the exposure's YAML configuration. You must explicitly list the upstream resources using `ref()` for models and `source()` for sources.

```yaml
exposures:
  - name: finance_dashboard
    type: dashboard
    depends_on:
      - ref('fct_revenue')
      - source('stripe', 'charges')
```

</back>
