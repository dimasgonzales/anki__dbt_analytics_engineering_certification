---
tags:
- card_type/factual
- development/modularity
- development/seeds
- pipelines/deployment-jobs
citations:
- cleaned_docs/seeds/index.md
guid: d6af3936dd
source: llm
uuid: eadd5aef-c4ec-5695-9c9f-538abe00dca6
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text confirms that seeds are not intended for raw production data or large datasets, and are best suited for static, business-specific reference data such as country codes, which directly supports the answer."
  citation:
    quote: "Seeds should **not** be used to load raw data (for example, large CSV exports from a production database). Since seeds are version controlled, they are best suited to files that contain business-specific logic, for example a list of country codes or user IDs of employees."
    is_quote_valid: true
---

<front>

What is the primary purpose of dbt seeds and for what type of data are they strictly intended?

</front>

---

<back>

Seeds are CSV files stored in the dbt repository used for loading static, infrequently changing reference data (e.g., country codes, exclusion lists). They should NOT be used for loading raw production data or large datasets.

</back>
