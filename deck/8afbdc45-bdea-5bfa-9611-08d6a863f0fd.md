---
tags:
- card_type/factual
- docs-generation
- modularity
- seeds
citations:
- cleaned_docs/python-models/rank_8.md
guid: 4122eb8c1f
source: llm
uuid: 8afbdc45-bdea-5bfa-9611-08d6a863f0fd
---

<front>

What is the primary use case for `dbt seed` versus external loading methods?

</front>

---

<back>

`dbt seed` is best reserved for small, static reference data (e.g., country codes, mapping tables) that changes infrequently and benefits from version control. It creates CSVs in the repository. For large or dynamic datasets, you should use warehouse-native commands (like `COPY INTO`) or EL tools.

</back>
