---
tags:
- card_type/factual
- debugging/compiled-code
- development/modularity
- development/sql-performance
citations:
- cleaned_docs/error-logs/rank_9.md
guid: 8eccc44586
source: llm
uuid: d9238dfa-fdea-5314-a84e-e155d4cbbce1
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly defines when the `NoNodesForSelectionCriteria` warning occurs, directly matching the answer's description."
  citation:
    quote: "Some of the examples use `NoNodesForSelectionCriteria`, which is a specific warning that occurs when your `--select` flag doesn't match any nodes/resources in your dbt project"
    is_quote_valid: true
---

<front>

What triggers the `NoNodesForSelectionCriteria` warning in dbt?

</front>

---

<back>

This warning is triggered when you provide a node selection argument (e.g., `--select my_model`) that results in **zero** items being selected for the run. It alerts you that the dbt command effectively did nothing.

</back>
