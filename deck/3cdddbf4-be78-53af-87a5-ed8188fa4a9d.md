---
tags:
- card_type/factual
- cli-commands
- contracts
- descriptions
citations:
- cleaned_docs/contracts/rank_6.md
guid: 8ffb3d366a
source: llm
uuid: 3cdddbf4-be78-53af-87a5-ed8188fa4a9d
---

<front>

If you define a `primary_key` constraint on a Snowflake or BigQuery model, why is it still strongly recommended to add a `unique` data test?

</front>

---

<back>

On these platforms, standard constraints are often **metadata-only** and are **not enforced** at runtime. While dbt defines the constraint for documentation/optimization, a `unique` data test is required to actually validate data integrity and detect duplicates.

</back>
