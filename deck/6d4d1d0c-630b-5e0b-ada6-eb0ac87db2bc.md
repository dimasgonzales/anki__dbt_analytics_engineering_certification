---
tags:
- card_type/scenario
- debugging/yaml-compilation
- documentation/lineage
- pipelines/deployment-jobs
citations:
- cleaned_docs/dbt-clone/rank_3.md
guid: d578480f37
source: llm
uuid: 6d4d1d0c-630b-5e0b-ada6-eb0ac87db2bc
---

<front>

You need to set up a CI environment where a downstream BI tool can query the modified models and their dependencies for validation. Should you use `--defer` or `dbt clone`?

</front>

---

<back>

You should use `dbt clone`.

**Why:** BI tools require queryable physical objects in the database. `--defer` relies on mixed pointers to production artifacts which may not exist in the CI schema, whereas `dbt clone` creates a fully materialized, queryable copy of the dataset.

</back>
