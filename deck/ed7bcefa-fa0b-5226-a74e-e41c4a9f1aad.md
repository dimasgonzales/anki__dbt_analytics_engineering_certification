---
tags:
  - docs-generation
  - lineage
  - test-types
citations:
- cleaned_docs/test-types/rank_5.md
guid: 737138baaf
source: llm
uuid: ed7bcefa-fa0b-5226-a74e-e41c4a9f1aad
---

<front>

You are modeling a `fct_shipping` table and need to ensure the combination of `shipment_id` and `service_provider` is unique. You also want this unique key available for downstream joins. How should you implement this?

</front>

---

<back>

You should materialize a surrogate key within the SQL model by hashing or concatenating the columns, then test it.

This approach serves two purposes: it allows for a standard `unique` test to validate the data, and it provides a physical primary key for downstream models to join on.

</back>
