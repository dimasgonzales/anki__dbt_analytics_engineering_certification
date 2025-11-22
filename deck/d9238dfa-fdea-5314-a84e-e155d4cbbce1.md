---
tags:
  - compiled-code
  - modularity
  - sql-performance
citations:
- cleaned_docs/error-logs/rank_9.md
guid: 8eccc44586
source: llm
uuid: d9238dfa-fdea-5314-a84e-e155d4cbbce1
---

<front>

What triggers the `NoNodesForSelectionCriteria` warning in dbt?

</front>

---

<back>

This warning is triggered when you provide a node selection argument (e.g., `--select my_model`) that results in **zero** items being selected for the run. It alerts you that the dbt command effectively did nothing.

</back>
