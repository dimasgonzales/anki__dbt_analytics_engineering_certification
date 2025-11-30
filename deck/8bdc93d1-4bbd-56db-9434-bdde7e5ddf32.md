---
tags:
- contracts
- project-config
- sources
citations:
- cleaned_docs/project-config/rank_1.md
guid: 59a7f2af9c
source: llm
uuid: 8bdc93d1-4bbd-56db-9434-bdde7e5ddf32
---

<front>

How do naming conventions for multi-word resource keys (like `saved-queries`) differ between `dbt_project.yml` and other property files (like `schema.yml`)?

</front>

---

<back>

Top-level resource keys in `dbt_project.yml` must use **hyphens** (kebab-case), while keys in property files must use **underscores** (snake_case).

*   `dbt_project.yml`: `saved-queries:`
*   `models/schema.yml`: `saved_queries:`

</back>
