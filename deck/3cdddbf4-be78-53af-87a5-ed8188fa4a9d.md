---
tags:
- card_type/factual
- development/cli-commands
- documentation/descriptions
- governance/contracts
citations:
- cleaned_docs/contracts/rank_6.md
guid: 8ffb3d366a
source: llm
uuid: 3cdddbf4-be78-53af-87a5-ed8188fa4a9d
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text confirms that in Snowflake, UNIQUE and PRIMARY KEY constraints are purely metadata and not enforced during data insertion, which directly supports the answer's claim that constraints are metadata-only and require unique data tests for actual validation. While BigQuery is not mentioned in the evidence, the provided information for Snowflake is sufficient to support the general reasoning in the answer."
  citation:
    quote: "only the `not null` (and the `not null` property of `primary key`) are actually checked at present. The rest of the constraints are purely metadata, not verified when inserting data."
    is_quote_valid: true
---

<front>

If you define a `primary_key` constraint on a Snowflake or BigQuery model, why is it still strongly recommended to add a `unique` data test?

</front>

---

<back>

On these platforms, standard constraints are often **metadata-only** and are **not enforced** at runtime. While dbt defines the constraint for documentation/optimization, a `unique` data test is required to actually validate data integrity and detect duplicates.

</back>
