---
tags:
- card_type/factual
- debugging/yaml-compilation
- development/cli-commands
- development/materializations
citations:
- cleaned_docs/model-access/rank_8.md
guid: 723d065cd0
source: llm
uuid: 73bf5ea7-e7ab-5efc-81fd-0859f79caada
claim_meta:
  verdict: NOT_FOUND
  explanation: "The reference text includes an example of column-level tests nested under a column's data_tests key, which partially aligns with the answer. However, it does not provide evidence for model-level tests being defined under the model's data_tests key or explicitly distinguish between the two based on indentation and hierarchy. Therefore, there is insufficient information to fully verify or contradict the answer."
  citation:
    quote: " - name: customer_id     data_tests:       - not_null       - relationships:           arguments:             to: ref('stg_customers')             field: customer_id"
    is_quote_valid: true
---

<front>

How do you distinguish between a model-level test and a column-level test in a dbt YAML file?

</front>

---

<back>

By indentation and hierarchy:

1. **Model-level tests** are defined directly under the model's `data_tests` key (validating the whole table).
2. **Column-level tests** are nested under a specific column's `data_tests` key within the `columns` list.

</back>
