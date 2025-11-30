---
tags:
- exposures
- lineage
- sources
citations:
- cleaned_docs/lineage/rank_4.md
guid: 3ecdd3a1d3
source: llm
uuid: eea93caa-fd99-52b9-b37b-cf0f35b0bce9
---

<front>

What is the primary benefit of 'Column-Level Lineage' over standard table-level lineage in dbt?

</front>

---

<back>

Column-Level Lineage allows you to trace specific fields (such as PII or primary keys) from their source all the way to downstream exposures. This is essential for auditing data usage and conducting precise impact analysis when a specific column's logic changes.

</back>
