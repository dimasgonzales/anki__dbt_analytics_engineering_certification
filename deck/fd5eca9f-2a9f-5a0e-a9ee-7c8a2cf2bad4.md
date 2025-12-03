---
tags:
- card_type/scenario
- debugging/compiled-code
- development/python-models
- development/seeds
citations:
- cleaned_docs/lineage/rank_9.md
guid: 2793bbb9e1
source: llm
uuid: fd5eca9f-2a9f-5a0e-a9ee-7c8a2cf2bad4
---

<front>

How does dbt Explorer help identify candidates for incremental materialization differently than a single `run_results.json` file?

</front>

---

<back>

dbt Explorer visualizes **historical execution trends** (e.g., over the last 3 months). A single run log only shows one duration, whereas Explorer reveals *trends*, such as a linear increase in runtime over time, which indicates a model is scanning a growing dataset and requires refactoring to incremental.

</back>
