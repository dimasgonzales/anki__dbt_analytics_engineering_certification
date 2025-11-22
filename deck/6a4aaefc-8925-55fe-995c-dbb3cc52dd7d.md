---
tags:
  - modularity
  - exposures
  - lineage
citations:
- cleaned_docs/exposures/rank_3.md
guid: eb985f7ace
source: llm
uuid: 6a4aaefc-8925-55fe-995c-dbb3cc52dd7d
---

<front>

How do you define dependencies for an exposure to ensure it appears in the dbt DAG?

</front>

---

<back>

Use the `depends_on` key within the exposure's YAML configuration. You must explicitly list the upstream resources using `ref()` for models and `source()` for sources.

```yaml
exposures:
  - name: finance_dashboard
    type: dashboard
    depends_on:
      - ref('fct_revenue')
      - source('stripe', 'charges')
```

</back>
