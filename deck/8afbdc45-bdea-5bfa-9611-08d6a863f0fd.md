---
tags:
- card_type/factual
- development/modularity
- development/seeds
- documentation/docs-generation
citations:
- cleaned_docs/python-models/rank_8.md
guid: 4122eb8c1f
source: llm
uuid: 8afbdc45-bdea-5bfa-9611-08d6a863f0fd
claim_meta:
  verdict: SUPPORTED
  explanation: "The answer accurately describes the primary use case for `dbt seed` as small, static reference data like country codes, which benefits from version control, and correctly advises against using it for large or dynamic datasets. This aligns with the reference text, which states seeds are for business-specific logic and not for raw data or large files, and recommends other tools for such cases."
  citation:
    quote: "Seeds should **not** be used to load raw data (for example, large CSV exports from a production database). Since seeds are version controlled, they are best suited to files that contain business-specific logic, for example a list of country codes or user IDs of employees."
    is_quote_valid: true
---

<front>

What is the primary use case for `dbt seed` versus external loading methods?

</front>

---

<back>

`dbt seed` is best reserved for small, static reference data (e.g., country codes, mapping tables) that changes infrequently and benefits from version control. It creates CSVs in the repository. For large or dynamic datasets, you should use warehouse-native commands (like `COPY INTO`) or EL tools.

</back>
