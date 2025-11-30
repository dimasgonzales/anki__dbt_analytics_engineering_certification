---
tags:
- deployment-jobs
- modularity
- seeds
citations:
- cleaned_docs/seeds/index.md
guid: d6af3936dd
source: llm
uuid: eadd5aef-c4ec-5695-9c9f-538abe00dca6
---

<front>

What is the primary purpose of dbt seeds and for what type of data are they strictly intended?

</front>

---

<back>

Seeds are CSV files stored in the dbt repository used for loading static, infrequently changing reference data (e.g., country codes, exclusion lists). They should NOT be used for loading raw production data or large datasets.

</back>
