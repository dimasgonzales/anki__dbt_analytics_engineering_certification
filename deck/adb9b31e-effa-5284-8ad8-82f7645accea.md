---
tags:
- card_type/factual
- development/modularity
- development/seeds
- documentation/lineage
citations:
- cleaned_docs/exposures/rank_2.md
guid: 4d1a516697
source: llm
uuid: adb9b31e-effa-5284-8ad8-82f7645accea
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly supports the answer by showing that exposures define lineage connections using the `depends_on` list in YAML, as illustrated in the example."
  citation:
    quote: "depends_on:   - ref('fct_orders')   - ref('dim_customers')   - source('gsheets', 'goals')   - metric('count_orders')"
    is_quote_valid: true
---

<front>

Since exposures are defined in YAML and not SQL, how do you establish lineage connections to the models they consume?

</front>

---

<back>

You must explicitly define dependencies using the `depends_on` list within the exposure's YAML properties. Unlike models that infer lineage from SQL, exposures require you to list nodes manually:
```yaml
depends_on:
  - ref('model_name')
  - source('source_name', 'table_name')
```

</back>
