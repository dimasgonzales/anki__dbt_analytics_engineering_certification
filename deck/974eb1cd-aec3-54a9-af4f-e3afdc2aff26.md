---
tags:
  - model-access
  - modularity
  - seeds
citations:
- cleaned_docs/contracts/rank_3.md
guid: 1f6348a68c
source: llm
uuid: 974eb1cd-aec3-54a9-af4f-e3afdc2aff26
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
