---
tags:
- card_type/scenario
- development/sources
- documentation/descriptions
- documentation/exposures
citations:
- cleaned_docs/lineage/rank_6.md
guid: 0f67d6e5b6
source: llm
uuid: f8dd65ed-f58a-514f-b96e-78b7dbfdcc65
---

<front>

A dashboard is showing stale data, but your dbt deployment job shows a status of "Success". What is the likely cause, and how do you verify it?

</front>

---

<back>

The dbt models likely built successfully using old data because the raw sources haven't updated. You should check the `freshness` metadata for the sources to see if `maxLoadedAt` meets your defined SLA.

```yaml
sources:
  - name: orders
    freshness:
      warn_after: {count: 12, period: hour}
```

</back>
