---
tags:
  - lineage
  - sources
  - test-config
citations:
- cleaned_docs/exposures/rank_3.md
guid: 9f0c7d572a
source: llm
uuid: fafc3009-ad58-5ad6-903c-10dd5e4fdcfc
---

<front>

What specific source property does an exposure allow you to visualize in the dbt documentation graph regarding data health?

</front>

---

<back>

Exposures allow you to visualize the **Source Freshness** status of upstream nodes. The graph displays the `state` (pass/warn/error) and `maxLoadedAt` timestamp of the sources that the exposure depends on.

</back>
