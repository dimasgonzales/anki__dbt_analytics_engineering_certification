---
tags:
- card_type/factual
- development/modularity
- development/seeds
- pipelines/dag-failures
citations:
- cleaned_docs/error-logs/rank_3.md
guid: be77b38df5
source: llm
uuid: ac19c7b1-24be-50cf-bda2-fe1cb206cab2
---

<front>

What does a 'Dependency Error' or 'Found a cycle' error indicate regarding the dbt DAG?

</front>

---

<back>

It indicates that the Directed Acyclic Graph (DAG) contains a loop. This happens when two or more models reference each other (e.g., Model A refs Model B, and Model B refs Model A), which prevents dbt from determining an execution order.

</back>
