---
tags:
  - materializations
  - snapshots
  - test-config
citations:
- cleaned_docs/snapshots/rank_7.md
guid: 8dfa3fb3d9
source: llm
uuid: 79ac0ae2-7f2e-52c2-b1cf-ef03d107aabe
---

<front>

You are configuring an incremental model on BigQuery using the `merge` strategy. You receive an error stating the configuration is invalid. What is the likely cause based on the `unique_key`?

</front>

---

<back>

You likely omitted the `unique_key` configuration. On BigQuery, the `merge` strategy explicitly requires a `unique_key` to identify which rows to update. If you do not have a unique key, you must use the `append` strategy or `insert_overwrite` (partition replacement).

</back>
