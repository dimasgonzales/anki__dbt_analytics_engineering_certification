---
tags:
  - snapshots
  - sources
  - materializations
citations:
- cleaned_docs/modularity/rank_2.md
guid: 8e1c054822
source: llm
uuid: 5f7c5acb-6adf-5e3f-96c2-797af3ce2fb7
---

<front>

You need to snapshot a source table `orders` that contains a reliable `updated_at` timestamp column. Which snapshot strategy should you use in your configuration?

</front>

---

<back>

Use the **timestamp** strategy. It is generally more performant than the `check` strategy because dbt only needs to look at the specified timestamp column to detect changes.

Config:
```sql
strategy='timestamp',
updated_at='updated_at',
```

</back>
