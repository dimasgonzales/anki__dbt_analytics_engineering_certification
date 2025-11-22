---
tags:
  - materializations
  - grants
  - contracts
citations:
- cleaned_docs/grants/rank_2.md
guid: 5a5994a405
source: llm
uuid: 07c61dd2-14e2-5aeb-8ebc-0dad9fb8b73d
---

<front>

What configuration method must be used to apply `GRANT USAGE ON SCHEMA` permissions in dbt?

</front>

---

<back>

You must use **Hooks** (specifically `on-run-end` or `post-hook`).

The `grants` resource config is scoped strictly to model objects (tables and views) and cannot handle schema-level permissions.

</back>
