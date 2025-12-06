---
tags:
- card_type/factual
- development/modularity
- development/seeds
- governance/model-access
citations:
- cleaned_docs/contracts/rank_3.md
guid: 1f6348a68c
source: llm
uuid: 974eb1cd-aec3-54a9-af4f-e3afdc2aff26
claim_meta:
  verdict: SUPPORTED
  explanation: "The reference text explicitly lists private, protected, and public as the valid access options for dbt models, and states that public models can be referenced everywhere, while protected models are limited to the same project, confirming that public access is required for cross-project referencing."
  citation:
    quote: "Public: Models with `public` access can be referenced everywhere."
    is_quote_valid: false
---

<front>

What are the valid options for the `access` configuration on a dbt model, and which one is required for cross-project referencing?

</front>

---

<back>

The valid options are `private`, `protected`, and `public`. To reference a model from a **different** dbt project (cross-project referencing), the model must be explicitly configured as **`public`**.

- `private`: Accessible only within the same group.
- `protected`: Accessible within the same project (default).
- `public`: Accessible by downstream projects.

</back>
