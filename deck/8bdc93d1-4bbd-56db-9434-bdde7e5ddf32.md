---
tags:
- card_type/factual
- development/project-config
- development/sources
- governance/contracts
citations:
- cleaned_docs/project-config/rank_1.md
guid: 59a7f2af9c
source: llm
uuid: 8bdc93d1-4bbd-56db-9434-bdde7e5ddf32
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly states the difference in naming conventions for multi-word resource keys, confirming that hyphens are used in dbt_project.yml and underscores in other YAML files, which directly aligns with the answer provided."
  citation:
    quote: "Use dashes (`-`) when configuring resource types with multiple words in your `dbt_project.yml` file. Use underscore (`_`) when configuring resource types with multiple words for YAML files other than the `dbt_project.yml` file."
    is_quote_valid: false
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
